# ENABLE_CLUSTER = True
# API_TOKEN = "1c3db106dd06b7eac9775f89d6601e1667750a5c"
# DTABLE_WEB_SERVER_URL = "https://dev.seatable.cn"
# DTABLE_SERVER_URL = "https://dtable-server-dev.seatable.cn"
# DTABLE_SERVER_API_URL = "https://dtable-server-dev-api.seatable.cn"
#
# local test
ENABLE_CLUSTER = False
API_TOKEN = "daec335184fe70863443d88443a12ef61ddfbf68"
DTABLE_WEB_SERVER_URL = "http://127.0.0.1:8000"
DTABLE_SERVER_URL = "http://127.0.0.1:5000"
DTABLE_SERVER_API_URL = "https://dtable-server-dev-api.seatable.cn"

TEXT_FILTER_CONSTANTS = [
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

NUMBER_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'equal', 'filter_term': '6'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'not_equal', 'filter_term': '6'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'less', 'filter_term': '6'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'greater', 'filter_term': '6'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'less_or_equal', 'filter_term': '6'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'greater_or_equal', 'filter_term': '6'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_not_empty', 'filter_term': '6'},
        "view_name": "filter_not_empty"
    },

]

COLLABORATOR_FILTER_CONSTANTS = [
    {
        "filter": {
            'column_key': 'KFqb',
            'filter_predicate': 'has_any_of',
            'filter_term': ["jiwei.ran@seafile.com",
                            "freeplant@163.com"]
        },
        "view_name": "filter_has_any_of"
    },
    {
        "filter": {
            'column_key': 'KFqb',
            'filter_predicate': 'has_all_of',
            'filter_term': ["jiwei.ran@seafile.com",
                            "freeplant@163.com"]
        },
        "view_name": "filter_has_all_of"
    },
    {
        "filter": {
            'column_key': 'KFqb',
            'filter_predicate': 'has_none_of',
            'filter_term': ["jiwei.ran@seafile.com",
                            "freeplant@163.com"]
        },
        "view_name": "filter_has_none_of"
    },
    {
        "filter": {
            'column_key': 'KFqb',
            'filter_predicate': 'is_exactly',
            'filter_term': ["jiwei.ran@seafile.com",
                            "freeplant@163.com"]
        },
        "view_name": "filter_is_exactly"
    },
    {
        "filter": {
            'column_key': 'KFqb',
            'filter_predicate': 'is_empty',
            'filter_term': []
        },
        "view_name": "filter_is_empty"
    },
    {
        "filter": {
            'column_key': 'KFqb',
            'filter_predicate': 'is_not_empty',
            'filter_term': []
        },
        "view_name": "filter_not_empty"
    },

]

IMAGE_FILETER_CONSTANT = [
    {
        "filter": {'column_key': 'Pds7', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "image_is_empty"
    },

    {
        "filter": {'column_key': 'Pds7', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "image_not_empty"
    },

]

FILE_FILETER_CONSTANT = [
    {
        "filter": {'column_key': 'ww18', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "file_is_empty"
    },
    {
        "filter": {'column_key': 'ww18', 'filter_predicate': 'is_not_empty', 'filter_term': '6'},
        "view_name": "file_not_empty"
    },
]

SINGLE_SELECT_FILETER_CONSTANT = [
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is', 'filter_term': '570298'},
        "view_name": "filter_is"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_not', 'filter_term': '570298'},
        "view_name": "filter_is_not"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_any_of', 'filter_term': ['228536', '263322']},
        "view_name": "filter_is_any_of"
    },

    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_none_of', 'filter_term': ['228536', '263322']},
        "view_name": "filter_is_none_of"
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

MULTIPLE_SELECT_FILTER_CONSTANTS = [
    {
        "filter": {
            'column_key': 'fNJJ',
            'filter_predicate': 'has_any_of',
            'filter_term': ["673440", "820767"]
        },
        "view_name": "filter_has_any_of"
    },
    {
        "filter": {
            'column_key': 'fNJJ',
            'filter_predicate': 'has_all_of',
            'filter_term': ["673440", "820767"]
        },
        "view_name": "filter_has_all_of"
    },
    {
        "filter": {
            'column_key': 'fNJJ',
            'filter_predicate': 'has_none_of',
            'filter_term': ["673440", "820767"]
        },
        "view_name": "filter_has_none_of"
    },
    {
        "filter": {
            'column_key': 'fNJJ',
            'filter_predicate': 'is_exactly',
            'filter_term': ["673440", "820767"]
        },
        "view_name": "filter_is_exactly"
    },
    {
        "filter": {
            'column_key': 'fNJJ',
            'filter_predicate': 'is_empty',
            'filter_term': []
        },
        "view_name": "filter_is_empty"
    },
    {
        "filter": {
            'column_key': 'fNJJ',
            'filter_predicate': 'is_not_empty',
            'filter_term': []
        },
        "view_name": "filter_not_empty"
    },

]

DURATION_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': '3bkv', 'filter_predicate': 'equal', 'filter_term': '1800'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': '3bkv', 'filter_predicate': 'not_equal', 'filter_term': '1800'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': '3bkv', 'filter_predicate': 'less', 'filter_term': '1800'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': '3bkv', 'filter_predicate': 'greater', 'filter_term': '1800'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': '3bkv', 'filter_predicate': 'less_or_equal', 'filter_term': '1800'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': '3bkv', 'filter_predicate': 'greater_or_equal', 'filter_term': '1800'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': '3bkv', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': '3bkv', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]




