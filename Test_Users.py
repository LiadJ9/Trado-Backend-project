# importing the necessary libraries
import time
import allure
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains as AC
import Assets.Pages.Backend_utils as U
from Assets.Pages.Users_Page import UsersPage as UP
import test_login


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(1)
@allure.title("getting to the users window")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to test getting to the users window
def test_1_getting_to_the_users_window(driver):
    test_driver = driver
    test_login.test_valid_login(test_driver)
    UP(test_driver).scroll_sidebar_down()
    time.sleep(2)
    UP(test_driver).click(UP.USERS_WINDOW_BUTTON)
    time.sleep(2)
    assert test_driver.current_url == 'http://qa-admin.trado.co.il/#/users'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(2)
@allure.title("searching for a user")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to test searching for a user
def test_2_search_for_a_user(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).search_first_name_to_search()
    time.sleep(2)
    first_name = UP(test_driver).get_text(UP.USER_FIRST_NAME)
    last_name = UP(test_driver).get_text(UP.USER_LAST_NAME)
    assert first_name == UP(test_driver).FIRST_NAME
    assert last_name == UP(test_driver).LAST_NAME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(3)
@allure.title("searching for a user using a partial name")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to test searching for a user using a partial name
def test_3_search_for_a_user_using_a_partial_name(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).search_partial_name_to_search()
    time.sleep(3)
    first_name = UP(test_driver).get_text(UP.USER_FIRST_NAME)
    last_name = UP(test_driver).get_text(UP.USER_LAST_NAME)
    assert first_name == UP(test_driver).FIRST_NAME
    assert last_name == UP(test_driver).LAST_NAME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(4)
