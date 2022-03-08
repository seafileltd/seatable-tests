from seatable_api import Base
import time
from filter_constant import API_TOKEN, DTABLE_WEB_SERVER_URL
from column_test.text_column_test import run_text_column_test
from column_test.number_column_test import run_number_colum_test
from column_test.multiple_select_column_test import run_multiple_select_column_test
from column_test.single_select_column_test import run_single_column_test
from column_test.image_column_test import run_image_column_test
from column_test.file_column_test import run_file_column_test
from column_test.duration_filter_test import run_duration_column_test
from column_test.date_filter_test import run_date_column_test
from column_test.collaborator_column_test import run_collaborator_column_test
from column_test.email_column_test import run_email_column_test
from column_test.rate_filter_test import run_rate_colum_test
from column_test.creator_column_test import run_creator_colum_test
from column_test.check_box_filter_test import run_checkbox_column_test
from column_test.modifier_column_test import run_modifier_colum_test
from column_test.url_column_test import run_url_column_test
from column_test.geolocation_column_test import run_location_column_test
from column_test.autonumber_filter_test import run_auto_number_colum_test




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

        run_url_column_test,
        run_location_column_test,
        run_modifier_colum_test,
        run_creator_colum_test,
        run_checkbox_column_test,
        run_email_column_test,
        run_rate_colum_test,
        run_auto_number_colum_test,
    ]










    for func in test_funcs:
        func(base, LOCAL_TEST)
        time.sleep(5)