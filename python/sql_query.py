from seatable_api import Base, context

api_token = context.api_token or "48d7488c9d7267abc020c5a8be497088522dd562"
server_url = context.server_url or "https://dev.seatable.cn/"

base = Base(api_token, server_url)
base.auth()


sql_list = [
    "Select * from Table1",
    "Select * from Table1 where 单选='女'",
    "Select 文本,sum(数字) from Table1 group by 文本",
]

def format_result(res_dict):
    res_list = []
    for column_name, column_value in res_dict.items():
        res_str = "%s: %s" % (column_name, column_value)
        res_list.append(res_str)
    return "\n".join(res_list)

for sql in sql_list:
    try:
        res_list = base.query(sql)
        count = len(res_list)
        print("+++SQL:'%s' Results count: %s+++" % (sql, count))
        for index, res in enumerate(res_list, 1):
            print("No: %s" % index)
            print(format_result(res))
            print("\n")
    except Exception as e:
        print("sql:%s, query error: %s" % (sql, e))
        print("\n")
        continue

    print("\n")
