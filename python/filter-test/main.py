from seatable_api import Base, SeaTableAPI
import requests
import json
import time
from sql_generator import filter2sql
ENABLE_CLUSTER = True
API_TOKEN = "1c3db106dd06b7eac9775f89d6601e1667750a5c"
DTABLE_WEB_SERVER_URL = "https://dev.seatable.cn"
DTABLE_SERVER_URL = "https://dtable-server-dev.seatable.cn"
DTABLE_SERVER_API_URL = "https://dtable-server-dev-api.seatable.cn"

if ENABLE_CLUSTER:
    dtable_server_url = DTABLE_SERVER_API_URL
else:
    dtable_server_url = DTABLE_SERVER_URL


def parse_response(response):
    if response.status_code >= 400:
        try:
            err_data = json.loads(response.text)
        except:
            raise ConnectionError(response.status_code, response.text)
    else:
        try:
            data = json.loads(response.text)
            return data
        except:
            pass


class MyBase(Base):

    def __init__(self, token, server_url):
        super(MyBase, self).__init__(token, server_url)

    def list_dtable_server_rows(self, table_name, view_name=None):
        """
        :param table_name: str
        :param view_name: str
        :param order_by: str
        :param desc: boolean
        :param start: int
        :param limit: int
        :return: list
        """
        url = self.dtable_server_url + '/api/v1/internal/dtables/' + self.dtable_uuid + '/rows/'
        params = {
            'table_name': table_name
        }


        if view_name:
            params['view_name'] = view_name

        response = requests.get(url, params=params, headers=self.headers, timeout=self.timeout)
        data = parse_response(response)
        return data.get('rows')



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

def format_filters(filter_items, filter_conjunction='And'):
    return {

        "filter_groups": [
            {
                "filters": [
                    filter_item for filter_item in filter_items
                ],

                "filter_conjunction": filter_conjunction
            },
        ],

    }

VIEW_NAME_EXCLUDE = ['默认视图', '归档']



# db-API returns
def filter_rows(filter_items, table_name, columns, conjunction='And'):
    filter_conditions = format_filters(filter_items, conjunction)
    sql = filter2sql(table_name, columns, filter_conditions, by_group=True)
    res = base.query(sql)
    return res, sql


def run(base, local_test=True, result_table='TestResult'):
    for table in base.get_metadata().get('tables'):
        table_name = table.get('name')
        if table_name in EXCLUDE_TABLE_NAME_ID_MAP.keys():
            continue
        if table_name not in TABLE_NAME_ID_MAP.keys():
            continue
        views = table.get('views')
        columns = table['columns']
        pass_num, fail_num, unmatch_filters, col_type = 0, 0, [], table_name
        for view in views:
            view_name = view.get('name')
            if view_name in VIEW_NAME_EXCLUDE:
                continue
            filter_items = view.get('filters')
            filter_conjunction = view.get('filter_conjunction', 'And')
            if not filter_items:
                continue
            for filter_item in filter_items:
                filter_item['view_name'] = view_name

            filter_rows_db, sql = filter_rows(filter_items, table_name, columns, filter_conjunction)

            if result_table == 'TestResult':
                filter_rows_page = base.list_rows(table_name, view_name)
            else:
                filter_rows_page = base.list_dtable_server_rows(table_name, view_name)
            # print(filter_rows_page, 'ssssssss')

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

        time.sleep(60)


if __name__ == '__main__':
    base = MyBase(API_TOKEN, DTABLE_WEB_SERVER_URL)
    base.auth()
    LOCAL_TEST = False
    run(base, LOCAL_TEST, result_table='TestResult')
