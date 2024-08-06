# local account
# DTABLE_WEB_SERVICE_URL = 'http://127.0.0.1:8000'
# DTABLE_SERVER_URL = 'http://127.0.0.1:5000'
# TEST_USER_EMAIL = '87d485c2281a42adbddb137a1070f395@auth.local'
# TEST_USER_PASSWORD = '111'
# TEST_READ_ONLY_USER_EMAIL = '0febcccbb7d744b581911d3fa628e631@auth.local'
# TEST_READ_ONLY_USER_PASSWORD = '111'
# TEST_TABLE_NAME = 'TableForTest'

ENABLE_CLUSTER = True
# dev account
DTABLE_WEB_SERVICE_URL = 'https://dev.seatable.cn'
DTABLE_SERVER_API_URL = 'https://dtable-server-dev-api.seatable.cn'
DTABLE_SERVER_URL = 'https://dtable-server-dev.seatable.cn'
API_GATEWAY_URL = DTABLE_WEB_SERVICE_URL.strip('/') + '/api-gateway'
# TEST_USER_EMAIL = '7b33259c2c3248aeb0347efbb1ab5df5@auth.local'
TEST_USER_EMAIL = 'seatable-test-01@seafile.com'
TEST_USER_PASSWORD = '12345678'
# TEST_READ_ONLY_USER_EMAIL = '503ddaa01f6e4458a2602267bef5a80f@auth.local'
TEST_READ_ONLY_USER_EMAIL = 'seatable-test-02@seafile.com'
TEST_READ_ONLY_USER_PASSWORD = '12345678'
TEST_TABLE_NAME = 'TableForTest'

# API Token
API_TOKEN_NAME_1 = 'api-test-1'
API_TOKEN_NAME_2 = 'api-test-2'

LOCAL_TEST = False


try:
    from local_constants import *
except:
    pass
