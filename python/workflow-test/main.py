import json
import os
import logging
import sys
import traceback
from functools import wraps
current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_script_dir)
sys.path.append(parent_dir)


import requests
from seatable_api import Base as _Base, Account
from seatable_api.constants import ColumnTypes

from local_settings import TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, SERVER_URL, \
    TEST_WORKFLOW_GROUP_NAME, LOCAL_TEST, BASE_API_TOKEN_FOR_WORKFLOW


class Base:

    def __init__(self, account: Account, name: str, group_name: str):
        self.account = account
        self.name = name
        workspace_list = account.list_workspaces()['workspace_list']
        self.workspace = next(filter(lambda workspace: workspace['name'] == group_name and workspace['is_admin'], workspace_list), None)
        assert self.workspace
        resp = self.account.add_base(name, self.workspace['id'])
        assert resp
        self.base: _Base = account.get_base(self.workspace['id'], name)
        assert self.base

    def delete(self):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workspace/{self.workspace['id']}/dtable/"
        resp = requests.delete(url, headers=self.account.token_headers, json={'name': self.name})
        assert resp.ok

    def list_workflows(self):
        params = {'workspace_id': self.workspace['id'], 'name': self.name}
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/"
        resp = requests.get(url, headers=self.account.token_headers, params=params)
        assert resp.ok
        workflow_list = resp.json()['workflow_list']
        return workflow_list


class Table:

    def __init__(self, base: Base, new_table_name=None):
        self.base = base
        if new_table_name:
            self.table = self.base.base.add_table(new_table_name)
            self.table_id = self.table['_id']
        else:
            self.table_id = '0000'
            self.table = self.base.base.get_metadata()['tables'][0]

        self.participants_column_name = 'participants'
        self.participants_column = self.base.base.insert_column(self.table_id, self.participants_column_name, ColumnTypes.COLLABORATOR)
        assert self.participants_column

        self.state_column_name = 'state'
        self.state_column = self.base.base.insert_column(self.table_id, self.state_column_name, ColumnTypes.SINGLE_SELECT)
        assert self.state_column

        self.text_column_name = 'text'
        self.text_column = self.base.base.insert_column(self.table_id, self.text_column_name, ColumnTypes.TEXT)
        assert self.text_column

        self.collaborator_column_name = 'collaborator'
        self.collaborator_column = self.base.base.insert_column(self.table_id, self.collaborator_column_name, ColumnTypes.COLLABORATOR)
        assert self.collaborator_column

        self.number_column_name = 'number'
        self.number_column = self.base.base.insert_column(self.table_id, self.number_column_name, ColumnTypes.NUMBER)
        assert self.number_column


class Workflow:

    def __init__(self, base: Base, table: Table, name: str):
        self.workflow = None
        self.base = base
        self.table = table
        self.name = name

        data = {
            'workspace_id': self.base.workspace['id'],
            'name': self.base.name,
            'workflow_config': json.dumps(self.gen_init_workflow_config())
        }

        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/"
        resp = requests.post(url, headers=base.account.token_headers, data=data)
        assert resp.ok
        self.workflow = resp.json()['workflow']
        assert self.workflow

    def gen_init_workflow_config(self):
        return {
            'workflow_name': self.name,
            'table_id': '0000',
            'state_column_key': self.table.state_column['key'],
            'participants_column_key': self.table.participants_column['key'],
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
                            {'key': self.table.collaborator_column['key']},
                            {'key': self.table.number_column['key']},
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
                            {'key': self.table.text_column['key']},
                            {'key': self.table.collaborator_column['key']},
                            {'key': self.table.number_column['key']},
                        ]
                    }
                },
                {
                    '_id': '54420',
                    'type': 'normal',
                    'name': 'Node1',
                    'participants': [self.base.account.username],
                    'participants_type': 'static',
                    'node_participants_column_key': '',
                    'next_node_id': '1',
                    'conditional_next_nodes': [],
                    'node_form': {
                        'readwrite_columns': [
                            {'key': '0000'},
                            {'key': self.table.text_column['key']},
                            {'key': self.table.collaborator_column['key']},
                            {'key': self.table.number_column['key']},
                        ],
                        'readonly_columns': []
                    },
                    "enable_processing_time_limit": True,
                    "processing_time_limit": "+1d"
                }
            ]
        }

    def update_workflow_name(self, name: str, account: Account):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow['token']}/"
        data = {'workflow_name': name}
        resp = requests.put(url, headers=account.token_headers, data=data)
        assert resp.ok
        workflow = resp.json()['workflow']
        assert json.loads(workflow['workflow_config'])['workflow_name'] == name
        self.workflow = workflow

    def update_workflow_config(self, account: Account):
        workflow_config = json.loads(self.workflow['workflow_config'])
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
        workflow_config['nodes'][2]['node_participants_column_key'] = self.table.collaborator_column['key']
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
                    {'key': self.table.text_column['key']},
                    {'key': self.table.collaborator_column['key']},
                ],
                'readonly_columns': []
            }
        })
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow['token']}/"
        data = {'workflow_config': json.dumps(workflow_config)}
        resp = requests.put(url, headers=account.token_headers, data=data)
        assert resp.ok
        workflow = resp.json()['workflow']
        assert workflow
        self.workflow = workflow

    def delete(self, account: Account):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow['token']}/"
        resp = requests.delete(url, headers=account.token_headers)
        assert resp.ok


