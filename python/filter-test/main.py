from seatable_api import Base
import time
from filter_constant import API_TOKEN, DTABLE_WEB_SERVER_URL
from text_column_test import run_text_column_test
from number_column_test import run_number_colum_test
from multiple_select_column_test import run_multiple_select_column_test
from single_select_column_test import run_single_column_test
from image_column_test import run_image_column_test
from file_column_test import run_file_column_test
from duration_filter_test import run_duration_column_test
from date_filter_test import run_date_column_test
from collaborator_column_test import run_collaborator_column_test

if __name__ == '__main__':
    base = Base(API_TOKEN, DTABLE_WEB_SERVER_URL)
    base.auth()

    LOCAL_TEST = True

    test_funcs = [
        run_text_column_test,
        run_number_colum_test,
        run_multiple_select_column_test,
        run_single_column_test,
        run_image_column_test,
        run_duration_column_test,
        run_file_column_test,
        run_date_column_test,
        run_collaborator_column_test,
    ]

    for func in test_funcs:
        func(base, LOCAL_TEST)
        time.sleep(5)