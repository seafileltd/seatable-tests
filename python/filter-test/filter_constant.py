ENABLE_CLUSTER = True
API_TOKEN = "1c3db106dd06b7eac9775f89d6601e1667750a5c"
DTABLE_WEB_SERVER_URL = "https://dev.seatable.cn"
DTABLE_SERVER_URL = "https://dtable-server-dev.seatable.cn"
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

EMAIL_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'contains', 'filter_term': '8982'},
        "view_name": "filter_contains"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'does_not_contain', 'filter_term': '8982'},
        "view_name": "filter_not_contain"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'is', 'filter_term': 'r350178982@126.com'},
        "view_name": "filter_is"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'is_not', 'filter_term': 'r350178982@126.com'},
        "view_name": "filter_is_not"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

URL_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'contains', 'filter_term': 'baidu'},
        "view_name": "filter_contains"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'does_not_contain', 'filter_term': 'baidu'},
        "view_name": "filter_not_contain"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'is', 'filter_term': 'http://www.baidu.com'},
        "view_name": "filter_is"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'is_not', 'filter_term': 'http://www.baidu.com'},
        "view_name": "filter_is_not"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'Z1cQ', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

CHECKBOX_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'eLiz', 'filter_predicate': 'is', 'filter_term': True},
        "view_name": "filter_check"
    },
    {
        "filter": {'column_key': 'eLiz', 'filter_predicate': 'is', 'filter_term': False},
        "view_name": "filter_uncheck"
    },

]

RATE_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'oykY', 'filter_predicate': 'equal', 'filter_term': '5'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': 'oykY', 'filter_predicate': 'not_equal', 'filter_term': '5'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': 'oykY', 'filter_predicate': 'less', 'filter_term': '5'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': 'oykY', 'filter_predicate': 'greater', 'filter_term': '5'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': 'oykY', 'filter_predicate': 'less_or_equal', 'filter_term': '5'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': 'oykY', 'filter_predicate': 'greater_or_equal', 'filter_term': '5'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': 'oykY', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'oykY', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

GEOLOCATION_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'q70F', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'q70F', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

CREATOR_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': '_creator', 'filter_predicate': 'contains', 'filter_term': ["jiwei.ran@seafile.com"]},
        "view_name": "filter_contains_c"
    },
    {
        "filter": {'column_key': '_creator', 'filter_predicate': 'does_not_contain',
                   'filter_term': ["jiwei.ran@seafile.com"]},
        "view_name": "filter_not_contain_c"
    },
    {
        "filter": {'column_key': '_creator', 'filter_predicate': 'is', 'filter_term': ["jiwei.ran@seafile.com"]},
        "view_name": "filter_is_c"
    },
    {
        "filter": {'column_key': '_creator', 'filter_predicate': 'is_not', 'filter_term': ["jiwei.ran@seafile.com"]},
        "view_name": "filter_is_not_c"
    },

]

MODIFIER_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': '_last_modifier', 'filter_predicate': 'contains',
                   'filter_term': ["jiwei.ran@seafile.com"]},
        "view_name": "filter_contains_m"
    },
    {
        "filter": {'column_key': '_last_modifier', 'filter_predicate': 'does_not_contain',
                   'filter_term': ["jiwei.ran@seafile.com"]},
        "view_name": "filter_not_contain_m"
    },
    {
        "filter": {'column_key': '_last_modifier', 'filter_predicate': 'is', 'filter_term': ["jiwei.ran@seafile.com"]},
        "view_name": "filter_is_m"
    },
    {
        "filter": {'column_key': '_last_modifier', 'filter_predicate': 'is_not',
                   'filter_term': ["jiwei.ran@seafile.com"]},
        "view_name": "filter_is_not_m"
    },

]

AUTONUMBER_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'contains', 'filter_term': '1'},
        "view_name": "filter_contains"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'does_not_contain', 'filter_term': '1'},
        "view_name": "filter_not_contain"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is', 'filter_term': 'Test-0005'},
        "view_name": "filter_is"
    },
    {
        "filter": {'column_key': '0000', 'filter_predicate': 'is_not', 'filter_term': 'Test-0005'},
        "view_name": "filter_is_not"
    },

]

