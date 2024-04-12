from . import Hash, engageTest
from APIGatewayTest import APIGatewayTest

class BaseOperations(APIGatewayTest):
    def run_workflow(self):
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
