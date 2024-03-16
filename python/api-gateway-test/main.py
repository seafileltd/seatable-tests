from seatable_api import Base
import requests
import time
SERVER_URL = "https://dev.seatable.cn"
API_TOKEN = "1e1ef4db90af4fa73025e8b6f1541f15e1fa0216"

TEST_RESULTS_TABLE_NAME = "TestResults"
TABLE_NAME = 'Table'
LINK_TABLE_NAME = 'LinkTable'

class APIGatewayTest(object):

    TEST_TYPE = None



    def __init__(self, base):

        self.base = base
        self.dtable_uuid = base.dtable_uuid
        self.headers = base.headers



    def format_url(self, api_url):

        gateway_url = "%s/api-gateway" % SERVER_URL
        return "%s/%s" % (gateway_url, api_url.lstrip('/'))


class APIGatewayMetaTest(APIGatewayTest):

    #  api-gateway functions designed by dtable-db

    TEST_TYPE = 'api-gateway-db'

    def __init__(self, base):
        super(APIGatewayMetaTest, self).__init__(base)

        self.tmp_rows = []

    def format_infos(self, test_name, success, other_infos=None):
        return {
            "Functions": test_name,
            "API-Type": self.TEST_TYPE,
            "Success": "Yes" if success else "No",
            "Details": "%s" % other_infos
        }

    def list_rows(self):
        api_url = self.format_url('/api/v2/dtables/%s/rows' % self.dtable_uuid)
        params = {
            'table_name': TABLE_NAME
        }
        resp = requests.get(api_url, params=params, headers=self.headers)

        success, detail = False, ''
        if resp.status_code == 200:
            success = True
            self.tmp_rows = resp.json().get('rows')
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'list-rows',
            success,
            detail
        )

    def add_rows(self):
        api_url = self.format_url('/api/v2/dtables/%s/batch-append-rows/' % self.dtable_uuid)
        data = {
            'table_name': TABLE_NAME,
            'rows': [
                {'Name': 'AA-%s' % str(int(time.time()))}
            ]
        }
        resp = requests.post(api_url, json=data, headers=self.headers)

        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'batch-append-rows',
            success,
            detail
        )


    def add_rows_to_bgs(self):
        # insert rows in bigdata storage
        api_url = self.format_url('/api/v2/dtables/%s/insert-archived-rows/' % self.dtable_uuid)
        data = {
            'table_name': TABLE_NAME,
            'rows': [
                {'Name': 'AA-bigdata-%s' % str(int(time.time()))}
            ]
        }
        resp = requests.post(api_url, json=data, headers=self.headers)

        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'insert-rows-into-bgs',
            success,
            detail
        )

    def update_rows(self):
        api_url = self.format_url('/api/v2/dtables/%s/rows/' % self.dtable_uuid)
        data = {
            'table_name': TABLE_NAME,
            'updates':[
                {
                    "row_id": self.tmp_rows[0]['_id'],
                    "row":{'Name': 'AA-update-rows-%s' % str(int(time.time()))}
                }
            ]
        }
        resp = requests.put(api_url, json=data, headers=self.headers)

        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'update-rows',
            success,
            detail
        )


    def run_workflow(self):
        # Test workflows for running the test functions
        workflows = [
            self.list_rows,
            self.add_rows,
            self.add_rows_to_bgs,
            self.update_rows
        ]

        for func in workflows:
            row_data = func()
            self.base.append_row(TEST_RESULTS_TABLE_NAME, row_data)




class APIGatewayProxyTest(APIGatewayTest):

    # api-gateway functions as proxy of dtable-server

    TEST_TYPE = 'dtable-server-proxy'


    def __init__(self, base):
        super(APIGatewayProxyTest, self).__init__(base)

        self.tmp_columns = []

    def format_infos(self, test_name, success, other_infos=None):
        return {
            "Functions": test_name,
            "API-Type": self.TEST_TYPE,
            "Success": "Yes" if success else "No",
            "Details": "%s" % other_infos
        }

    def list_columns(self):
        api_url = self.format_url('/api/v2/dtables/%s/columns' % self.dtable_uuid)
        params = {
            'table_name': TABLE_NAME
        }
        resp = requests.get(api_url, params=params, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            self.tmp_columns = resp.json().get('columns')
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'list-columns',
            success,
            detail
        )

    def insert_column(self):
        api_url = self.format_url('/api/v2/dtables/%s/columns/' % self.dtable_uuid)

        data = {
            'table_name': TABLE_NAME,
            'column_name': 'Col_New_%s' % str(int(time.time()))[4:]
        }
        resp = requests.post(api_url, json=data, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'insert-columns',
            success,
            detail
        )


    def run_workflow(self):
        # Test workflows for running the test functions
        workflows = [
            self.list_columns,
            self.insert_column,
        ]

        for func in workflows:
            row_data = func()
            self.base.append_row(TEST_RESULTS_TABLE_NAME, row_data)



if __name__ == '__main__':

    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    test_db = APIGatewayMetaTest(base)
    test_proxy = APIGatewayProxyTest(base)

    test_db.run_workflow()
    test_proxy.run_workflow()

