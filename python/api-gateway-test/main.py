from seatable_api import Base
from seatable_api.constants import ColumnTypes
import requests
import time
SERVER_URL = "https://dev.seatable.cn"
API_TOKEN = "1e1ef4db90af4fa73025e8b6f1541f15e1fa0216"

TEST_RESULTS_TABLE_NAME = "TestResults"
TABLE_NAME = 'Table'
LINK_TABLE_NAME = 'LinkTable'

Hash = {}

def engageTest(*hashKeys):
    def dec(func):
        def wrapper(self, *args, **kwargs):
            for key in hashKeys:
                if key not in Hash:
                    print(f"Function {func.__name__} has ignored, due to {key} not found in hash map!")
                    return
            if not self.base.is_authed:
                self.base.auth()
            test_name, success, detail = func.__name__, True, None
            try:
                func(self, *args, **kwargs)
            except Exception as e:
                success = False
                detail = repr(e)
            self.base.append_row(TEST_RESULTS_TABLE_NAME, self.format_infos(test_name, success, detail))
        return wrapper
    return dec

class APIGatewayTest(object):

    TEST_TYPE = None

    def __init__(self, base: Base):
        self.base = base
        self.dtable_uuid = base.dtable_uuid
        self.headers = base.headers
        self.testFuns = []

    def format_url(self, api_url):

        gateway_url = "%s/api-gateway" % SERVER_URL
        return "%s/%s" % (gateway_url, api_url.lstrip('/'))
    
    
    def format_infos(self, test_name, success, other_infos=None):
        return {
            "Functions": test_name,
            #"API-Type": self.TEST_TYPE,
            "Success": "Yes" if success else "No",
            "Details": "%s" % other_infos if other_infos is not None else ""
        }

class APIGatewayMetaTest(APIGatewayTest):

    #  api-gateway functions designed by dtable-db

    TEST_TYPE = 'api-gateway-db'

    def __init__(self, base):
        super(APIGatewayMetaTest, self).__init__(base)

        self.tmp_rows = []


    def list_rows(self):
        api_url = self.format_url('/api/v2/dtables/%s/rows' % self.dtable_uuid)
        params = {
            'table_name': TABLE_NAME
        }
        resp = requests.get(api_url, params=params, headers=self.headers)
        
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
            self.tmp_rows = resp.json().get('rows')
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'list-rows',
            success,
            detail
        )

    def add_rows(self):
        api_url = self.format_url('/api/v2/dtables/%s/batch-append-rows/' % self.dtable_uuid)
        data = {
            'table_name': TABLE_NAME,
            'rows': [
                {'Name': 'AA-%s' % str(int(time.time()))}
            ]
        }
        resp = requests.post(api_url, json=data, headers=self.headers)

        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'batch-append-rows',
            success,
            detail
        )

    def add_rows_to_bgs(self):
        # insert rows in bigdata storage
        api_url = self.format_url('/api/v2/dtables/%s/insert-archived-rows/' % self.dtable_uuid)
        data = {
            'table_name': TABLE_NAME,
            'rows': [
                {'Name': 'AA-bigdata-%s' % str(int(time.time()))}
            ]
        }
        resp = requests.post(api_url, json=data, headers=self.headers)

        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'insert-rows-into-bgs',
            success,
            detail
        )

    def update_rows(self):
        api_url = self.format_url('/api/v2/dtables/%s/rows/' % self.dtable_uuid)
        data = {
            'table_name': TABLE_NAME,
            'updates':[
                {
                    "row_id": self.tmp_rows[0]['_id'],
                    "row":{'Name': 'AA-update-rows-%s' % str(int(time.time()))}
                }
            ]
        }
        resp = requests.put(api_url, json=data, headers=self.headers)

        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'update-rows',
            success,
            detail
        )

    
    def run_workflow(self):
        # Test workflows for running the test functions
        workflows = [
            self.list_rows,
            self.add_rows,
            self.add_rows_to_bgs,
            self.update_rows
        ]

        for func in workflows:
            row_data = func()
            self.base.append_row(TEST_RESULTS_TABLE_NAME, row_data)

