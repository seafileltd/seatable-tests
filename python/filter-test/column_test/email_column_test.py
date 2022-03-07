import requests
import json
from seatable_api import Base
from filter_constant import API_TOKEN, DTABLE_WEB_SERVER_URL, EMAIL_FILTER_CONSTANTS, \
    DTABLE_SERVER_URL, DTABLE_SERVER_API_URL, ENABLE_CLUSTER

if ENABLE_CLUSTER:
    dtable_server_url = DTABLE_SERVER_API_URL
else:
    dtable_server_url = DTABLE_SERVER_URL

COLUMN_TYPE = 'email'


base = Base(API_TOKEN, DTABLE_WEB_SERVER_URL)
base.auth()


def format_filters(filter_item):
    return {

        "filter_groups": [
            {
                "filters": [
                    filter_item,
                ],
            },
        ],

    }


# db-API returns
def filter_rows(filter_item):
    api_url = "%s/api/v1/internal/dtables/%s/filter-rows/" % (
        dtable_server_url.rstrip("/"),
        base.dtable_uuid,
    )

    params = {
        "table_id": "S1UQ",
        "filter_conditions": format_filters(filter_item)
    }

    res = requests.post(api_url, json=params, headers=base.headers)
    filtered_rows = res.json().get('rows')
    return filtered_rows

def run(base, table_name, print_out=True):
    pass_num, fail_num, unmatch_filters, col_type = 0, 0, [], COLUMN_TYPE

    for f in EMAIL_FILTER_CONSTANTS:
        filter_item = f.get('filter')
        view_name = f.get('view_name')

        filter_rows_db = filter_rows(filter_item)
        filter_rows_page = base.list_rows(table_name, view_name)

        if len(filter_rows_db) != len(filter_rows_page):
            fail_num += 1
            unmatch_filters.append(filter_item)

        else:
            row_ids_sorted_db = sorted([row.get('_id') for row in filter_rows_db])
            row_ids_sorted_page = sorted([row.get('_id') for row in filter_rows_page])


            if row_ids_sorted_db != row_ids_sorted_page:
                fail_num += 1
                unmatch_filters.append(filter_item)
            else:
                pass_num += 1

    test_result = {
        'SuccessNo': pass_num,
        'FailNo': fail_num,
        'Unmatch Filters': unmatch_filters and "\n\n".join([
            json.dumps(i) for i in unmatch_filters
        ]) or "",
        'ColumnType': col_type,
    }

    if print_out:
        print(test_result)
    return test_result

def run_email_column_test(base, local_test):
    table_name = 'EmailFilter'
    test_result_table_name = 'TestResult'

    result = run(base, table_name, print_out=local_test)

    if not local_test:
        base.append_row(test_result_table_name, result)

if __name__ == '__main__':
    # filter_rows()
    # get_row_by_view()

    LOCAL_TEST = True

    base = Base(API_TOKEN, DTABLE_WEB_SERVER_URL)
    base.auth()

    run_email_column_test(base, LOCAL_TEST)
