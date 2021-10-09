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
    query_result_dict_keys = set(query_result_dict.keys())
    expected_result_dict_keys = set(expected_result_dict.keys())
    key_diff = expected_result_dict_keys.difference(query_result_dict_keys)
    if key_diff:
        return False, key_diff, None, None, 'miss_keys'
    for key, value in query_result_dict.items():
        expected_value = expected_result_dict.get(key)
        if value != expected_value:
            return False, key, value, expected_value, 'unmatched'
    return True, None, None, None, None

def test_order_by(query_result, expected_result):
    if query_result != expected_result:
        return False
    return True

def test_common_query(query_result, expected_result):
    if len(query_result) == len(expected_result):
        for res in query_result:
            if res not in expected_result:
                return False
        return True
    else:
        return False

def run():
    error_msgs = []
    for ref in REFERENCES:
        sql = ref.get('sql')
        query_type = ref.get('type')
        query_result = base.query(sql)
        expected_result = ref.get('expected_result')
        error_msg = ''
        if query_type == 'Map':
            query_result = query_result[0]
            expected_result = expected_result[0]
            pass_test, key, value, expected_value, error_type = test_map_data(query_result, expected_result)
            if not pass_test:
                if error_type == 'unmatched':
                    error_msg = "SQL:%s \nValue unmatched: %s column %s expected, \nbut %s returned " % (sql, key, expected_value, value)
                elif error_type == 'miss_keys':
                    error_msg = "SQL: %s \n Value unmatched: %s column data does not return" % (sql,key)

        if query_type == 'GroupBy':
            pass_test = test_group_by(query_result, expected_result)
            if not pass_test:
                error_msg = "SQL: %s \n Value unmatched: %s expected, \nbut %s returned " % (sql, expected_result, query_result)

        if query_type == 'OrderBy':
            pass_test = test_order_by(query_result, expected_result)
            if not pass_test:
                error_msg = "SQL: %s \n Value error: %s expected, \nbut %s returned " % (sql, expected_result, query_result)

        if query_type == 'Common':
            pass_test = test_common_query(query_result, expected_result)
            if not pass_test:
                error_msg = "SQL: %s \n Value error: %s expected, \nbut %s returned " % (sql, expected_result, query_result)
                print("Value error: %s expected, but %s returned " % (expected_result, query_result))

        if error_msg:
            error_msgs.append(error_msg)

    results = "Test success"
    if error_msgs:
        results = "\n\n".join(error_msgs)
    base.append_row('TestResults', {'Results': results})


if __name__ == '__main__':
    run()
    # for ref in REFERENCES:
    #     print(ref.get('sql'))
