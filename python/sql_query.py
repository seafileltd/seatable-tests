from seatable_api import Base, context

from python.references import REFERENCES

api_token = context.api_token or "48d7488c9d7267abc020c5a8be497088522dd562"
server_url = context.server_url or "https://dev.seatable.cn/"

base = Base(api_token, server_url)
base.auth()

for ref in REFERENCES:
    sql = ref.get('sql')
    query_result = base.query(sql)[0]
    expected_result = ref.get('expected_result')[0]
    for key, value in query_result.items():
        expected_value = expected_result.get(key)
        if value != expected_result.get(key):
            print ("Value error: %s column %s expected, but %s returned " % (key, expected_value, value))