from seatable_api import Base, context

api_token = context.api_token or "48d7488c9d7267abc020c5a8be497088522dd562"
server_url = context.server_url or "https://dev.seatable.cn/"

base = Base(api_token, server_url)
base.auth()


sql_list = [
    (
        "Select * from Table1 limit 1", "List"
    ),
    (
        "Select 文本,sum(数字) from Table1 group by 文本", "Group"
    )
]

for sql, query_type in sql_list:
    res_list = base.query(sql)
    count = len(res_list)
    print("+++SQL:'%s' Results count: %s+++" % (sql, count))
    if query_type == 'List' and count >= 1:
        results = res_list[0]
        str_list = []
        for column_name, column_value in results.items():
            str_list.append("%s : %s" % (column_name, column_value))
        print("\n".join(str_list))
    elif query_type == 'Group':
        for index, res in enumerate(res_list, 1):
            print("No%s---%s" % (index, res))
    else:
        continue
    print("\n")

