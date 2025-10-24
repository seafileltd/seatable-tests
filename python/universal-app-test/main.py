import os
import sys
current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_script_dir)
sys.path.append(parent_dir)


from seatable_api import Base, Account
import requests

from local_settings import TEST_APP_USER_EMAIL, TEST_APP_USER_PWD, SERVER_URL, BASE_API_TOKEN_FOR_APP_TEST, \
    TEST_APP_TMP_APP_USER_EMAIL

API_TOKEN = BASE_API_TOKEN_FOR_APP_TEST
EMAIL = TEST_APP_USER_EMAIL
PWD = TEST_APP_USER_PWD

TMP_APP_USER = TEST_APP_TMP_APP_USER_EMAIL

APP_TOKEN = "f25bf553-5e90-4329-91af-67a3e01e21cc"

TEST_RESULTS_TABLE_NAME = "TestResults"

def get_base():
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()
    return base

def get_account():
    account = Account(EMAIL, PWD, SERVER_URL)
    account.auth()
    return account


class UniversalAppAdminAPITest(object):

    TEST_TYPE = 'admin-api'


    def __init__(self, base, account):

        self.base = base
        self.account = account

        self.tmp_role_id = None

        self.tmp_app_user = TMP_APP_USER
        self.tmp_app_user_id = None
        self.tmp_link_token = None


    @property
    def headers(self):
        return {
            "Authorization": "Token %s" % self.account.token
        }

    def format_infos(self, test_name, success, other_infos=None):
        return {
            "测试功能": test_name,
            "API 类型": self.TEST_TYPE,
            "Success": "Yes" if success else "No",
            "详情": "%s" % other_infos
        }

    def list_users(self):
        url = "%s/api/v2.1/universal-apps/%s/app-users/" % (SERVER_URL.strip('/'), APP_TOKEN)
        resp = requests.get(url, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '列出 APP 用户',
            success,
            detail
        )

    def list_roles(self):
        url = "%s/api/v2.1/universal-apps/%s/app-roles/" % (SERVER_URL.strip('/'), APP_TOKEN)
        resp = requests.get(url, headers=self.headers)
        print(resp.json())
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '列出 APP 角色',
            success,
            detail
        )

    def add_role(self, role_name="test_role_1"):
        url = "%s/api/v2.1/universal-apps/%s/app-roles/" % (SERVER_URL.strip('/'), APP_TOKEN)
        data = {
            "role_name": role_name,
            "permission": "rw"
        }
        resp = requests.post(url, json=data, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
            self.tmp_role_id = resp.json().get('app_role', {}).get('id')
        else:
            success = False
            detail = resp.content

        return self.format_infos(
            '添加 APP 角色',
            success,
            detail
        )

    def put_role(self):
        url = "%s/api/v2.1/universal-apps/%s/app-roles/%s/" % (SERVER_URL.strip('/'), APP_TOKEN, self.tmp_role_id)
        data = {
            "role_name": "test_role_1_modified",
            "permission": "rw"
        }
        resp = requests.put(url, data=data, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '修改 APP 角色名称',
            success,
            detail
        )

    def delete_role(self):
        url = "%s/api/v2.1/universal-apps/%s/app-roles/%s/" % (SERVER_URL.strip('/'), APP_TOKEN, self.tmp_role_id)
        resp = requests.delete(url, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
            self.tmp_role_id = None
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '删除 APP 角色',
            success,
            detail
        )

    def add_user(self):
        url = "%s/api/v2.1/universal-apps/%s/app-users/" % (SERVER_URL.strip('/'), APP_TOKEN)
        data = {
            "app_user": self.tmp_app_user,
            "app_role_id": self.tmp_role_id,
        }
        resp = requests.post(url, json=data, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
            self.tmp_app_user_id = resp.json().get("app_user", {}).get('id')
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '添加 APP 用户',
            success,
            detail
        )

    def put_user(self):
        url = "%s/api/v2.1/universal-apps/%s/app-users/%s/" % (SERVER_URL.strip('/'), APP_TOKEN, self.tmp_app_user_id)
        data = {
            "is_active": 'false'
        }
        resp = requests.put(url, data=data, headers=self.headers)
        print(resp.content)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '修改 APP 用户状态',
            success,
            detail
        )

    def add_invite_link(self):
        url = "%s/api/v2.1/universal-apps/%s/invite-links/" % (SERVER_URL.strip('/'), APP_TOKEN)
        data = {
            "role_name": "test_role_1_modified",
            "password": "11111111",
            "expire_days": 10
        }
        resp = requests.post(url, json=data, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
            self.tmp_link_token = resp.json().get('app_share_link', {}).get('token')
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '添加 App 分享链接',
            success,
            detail
        )

    def list_app_invite_links(self):
        url = "%s/api/v2.1/universal-apps/%s/invite-links/" % (SERVER_URL.strip('/'), APP_TOKEN)
        resp = requests.get(url, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
            print(resp.json())
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '列出 App 分享链接',
            success,
            detail
        )

    def delete_app_invite_link(self):
        url = "%s/api/v2.1/universal-apps/%s/invite-links/%s" % (SERVER_URL.strip('/'), APP_TOKEN, self.tmp_link_token)
        resp = requests.delete(url, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '删除 App 分享链接',
            success,
            detail
        )

    def delete_user(self):
        url = "%s/api/v2.1/universal-apps/%s/app-users/%s" % (SERVER_URL.strip('/'), APP_TOKEN, self.tmp_app_user_id)
        resp = requests.delete(url, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
            self.tmp_app_user_id = None
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            '删除 APP 用户',
            success,
            detail
        )





if __name__ == '__main__':

    base = get_base()
    account = get_account()

    api_tests = UniversalAppAdminAPITest(base, account)
    test_pool = [
        api_tests.list_users,
        api_tests.list_roles,

        api_tests.add_role,
        api_tests.add_user,

        api_tests.put_user,
        api_tests.put_role,

        api_tests.add_invite_link,
        api_tests.list_app_invite_links,
        api_tests.delete_app_invite_link,

        api_tests.delete_user,
        api_tests.delete_role,
    ]

    for func in test_pool:
        row_data = func()
        base.append_row(TEST_RESULTS_TABLE_NAME, row_data)