class WorkflowTask:

    def __init__(self, base: Base, table: Table, workflow: Workflow, initiator_account: Account, workflow_task: dict):
        self.base = base
        self.table = table
        self.workflow = workflow
        self.initiator_account = initiator_account

        self.workflow_task = workflow_task

    @classmethod
    def submit_workflow_task(cls, base: Base, table: Table, workflow: Workflow, initiator_account: Account, form_data: dict):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{workflow.workflow['token']}/task-submit/"
        data = {'row_data': json.dumps(form_data)}
        resp = requests.post(url, headers=initiator_account.token_headers, data=data)
        assert resp.ok
        workflow_task = resp.json()['task']
        assert workflow_task
        sql = f"SELECT * FROM `{table.table['name']}` WHERE _id='{workflow_task['row_id']}'"
        rows = base.base.query(sql)
        assert rows
        workflow_task = cls(base, table, workflow, initiator_account, workflow_task)
        workflow_task.reload_workflow_task()
        workflow_task.check_task_state()
        return workflow_task

    def reload_workflow_task(self):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/"
        params = {
            'filter_type': 'initiated'
        }
        resp = requests.get(url, headers=self.initiator_account.token_headers, params=params)
        assert resp.ok
        task_list = resp.json()['task_list']
        assert task_list
        task = next(filter(lambda item: item['id'] == self.workflow_task['id'], task_list), None)
        assert task
        self.workflow_task = task

    def check_task_state(self):
        sql = f"SELECT `{self.table.state_column_name}`, `{self.table.participants_column_name}` FROM `{self.table.table['name']}` WHERE _id='{self.workflow_task['row_id']}'"
        results = self.base.base.query(sql)
        assert results
        assert results[0].get(self.table.state_column_name) == self.workflow_task['current_node']['name']
        assert (results[0].get(self.table.participants_column_name) or []) == [item['email'] for item in self.workflow_task['participants']]

    def transfer_task(self, transfer_account: Account, row_data: dict):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/{self.workflow_task['id']}/transfer/"
        data = {
            'row_data': json.dumps(row_data),
            'node_id': self.workflow_task['node_id']
        }
        resp = requests.post(url, headers=transfer_account.token_headers, data=data)
        assert resp.ok
        self.reload_workflow_task()
        self.check_task_state()


def wrap_test(name, describe=None, raise_exception=True):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):

            try:
                func(self, *args, **kwargs)
            except Exception as e:
                self.test_results.append({
                    'name': name,
                    'describe': describe,
                    'function': func.__name__,
                    'is_pass': False,
                    'error': traceback.format_exc(),
                })
                if raise_exception:
                    raise e
            else:
                self.test_results.append({
                    'name': name,
                    'describe': describe,
                    'function': func.__name__,
                    'is_pass': True,
                    'error': None
                })

        return wrapper
    return actual_decorator



