from seatable_api import Base, context

from references import REFERENCES

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
    for key, value in expected_result_dict.items():
        query_value = query_result_dict.get(key)
        if value != query_value:
            return False, key, value, query_value, 'unmatched'
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
    failed_sql = []
    pass_num = 0
    fail_num = 0
    error_msg = ''
    try:
        for ref in REFERENCES:
            sql = ref.get('sql')
            query_type = ref.get('type')
            query_result = base.query(sql)
            expected_result = ref.get('expected_result')
            error_flag = False
            if query_type == 'Map':
                query_result = query_result[0]
                expected_result = expected_result[0]
                pass_test, key, value, expected_value, error_type = test_map_data(query_result, expected_result)
                if not pass_test:
                    if error_type == 'unmatched':
                        fail_num += 1
                        error_flag = True
                    elif error_type == 'miss_keys':
                        fail_num += 1
                        error_flag = True
                else:
                    pass_num += 1

            if query_type == 'GroupBy':
                pass_test = test_group_by(query_result, expected_result)
                if not pass_test:
                    fail_num += 1
                    error_flag = True
                else:
                    pass_num += 1
            if query_type == 'OrderBy':
                pass_test = test_order_by(query_result, expected_result)
                if not pass_test:
                    fail_num += 1
                    error_flag = True
                else:
                    pass_num += 1
            if query_type == 'Common':
                pass_test = test_common_query(query_result, expected_result)
                if not pass_test:
                    fail_num += 1
                    error_flag = True
                else:
                    pass_num += 1

            if error_flag:
                failed_sql.append(sql)
    except Exception as e:
        error_msg = e

    # print(pass_num)
    # print(fail_num)
    # print("\n".join(failed_sql))

    base.append_row(
        'TestResults',
        {
            'SuccessNo': pass_num,
            'FailNo': fail_num,
            'FailedSQL': failed_sql and "\n\n".join(failed_sql) or "",
            'ErrorMsg': error_msg
        })


if __name__ == '__main__':
    run()
    # for ref in REFERENCES:
    #     print(ref.get('sql'))
