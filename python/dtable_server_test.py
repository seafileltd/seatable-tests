import requests
from seatable_api import Base, context
from constants import DTABLE_SERVER_URL, DTABLE_WEB_SERVICE_URL, \
    TEST_USER_EMAIL, TEST_USER_PASSWORD, \
    TEST_READ_ONLY_USER_EMAIL, TEST_READ_ONLY_USER_PASSWORD, TEST_TABLE_NAME

class DTableServerTest(object):

    def __init__(self):
        self.dtable_uuid = ''
        self.workspace_id = ''

        self.auth_token = ''
        self.dtable_access_token = ''

        self.read_auth_token = ''
        self.read_dtable_access_token = ''


        self.table_id = ''
        self.row_id = ''
        self.comment_id = ''

    def _format_error_msg(self, api_url, api_name, msg):
        return "[API:%s][URL: %s] error: %s" % (api_name, api_url, msg)

    def _format_header(self, token):
        return {
            "Authorization": 'Token %s' % token
        }

    def _ping_test(self, name, url):
        success, error_msg = False, None
        try:
            res = requests.get(url)
            status_code = res.status_code
            if status_code == 200:
                success = True
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)
        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    # Base ping test for dtable-web and dtable-server
    def dtable_server_ping_test(self):
        name = 'dtable server ping'
        url = DTABLE_SERVER_URL.rstrip('/') + '/ping/'
        return self._ping_test(name, url)

    def dtable_web_ping_test(self):
        name = 'dtable web ping'
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api2/ping/'
        return self._ping_test(name, url)


    # API test for dtable-web, including user authorization, add base, share base, delete base and so on
    def dtable_web_auth_token_test(self):
        name = 'dtable web auth token'
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api2/auth-token/'
        success, error_msg = False, None
        request_data = {
            'username': TEST_USER_EMAIL,
            'password': TEST_USER_PASSWORD
        }
        try:
            res = requests.post(
                url,
                data=request_data
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
                auth_token = res.json().get('token')
                self.auth_token = auth_token
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)
        return success, error_msg

    def dtable_web_auth_token_readonly_test(self):
        name = 'dtable web readonly auth token'
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api2/auth-token/'
        success, error_msg = False, None
        request_data = {
            'username': TEST_READ_ONLY_USER_EMAIL,
            'password': TEST_READ_ONLY_USER_PASSWORD
        }
        try:
            res = requests.post(
                url,
                data=request_data
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
                auth_token = res.json().get('token')
                self.read_auth_token = auth_token
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)
        return success, error_msg

    def get_workspaces_test(self):
        name = "dtable web get workspaces"
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/workspaces/'
        success, error_msg = False, None
        headers = self._format_header(self.auth_token)
        try:
            res = requests.get(
                url,
                headers=headers
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
                workspaces = res.json().get('workspace_list')
                for workspace in workspaces:
                    if workspace.get('type') == 'personal':
                        self.workspace_id = workspace.get('id')
                        break

            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)
        return success, error_msg

    def create_base_test(self):
        name = "dtable web create base"
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/dtables/'
        success, error_msg = False, None
        request_data = {
            'name': TEST_TABLE_NAME,
            'owner': TEST_USER_EMAIL,
        }
        headers = self._format_header(self.auth_token)
        try:
            res = requests.post(
                url,
                data=request_data,
                headers=headers,
            )
            status_code = res.status_code
            if status_code == 201:
                success = True
                # workspace_id = res.json().get('table', {}).get('workspace_id', None)
                # self.workspace_id = workspace_id
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def get_base_access_token_test(self):
        name = 'dtable web get base access token'
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/workspace/%s/dtable/%s/access-token/' % (
            self.workspace_id,
            TEST_TABLE_NAME
        )
        success, error_msg = False, None
        headers = self._format_header(self.auth_token)
        try:
            res = requests.get(
                url,
                headers=headers,
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
                access_token = res.json().get('access_token')
                dtable_uuid = res.json().get('dtable_uuid')
                self.dtable_access_token = access_token
                self.dtable_uuid = dtable_uuid
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def share_base_to_readonly_user_test(self):
        name = 'dtable web share base to readonly user'
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/workspace/%s/dtable/%s/share/' % (
            self.workspace_id,
            TEST_TABLE_NAME
        )
        success, error_msg = False, None
        headers = self._format_header(self.auth_token)
        request_data = {
            'email': TEST_READ_ONLY_USER_EMAIL,
            'permission': 'r'
        }
        try:
            res = requests.post(
                url,
                data=request_data,
                headers=headers,
            )
            status_code = res.status_code
            if status_code == 201:
                success = True
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def get_base_readonly_access_token_test(self):
        name = 'dtable web get base readonly access token'
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/workspace/%s/dtable/%s/access-token/' % (
            self.workspace_id,
            TEST_TABLE_NAME
        )
        success, error_msg = False, None
        headers = self._format_header(self.read_auth_token)
        try:
            res = requests.get(
                url,
                headers=headers,
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
                access_token = res.json().get('access_token')
                self.read_dtable_access_token = access_token
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def delete_base_test(self):
        name = "dtable web delete base"
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/workspace/%s/dtable/' % self.workspace_id
        success, error_msg = False, None
        request_data = {
            'name': TEST_TABLE_NAME,
        }
        headers = self._format_header(self.auth_token)
        try:
            res = requests.delete(
                url,
                data=request_data,
                headers=headers,
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg


    # API test for dtable-server, including get row, add row, update row, delete row and so on
    def get_dtable_test(self):
        name = 'get dtable test'
        url = DTABLE_SERVER_URL.rstrip('/') + "/dtables/%s/" % self.dtable_uuid
        success, error_msg = False, None
        headers = self._format_header(self.dtable_access_token)
        try:
            res = requests.get(
                url,
                headers=headers
            )
            status_code = res.status_code
            if status_code == 200:
                tables = res.json().get('tables')
                if tables:
                    table = tables[0]
                    table_name = table.get('name', '')
                    if table_name == 'Table1':
                        success = True
                        self.table_id = table.get('_id')
                        self.row_id = table.get('rows')[0].get('_id')

                    else:
                        err = 'Unexpected table name : %s, expected %s' % (table_name, 'Table1')
                        error_msg = self._format_error_msg(url, name, err)
                else:
                    err = 'Base is empty'
                    error_msg = self._format_error_msg(url, name, err)

            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)
        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def _create_row(self, name, token, expected_status_code=200):
        url = DTABLE_SERVER_URL.rstrip('/') + "/api/v1/dtables/%s/rows/" % self.dtable_uuid
        success, error_msg = False, None
        headers = self._format_header(token)
        headers['Content-Type'] = 'application/json'
        json_data = {
            "row": {
                'Name': 'I am a new row'
            },
            "table_name": 'Table1'
        }

        try:
            res = requests.post(
                url,
                json=json_data,
                headers=headers
            )
            status_code = res.status_code
            if status_code == expected_status_code:
                success = True
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, expected_status_code)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def _update_row(self, name, token, expected_status_code=200):
        url = DTABLE_SERVER_URL.rstrip('/') + "/api/v1/dtables/%s/rows/" % self.dtable_uuid
        success, error_msg = False, None
        headers = self._format_header(token)
        headers['Content-Type'] = 'application/json'
        json_data = {
            "row": {
                'Name': 'I am updated'
            },
            "table_name": 'Table1',
            "row_id": self.row_id,
        }

        try:
            res = requests.put(
                url,
                json=json_data,
                headers=headers
            )
            status_code = res.status_code
            if status_code == expected_status_code:
                success = True
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, expected_status_code)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def _delete_row(self, name, token, expected_status_code=200):
        url = DTABLE_SERVER_URL.rstrip('/') + "/api/v1/dtables/%s/rows/" % self.dtable_uuid
        success, error_msg = False, None
        headers = self._format_header(token)
        headers['Content-Type'] = 'application/json'
        json_data = {
            "table_name": 'Table1',
            "row_id": self.row_id,
        }

        try:
            res = requests.delete(
                url,
                json=json_data,
                headers=headers
            )
            status_code = res.status_code
            if status_code == expected_status_code:
                success = True
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, expected_status_code)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg



    def user_create_row_test(self):
        name  = "user create row"
        return self._create_row(name, self.dtable_access_token, expected_status_code=200)

    def readonly_user_create_row_test(self):
        name  = "readonly user create row"
        return self._create_row(name, self.read_dtable_access_token, expected_status_code=403)

    def user_update_row_test(self):
        name = "user update row"
        return self._update_row(name, self.dtable_access_token, expected_status_code=200)

    def readonly_user_update_row_test(self):
        name = "readonly user update row"
        return self._update_row(name, self.read_dtable_access_token, expected_status_code=403)

    def user_delete_row_test(self):
        name = "user delete row"
        return self._delete_row(name, self.dtable_access_token, expected_status_code=200)

    def readonly_user_delete_row_test(self):
        name = "readonly user delete row"
        return self._delete_row(name, self.read_dtable_access_token, expected_status_code=403)

    def filter_row_test(self):
        name = "filter row test"
        url = DTABLE_SERVER_URL.rstrip('/') + "/api/v1/dtables/%s/filtered-rows/?table_name=Table1" % self.dtable_uuid
        success, error_msg = False, None
        headers = self._format_header(self.dtable_access_token)
        headers['Content-Type'] = 'application/json'
        json_data = {
            "filters": [
                {
                    "column_name": "Name",
                    "filter_predicate": "contains",
                    "filter_term": "I am"
                }
            ],
            "filter_conjunction": "And"
        }

        try:
            res = requests.get(
                url,
                json=json_data,
                headers=headers
            )
            status_code = res.status_code
            if status_code == 200:
                rows = res.json().get('rows')
                row_value = rows[-1].get('Name')
                if row_value == 'I am a new row':
                    success = True
                else:
                    err = 'Unexpected filter content : %s, expected %s' % (row_value, 'I am a new row')
                    error_msg = self._format_error_msg(url, name, err)

            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def add_row_comment_test(self):
        name = "add row comment"
        url = DTABLE_SERVER_URL.rstrip('/') + '/api/v1/dtables/%s/comments/?row_id=%s&table_id=%s' % (
            self.dtable_uuid,
            self.row_id,
            self.table_id,
        )
        success, error_msg = False, None
        request_data = {"comment": "test comment info"}
        headers = self._format_header(self.dtable_access_token)
        headers['Content-Type'] = 'application/json'
        try:
            res = requests.post(
                url,
                json=request_data,
                headers=headers,
            )
            status_code = res.status_code
            if status_code == 200:
                result_success = res.json().get('success')
                if result_success:
                    success = True
                else:
                    err = 'Unexpected response : %s, expected %s' % (result_success, 'True')
                    error_msg = self._format_error_msg(url, name, err)
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def get_row_comment_test(self):
        name = "get row comment"
        url = DTABLE_SERVER_URL.rstrip('/') + '/api/v1/dtables/%s/comments/?row_id=%s' % (
            self.dtable_uuid,
            self.row_id,
        )
        success, error_msg = False, None
        headers = self._format_header(self.dtable_access_token)
        headers['Content-Type'] = 'application/json'
        try:
            res = requests.get(
                url,
                headers=headers,
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
                comments = res.json()
                self.comment_id = comments and comments[0] and comments[0].get('id') or ''
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg


    def delete_row_comment_test(self):
        name = "delete row comment"
        url = DTABLE_SERVER_URL.rstrip('/') + '/api/v1/dtables/%s/comments/%s/' % (
            self.dtable_uuid,
            self.comment_id
        )
        success, error_msg = False, None
        headers = self._format_header(self.dtable_access_token)
        headers['Content-Type'] = 'application/json'
        try:
            res = requests.delete(
                url,
                headers=headers,
            )
            status_code = res.status_code
            if status_code == 200:
                result_success = res.json().get('success')
                if result_success:
                    success = True
                else:
                    err = 'Unexpected response : %s, expected %s' % (result_success, 'True')
                    error_msg = self._format_error_msg(url, name, err)
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)

        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def run(self, print_out=True):
        test_funcs_in_order = [
            # ping test
            self.dtable_server_ping_test,
            self.dtable_web_ping_test,

            # dtable-web-test user
            self.dtable_web_auth_token_test,
            self.get_workspaces_test,
            self.create_base_test,
            self.get_base_access_token_test,

            # dtable-web-test readonly user
            self.dtable_web_auth_token_readonly_test,
            self.share_base_to_readonly_user_test,
            self.get_base_readonly_access_token_test,

            # dtable-server-test user
            self.get_dtable_test,
            self.user_create_row_test,
            self.filter_row_test,
            self.add_row_comment_test,
            self.get_row_comment_test,
            self.delete_row_comment_test,
            self.user_update_row_test,
            self.user_delete_row_test,



            # dtable-server-test readonly user
            self.readonly_user_create_row_test,
            self.readonly_user_update_row_test,
            self.readonly_user_delete_row_test,



            # finally the test base should be deleted
            self.delete_base_test
        ]
        pass_num, fail_num, error_list = 0, 0, []
        for func in test_funcs_in_order:
            success, err_msg = func()
            if print_out:
                print(success, err_msg)
            if success:
                pass_num += 1
            else:
                fail_num += 1

            if err_msg:
                error_list.append(err_msg)


        test_result = {
            'SuccessNo': pass_num,
            'FailNo': fail_num,
            'ErrorMsg': error_list and "\n\n".join(error_list) or "",
        }

        return test_result


if __name__ == '__main__':

    LOCAL_TEST = False

    dst = DTableServerTest()
    test_result = dst.run(print_out=LOCAL_TEST)

    Table_name = 'DTableServerTest'

    if not LOCAL_TEST:
        api_token = context.api_token or "4e118011faa89319b07e426204925d7585dd5037"
        server_url = context.server_url or "https://dev.seatable.cn/"

        base = Base(api_token, server_url)
        base.auth()
        base.append_row(Table_name, test_result)

