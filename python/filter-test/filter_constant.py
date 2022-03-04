ENABLE_CLUSTER = True
API_TOKEN = "1c3db106dd06b7eac9775f89d6601e1667750a5c"
DTABLE_WEB_SERVER_URL = "https://dev.seatable.cn"
DTABLE_SERVER_URL = "https://dtable-server-dev.seatable.cn"
DTABLE_SERVER_API_URL = "https://dtable-server-dev-api.seatable.cn"
#
# local test
# ENABLE_CLUSTER = False
# API_TOKEN = "daec335184fe70863443d88443a12ef61ddfbf68"
# DTABLE_WEB_SERVER_URL = "http://127.0.0.1:8000"
# DTABLE_SERVER_URL = "http://127.0.0.1:5000"
# DTABLE_SERVER_API_URL = "https://dtable-server-dev-api.seatable.cn"

# LOCAL_TEST = True

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

DATE_FILTER_CONSTANT = [
    {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '2022-03-14',
            'filter_term_modifier': 'exact_date'
        },
        'view_name': 'filter_is_exact_date'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '',
            'filter_term_modifier': 'today'
        },
        'view_name': 'filter_is_today'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '',
            'filter_term_modifier': 'tomorrow'
        },
        'view_name': 'filter_is_tomorrow'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '',
            'filter_term_modifier': 'yesterday'
        },
        'view_name': 'filter_is_yesterday'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '',
            'filter_term_modifier': 'one_week_from_now'
        },
        'view_name': 'filter_is_after_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '',
            'filter_term_modifier': 'one_month_from_now'
        },
        'view_name': 'filter_is_after_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '',
            'filter_term_modifier': 'one_week_ago'
        },
        'view_name': 'filter_is_before_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '',
            'filter_term_modifier': 'one_month_ago'
        },
        'view_name': 'filter_is_before_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_ago'
        },
        'view_name': 'filter_is_before_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_from_now'
        },
        'view_name': 'filter_is_after_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'the_past_week'
        },
        'view_name': 'filter_within_last_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'the_past_month'
        },
        'view_name': 'filter_within_last_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'the_past_year'
        },
        'view_name': 'filter_within_last_year'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'this_week'
        },
        'view_name': 'filter_within_this_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'this_month'
        },
        'view_name': 'filter_within_this_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'this_year'
        },
        'view_name': 'filter_within_this_year'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'the_next_week'
        },
        'view_name': 'filter_within_next_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'the_next_month'
        },
        'view_name': 'filter_within_next_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '',
            'filter_term_modifier': 'the_next_year'
        },
        'view_name': 'filter_within_next_year'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '10',
            'filter_term_modifier': 'the_next_numbers_of_days'
        },
        'view_name': 'filter_within_after_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_within',
            'filter_term': '10',
            'filter_term_modifier': 'the_past_numbers_of_days'
        },
        'view_name': 'filter_within_before_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '2022-03-14',
            'filter_term_modifier': 'exact_date'
        },
        'view_name': 'filter_before_exact_date'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '',
            'filter_term_modifier': 'today'
        },
        'view_name': 'filter_before_today'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '',
            'filter_term_modifier': 'yesterday'
        },
        'view_name': 'filter_before_yesterday'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '',
            'filter_term_modifier': 'tomorrow'
        },
        'view_name': 'filter_before_tomorrow'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '',
            'filter_term_modifier': 'one_week_from_now'
        },
        'view_name': 'filter_before_after_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '',
            'filter_term_modifier': 'one_month_from_now'
        },
        'view_name': 'filter_before_after_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '',
            'filter_term_modifier': 'one_week_ago'
        },
        'view_name': 'filter_before_before_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '',
            'filter_term_modifier': 'one_month_ago'
        },
        'view_name': 'filter_before_before_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_ago'
        },
        'view_name': 'filter_before_before_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_before',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_from_now'
        },
        'view_name': 'filter_before_after_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '2022-03-14',
            'filter_term_modifier': 'exact_date'
        },
        'view_name': 'filter_on_and_before_exact_date'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '',
            'filter_term_modifier': 'yesterday'
        },
        'view_name': 'filter_on_and_before_yesterday'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '',
            'filter_term_modifier': 'tomorrow'
        },
        'view_name': 'filter_on_and_before_tomorrow'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '',
            'filter_term_modifier': 'today'
        },
        'view_name': 'filter_on_and_before_today'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '',
            'filter_term_modifier': 'one_week_from_now'
        },
        'view_name': 'filter_on_and_before_after_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '',
            'filter_term_modifier': 'one_week_ago'
        },
        'view_name': 'filter_on_and_before_before_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '',
            'filter_term_modifier': 'one_month_from_now'
        },
        'view_name': 'filter_on_and_before_after_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '',
            'filter_term_modifier': 'one_month_ago'
        },
        'view_name': 'filter_on_and_before_before_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_ago'
        },
        'view_name': 'filter_on_and_before_before_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_before',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_from_now'
        },
        'view_name': 'filter_on_and_before_after_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '',
            'filter_term_modifier': 'today'
        },
        'view_name': 'filter_after_today'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '',
            'filter_term_modifier': 'tomorrow'
        },
        'view_name': 'filter_after_tomorrow'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '',
            'filter_term_modifier': 'yesterday'
        },
        'view_name': 'filter_after_yesterday'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '2022-03-14',
            'filter_term_modifier': 'exact_date'
        },
        'view_name': 'filter_after_exact_date'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '',
            'filter_term_modifier': 'one_week_from_now'
        },
        'view_name': 'filter_after_after_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '',
            'filter_term_modifier': 'one_month_from_now'
        },
        'view_name': 'filter_after_after_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '',
            'filter_term_modifier': 'one_week_ago'
        },
        'view_name': 'filter_after_before_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '',
            'filter_term_modifier': 'one_month_ago'
        },
        'view_name': 'filter_after_before_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_ago'
        },
        'view_name': 'filter_after_before_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_after',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_from_now'
        },
        'view_name': 'filter_after_after_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '',
            'filter_term_modifier': 'today'
        },
        'view_name': 'filter_on_and_after_today'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '',
            'filter_term_modifier': 'yesterday'
        },
        'view_name': 'filter_on_and_after_yesterday'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '',
            'filter_term_modifier': 'tomorrow'
        },
        'view_name': 'filter_on_and_after_tomorrow'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '2022-03-14',
            'filter_term_modifier': 'exact_date'
        },
        'view_name': 'filter_on_and_after_exact_date'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '',
            'filter_term_modifier': 'one_week_from_now'
        },
        'view_name': 'filter_on_and_after_after_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '',
            'filter_term_modifier': 'one_month_from_now'
        },
        'view_name': 'filter_on_and_after_after_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '',
            'filter_term_modifier': 'one_week_ago'
        },
        'view_name': 'filter_on_and_after_before_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '',
            'filter_term_modifier': 'one_month_ago'
        },
        'view_name': 'filter_on_and_after_before_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_from_now'
        },
        'view_name': 'filter_on_and_after_after_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_on_or_after',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_ago'
        },
        'view_name': 'filter_on_and_after_before_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '2022-03-14',
            'filter_term_modifier': 'exact_date'
        },
        'view_name': 'filter_is_not_exact_date'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '',
            'filter_term_modifier': 'today'
        },
        'view_name': 'filter_is_not_today'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '',
            'filter_term_modifier': 'yesterday'
        },
        'view_name': 'filter_is_not_yesterday'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '',
            'filter_term_modifier': 'tomorrow'
        },
        'view_name': 'filter_is_not_tomorrow'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '',
            'filter_term_modifier': 'one_week_from_now'
        },
        'view_name': 'filter_is_not_after_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '',
            'filter_term_modifier': 'one_month_from_now'
        },
        'view_name': 'filter_is_not_after_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '',
            'filter_term_modifier': 'one_week_ago'
        },
        'view_name': 'filter_is_not_before_a_week'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '',
            'filter_term_modifier': 'one_month_ago'
        },
        'view_name': 'filter_is_not_before_a_month'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_from_now'
        },
        'view_name': 'filter_is_not_after_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not',
            'filter_term': '10',
            'filter_term_modifier': 'number_of_days_ago'
        },
        'view_name': 'filter_is_not_before_number_of_days'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_empty',
            'filter_term': '',
            'filter_term_modifier': 'exact_date'
        },
        'view_name': 'filter_is_empty'
    }, {
        'filter': {
            'column_key': '0000',
            'filter_predicate': 'is_not_empty',
            'filter_term': '',
            'filter_term_modifier': 'exact_date'
        },
        'view_name': 'filter_not_empty'
    }
]