STRING_FORMULA_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'zLvt', 'filter_predicate': 'contains', 'filter_term': 'A'},
        "view_name": "filter_contains"
    },
    {
        "filter": {'column_key': 'zLvt', 'filter_predicate': 'does_not_contain', 'filter_term': 'A'},
        "view_name": "filter_not_contain"
    },
    {
        "filter": {'column_key': 'zLvt', 'filter_predicate': 'is', 'filter_term': 'aa'},
        "view_name": "filter_is"
    },
    {
        "filter": {'column_key': 'zLvt', 'filter_predicate': 'is_not', 'filter_term': 'aa'},
        "view_name": "filter_is_not"
    },
    {
        "filter": {'column_key': 'zLvt', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'zLvt', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

BOOL_FORMULA_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'Pp5b', 'filter_predicate': 'is', 'filter_term': True},
        "view_name": "filter_checked"
    },
    {
        "filter": {'column_key': 'Pp5b', 'filter_predicate': 'is', 'filter_term': False},
        "view_name": "filter_uncheck"
    },

]

NUMBER_FORMULA_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'G3HW', 'filter_predicate': 'equal', 'filter_term': '6'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': 'G3HW', 'filter_predicate': 'not_equal', 'filter_term': '6'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': 'G3HW', 'filter_predicate': 'less', 'filter_term': '6'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': 'G3HW', 'filter_predicate': 'greater', 'filter_term': '6'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': 'G3HW', 'filter_predicate': 'less_or_equal', 'filter_term': '6'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': 'G3HW', 'filter_predicate': 'greater_or_equal', 'filter_term': '6'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': 'G3HW', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'G3HW', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

TEXT_LINK_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'ohNr', 'filter_predicate': 'contains', 'filter_term': 'B'},
        "view_name": "filter_contains"
    },
    {
        "filter": {'column_key': 'ohNr', 'filter_predicate': 'does_not_contain', 'filter_term': 'B'},
        "view_name": "filter_not_contain"
    },
    {
        "filter": {'column_key': 'ohNr', 'filter_predicate': 'is', 'filter_term': 'B'},
        "view_name": "filter_is"
    },
    {
        "filter": {'column_key': 'ohNr', 'filter_predicate': 'is_not', 'filter_term': 'B'},
        "view_name": "filter_is_not"
    },
    {
        "filter": {'column_key': 'ohNr', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'ohNr', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

SINGLE_SELECT_LINK_FILTER_CONSTANTS = [
    {
        "filter": {
            'column_key': '4m7p',
            'filter_predicate': 'has_any_of',
            'filter_term': ["65472", "183974"]
        },
        "view_name": "filter_has_any_of"
    },
    {
        "filter": {
            'column_key': '4m7p',
            'filter_predicate': 'has_all_of',
            'filter_term': ["65472", "183974"]
        },
        "view_name": "filter_has_all_of"
    },
    {
        "filter": {
            'column_key': '4m7p',
            'filter_predicate': 'has_none_of',
            'filter_term': ["65472", "183974"]
        },
        "view_name": "filter_has_none_of"
    },
    {
        "filter": {
            'column_key': '4m7p',
            'filter_predicate': 'is_exactly',
            'filter_term': ["65472", "183974"]
        },
        "view_name": "filter_is_exactly"
    },
    {
        "filter": {
            'column_key': '4m7p',
            'filter_predicate': 'is_empty',
            'filter_term': []
        },
        "view_name": "filter_is_empty"
    },
    {
        "filter": {
            'column_key': '4m7p',
            'filter_predicate': 'is_not_empty',
            'filter_term': []
        },
        "view_name": "filter_not_empty"
    },

]

NUMBER_LINK_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'Bh91', 'filter_predicate': 'equal', 'filter_term': '6'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': 'Bh91', 'filter_predicate': 'not_equal', 'filter_term': '6'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': 'Bh91', 'filter_predicate': 'less', 'filter_term': '6'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': 'Bh91', 'filter_predicate': 'greater', 'filter_term': '6'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': 'Bh91', 'filter_predicate': 'less_or_equal', 'filter_term': '6'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': 'Bh91', 'filter_predicate': 'greater_or_equal', 'filter_term': '6'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': 'Bh91', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'Bh91', 'filter_predicate': 'is_not_empty', 'filter_term': '6'},
        "view_name": "filter_not_empty"
    },

]

