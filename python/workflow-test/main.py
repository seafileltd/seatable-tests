import json
import os
import sys
current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_script_dir)
sys.path.append(parent_dir)


import requests
from seatable_api import Base, Account
from seatable_api.constants import ColumnTypes

from local_settings import TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, TEST_WORKFLOW_SERVER_URL, TEST_WORKFLOW_GROUP_NAME, LOCAL_TEST


class TestBase:

    def __init__(self, account: Account, name: str, group_name: str):
        self.account = account
        self.name = name
        workspace_list = account.list_workspaces()['workspace_list']
        self.workspace = next(filter(lambda workspace: workspace['name'] == group_name and workspace['is_admin'], workspace_list), None)
        assert self.workspace
        resp = self.account.add_base(name, self.workspace['id'])
        assert resp
        self.base: Base = account.get_base(self.workspace['id'], name)
        assert self.base

    def delete_base(self):
        url = f"{TEST_WORKFLOW_SERVER_URL.strip('/')}/api/v2.1/workspace/{self.workspace['id']}/dtable/"
        resp = requests.delete(url, headers=self.account.token_headers, json={'name': self.name})
        assert resp.ok


class TestTable:

    def __init__(self, test_base: TestBase, new_table_name=None):
        self.test_base = test_base
        if new_table_name:
            self.table = self.test_base.base.add_table(new_table_name)
            self.table_id = self.table['_id']
        else:
            self.table_id = '0000'
            self.table = self.test_base.base.get_metadata()['tables'][0]

        self.participants_column_name = 'participants'
        self.participants_column = self.test_base.base.insert_column(self.table_id, self.participants_column_name, ColumnTypes.COLLABORATOR)
        assert self.participants_column

        self.state_column_name = 'state'
        self.state_column = self.test_base.base.insert_column(self.table_id, self.state_column_name, ColumnTypes.SINGLE_SELECT)
        assert self.state_column

        self.text_column_name = 'text'
        self.text_column = self.test_base.base.insert_column(self.table_id, self.text_column_name, ColumnTypes.TEXT)
        assert self.text_column

        self.collaborator_column_name = 'collaborator'
        self.collaborator_column = self.test_base.base.insert_column(self.table_id, self.collaborator_column_name, ColumnTypes.COLLABORATOR)
        assert self.collaborator_column


class TestWorkflow:

    def __init__(self, test_base: TestBase, test_table: TestTable, name: str):
        self.workflow = None
        self.test_base = test_base
        self.test_table = test_table
        self.name = name

        data = {
            'workspace_id': self.test_base.workspace['id'],
            'name': self.test_base.name,
            'workflow_config': json.dumps(self.gen_init_workflow_config())
        }

        url = f"{TEST_WORKFLOW_SERVER_URL.strip('/')}/api/v2.1/workflows/"
        resp = requests.post(url, headers=test_base.account.token_headers, data=data)
        assert resp.ok
        self.workflow = resp.json()['workflow']
        assert self.workflow

    def gen_init_workflow_config(self):
        return {
            'workflow_name': self.name,
            'table_id': '0000',
            'state_column_key': self.test_table.state_column['key'],
            'participants_column_key': self.test_table.participants_column['key'],
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
                            {'key': self.test_table.text_column['key']},
                            {'key': self.test_table.collaborator_column['key']},
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
                            {'key': self.test_table.text_column['key']},
                            {'key': self.test_table.collaborator_column['key']},
                        ]
                    }
                },
                {
                    '_id': '54420',
                    'type': 'normal',
                    'name': 'Node1',
                    'participants': [self.test_base.account.username],
                    'participants_type': 'static',
                    'node_participants_column_key': '',
                    'next_node_id': '1',
                    'conditional_next_nodes': [],
                    'node_form': {
                        'readwrite_columns': [
                            {'key': '0000'},
                            {'key': self.test_table.text_column['key']},
                            {'key': self.test_table.collaborator_column['key']},
                        ],
                        'readonly_columns': []
                    }
                }
            ]
        }

    def update_workflow_name(self, name: str, account: Account):
        url = f"{TEST_WORKFLOW_SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow['token']}/"
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
        workflow_config['nodes'][2]['node_participants_column_key'] = self.test_table.collaborator_column['key']
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
                    {'key': self.test_table.text_column['key']},
                    {'key': self.test_table.collaborator_column['key']},
                ],
                'readonly_columns': []
            }
        })
        url = f"{TEST_WORKFLOW_SERVER_URL.strip('/')}/api/v2.1/workflows/{self.workflow['token']}/"
        data = {'workflow_config': json.dumps(workflow_config)}
        resp = requests.put(url, headers=account.token_headers, data=data)
        assert resp.ok
        workflow = resp.json()['workflow']
        assert workflow
        self.workflow = workflow


