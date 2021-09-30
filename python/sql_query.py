from seatable_api import Base, context

from python.references import REFERENCES

api_token = context.api_token or "48d7488c9d7267abc020c5a8be497088522dd562"
server_url = context.server_url or "https://dev.seatable.cn/"

base = Base(api_token, server_url)
base.auth()


def test_group_by(query_result, expected_result):
    if len(query_result) == len(expected_result):
        for res in query_result:
            if res not in expected_result:
                return False
        return True
    else:
        return False

def test_map_data(query_result_dict, expected_result_dict):
    for key, value in query_result_dict.items():
        expected_value = expected_result_dict.get(key)
        if value != expected_value:
            return False, key, value, expected_value
    return True, None, None, None

def test_order_by(query_result, expected_result):
    if query_result != expected_result:
        return False
    return True

def test_common_query(query_result, expected_result):
    if len(query_result) == len(expected_result):
        for res in query_result:
            if res not in expected_result:
                print(res,'ddddd')
                return False
        return True
    else:
        return False

for ref in REFERENCES:
    sql = ref.get('sql')
    query_type = ref.get('type')
    query_result = base.query(sql)
    expected_result = ref.get('expected_result')
    print("===========SQL: %s===========" % sql)
    if query_type == 'Map':
        query_result = query_result[0]
        expected_result = expected_result[0]
        pass_test, key, value, expected_value = test_map_data(query_result, expected_result)
        if not pass_test:
            print("Value unmatched: %s column %s expected, but %s returned " % (key, expected_value, value))
        else:
            print('Test success')

    if query_type == 'GroupBy':
        pass_test = test_group_by(query_result, expected_result)
        if not pass_test:
            print("Value unmatched: %s expected, but %s returned " % (expected_result, query_result))
        else:
            print("Test success")

    if query_type == 'OrderBy':
        pass_test = test_order_by(query_result, expected_result)
        if not pass_test:
            print("Value error: %s expected, but %s returned " % (expected_result, query_result))
        else:
            print("Test success")

    if query_type == 'Common':
        pass_test = test_common_query(query_result, expected_result)
        if not pass_test:
            print("Value error: %s expected, but %s returned " % (expected_result, query_result))
        else:
            print("Test success")

    print("\n")