AUTONUMBER_LINK_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': '992E', 'filter_predicate': 'contains', 'filter_term': '005'},
        "view_name": "filter_contains"
    },
    {
        "filter": {'column_key': '992E', 'filter_predicate': 'does_not_contain', 'filter_term': '005'},
        "view_name": "filter_not_contain"
    },
    {
        "filter": {'column_key': '992E', 'filter_predicate': 'is', 'filter_term': 'link-0005'},
        "view_name": "filter_is"
    },
    {
        "filter": {'column_key': '992E', 'filter_predicate': 'is_not', 'filter_term': 'link-0005'},
        "view_name": "filter_is_not"
    },

]

FORMULA_LINK_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': '14a3', 'filter_predicate': 'equal', 'filter_term': '15'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': '14a3', 'filter_predicate': 'not_equal', 'filter_term': '15'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': '14a3', 'filter_predicate': 'less', 'filter_term': '15'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': '14a3', 'filter_predicate': 'greater', 'filter_term': '15'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': '14a3', 'filter_predicate': 'less_or_equal', 'filter_term': '15'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': '14a3', 'filter_predicate': 'greater_or_equal', 'filter_term': '15'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': '14a3', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': '14a3', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

NUMBER_FORMULA_PERCENTAGE_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'bniR', 'filter_predicate': 'equal', 'filter_term': '50%'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': 'bniR', 'filter_predicate': 'not_equal', 'filter_term': '50%'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': 'bniR', 'filter_predicate': 'less', 'filter_term': '50%'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': 'bniR', 'filter_predicate': 'greater', 'filter_term': '50%'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': 'bniR', 'filter_predicate': 'less_or_equal', 'filter_term': '50%'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': 'bniR', 'filter_predicate': 'greater_or_equal', 'filter_term': '50%'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': 'bniR', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'bniR', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

NUMBER_FORMULA_CURRENCY_US_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'ks14', 'filter_predicate': 'equal', 'filter_term': '$15'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': 'ks14', 'filter_predicate': 'not_equal', 'filter_term': '$15'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': 'ks14', 'filter_predicate': 'less', 'filter_term': '$15'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': 'ks14', 'filter_predicate': 'greater', 'filter_term': '$15'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': 'ks14', 'filter_predicate': 'less_or_equal', 'filter_term': '$15'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': 'ks14', 'filter_predicate': 'greater_or_equal', 'filter_term': '$15'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': 'ks14', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'ks14', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

NUMBER_FORMULA_SPLIT_BY_COMMA_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'equal', 'filter_term': '100,000'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'not_equal', 'filter_term': '100,000'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'less', 'filter_term': '100,000'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'greater', 'filter_term': '100,000'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'less_or_equal', 'filter_term': '100,000'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'greater_or_equal', 'filter_term': '100,000'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

NUMBER_FORMULA_DOT_SPLIT_BY_DOT_FILTER_CONSTANTS = [
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'equal', 'filter_term': '28.92546550'},
        "view_name": "filter_equal"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'not_equal', 'filter_term': '28.92546550'},
        "view_name": "filter_not_equal"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'less', 'filter_term': '28.92546550'},
        "view_name": "filter_less"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'greater', 'filter_term': '28.92546550'},
        "view_name": "filter_greater"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'less_or_equal', 'filter_term': '28.92546550'},
        "view_name": "filter_less_equal"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'greater_or_equal', 'filter_term': '28.92546550'},
        "view_name": "filter_greater_equal"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'is_empty', 'filter_term': ''},
        "view_name": "filter_is_empty"
    },
    {
        "filter": {'column_key': 'rrrq', 'filter_predicate': 'is_not_empty', 'filter_term': ''},
        "view_name": "filter_not_empty"
    },

]