@allure.title("validate first name in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate first name in the table
def test_4_validate_first_name_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    data = UP(test_driver).get_text(UP.USER_FIRST_NAME)
    assert data == UP(test_driver).FIRST_NAME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(5)
@allure.title("validate last name in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate last name in the table
def test_5_validate_last_name_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    data = UP(test_driver).get_text(UP.USER_LAST_NAME)
    assert data == UP(test_driver).LAST_NAME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(6)
@allure.title("validate email in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate email in the table
def test_6_validate_email_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    data = UP(test_driver).get_text(UP.USER_EMAIL)
    assert data == UP(test_driver).EMAIL


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(7)
@allure.title("validate phone number in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate phone number in the table
def test_7_validate_phone_number_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    data = UP(test_driver).get_text(UP.USER_PHONE_NUMBER)
    assert data == UP(test_driver).PHONE


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(8)
@allure.title("validate address in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate address in the table
def test_8_validate_address_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    data = UP(test_driver).get_text(UP.USER_ADDRESS)
    address = f'{UP(test_driver).STREET} {UP(test_driver).BUILDING}/{UP(test_driver).APARTMENT}, {UP(test_driver).CITY}'
    assert data == address


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(9)
@allure.title("validate marketing list in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate marketing list in the table
def test_9_validate_marketing_list_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    data = UP(test_driver).get_text(UP.USER_MARKETING_LIST)
    assert data == '✗'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(10)
@allure.title("validate ETrado in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate ETrado in the table
def test_10_validate_etrado_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    data = UP(test_driver).get_text(UP.USER_ETRADO_APPROVED)
    assert data == '✓'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(11)
@allure.title("validate active status in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate active status in the table
def test_11_validate_active_status_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    data = UP(test_driver).get_text(UP.USER_ACTIVE)
    assert data == '✓'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(12)
@allure.title("validate last seen in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate last seen in the table
def test_12_validate_last_seen_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).scroll_table_left()
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_LAST_SEEN)
    assert data == UP(test_driver).LAST_SEEN


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(13)
@allure.title("validate crated at in the table")
@allure.severity(allure.severity_level.CRITICAL)  # test importance: CRITICAL/SANITY
# creating a test to validate crated at in the table
def test_13_validate_crated_at_in_the_table(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).scroll_table_left()
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_CREATED_AT)
    assert data == UP(test_driver).CREATED_AT


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(14)
@allure.title("validate the id in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the id in user details
def test_14_validate_the_id_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    data = UP(test_driver).get_default_value(UP.id_box)
    assert data == UP(test_driver).ID


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(15)
@allure.title("validate the first name in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the first name in user details
def test_15_validate_the_first_name_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    data = UP(test_driver).get_default_value(UP.first_name_box)
    assert data == UP(test_driver).FIRST_NAME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(16)
@allure.title("validate the last name in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the last name in user details
def test_16_validate_the_last_name_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    data = UP(test_driver).get_default_value(UP.last_name_box)
    assert data == UP(test_driver).LAST_NAME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(17)
@allure.title("validate the email in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the email in user details
def test_17_validate_the_email_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    data = UP(test_driver).get_default_value(UP.email_box)
    assert data == UP(test_driver).EMAIL


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(18)
@allure.title("validate the phone number in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the phone number in user details
def test_18_validate_the_phone_number_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    data = UP(test_driver).get_default_value(UP.phone_number_box)
    assert data == UP(test_driver).PHONE


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(19)
@allure.title("validate the additional phone number in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the additional phone number in user details
def test_19_validate_the_additional_phone_number_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    data = UP(test_driver).get_default_value(UP.additional_phone_number_box)
    assert data == UP(test_driver).PHONE


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(20)
@allure.title("validate the credit score meter in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the credit score meter in user details
def test_20_validate_the_credit_score_meter_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.credit_score)
    assert data == UP(test_driver).CREDIT_SCORE


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(21)
@allure.title("validate the city in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the city in user details
def test_21_validate_the_city_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.city_box)
    assert data == UP(test_driver).CITY


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(22)
@allure.title("validate the street in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the street in user details
def test_22_validate_the_street_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.street_box)
    assert data == UP(test_driver).STREET


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(23)
@allure.title("validate the building in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the building in user details
def test_23_validate_the_building_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.building_box)
    assert data == UP(test_driver).BUILDING


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(24)
@allure.title("validate the apartment in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the apartment in user details
def test_24_validate_the_apartment_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.apartment_box)
    assert data == UP(test_driver).APARTMENT


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(25)
@allure.title("validate the floor in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the floor in user details
def test_25_validate_the_floor_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.floor_box)
    assert data == UP(test_driver).FLOOR


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(26)
@allure.title("validate the comment in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the comment in user details
def test_26_validate_the_comment_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.comment_box)
    assert data == UP(test_driver).COMMENT


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(27)
@allure.title("validate the account owner in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the account owner in user details
def test_27_validate_the_account_owner_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.account_owner_box)
    assert data == UP(test_driver).ACCOUNT_OWNER


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(28)
@allure.title("validate the account number in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the account number in user details
def test_28_validate_the_account_number_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.number_account_box)
    assert data == UP(test_driver).NUMBER_ACCOUNT


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(29)
@allure.title("validate the branch number in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the branch number in user details
def test_29_validate_the_branch_number_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.number_branch_box)
    assert data == UP(test_driver).NUMBER_BRANCH


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(30)
@allure.title("validate the name of the bank in user detail")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the name of the bank in user detail
def test_30_validate_the_name_of_the_bank_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_once()
    data = UP(test_driver).get_default_value(UP.bank_name_box)
    assert data == UP(test_driver).BANK_NAME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(31)
@allure.title("validate the credit score in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the credit score in user details
def test_31_validate_the_credit_score_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_twice()
    data = UP(test_driver).get_default_value(UP.credit_score_box)
    assert data == UP(test_driver).CREDIT_SCORE


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(32)
@allure.title("validate the balance in user detail")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the balance in user detail
def test_32_validate_the_balance_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_twice()
    data = UP(test_driver).get_default_value(UP.balance_box)
    assert data == UP(test_driver).BALANCE


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(33)
@allure.title("validate the income in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the income in user details
def test_33_validate_the_income_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_twice()
    data = UP(test_driver).get_default_value(UP.income_box)
    assert data == UP(test_driver).INCOME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(34)
@allure.title("validate the 'outcome' in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the 'outcome' in user details
def test_34_validate_the_outcome_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_twice()
    data = UP(test_driver).get_default_value(UP.outcome_box)
    assert data == UP(test_driver).OUTCOME


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(35)
@allure.title("validate the status of marketing list in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the status of marketing list in user details
def test_35_validate_the_status_of_marketing_list_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_twice()
    data = UP(test_driver).get_element_color(UP(test_driver).marketing_list_button)
    assert data == UP(test_driver).OFF_COLOR


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(36)
@allure.title("validate the status of ETrado approved in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the status of ETrado approved in user details
def test_36_validate_the_status_of_etrado_approved_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_twice()
    data = UP(test_driver).get_element_color(UP(test_driver).ETrado_approved_button)
    assert data == UP(test_driver).ON_COLOR


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(37)
@allure.title("validate the status of 'Takanon' in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the status of 'Takanon' in user details
def test_37_validate_the_status_of_takanon_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    UP(test_driver).scroll_user_details_down_twice()
    data = UP(test_driver).get_element_color(UP(test_driver).Takanon_button)
    assert data == UP(test_driver).ON_COLOR


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(38)
@allure.title("validate the picture in user details")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to validate the picture in user details
def test_38_validate_the_picture_in_user_details(driver):
    test_driver = driver
    test_2_search_for_a_user(test_driver)
    UP(test_driver).click(UP(test_driver).USER_LAST_NAME)
    time.sleep(2)
    data = UP(test_driver).get_inner_html(UP.picture_box)
    assert data != '<img src=\"https://storage.cloud.google.com/trado_images/user/3r71hi9klfje3vwo4jp555dl45kvcz9' \
                   '-1682152288223\"><input type=\"file\" accept=\"image/*\">'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(39)
@allure.title("navigate between pages using page number")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to navigate between pages using page number
def test_39_navigate_between_pages_using_page_number(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-50 מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).page_number_2)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 51-100 מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).page_number_1)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-50 מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).page_number_3)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 101-150 מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(40)
@allure.title("move one page forward")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to move 1-page forward
def test_40_move_one_page_forward(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).click(UP(test_driver).one_page_forwards)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 51-100 מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(41)
@allure.title("move to last page")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to move to last page
def test_41_move_to_last_page(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).click(UP(test_driver).last_page)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1101-1150 מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(42)
@allure.title("move one page backwards")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to move 1-page backwards
def test_42_move_one_page_backwards(driver):
    test_driver = driver
    test_40_move_one_page_forward(test_driver)
    UP(test_driver).click(UP(test_driver).one_page_backwards)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-50 מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(43)
@allure.title("move to the first page")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to move to the first page
def test_43_move_to_the_first_page(driver):
    test_driver = driver
    test_41_move_to_last_page(test_driver)
    UP(test_driver).click(UP(test_driver).first_page)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-50 מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(44)
@allure.title("search for a user from a different page")
@allure.severity(allure.severity_level.NORMAL)  # test importance: HIGH
# creating a test to search for a user from a different page
def test_44_search_for_a_user_from_a_different_page(driver):
    test_driver = driver
    test_40_move_one_page_forward(test_driver)
    UP(test_driver).search_first_name_to_search()
    time.sleep(2)
    try:
        first_name = UP(test_driver).get_text(UP.USER_FIRST_NAME)
        last_name = UP(test_driver).get_text(UP.USER_LAST_NAME)
        assert first_name == UP(test_driver).FIRST_NAME
        assert last_name == UP(test_driver).LAST_NAME
    except NoSuchElementException:
        print("\nThere was no user shown")
        assert False


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(45)
@allure.title("sort the table by first name")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by first name
def test_45_sort_the_table_by_first_name(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).click(UP(test_driver).FIRST_NAME_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_FIRST_NAME)
    assert data == ''

    UP(test_driver).click(UP(test_driver).FIRST_NAME_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_FIRST_NAME)
    assert data == 'שדב'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(46)
@allure.title("sort the table by last name")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by last name
def test_46_sort_the_table_by_last_name(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).click(UP(test_driver).LAST_NAME_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_LAST_NAME)
    assert data == ''

    UP(test_driver).click(UP(test_driver).LAST_NAME_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_LAST_NAME)
    assert data == 'תקלה'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(47)
@allure.title("sort the table by email")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by email
def test_47_sort_the_table_by_email(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).click(UP(test_driver).EMAIL_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_EMAIL)
    assert data == ''

    UP(test_driver).click(UP(test_driver).EMAIL_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_EMAIL)
    assert data == 'zzzzz@gmail.com'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(48)
@allure.title("sort the table by phone number")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by phone number
def test_48_sort_the_table_by_phone_number(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).click(UP(test_driver).PHONE_NUMBER_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_PHONE_NUMBER)
    assert data == ''

    UP(test_driver).click(UP(test_driver).PHONE_NUMBER_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_PHONE_NUMBER)
    assert data == 'צהמעגכגגעכגעגכ'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(49)
@allure.title("sort the table by address")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by address
def test_49_sort_the_table_by_address(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).click(UP(test_driver).ADDRESS_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_ADDRESS)
    assert data == ''

    UP(test_driver).click(UP(test_driver).ADDRESS_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_ADDRESS)
    assert data == 'Telavive 22/4'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(50)
@allure.title("sort the table by marketing list status")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by marketing list statu
def test_50_sort_the_table_by_marketing_list_status(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).scroll_table_left()
    time.sleep(2)
    UP(test_driver).click(UP(test_driver).MARKETING_LIST_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_MARKETING_LIST)
    assert data == '✓'

    UP(test_driver).click(UP(test_driver).MARKETING_LIST_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_MARKETING_LIST)
    assert data == '✗'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(51)
@allure.title("sort the table by ETrado status")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by ETrado status
def test_51_sort_the_table_by_etrado_status(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).scroll_table_left()
    UP(test_driver).click(UP(test_driver).ETRADO_APPROVED_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_ETRADO_APPROVED)
    assert data == '✓'

    UP(test_driver).click(UP(test_driver).ETRADO_APPROVED_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_ETRADO_APPROVED)
    assert data == '✗'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(52)
@allure.title("sort the table by active status")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by ETrado status
def test_52_sort_the_table_by_active_status(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).scroll_table_left()
    UP(test_driver).click(UP(test_driver).ACTIVE_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_ACTIVE)
    assert data == '✓'

    UP(test_driver).click(UP(test_driver).ACTIVE_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_ACTIVE)
    assert data == '✗'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(53)
@allure.title("sort the table by last seen")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by last seen
def test_53_sort_the_table_by_last_seen(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).scroll_table_left()
    UP(test_driver).click(UP(test_driver).LAST_SEEN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_LAST_SEEN)
    assert data == '20/01/21, 09:41'

    UP(test_driver).click(UP(test_driver).LAST_SEEN)
    time.sleep(2)
    UP(test_driver).scroll_table_left()
    data = UP(test_driver).get_text(UP.USER_LAST_SEEN)
    assert data == 'היום, 15:46'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(54)
@allure.title("sort the table by date of creation")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to sort the table by date of creation
def test_54_sort_the_table_by_date_of_creation(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).scroll_table_left()
    UP(test_driver).click(UP(test_driver).CREATED_AT_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_CREATED_AT)
    assert data == '19/01/21, 11:13'

    UP(test_driver).click(UP(test_driver).CREATED_AT_COLUMN)
    time.sleep(2)
    data = UP(test_driver).get_text(UP.USER_CREATED_AT)
    assert data == 'היום, 15:46'


# creating the test setup for the allure report
@allure.epic('Test Users')
@allure.id(55)
@allure.title("changing the amount of rows displayed")
@allure.severity(allure.severity_level.MINOR)  # test importance: MEDIUM
# creating a test to test changing the amount of rows displayed
def test_55_changing_the_amount_of_rows_displayed(driver):
    test_driver = driver
    test_1_getting_to_the_users_window(test_driver)
    UP(test_driver).click(UP(test_driver).display_amount)
    UP(test_driver).click(UP(test_driver).amount_option_1)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-20' \
                           f' מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).display_amount)
    UP(test_driver).click(UP(test_driver).amount_option_2)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-50' \
                           f' מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).display_amount)
    UP(test_driver).click(UP(test_driver).amount_option_3)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-75' \
                           f' מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).display_amount)
    UP(test_driver).click(UP(test_driver).amount_option_4)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-100' \
                           f' מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).display_amount)
    UP(test_driver).click(UP(test_driver).amount_option_5)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-150' \
                           f' מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).display_amount)
    UP(test_driver).click(UP(test_driver).amount_option_6)
    time.sleep(2)
    current_rows = UP(test_driver).get_text(UP(test_driver).rows_displayed)
    assert current_rows == f'מציג 1-200' \
                           f' מתוך {UP(test_driver).AMOUNT_OF_USERS} שורות'

    UP(test_driver).click(UP(test_driver).display_amount)
    UP(test_driver).click(UP(test_driver).amount_option_7)
    time.sleep(5)
    current_rows = UP(test_driver).get_text(UP(test_driver).all_rows_displayed)
    assert current_rows == f'סה״כ: {UP(test_driver).AMOUNT_OF_USERS} שורות'
