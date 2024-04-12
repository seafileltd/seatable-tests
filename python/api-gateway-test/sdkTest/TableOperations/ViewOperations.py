from APIGatewayTest import APIGatewayTest
from config import TABLE_NAME
from . import Hash, engageTest

class ViewOperations(APIGatewayTest):
    def run_workflow(self):
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
