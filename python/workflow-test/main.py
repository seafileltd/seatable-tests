import json
import os
import sys
current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_script_dir)
sys.path.append(parent_dir)


import requests
from seatable_api import Base, Account
from seatable_api.constants import ColumnTypes

from local_settings import TEST_USER_EMAIL, TEST_USER_PWD, TEST_SERVER_URL, TEST_GROUP_NAME


account = None

workspace = None
dtable_name = 'test-workflow'
dtable = None

table_id = '0000'
table = None
participants_column = None
participants_column_name = 'participants'
state_column = None
state_column_name = 'state'

text_column = None
collaborator_column = None

workflow = None
workflow_task = None
workflow_task_row = None

def auth_token():
    global account
    account = Account(TEST_USER_EMAIL, TEST_USER_PWD, TEST_SERVER_URL)
    account.auth()
    assert account and account.token
    account.load_account_info()
    assert account.username


def prepare_base():
    global account, workspace, dtable_name, dtable
    workspace_list = account.list_workspaces()['workspace_list']
    workspace = next(filter(lambda workspace: workspace['name'] == TEST_GROUP_NAME and workspace['is_admin'], workspace_list), None)
    assert workspace
    resp_dtable = account.add_base(dtable_name, workspace['id'])
    assert resp_dtable
    dtable = account.get_base(workspace['id'], dtable_name)
    assert dtable


def delete_base():
    global account, workspace, dtable_name
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workspace/{workspace['id']}/dtable/"
    resp = requests.delete(url, headers=account.token_headers, json={'name': dtable_name})
    assert resp.ok


def prepare_table():
    global account, workspace, state_column, participants_column, text_column, collaborator_column, dtable, table
    participants_column = dtable.insert_column(table_id, participants_column_name, ColumnTypes.COLLABORATOR)
    assert participants_column
    state_column = dtable.insert_column(table_id, state_column_name, ColumnTypes.SINGLE_SELECT)
    assert state_column
    text_column = dtable.insert_column(table_id, 'text', ColumnTypes.TEXT)
    assert text_column
    collaborator_column = dtable.insert_column(table_id, 'collaborator', ColumnTypes.COLLABORATOR)
    assert collaborator_column
    table = dtable.get_metadata()['tables'][0]


def gen_init_workflow_config():
    global state_column, participants_column, text_column, collaborator_column, account
    return {
        'workflow_name': 'test-workflow',
        'table_id': '0000',
        'state_column_key': state_column['key'],
        'participants_column_key': participants_column['key'],
        'nodes': [
            {
                '_id': 'init',
                'type': 'init',
                'name': 'Start',
                'next_node_id': '54420',
                'conditional_next_nodes': [],
                'node_form': {
                    'readwrite_columns': [
                        {'key': '0000'},
                        {'key': text_column['key']},
                        {'key': collaborator_column['key']},
                    ]
                }
            },
            {
                '_id': '1',
                'type': 'completed',
                'name': 'Finished',
                'finish_task_message': '',
                'node_form': {
                    'readonly_columns': [
                        {'key': '0000'},
                        {'key': text_column['key']},
                        {'key': collaborator_column['key']},
                    ]
                }
            },
            {
                '_id': '54420',
                'type': 'normal',
                'name': 'Node1',
                'participants': [account.username],
                'participants_type': 'static',
                'node_participants_column_key': '',
                'next_node_id': '1',
                'conditional_next_nodes': [],
                'node_form': {
                    'readwrite_columns': [
                        {'key': '0000'},
                        {'key': text_column['key']},
                        {'key': collaborator_column['key']},
                    ],
                    'readonly_columns': []
                }
            }
        ]
    }


def test_create_workflow():
    global account, workspace, dtable_name, workflow
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/"
    data = {
        'workspace_id': workspace['id'],
        'name': dtable_name,
        'workflow_config': json.dumps(gen_init_workflow_config())
    }
    resp = requests.post(url, headers=account.token_headers, data=data)
    assert resp.ok
    workflow = resp.json()['workflow']
    assert workflow