class TestWorkflowTask:

    def __init__(self, test_base: TestBase, test_table: TestTable, test_workflow: TestWorkflow, initiator_account: Account, workflow_task: dict):
        self.test_base = test_base
        self.test_table = test_table
        self.test_workflow = test_workflow
        self.initiator_account = initiator_account

        self.workflow_task = workflow_task

    @classmethod
    def submit_workflow_task(cls, test_base: TestBase, test_table: TestTable, test_workflow: TestWorkflow, initiator_account: Account, form_data: dict):
        url = f"{TEST_WORKFLOW_SERVER_URL.strip('/')}/api/v2.1/workflows/{test_workflow.workflow['token']}/task-submit/"
        data = {'row_data': json.dumps(form_data)}
        resp = requests.post(url, headers=initiator_account.token_headers, data=data)
        assert resp.ok
        workflow_task = resp.json()['task']
        assert workflow_task
        sql = f"SELECT * FROM `{test_table.table['name']}` WHERE _id='{workflow_task['row_id']}'"
        rows = test_base.base.query(sql)
        assert rows
        test_workflow_task = cls(test_base, test_table, test_workflow, initiator_account, workflow_task)
        test_workflow_task.reload_workflow_task()
        test_workflow_task.check_row()
        return test_workflow_task

    def test_initiatied_tasks(self):
        url = f"{TEST_WORKFLOW_SERVER_URL.strip('/')}/api/v2.1/workflows/{self.test_workflow.workflow['token']}/tasks/"
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

    def reload_workflow_task(self):
        return self.test_initiatied_tasks()

    def check_row(self):
        sql = f"SELECT `{self.test_table.state_column_name}`, `{self.test_table.participants_column_name}` FROM `{self.test_table.table['name']}` WHERE _id='{self.workflow_task['row_id']}'"
        results = self.test_base.base.query(sql)
        assert results
        assert results[0].get(self.test_table.state_column_name) == self.workflow_task['current_node']['name']
        assert (results[0].get(self.test_table.participants_column_name) or []) == [item['email'] for item in self.workflow_task['participants']]

    def test_transfer_task(self, transfer_account: Account, row_data: dict):
        url = f"{TEST_WORKFLOW_SERVER_URL.strip('/')}/api/v2.1/workflows/{self.test_workflow.workflow['token']}/tasks/{self.workflow_task['id']}/transfer/"
        data = {
            'row_data': json.dumps(row_data),
            'node_id': self.workflow_task['node_id']
        }
        resp = requests.post(url, headers=transfer_account.token_headers, data=data)
        assert resp.ok
        self.reload_workflow_task()
        self.check_row()


def main():
    account = Account(TEST_WORKFLOW_USER_EMAIL, TEST_WORKFLOW_USER_PWD, TEST_WORKFLOW_SERVER_URL)
    account.auth()
    account.load_account_info()

    test_base = TestBase(account, 'test-workflow', TEST_WORKFLOW_GROUP_NAME)
    test_table = TestTable(test_base)
    try:
        test_workflow = TestWorkflow(test_base, test_table, 'test-workflow')

        test_workflow.update_workflow_name('new-test-workflow', test_base.account)
        test_workflow.update_workflow_name('test-workflow', test_base.account)
        test_workflow.update_workflow_config(test_base.account)

        test_workflow_task = TestWorkflowTask.submit_workflow_task(test_base, test_table, test_workflow, account, {test_table.text_column_name: 'abc'})

        test_workflow_task.test_transfer_task(test_base.account, {test_table.text_column_name: 'def'})
    except Exception as e:
        raise e
    finally:
        test_base.delete_base()


if __name__ == '__main__':
    main()
