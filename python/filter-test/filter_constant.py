ENABLE_CLUSTER = True
API_TOKEN = "1c3db106dd06b7eac9775f89d6601e1667750a5c"
DTABLE_WEB_SERVER_URL = "https://dev.seatable.cn"
DTABLE_SERVER_URL = "https://dtable-server-dev.seatable.cn"
DTABLE_SERVER_API_URL = "https://dtable-server-dev-api.seatable.cn"

FILTER_CONSTANTS = [
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'contains', 'filter_term': 'A'},
        "view_name": "filter_contains"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'does_not_contain', 'filter_term': 'A'},
        "view_name": "filter_not_contain"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is', 'filter_term': 'ABCD'},
        "view_name": "filter_is"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_not', 'filter_term': 'ABCD'},
        "view_name": "filter_is_not"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]
