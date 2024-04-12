from config import SERVER_URL
from seatable_api import Base

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
    
    def run_workflow(self):
        pass #test procedures

    def __call__(self):
        return self.run_workflow()
