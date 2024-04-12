from APIGatewayTest import APIGatewayTest
from sdkTest import BaseOperations
from sdkTest.TableOperations import ViewOperations, ColumnOperations, RowOperations,LinkOperations
from seatable_api import Base
from config import API_TOKEN, SERVER_URL

class MetaTest_PythonSDK(APIGatewayTest):
    def run_workflow(self):
        self.testBaseOperations()
        self.testTableOperations()

    def testBaseOperations(self):
        base_ops = BaseOperations.BaseOperations(self.base)
        base_ops()

    def testTableOperations(self):
        view_ops = ViewOperations.ViewOperations(self.base)
        view_ops()

        column_ops = ColumnOperations.ColumnOperations(self.base)
        column_ops()

        row_ops = RowOperations.RowOperations(self.base)
        row_ops()

        link_ops = LinkOperations.LinkOperations(self.base)
        link_ops()
           
if __name__ == '__main__':

    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    sdk_test = MetaTest_PythonSDK(base)
    sdk_test()