LINK_FORMULA_EMPTY_FILTER = [
    {
        "filter": {'column_key': 'YlR7', 'filter_predicate': 'is_empty', 'filter_term': '', 'name': 'lookup_text'},
        "view_name": "empty_lookup_text"
    },
    {
        "filter": {'column_key': '5Euc', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_number'},
        "view_name": "empty_lookup_number"
    },
    {
        "filter": {'column_key': '23Cs', 'filter_predicate': 'is_empty', 'filter_term': [],'name': 'lookup_collaborator'},
        "view_name": "empty_lookup_collaborator"
    },
    {
        "filter": {'column_key': 'zVBz', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_date'},
        "view_name": "empty_lookup_date"
    },
    {
        "filter": {'column_key': 'Q5A5', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_duration'},
        "view_name": "empty_lookup_duration"
    },
    {
        "filter": {'column_key': 'fzyo', 'filter_predicate': 'is_empty', 'filter_term': [],'name': 'lookup_single_select'},
        "view_name": "empty_lookup_single_select"
    },
    {
        "filter": {'column_key': 'RrfC', 'filter_predicate': 'is_empty', 'filter_term': [],'name': 'lookup_multiple_select'},
        "view_name": "empty_lookup_multiple_select"
    },
    {
        "filter": {'column_key': '98jW', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_image'},
        "view_name": "empty_lookup_image"
    },
    {
        "filter": {'column_key': 'lETo', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_file'},
        "view_name": "empty_lookup_file"
    },
    {
        "filter": {'column_key': '6SDM', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_email'},
        "view_name": "empty_lookup_email"
    },
    {
        "filter": {'column_key': 'DSS4', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_url'},
        "view_name": "empty_lookup_URL"
    },

    {
        "filter": {'column_key': '6Mj0', 'filter_predicate': 'is', 'filter_term': False,'name': 'lookup_checkbox'},
        "view_name": "empty_lookup_checkbox"
    },
    {
        "filter": {'column_key': 'hMmq', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_rate'},
        "view_name": "empty_lookup_rate"
    },
    {
        "filter": {'column_key': 'A6C7', 'filter_predicate': 'is_empty', 'filter_term': [],'name': 'lookup_creator'},
        "view_name": "empty_lookup_creator"
    },
    {
        "filter": {'column_key': 'bstH', 'filter_predicate': 'is_empty', 'filter_term': [],'name': 'lookup_modifier'},
        "view_name": "empty_lookup_modifier"
    },
    {
        "filter": {'column_key': '5XbW', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_ctime'},
        "view_name": "empty_lookup_ctime"
    },
    {
        "filter": {'column_key': 'B3J7', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_mtime'},
        "view_name": "empty_lookup_mtime"
    },
    {
        "filter": {'column_key': 'O417', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_location'},
        "view_name": "empty_lookup_location"
    },
    {
        "filter": {'column_key': 'oH2J', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'lookup_formula'},
        "view_name": "empty_lookup_formula"
    },
    {
        "filter": {'column_key': 'ygYd', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'countlinks'},
        "view_name": "empty_countlinks"
    },
    {
        "filter": {'column_key': '4wMs', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'rollup_text'},
        "view_name": "empty_rollup_text"
    },
    {
        "filter": {'column_key': 'kw4q', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'rollup_number'},
        "view_name": "empty_rollup_number"
    },
    {
        "filter": {'column_key': 'j3Hl', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'rollup_date'},
        "view_name": "empty_rollup_date"
    },
    {
        "filter": {'column_key': 'pmGX', 'filter_predicate': 'is_empty', 'filter_term': '','name': 'findmin'},
        "view_name": "empty_findmin"
    },

]
