from APIGatewayTest import APIGatewayTest
from seatable_api.constants import ColumnTypes
from config import TABLE_NAME
from . import engageTest, Hash

class ColumnOperations(APIGatewayTest):
    def run_workflow(self):
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