class WorkflowTest:
    """workflow CRUD"""

    def __init__(self):
        self.account: Account = None
        self.base: Base = None
        self.table: Table = None
        self.workflow: Workflow = None
        self.test_results = []

    @wrap_test('Test create workflow')
    def test_create_workflow(self):
        self.workflow = Workflow(self.base, self.table, 'test-workflow')

    @wrap_test('Test list workflows')
    def test_list_workflows(self):
        workflow_list = self.base.list_workflows()
        assert next(filter(lambda workflow: workflow['id'] == self.workflow.workflow['id'], workflow_list), None)
        assert next(filter(lambda workflow: workflow['id'] == self.workflow.workflow['id'], workflow_list), None)['id'] == self.workflow.workflow['id']

    @wrap_test('Test update workflow')
    def test_update_workflow(self):
        self.workflow.update_workflow_name('new-test-workflow', self.base.account)
        self.workflow.update_workflow_name('test-workflow', self.base.account)
        self.workflow.update_workflow_config(self.base.account)

    @wrap_test('Test delete workflow')
    def test_delete_workflow(self):
        self.workflow.delete(self.base.account)
        workflow_list = self.base.list_workflows()
        assert not workflow_list

    def run(self):
        self.account = Account(TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, SERVER_URL)
        self.account.auth()
        self.account.load_account_info()

        self.base = Base(self.account, 'test-workflow', TEST_WORKFLOW_GROUP_NAME)
        self.table = Table(self.base)

        try:
            self.test_create_workflow()
            self.test_list_workflows()
            self.test_update_workflow()
            self.test_delete_workflow()
        except Exception as e:
            logging.exception(e)
        finally:
            self.base.delete()


class WorkflowTaskTest:
    """workflow task submit and transfer"""

    def __init__(self):
        self.account: Account = None
        self.base: Base = None
        self.table: Table = None
        self.workflow: Workflow = None
        self.workflow_task: WorkflowTask = None
        self.test_results = []

    @wrap_test('Test submit workflow task')
    def test_submit_workflow_task(self):
        self.workflow_task = WorkflowTask.submit_workflow_task(self.base, self.table, self.workflow, self.account, {self.table.table['columns'][0]['name']: 'abc', self.table.collaborator_column_name: [self.account.username]})

    @wrap_test('Test transfer workflow task')
    def test_transfer_workflow_task(self):
        self.workflow_task.transfer_task(self.account, {self.table.text_column_name: 'def'})

    @wrap_test('Test submit workflow task with conditional next node')
    def test_submit_workflow_task_with_conditional_next_node(self):
        self.workflow_task = WorkflowTask.submit_workflow_task(self.base, self.table, self.workflow, self.account, {self.table.table['columns'][0]['name']: '123'})
        assert self.workflow_task.workflow_task['task_state'] == 'finished'

    @wrap_test('Test transfer with conditional next node')
    def test_transfer_workflow_task_with_conditional_next_node(self):
        self.workflow_task = WorkflowTask.submit_workflow_task(self.base, self.table, self.workflow, self.account, {self.table.table['columns'][0]['name']: 'def', self.table.collaborator_column_name: [self.account.username]})
        self.workflow_task.transfer_task(self.account, {self.table.table['columns'][0]['name']: '123'})
        assert self.workflow_task.workflow_task['task_state'] == 'finished'

    def run(self):
        self.account = Account(TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, SERVER_URL)
        self.account.auth()
        self.account.load_account_info()

        self.base = Base(self.account, 'test-workflow', TEST_WORKFLOW_GROUP_NAME)
        self.table = Table(self.base)
        self.workflow = Workflow(self.base, self.table, 'test-workflow')

        # update workflow_config to make workflow ready
        self.workflow.update_workflow_config(self.account)

        try:
            self.test_submit_workflow_task()
            self.test_transfer_workflow_task()

            self.test_submit_workflow_task_with_conditional_next_node()

            self.test_transfer_workflow_task_with_conditional_next_node()
        except Exception as e:
            logging.exception(e)
        finally:
            self.base.delete()


