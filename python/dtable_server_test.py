import requests
from seatable_api import Base, context
from constants import DTABLE_SERVER_API_URL, DTABLE_SERVER_URL,DTABLE_WEB_SERVICE_URL, \
    TEST_USER_EMAIL, TEST_USER_PASSWORD, \
    TEST_READ_ONLY_USER_EMAIL, TEST_READ_ONLY_USER_PASSWORD, TEST_TABLE_NAME, ENABLE_CLUSTER, \
    API_TOKEN_NAME_1, API_TOKEN_NAME_2, API_GATEWAY_URL, LOCAL_TEST


if ENABLE_CLUSTER:
    dtable_server_api_url = DTABLE_SERVER_API_URL
else:
    dtable_server_api_url = DTABLE_SERVER_URL


class DTableServerTest(object):

    def __init__(self):
        self.dtable_uuid = ''
        self.workspace_id = ''

        self.auth_token = ''
        self.dtable_access_token = ''

        self.read_auth_token = ''
        self.read_dtable_access_token = ''


        self.table_id = ''
        self.row_id = ''  # row created by user
        self.app_row_id = ''  # row created by app-1
        self.app_batch_row_id = ''  # row batched created by app-1
        self.api_gateway_app_row_id = ''  # row created by app-1 through api-gateway

        self.comment_id = ''

        self.username = ''
        self.readonly_username = ''

        self.api_token_dict = {}

        self.dtable_server_api_url = ''

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
        url = self.dtable_server_api_url.rstrip('/') + '/api/v2/ping/'
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

    def get_user_info_test(self):
        name = "dtable web get user info"
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/user/'
        success, error_msg = False, None
        headers = self._format_header(self.auth_token)
        try:
            res = requests.get(
                url,
                headers = headers
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
                self.username = res.json().get('email')
            else:
                err = 'Unexpected status code : %s, expected %s' % (status_code, 200)
                error_msg = self._format_error_msg(url, name, err)
        except Exception as err:
            error_msg = self._format_error_msg(url, name, err)
        return success, error_msg

    def get_readonly_user_info_test(self):
        name = "dtable web get user info"
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/user/'
        success, error_msg = False, None
        headers = self._format_header(self.read_auth_token)
        try:
            res = requests.get(
                url,
                headers = headers
            )
            status_code = res.status_code
            if status_code == 200:
                success = True
                self.readonly_username = res.json().get('email')
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
            'owner': self.username,
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
            'email': self.readonly_username,
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


    # API test for dtable-api-gateway, including get row, add row, update row, delete row and so on
    def get_dtable_test(self):
        name = 'get dtable test'
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/" % self.dtable_uuid
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
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        success, error_msg = False, None
        headers = self._format_header(token)
        headers['Content-Type'] = 'application/json'
        json_data = {
            "rows": [{
                'Name': 'I am a new row'
            }],
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
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        success, error_msg = False, None
        headers = self._format_header(token)
        headers['Content-Type'] = 'application/json'
        # json_data = {
        #     "row": {
        #         'Name': 'I am updated'
        #     },
        #     "table_name": 'Table1',
        #     "row_id": self.row_id,
        # }

        json_data = {
            'table_name': 'Table1',
            'updates': [
                {
                    'row_id': self.row_id,
                    'row': {
                        'Name': 'I am updated'
                    }
                }
            ]
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
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        success, error_msg = False, None
        headers = self._format_header(token)
        headers['Content-Type'] = 'application/json'
        json_data = {
            "table_name": 'Table1',
            "row_ids": [self.row_id],
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
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/filtered-rows/?table_name=Table1" % self.dtable_uuid
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
        url = DTABLE_WEB_SERVICE_URL.rstrip('/').rstrip('/') + '/api/v2.1/dtables/%s/comments/' % (
            self.dtable_uuid,
        )
        success, error_msg = False, None
        request_data = {"comment": "test comment info", "row_id": self.row_id, "table_id": self.table_id}
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
        url = self.dtable_server_api_url.rstrip('/') + '/api/v2/dtables/%s/comments/?row_id=%s' % (
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

    def api_token_test(self):
        name = 'create api token'
        success, error_msg = False, None
        for api_token_name in [API_TOKEN_NAME_1, API_TOKEN_NAME_2]:
            url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/workspace/%s/dtable/%s/api-tokens/' % (
                self.workspace_id,
                TEST_TABLE_NAME
            )
            data = {
                'app_name': api_token_name,
                'permission': 'rw'
            }
            headers = self._format_header(self.auth_token)
            try:
                res = requests.post(url, json=data, headers=headers)
                if not res.ok:
                    error_msg = self._format_error_msg(url, name, 'Unexpected api token: %s status code: %s response: %s' % (api_token_name, res.status_code, res.text))
                else:
                    self.api_token_dict[api_token_name] = {'api_token': res.json()['api_token']}
                    success = True
            except Exception as err:
                error_msg = self._format_error_msg(url, name, err)

        return success, error_msg

    def app_access_token_test(self):
        name = 'app access token'
        url = DTABLE_WEB_SERVICE_URL.rstrip('/') + '/api/v2.1/dtable/app-access-token/'
        success, error_msg = False, None
        for info in self.api_token_dict.values():
            headers = self._format_header(info['api_token'])
            try:
                res = requests.get(url, headers=headers)
                if not res.ok:
                    error_msg = self._format_error_msg(url, name, 'Unexpected status code: %s response: %s' % (res.status_code, res.text))
                else:
                    success = True
                    info['access_token'] = res.json()['access_token']
                    if not self.dtable_server_api_url:
                        self.dtable_server_api_url = res.json()['dtable_server']
            except Exception as err:
                error_msg = self._format_error_msg(url, name, err)
        return success, error_msg

    def append_row_creator_modifier_test(self):
        name = 'append row test creator modifier'

        api_name = API_TOKEN_NAME_1
        api_token_info = self.api_token_dict.get(api_name)
        if not api_token_info or not api_token_info.get('api_token') or not api_token_info.get('access_token'):
            return False, self._format_error_msg(None, name, 'api %s info: %s not created or no access token' % (api_name, api_token_info))

        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        headers = self._format_header(api_token_info['access_token'])
        data = {
            'table_name': 'Table1',
            'rows': [{
                'Name': 'From %s' % api_name
            }]
        }
        try:
            res = requests.post(url, headers=headers, json=data)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected status code: %s response: %s' % (res.status_code, res.text))
            self.app_row_id = res.json()['row_ids'][0]['_id']
            row = res.json()['first_row']
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        if not (row.get('_creator') == row.get('_last_modifier') == api_name):
            return False, self._format_error_msg(url, name, '_creator: %s _last_modifier: %s api_token_name: %s' % (
                row.get('_creator'), row.get('_last_modifier'), api_name
            ))

        return True, None

    def update_row_creator_modifier_test(self):
        name = 'update row test creator modifier'

        origin_api_name = API_TOKEN_NAME_1
        api_name = API_TOKEN_NAME_2
        api_token_info = self.api_token_dict.get(api_name)
        if not api_token_info or not api_token_info.get('api_token') or not api_token_info.get('access_token'):
            return False, self._format_error_msg(None, name, 'api %s info: %s not created or no access token' % (api_name, api_token_info))
        if not self.app_row_id:
            return False, self._format_error_msg(None, name, 'row created by %s not found' % origin_api_name)

        # update
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        headers = self._format_header(api_token_info['access_token'])
        # data = {
        #     'table_name': 'Table1',
        #     'row_id': self.app_row_id,
        #     'row': {
        #         'Name': 'Updated by %s' % api_name
        #     }
        # }

        data = {
            'table_name': 'Table1',
            'updates': [
                {
                    'row_id': self.app_row_id,
                    'row': {
                        'Name': 'Updated by %s' % api_name
                    }
                }
            ]
        }
        
        try:
            res = requests.put(url, headers=headers, json=data)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected update row status code: %s response: %s' % (res.status_code, res.text))
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        # get
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/%s/" % (self.dtable_uuid, self.app_row_id)
        headers = self._format_header(api_token_info['access_token'])
        params = {
            'table_name': 'Table1'
        }
        try:
            res = requests.get(url, headers=headers, params=params)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected get row status code: %s response: %s' % (res.status_code, res.text))
            row = res.json()
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        if not (row.get('_creator') == origin_api_name and row.get('_last_modifier') == api_name):
            return False, self._format_error_msg(url, name, '_creator: %s _last_modifier: %s api_token_name: %s' % (
                row.get('_creator'), row.get('_last_modifier'), api_name
            ))

        return True, None

    def batch_append_rows_test(self):
        name = 'batch append rows test creator modifier'

        api_name = API_TOKEN_NAME_1
        api_token_info = self.api_token_dict.get(api_name)
        if not api_token_info or not api_token_info.get('api_token') or not api_token_info.get('access_token'):
            return False, self._format_error_msg(None, name, 'api %s info: %s not created or no access token' % (api_name, api_token_info))

        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        headers = self._format_header(api_token_info['access_token'])
        data = {
            'table_name': 'Table1',
            'rows': [{
                'Name': 'From %s' % api_name
            }],
            'return_rows': True
        }
        try:
            res = requests.post(url, headers=headers, json=data)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected batch append rows status code: %s response: %s' % (res.status_code, res.text))
            self.app_batch_row_id = res.json()['row_ids'][0]['_id']
            row = res.json()['first_row']
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        if not (row.get('_creator') == row.get('_last_modifier') == api_name):
            return False, self._format_error_msg(url, name, '_creator: %s _last_modifier: %s api_token_name: %s' % (
                row.get('_creator'), row.get('_last_modifier'), api_name
            ))

        return True, None

    def batch_update_rows_test(self):
        name = 'batch update rows test creator modifier'

        origin_api_name = API_TOKEN_NAME_1
        api_name = API_TOKEN_NAME_2
        api_token_info = self.api_token_dict.get(api_name)
        if not api_token_info or not api_token_info.get('api_token') or not api_token_info.get('access_token'):
            return False, self._format_error_msg(None, name, 'api %s info: %s not created or no access token' % (api_name, api_token_info))
        if not self.app_batch_row_id:
            return False, self._format_error_msg(None, name, 'batch row created by %s not found' % origin_api_name)

        # update
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        headers = self._format_header(api_token_info['access_token'])
        data = {
            'table_name': 'Table1',
            'updates': [
                {
                    'row_id': self.app_batch_row_id,
                    'row': {
                        'Name': 'Updated by %s' % api_name
                    }
                }
            ]
        }
        try:
            res = requests.put(url, headers=headers, json=data)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected batch update rows status code: %s response: %s' % (res.status_code, res.text))
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        # get
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/%s/" % (self.dtable_uuid, self.app_batch_row_id)
        headers = self._format_header(api_token_info['access_token'])
        params = {
            'table_name': 'Table1'
        }
        try:
            res = requests.get(url, headers=headers, params=params)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected get row status code: %s response: %s' % (res.status_code, res.text))
            row = res.json()
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        if not (row.get('_creator') == origin_api_name and row.get('_last_modifier') == api_name):
            return False, self._format_error_msg(url, name, '_creator: %s _last_modifier: %s api_token_name: %s' % (
                row.get('_creator'), row.get('_last_modifier'), api_name
            ))

        return True, None

    def api_gateway_append_rows_test(self):
        name = 'api-gateway append rows test creator modifier'

        api_name = API_TOKEN_NAME_1
        api_token_info = self.api_token_dict.get(api_name)
        if not api_token_info or not api_token_info.get('api_token') or not api_token_info.get('access_token'):
            return False, self._format_error_msg(None, name, 'api %s info: %s not created or no access token' % (api_name, api_token_info))

        # append row
        url = API_GATEWAY_URL.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        headers = self._format_header(api_token_info['access_token'])
        cell_value = 'From api-gateway %s' % api_name
        data = {
            'table_name': 'Table1',
            'rows': [{
                'Name': cell_value
            }]
        }
        try:
            res = requests.post(url, headers=headers, json=data)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected api-gateway append rows status code: %s response: %s' % (res.status_code, res.text))
            if res.json()['inserted_row_count'] != 1:
                return False, self._format_error_msg(url, name, 'Unexpected api-gateway append rows insert rows count %s' % res.json()['inserted_row_count'])
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        # get row
        url = API_GATEWAY_URL.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        headers = self._format_header(api_token_info['access_token'])
        params = {
            'table_name': 'Table1',
            'convert_keys': True
        }
        try:
            res = requests.get(url, headers=headers, params=params)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected api-gateway get rows status code: %s response: %s' % (res.status_code, res.text))
            rows = res.json()['rows']
            row = next(filter(lambda row: row['Name'] == cell_value, rows), None)
            if not row:
                return False, self._format_error_msg(url, name, 'Unexpected api-gateway get no rows')
            self.api_gateway_app_row_id = row['_id']
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        if not (row.get('_creator') == row.get('_last_modifier') == api_name):
            return False, self._format_error_msg(url, name, '_creator: %s _last_modifier: %s api_token_name: %s' % (
                row.get('_creator'), row.get('_last_modifier'), api_name
            ))

        return True, None

    def api_gateway_update_rows_test(self):
        name = 'api-gateway update rows test creator modifier'

        origin_api_name = API_TOKEN_NAME_1
        api_name = API_TOKEN_NAME_2
        api_token_info = self.api_token_dict.get(api_name)
        if not api_token_info or not api_token_info.get('api_token') or not api_token_info.get('access_token'):
            return False, self._format_error_msg(None, name, 'api %s info: %s not created or no access token' % (api_name, api_token_info))
        if not self.api_gateway_app_row_id:
            return False, self._format_error_msg(None, name, 'api-gateway row created by %s not found' % origin_api_name)

        # update
        url = API_GATEWAY_URL.rstrip('/') + "/api/v2/dtables/%s/rows/" % self.dtable_uuid
        headers = self._format_header(api_token_info['access_token'])
        data = {
            'table_name': 'Table1',
            'updates': [
                {
                    'row_id': self.api_gateway_app_row_id,
                    'row': {
                        'Name': 'Updated by %s' % api_name
                    }
                }
            ]
        }
        try:
            res = requests.put(url, headers=headers, json=data)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected api-gateway update rows status code: %s response: %s' % (res.status_code, res.text))
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        # get row
        url = self.dtable_server_api_url.rstrip('/') + "/api/v2/dtables/%s/rows/%s/" % (self.dtable_uuid, self.api_gateway_app_row_id)
        headers = self._format_header(api_token_info['access_token'])
        params = {
            'table_name': 'Table1'
        }
        try:
            res = requests.get(url, headers=headers, params=params)
            if not res.ok:
                return False, self._format_error_msg(url, name, 'Unexpected get row status code: %s response: %s' % (res.status_code, res.text))
            row = res.json()
        except Exception as err:
            return False, self._format_error_msg(url, name, err)

        if not (row.get('_creator') == origin_api_name and row.get('_last_modifier') == api_name):
            return False, self._format_error_msg(url, name, '_creator: %s _last_modifier: %s api_token_name: %s' % (
                row.get('_creator'), row.get('_last_modifier'), api_name
            ))

        return True, None

    def run(self, print_out=True):
        test_funcs_in_order = [
            # ping test
            self.dtable_web_ping_test,

            # dtable-web-test user
            self.dtable_web_auth_token_test,
            self.get_user_info_test,
            self.get_workspaces_test,
            self.create_base_test,
            self.get_base_access_token_test,

            # dtable-web-test readonly user
            self.dtable_web_auth_token_readonly_test,
            self.get_readonly_user_info_test,
            self.share_base_to_readonly_user_test,
            self.get_base_readonly_access_token_test,

            self.api_token_test,
            self.app_access_token_test,

            self.dtable_server_ping_test,

            # dtable-server-test user
            self.get_dtable_test,
            self.user_create_row_test,
            # self.filter_row_test,
            self.add_row_comment_test,
            self.get_row_comment_test,
            self.user_update_row_test,
            self.user_delete_row_test,

            # create api-token, app-access-token
            # and then test _creator, _last_modifier
            self.append_row_creator_modifier_test,
            self.update_row_creator_modifier_test,
            self.batch_append_rows_test,
            self.batch_update_rows_test,
            self.api_gateway_append_rows_test,
            self.api_gateway_update_rows_test,

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
        if print_out:
            print(test_result)
        return test_result


if __name__ == '__main__':

    dst = DTableServerTest()
    test_result = dst.run(print_out=LOCAL_TEST)

    Table_name = 'DTableServerTest'

    if not LOCAL_TEST:
        api_token = context.api_token or "4e118011faa89319b07e426204925d7585dd5037"
        server_url = context.server_url or "https://dev.seatable.cn/"

        base = Base(api_token, server_url)
        base.auth()
        base.append_row(Table_name, test_result)

