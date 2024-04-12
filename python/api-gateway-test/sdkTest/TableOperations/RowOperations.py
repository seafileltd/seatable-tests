from APIGatewayTest import APIGatewayTest
from config import TABLE_NAME
from . import Hash, engageTest

class RowOperations(APIGatewayTest):
    def run_workflow(self):
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
    