class WorkflowTaskViewTest:
    """workflow view for initiator, admin, participant tests"""

    def __init__(self):
        self.account: Account = None
        self.base: Base = None
        self.table: Table = None
        self.workflow: Workflow = None
        self.workflow_task: WorkflowTask = None
        self.test_results = []

    @wrap_test('Test view task as initiator')
    def test_initiator_view(self):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/{self.workflow_task.workflow_task['id']}/initiator-view/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        resp_json = resp.json()
        row = resp_json['row']
        nodes = resp_json.get('nodes')
        assert nodes
        init_node = next(filter(lambda node: node['type'] == 'init', nodes), None)
        assert init_node
        node_form = init_node.get('node_form')
        assert node_form
        readwrite_columns = node_form.get('readwrite_columns') or []
        valid_column_keys = [col['key'] for col in readwrite_columns] + [self.table.state_column['key'], self.table.participants_column['key']]
        for column_key in row:
            if column_key == '_id':
                continue
            assert column_key in valid_column_keys

    @wrap_test('Test view task as participant')
    def test_participant_view(self):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/{self.workflow_task.workflow_task['id']}/participant-view/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        resp_json = resp.json()
        row = resp_json['row']
        current_node = resp_json['current_node']
        node_form = current_node.get('node_form')
        assert node_form
        readonly_columns = node_form.get('readonly_columns') or []
        readwrite_columns = node_form.get('readwrite_columns') or []
        valid_column_keys = [col['key'] for col in readwrite_columns + readonly_columns] + [self.table.state_column['key'], self.table.participants_column['key']]
        for column_key in row:
            if column_key == '_id':
                continue
            assert column_key in valid_column_keys

    @wrap_test('Test view task as admin')
    def test_admin_view(self):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/{self.workflow_task.workflow_task['id']}/admin-view/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        resp_json = resp.json()
        row = resp_json['row']
        current_node = resp_json['current_node']
        node_form = current_node.get('node_form')
        assert node_form
        readonly_columns = node_form.get('readonly_columns') or []
        readwrite_columns = node_form.get('readwrite_columns') or []
        valid_column_keys = [col['key'] for col in readwrite_columns + readonly_columns] + [self.table.state_column['key'], self.table.participants_column['key']]
        for column_key in row:
            if column_key == '_id':
                continue
            assert column_key in valid_column_keys

    def run(self):
        self.account = Account(TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, SERVER_URL)
        self.account.auth()
        self.account.load_account_info()

        self.base = Base(self.account, 'test-workflow', TEST_WORKFLOW_GROUP_NAME)
        self.table = Table(self.base)
        self.workflow = Workflow(self.base, self.table, 'test-workflow')

        # update workflow_config to make workflow ready
        self.workflow.update_workflow_config(self.account)
        self.workflow_task = WorkflowTask.submit_workflow_task(self.base, self.table, self.workflow, self.account, {self.table.table['columns'][0]['name']: 'abc', self.table.collaborator_column_name: [self.account.username]})

        try:
            self.test_initiator_view()
            self.test_participant_view()
            self.test_admin_view()
        except Exception as e:
            logging.exception(e)
        finally:
            self.base.delete()


class WorkflowTaskListTest:
    """list of tasks about ongoing, initiatied-of-one-workflow and all-of-one-workflow"""

    def __init__(self):
        self.account: Account = None
        self.base: Base = None
        self.table: Table = None
        self.workflow: Workflow = None
        self.node1_workflow_task: WorkflowTask = None
        self.node2_workflow_task: WorkflowTask = None
        self.completed_workflow_task: WorkflowTask = None
        self.test_results = []

    @wrap_test('Test submitted tasks')
    def test_submitted_tasks(self):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/?filter_type=initiated"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        task_list = resp.json()['task_list']
        assert len(task_list) == 3
        count = resp.json()['count']
        assert count == 3

    @wrap_test('Test ongoing tasks')
    def test_ongoing_tasks(self):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/?filter_type=ongoing"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        task_list = resp.json()['task_list']
        assert len(task_list) == 2
        count = resp.json()['count']
        assert count == 2

    @wrap_test('Test all tasks')
    def test_all_tasks(self):
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/?filter_type=all"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        task_list = resp.json()['task_list']
        assert len(task_list) == 3
        count = resp.json()['count']
        assert count == 3

    def run(self):
        self.account = Account(TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, SERVER_URL)
        self.account.auth()
        self.account.load_account_info()

        self.base = Base(self.account, 'test-workflow', TEST_WORKFLOW_GROUP_NAME)
        self.table = Table(self.base)
        self.workflow = Workflow(self.base, self.table, 'test-workflow')

        # update workflow_config to make workflow ready
        self.workflow.update_workflow_config(self.account)
        self.node1_workflow_task = WorkflowTask.submit_workflow_task(self.base, self.table, self.workflow, self.account, {self.table.table['columns'][0]['name']: 'abc', self.table.collaborator_column_name: [self.account.username]})
        self.node2_workflow_task = WorkflowTask.submit_workflow_task(self.base, self.table, self.workflow, self.account, {self.table.table['columns'][0]['name']: 'abc', self.table.collaborator_column_name: [self.account.username]})
        self.node2_workflow_task.transfer_task(self.account, {self.table.table['columns'][0]['name']: 'def'})
        self.completed_workflow_task = WorkflowTask.submit_workflow_task(self.base, self.table, self.workflow, self.account, {self.table.table['columns'][0]['name']: '123'})

        try:
            self.test_submitted_tasks()
            self.test_ongoing_tasks()
            self.test_all_tasks()
        except Exception as e:
            logging.exception(e)
        finally:
            self.base.delete()