class APIGatewayProxyTest(APIGatewayTest):

    # api-gateway functions as proxy of dtable-server

    TEST_TYPE = 'dtable-server-proxy'

    def __init__(self, base):
        super(APIGatewayProxyTest, self).__init__(base)

        self.tmp_columns = []
    
    def list_columns(self):
        api_url = self.format_url('/api/v2/dtables/%s/columns' % self.dtable_uuid)
        params = {
            'table_name': TABLE_NAME
        }
        resp = requests.get(api_url, params=params, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            self.tmp_columns = resp.json().get('columns')
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'list-columns',
            success,
            detail
        )

    def insert_column(self):
        api_url = self.format_url('/api/v2/dtables/%s/columns/' % self.dtable_uuid)

        data = {
            'table_name': TABLE_NAME,
            'column_name': 'Col_New_%s' % str(int(time.time()))[4:]
        }
        resp = requests.post(api_url, json=data, headers=self.headers)
        success, detail = False, ''
        if resp.status_code == 200:
            success = True
        else:
            success = False
            detail = resp.content
        return self.format_infos(
            'insert-columns',
            success,
            detail
        )
    
    def run_workflow(self):
        # Test workflows for running the test functions
        
        workflows = [
            self.list_columns,
            self.insert_column,
        ]

        for func in workflows:
            row_data = func()
            self.base.append_row(TEST_RESULTS_TABLE_NAME, row_data)