def test_update_workflow():
    global workflow, account, collaborator_column
    # update workflow name
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/{workflow['token']}/"
    workflow_name = 'new-test-workflow'
    data = {'workflow_name': workflow_name}
    resp = requests.put(url, headers=account.token_headers, data=data)
    assert resp.ok
    assert json.loads(resp.json()['workflow']['workflow_config'])['workflow_name'] == 'new-test-workflow'

    # update workflow name back
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/{workflow['token']}/"
    workflow_name = 'test-workflow'
    data = {'workflow_name': workflow_name}
    resp = requests.put(url, headers=account.token_headers, data=data)
    assert resp.ok
    assert json.loads(resp.json()['workflow']['workflow_config'])['workflow_name'] == 'test-workflow'
    workflow = resp.json()['workflow']

    # update workflow config
    workflow_config = json.loads(workflow['workflow_config'])
    workflow_config['nodes'][0]['conditional_next_nodes'] = [
        {
            "_id": "496384",
            "next_node_id": "1",
            "filters": [
                {
                    "column_key": "0000",
                    "filter_predicate": "contains",
                    "filter_term": "123"
                }
            ],
            "filter_conjunction": "And"
        }
    ]
    workflow_config['nodes'][2]['next_node_id'] = '66666'
    workflow_config['nodes'][2]['participants_type'] = 'dynamic'
    workflow_config['nodes'][2]['node_participants_column_key'] = collaborator_column['key']
    workflow_config['nodes'][2]['conditional_next_nodes'] = [
        {
            "_id": "496385",
            "next_node_id": "1",
            "filters": [
                {
                    "column_key": "0000",
                    "filter_predicate": "contains",
                    "filter_term": "123"
                }
            ],
            "filter_conjunction": "And"
        }
    ]
    workflow_config['nodes'].append({
        '_id': '66666',
        'type': 'normal',
        'name': 'Node2',
        'participants': [account.username],
        'participants_type': 'static',
        'node_participants_column_key': '',
        'next_node_id': '1',
        'conditional_next_nodes': [],
        'node_form': {
            'readwrite_columns': [
                {'key': '0000'},
                {'key': text_column['key']},
                {'key': collaborator_column['key']},
            ],
            'readonly_columns': []
        }
    })
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/{workflow['token']}/"
    data = {'workflow_config': json.dumps(workflow_config)}
    resp = requests.put(url, headers=account.token_headers, data=data)
    assert resp.ok
    workflow = resp.json()['workflow']
    assert workflow


def test_list_workflows():
    global account, workflow
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/shared/"
    resp = requests.get(url, headers=account.token_headers)
    assert resp.ok
    my_managed_workflows = resp.json()['my_managed_workflows']
    assert my_managed_workflows
    filtered_workflow = next(filter(lambda item: item['id'] == workflow['id'], my_managed_workflows), None)
    assert filtered_workflow


def test_delete_workflow():
    global account, workflow
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/{workflow['token']}/"
    resp = requests.delete(url, headers=account.token_headers)
    assert resp.ok


def test_submit_task():
    global workflow, account, dtable, table, text_column, workflow_task, workflow_task_row, participants_column, collaborator_column
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/{workflow['token']}/task-submit/"
    row_data = {
        table['columns'][0]['name']: 'test',
        text_column['name']: 'text',
        collaborator_column['name']: [account.username]
    }
    data = {'row_data': json.dumps(row_data)}
    resp = requests.post(url, headers=account.token_headers, data=data)
    assert resp.ok
    workflow_task = resp.json()['task']
    assert workflow_task
    sql = f"SELECT * FROM `{table['name']}` WHERE _id='{workflow_task['row_id']}'"
    rows = dtable.query(sql)
    assert rows
    workflow_task_row = rows[0]
    assert workflow_task_row.get(table['columns'][0]['name']) == 'test'
    assert workflow_task_row.get(participants_column['name']) == [account.username]


def test_list_ongoing_tasks():
    global account, workflow, workflow_task
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/ongoing-tasks/"
    resp = requests.get(url, headers=account.token_headers)
    assert resp.ok
    task_list = resp.json()['task_list']
    task = next(filter(lambda task: task['id'] == workflow_task['id'], task_list), None)
    assert task


def test_transfer_task():
    global account, workflow, workflow_task, table
    # normal transfer
    ## transfer
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/{workflow['token']}/tasks/{workflow_task['id']}/transfer/"
    row_data = {
        table['columns'][0]['name']: 'abc'
    }
    data = {
        'row_data': json.dumps(row_data),
        'node_id': workflow_task['node_id']
    }
    resp = requests.post(url, headers=account.token_headers, data=data)
    assert resp.ok
    ## list initiated tasks, check task current node
    url = f"{TEST_SERVER_URL.strip('/')}/api/v2.1/workflows/{workflow['token']}/tasks/"
    params = {
        'filter_type': 'initiated'
    }
    resp = requests.get(url, headers=account.token_headers, params=params)
    assert resp.ok
    task_list = resp.json()['task_list']
    assert task_list
    task = next(filter(lambda item: item['id'] == workflow_task['id'], task_list), None)
    assert task
    assert task['node_id'] == '66666'

    # conditional transfer to finish node


auth_token()

prepare_base()
prepare_table()

try:
    test_create_workflow()
    test_update_workflow()
    test_list_workflows()

    test_submit_task()
    test_list_ongoing_tasks()

    test_transfer_task()

    test_delete_workflow()
except Exception as e:
    raise e
finally:
    delete_base()