class InvalidTaskInOngoingListTest:

    def __init__(self):
        self.account: Account = None

        self.base1: Base = None
        self.base2: Base = None

        self.table1: Table = None
        self.table2: Table = None

        self.workflow1: Workflow = None
        self.workflow2: Workflow = None

        self.workflow1_task: WorkflowTask = None
        self.workflow2_task: WorkflowTask = None

        self.test_results = []

    @wrap_test('Test invalid task in ongoing list', describe='Test whether a base with only one workflow can correctly retrieve the ongoing list after the workflow invalid', raise_exception=False)
    def test_invalid_task_in_ongoing_list(self):
        self.workflow1 = Workflow(self.base1, self.table1, 'test-workflow-1')
        self.workflow1.update_workflow_config(self.account)
        self.workflow2 = Workflow(self.base2, self.table2, 'test-workflow-2')
        self.workflow2.update_workflow_config(self.account)

        self.workflow1_task = WorkflowTask.submit_workflow_task(self.base1, self.table1, self.workflow1, self.account, {self.table1.table['columns'][0]['name']: 'abc', self.table1.collaborator_column_name: [self.account.username]})
        self.workflow2_task = WorkflowTask.submit_workflow_task(self.base2, self.table2, self.workflow2, self.account, {self.table2.table['columns'][0]['name']: 'def', self.table2.collaborator_column_name: [self.account.username]})

        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/ongoing-tasks/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        task_list: list = resp.json()['task_list']
        find_workflow1_task = next(filter(lambda task: task['id'] == self.workflow1_task.workflow_task['id'], task_list), None)
        assert find_workflow1_task
        assert find_workflow1_task['is_valid']
        find_workflow2_task = next(filter(lambda task: task['id'] == self.workflow2_task.workflow_task['id'], task_list), None)
        assert find_workflow2_task
        assert find_workflow2_task['is_valid']

        # delete column to make workflow invalid
        self.base2.base.delete_column(self.table2.table['name'], self.table2.state_column['key'])
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/ongoing-tasks/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        task_list: list = resp.json()['task_list']
        find_workflow1_task = next(filter(lambda task: task['id'] == self.workflow1_task.workflow_task['id'], task_list), None)
        assert find_workflow1_task
        assert find_workflow1_task['is_valid']
        find_workflow2_task = next(filter(lambda task: task['id'] == self.workflow2_task.workflow_task['id'], task_list), None)
        assert find_workflow2_task
        assert not find_workflow2_task['is_valid']

    def run(self):
        self.account = Account(TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, SERVER_URL)
        self.account.auth()
        self.account.load_account_info()

        self.base1 = Base(self.account, 'test-workflow-1', TEST_WORKFLOW_GROUP_NAME)
        self.table1 = Table(self.base1)

        self.base2 = Base(self.account, 'test-workflow-2', TEST_WORKFLOW_GROUP_NAME)
        self.table2 = Table(self.base2)

        try:
            self.test_invalid_task_in_ongoing_list()
        except Exception as e:
            logging.exception(e)
        finally:
            self.base1.delete()
            self.base2.delete()


