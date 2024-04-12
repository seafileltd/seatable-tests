from config import TABLE_NAME, LINK_TABLE_NAME
from APIGatewayTest import APIGatewayTest
from seatable_api.constants import ColumnTypes
from . import Hash, engageTest

class LinkOperations(APIGatewayTest):
    def run_workflow(self):
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
       