class APIGatewayMetaTest_PythonSDK:
    def __init__(self, base):
        self.BaseOperations(base)
        self.TableOperations(base)

    class BaseOperations(APIGatewayTest):
        def __init__(self, base):
            self.base = base
            self.get_metadata()
            self.add_table()
            self.rename_table()
            self.delete_table()

        @engageTest()
        def get_metadata(self):
            self.base.get_metadata()
        
        @engageTest()
        def add_table(self):
            self.base.add_table("TestAddTable")
            Hash["HasAddedTable"] = True
        
        @engageTest("HasAddedTable")
        def rename_table(self):
            self.base.rename_table("TestAddTable", "TestRenameTable")
            Hash["HasRenamedTable"] = True
        
        @engageTest("HasAddedTable")
        def delete_table(self):
            self.base.delete_table("TestRenameTable" if "HasRenamedTable" in Hash else "TestAddTable")            
   
    class TableOperations:
        def __init__(self, base):
            self.ViewOperations(base)
            self.ColumnOperations(base)
            self.RowOperations(base)
            self.LinkOperations(base)

        class ViewOperations(APIGatewayTest):
            def __init__(self, base):
                self.base = base
                self.list_views()
                self.add_view()
                self.get_view_by_name()
                self.rename_view()
                self.delete_view()

            @engageTest()
            def list_views(self):
                self.base.list_views(TABLE_NAME)
            
            @engageTest()
            def add_view(self):
                self.base.add_view(TABLE_NAME, "TestAddView")
                Hash["HasAddedView"] = True
            
            @engageTest("HasAddedView")
            def get_view_by_name(self):
                self.base.get_view_by_name(TABLE_NAME, "TestAddView")
                

            @engageTest("HasAddedView")
            def rename_view(self):
                self.base.rename_view(TABLE_NAME, "TestAddView", "TestRenameView")
                Hash["HasRenamedView"] = True
            
            @engageTest("HasAddedView")
            def delete_view(self):
                self.base.delete_view(TABLE_NAME, "TestRenameView" if "HasRenamedView" in Hash else "TestAddView")

        class ColumnOperations(APIGatewayTest):
            def __init__(self, base):
                self.base = base
                self.list_columns()
                self.get_column_by_name()
                self.get_columns_by_type()
                self.insert_column()
                self.rename_column()
                self.resize_column()
                self.freeze_column()
                self.move_column()
                self.modify_column_type()
                self.add_column_options()
                self.add_column_cascade_settings()
                self.delete_column()

            @engageTest()
            def list_columns(self):
                self.base.list_columns(TABLE_NAME)

            @engageTest()
            def get_column_by_name(self):
                self.base.get_column_by_name(TABLE_NAME, "Name")

            @engageTest()
            def get_columns_by_type(self):
                self.base.get_columns_by_type(TABLE_NAME, ColumnTypes.TEXT)

            @engageTest()
            def insert_column(self):
                for i in range(10):
                    self.base.insert_column(TABLE_NAME, f"TestColumnInsert{i}", ColumnTypes.TEXT)
                self.base.insert_column(TABLE_NAME, "TestColumnInsert10", ColumnTypes.TEXT, "TestColumnInsert6")
                Hash["HasAddedColumn"] = True
                Hash["CanAddColumn"] = True

            @engageTest("HasAddedColumn")
            def rename_column(self):
                self.base.rename_column(TABLE_NAME, "TestColumnInsert10", "TestColumnInsertRename")
                Hash["HasRenamedColumn"] = True

            @engageTest("HasAddedColumn")
            def resize_column(self):
                self.base.resize_column(TABLE_NAME, "TestColumnInsertRename" if "HasRenamedColumn" in Hash else "TestColumnInsert10", 100)

            @engageTest("HasAddedColumn")
            def freeze_column(self):
                self.base.freeze_column(TABLE_NAME, "TestColumnInsertRename" if "HasRenamedColumn" in Hash else "TestColumnInsert10", True)
                self.base.freeze_column(TABLE_NAME, "TestColumnInsertRename" if "HasRenamedColumn" in Hash else "TestColumnInsert10", False)

            @engageTest("HasAddedColumn")
            def move_column(self):
                self.base.move_column(TABLE_NAME, "TestColumnInsertRename" if "HasRenamedColumn" in Hash else "TestColumnInsert10", "TestColumnInsert9")

            @engageTest("HasAddedColumn")
            def modify_column_type(self):
                self.base.modify_column_type(TABLE_NAME, "TestColumnInsert9", ColumnTypes.SINGLE_SELECT)
                self.base.modify_column_type(TABLE_NAME, "TestColumnInsertRename" if "HasRenamedColumn" in Hash else "TestColumnInsert10", ColumnTypes.SINGLE_SELECT)
                Hash["HasModifiedColumn"] = True

            @engageTest("HasModifiedColumn")
            def add_column_options(self):
                self.base.add_column_options(TABLE_NAME, "TestColumnInsertRename" if "HasRenamedColumn" in Hash else "TestColumnInsert10", [
                    {"name": "ddd", "color": "#aaa", "textColor": "#000000"},
                    {"name": "eee", "color": "#aaa", "textColor": "#000000"},
                    {"name": "fff", "color": "#aaa", "textColor": "#000000"}
                    ])
                Hash["HasAddedColumnOptions"] = True
                
            @engageTest("HasAddedColumnOptions")
            def add_column_cascade_settings(self):
                self.base.add_column_cascade_settings(TABLE_NAME, "TestColumnInsert9", "TestColumnInsertRename" if "HasRenamedColumn" in Hash else "TestColumnInsert10", {
                        "ddd": ["ddd-1", "ddd-2"], 
                        "eee": ["eee-1", "eee-2"],
                        "fff": ["fff-1", "fff-2"]
                    })
            
            @engageTest("HasAddedColumn")
            def delete_column(self):
                for i in range(10):
                    self.base.delete_column(TABLE_NAME, f"TestColumnInsert{i}")
                self.base.delete_column(TABLE_NAME, "TestColumnInsertRename" if "HasRenamedColumn" in Hash else "TestColumnInsert10")
                Hash["CanDeleteColumn"] = True

        class RowOperations(APIGatewayTest):
            def __init__(self, base: Base):
                self.base = base
                self.list_rows()
                self.append_row()
                self.get_row()
                self.update_row()
                self.insert_row()
                self.batch_append_rows()
                self.__update_row_ids()
                self.batch_update_rows()
                self.delete_row()
                self.batch_delete_rows()
                self.__extreme_rows_op()

            @engageTest()
            def list_rows(self):
                self.base.list_rows(TABLE_NAME)
                Hash["CanListRows"] = True

            @engageTest()
            def append_row(self):
                self.base.append_row(TABLE_NAME, {"Name": "TestAppend"})
                if "CanListRows" in Hash:
                    Hash["LastRowId"] = self.base.list_rows(TABLE_NAME)[-1]["_id"]

            @engageTest("LastRowId")
            def get_row(self):
                self.base.get_row(TABLE_NAME, Hash["LastRowId"])

            @engageTest("LastRowId")
            def update_row(self):
                self.base.update_row(TABLE_NAME, Hash["LastRowId"], {"Name": "TestUpdateRow"})

            @engageTest("LastRowId")
            def insert_row(self):
                self.base.insert_row(TABLE_NAME, {"Name": "TestInsertRow"}, Hash["LastRowId"])

            @engageTest()
            def batch_append_rows(self):
                self.base.batch_append_rows(TABLE_NAME, [{"Name": f"TestBatchAppend{i}"} for i in range(998)])
                Hash["CanBatchAppendRows"] = True

            def __update_row_ids(self):
                if "CanListRows" in Hash:
                    Hash["RowIds"] = [row["_id"] for row in self.base.list_rows(TABLE_NAME)]

            @engageTest("RowIds")
            def batch_update_rows(self):
                self.base.batch_update_rows(TABLE_NAME, [
                    {
                        "row_id" : rowId,
                        "row" : {
                            "Name" : f"TestBatchUpdate{index}"
                        }
                    }
                    for index, rowId in enumerate(Hash["RowIds"])
                ])

            @engageTest("RowIds")
            def delete_row(self):
                self.base.delete_row(TABLE_NAME, Hash["RowIds"][-1])
                Hash["RowIds"] = Hash["RowIds"][:-1]

            @engageTest("RowIds")
            def batch_delete_rows(self):
                self.base.batch_delete_rows(TABLE_NAME, Hash["RowIds"])
                Hash["CanBatchDeleteRows"] = True

            def __extreme_rows_op(self):
                if "CanListRows" not in Hash or \
                   "CanBatchAppendRows" not in Hash or \
                   "CanBatchDeleteRows" not in Hash:
                    return
                
                try:
                    for i in range(99):
                        self.base.batch_append_rows(TABLE_NAME, [{"Name": f"ExtremeTest{j}_batch{i}"} for j in range(1000)])

                    while len(rows := self.base.list_rows(TABLE_NAME)) > 0:
                        self.base.batch_delete_rows(TABLE_NAME, [row["_id"] for row in rows])

                except Exception as e:
                    print(repr(e))
            
        class LinkOperations(APIGatewayTest):
            def __init__(self, base: Base):
                self.base = base
                self.__pre_link_test()
                self.get_column_link_id()
                self.add_link()
                self.update_link()
                self.batch_update_links()
                self.remove_link()

            def __pre_link_test(self):
                if "CanAddColumn" in Hash and \
                   "CanBatchAppendRows" in Hash and \
                   "CanListRows" in Hash:
                    
                    self.base.batch_append_rows(TABLE_NAME, [{"Name": f"TestName{i}"} for i in range(10)])
                    self.base.batch_append_rows(LINK_TABLE_NAME, [{"名称": f"TestLinkValue{i}"} for i in range(10)])

                    self.base.insert_column(TABLE_NAME, "TestLinkColumn", ColumnTypes.LINK, column_data={
                        "table" : TABLE_NAME,
                        "other_table" : LINK_TABLE_NAME
                    })

                    Hash["Table_RowIds"] = [row["_id"] for row in self.base.list_rows(TABLE_NAME)]
                    Hash["LinkTable_RowIds"] = [row["_id"] for row in self.base.list_rows(LINK_TABLE_NAME)]

                    Hash["CanDoLinkTest"] = True

            @engageTest("CanDoLinkTest")
            def get_column_link_id(self):
                Hash["LinkId"] = self.base.get_column_link_id(TABLE_NAME, "TestLinkColumn")
            
            @engageTest("LinkId")
            def add_link(self):
                self.base.add_link(Hash["LinkId"], TABLE_NAME, LINK_TABLE_NAME, Hash["Table_RowIds"][0], Hash["LinkTable_RowIds"][0])
                Hash["HasAddedLink"] = True

            @engageTest("HasAddedLink")
            def update_link(self):
                self.base.update_link(Hash["LinkId"], TABLE_NAME, LINK_TABLE_NAME, Hash["Table_RowIds"][0], Hash[["LinkTable_RowIds"][-1]])

            @engageTest("LinkId")
            def batch_update_links(self):
                self.base.batch_update_links(Hash["LinkId"], TABLE_NAME, LINK_TABLE_NAME, Hash["Table_RowIds"], {
                    Hash["Table_RowIds"][i] : [Hash["LinkTable_RowIds"][i]]
                    for i in range(10)
                })

            @engageTest("LinkId")
            def remove_link(self):
                for table_id, linktable_id in zip(Hash["Table_RowIds"], Hash["LinkTable_RowIds"]):
                    self.base.remove_link(Hash["LinkId"], TABLE_NAME, LINK_TABLE_NAME, table_id, linktable_id)

                if "CanBatchDeleteRows" in Hash:
                    self.base.batch_delete_rows(TABLE_NAME, Hash["Table_RowIds"])
                    self.base.batch_delete_rows(LINK_TABLE_NAME, Hash["LinkTable_RowIds"])

                if "CanDeleteColumn" in Hash:
                    self.base.delete_column(TABLE_NAME, "TestLinkColumn")
                
if __name__ == '__main__':

    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    '''
    test_db = APIGatewayMetaTest(base)
    test_proxy = APIGatewayProxyTest(base)

    test_db.run_workflow()
    test_proxy.run_workflow()
    '''

    APIGatewayMetaTest_PythonSDK(base)


