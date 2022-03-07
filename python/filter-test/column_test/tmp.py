from seatable_api import Base
from seatable_api.constants import ColumnTypes

API_TOKEN = "daec335184fe70863443d88443a12ef61ddfbf68"
DTABLE_WEB_SERVER_URL = "http://127.0.0.1:8000"
DTABLE_SERVER_URL = "http://127.0.0.1:5000"
DTABLE_SERVER_API_URL = "https://dtable-server-dev-api.seatable.cn"

base = Base(API_TOKEN, DTABLE_WEB_SERVER_URL)
base.auth()

base.modify_column_type('CTime', 'R6An', ColumnTypes.CTIME)