class InvalidFormColumnTaskDetailTest:

    def __init__(self):
        self.account: Account = None
        self.base: Base = None
        self.table: Table = None
        self.workflow: Workflow = None
        self.workflow_task: WorkflowTask = None
        self.test_results = []

    @wrap_test('Test invalid form column task detail', describe='Test whether task details can be correctly retrieved after a field in the workflow node is deleted', raise_exception=False)
    def test_invalid_form_column_task_detail(self):
        self.workflow_task = WorkflowTask.submit_workflow_task(self.base, self.table, self.workflow, self.account, {self.table.collaborator_column_name: [self.account.username], self.table.text_column_name: 'abc', self.table.number_column_name: 123})
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/ongoing-tasks/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/{self.workflow_task.workflow_task['id']}/participant-view/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        resp_json = resp.json()
        readwrite_columns_keys = [col['key'] for col in (resp_json.get('readwrite_columns') or [])]
        assert self.table.number_column['key'] in readwrite_columns_keys

        self.base.base.delete_column(self.table.table['name'], self.table.number_column['key'])

        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/ongoing-tasks/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        url = f"{SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow.workflow['token']}/tasks/{self.workflow_task.workflow_task['id']}/participant-view/"
        resp = requests.get(url, headers=self.account.token_headers)
        assert resp.ok
        resp_json = resp.json()
        readwrite_columns_keys = [col['key'] for col in (resp_json.get('readwrite_columns') or [])]
        assert self.table.number_column['key'] not in readwrite_columns_keys

    def run(self):
        self.account = Account(TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, SERVER_URL)
        self.account.auth()
        self.account.load_account_info()

        self.base = Base(self.account, 'test-workflow', TEST_WORKFLOW_GROUP_NAME)
        self.table = Table(self.base)
        self.workflow = Workflow(self.base, self.table, 'test-workflow')
        self.workflow.update_workflow_config(self.account)

        try:
            self.test_invalid_form_column_task_detail()
        except Exception as e:
            logging.exception(e)
        finally:
            self.base.delete()


def main():
    test_results = []

    test_error = ''
    is_pass = True

    try:
        workflow_test = WorkflowTest()
        workflow_test.run()
        test_results.extend(workflow_test.test_results)

        workflow_task_test = WorkflowTaskTest()
        workflow_task_test.run()
        test_results.extend(workflow_task_test.test_results)

        workflow_task_view_test = WorkflowTaskViewTest()
        workflow_task_view_test.run()
        test_results.extend(workflow_task_view_test.test_results)

        workflow_task_list_test = WorkflowTaskListTest()
        workflow_task_list_test.run()
        test_results.extend(workflow_task_list_test.test_results)

        invalid_task_in_ongoing_list_test = InvalidTaskInOngoingListTest()
        invalid_task_in_ongoing_list_test.run()
        test_results.extend(invalid_task_in_ongoing_list_test.test_results)

        invalid_form_column_task_detail_test = InvalidFormColumnTaskDetailTest()
        invalid_form_column_task_detail_test.run()
        test_results.extend(invalid_form_column_task_detail_test.test_results)

    except Exception as e:
        test_error = traceback.format_exc()
        is_pass = False
    else:
        is_pass = all([item['is_pass'] for item in test_results])

    if LOCAL_TEST:
        [print(item) for item in test_results]
    else:
        lines = []
        for item in test_results:
            tmp_lines = []
            tmp_lines.append(f"name: {item['name']}")
            if item.get('describe'):
                tmp_lines.append(f"describe: {item['describe']}")
            tmp_lines.append(f"is_pass: {item['is_pass']}")
            if item.get('error'):
                tmp_lines.append(f"error: {item['error']}")
            lines.append('\n'.join(tmp_lines))

        if test_error:
            detail = '\n'.join(lines + ['\n\n\n', test_error])
        else:
            detail = '\n'.join(lines)

        detail = f"```\n{detail}\n```"
        base = _Base(BASE_API_TOKEN_FOR_WORKFLOW, SERVER_URL)
        base.auth()
        base.append_row('TestResults', {'detail': detail, 'is_pass': is_pass})


if __name__ == '__main__':
    main()
