from seatable_api import Base
import requests
import json
import time
ENABLE_CLUSTER = True
API_TOKEN = "1c3db106dd06b7eac9775f89d6601e1667750a5c"
DTABLE_WEB_SERVER_URL = "https://dev.seatable.cn"
DTABLE_SERVER_URL = "https://dtable-server-dev.seatable.cn"
DTABLE_SERVER_API_URL = "https://dtable-server-dev-api.seatable.cn"


if ENABLE_CLUSTER:
    dtable_server_url = DTABLE_SERVER_API_URL
else:
    dtable_server_url = DTABLE_SERVER_URL

base = Base(API_TOKEN, DTABLE_WEB_SERVER_URL)
base.auth()
EXCLUDE_TABLE_NAME_ID_MAP = {
    'TestResult': 'MCkc',
    'TestResultNumber': 'C603',

    # 'NumberFormula': 'vo4O',
    # 'NumberFormulaPercentage': 'v0BK',
    # 'NumberFormulaCurrencyUS': '209x',
    'Link-Parent': 'olDx',

    'NumberTmp': 'n7P8',

}

TABLE_NAME_ID_MAP = {
    'TextFilter': '0000',
    'NumberFilter': 'NkF3',
    'CollaboratorFilter': 'x2nE',
    'SingleSelectFilter': 'Y5Bn',
    'MultipleSelectFilter': 'VFBq',
    'FileFilter': '9Hr0',
    'ImageFilter': 'C4MU',
    'DurationFilter': '3LS7',
    'DateFilter': 'q4Y1',
    'EmailFilter': 'S1UQ',
    'URLFilter': 'ynrL',
    'CheckboxFilter': 'dQu4',
    'RateFilter': 'Om5c',
    'GeoLocationFilter': 'ye1O',
    'CreatorAndModifilerFilter': 't0wJ',
    'AutoNumberFilter': 'dr15',
    # 'FormulaDateFilter': '47rb',
    'DateFomula': 'XLJY',
    'StringFormula': '9U68',
    'BoolFormula': 'Jfe7',

    'LinkDate': 'ZU6f',
    'LinkText': 'Fmxg',
    'LinkEmail': '6R8c',
    'LinkSingleSelect': '3xuf',
    'LinkNumber': 'ki51',
    'LinkAutoNumber': 'K2Y3',
    'LinkFormula': 'W3ta',
    'LinkLookUpEmpty': 'E1zi',
    'LinkLookUpOtherFilters':'36DV',

    'LookUpFormula':'vPb8',

    'NumberFormula': 'vo4O',
    'NumberFormulaPercentage': 'v0BK',
    'NumberFormulaCurrencyUS': '209x',
    'NumberFomulaSplitByComma': 'vVZ1',
    'NumberFomulaDotSplitByDot': '2x7k'
}

def format_filters(filter_items):
    return {

        "filter_groups": [
            {
                "filters": [
                    filter_item for filter_item in filter_items
                ],
            },
        ],

    }

VIEW_NAME_EXCLUDE = ['默认视图', '归档']


# db-API returns
def filter_rows(filter_items, table_id):
    api_url = "%s/api/v1/internal/dtables/%s/filter-rows/" % (
        dtable_server_url.rstrip("/"),
        base.dtable_uuid,
    )

    params = {
        "table_id": table_id,
        "filter_conditions": format_filters(filter_items)
    }

    res = requests.post(api_url, json=params, headers=base.headers)
    filtered_rows = res.json().get('rows')
    return filtered_rows


def run(base, local_test=True, result_table='TestResult'):
    for table in base.get_metadata().get('tables'):
        table_name = table.get('name')
        table_id = table.get('_id')
        if table_name in EXCLUDE_TABLE_NAME_ID_MAP.keys():
            continue
        if table_name not in TABLE_NAME_ID_MAP.keys():
            continue
        views = table.get('views')
        pass_num, fail_num, unmatch_filters, col_type = 0, 0, [], table_name
        for view in views:
            view_name = view.get('name')
            if view_name in VIEW_NAME_EXCLUDE:
                continue
            filter_items = view.get('filters')
            if not filter_items:
                continue
            for filter_item in filter_items:
                filter_item['view_name'] = view_name
            filter_rows_db = filter_rows(filter_items, table_id)
            filter_rows_page = base.list_rows(table_name, view_name)

            if len(filter_rows_db) != len(filter_rows_page):
                fail_num += 1
                unmatch_filters.append(filter_items)

            else:
                row_ids_sorted_db = sorted([row.get('_id') for row in filter_rows_db])
                row_ids_sorted_page = sorted([row.get('_id') for row in filter_rows_page])

                if row_ids_sorted_db != row_ids_sorted_page:
                    fail_num += 1
                    unmatch_filters.append(filter_items)
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

        if local_test:
            print(test_result)
        else:
            base.append_row(result_table, test_result)

        time.sleep(10)


if __name__ == '__main__':
    base = Base(API_TOKEN, DTABLE_WEB_SERVER_URL)
    base.auth()
    LOCAL_TEST = False
    run(base, LOCAL_TEST)