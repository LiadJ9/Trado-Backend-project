import os
import random
import allure
import pymongo

from Assets.Pages.Departments_page import DepartmentsPage as BP
from Assets.Pages.Commons import LogIn
import Assets.Pages.MongoDB_requests as R
import Assets.Pages.Backend_utils as U


@allure.epic('Test Departments')
@allure.id(43)
@allure.title("click department button")
@allure.description('Navigate to department page')
@allure.severity(allure.severity_level.NORMAL)
def test_click_departments_button(driver):
    department = BP(driver)
    login = LogIn(driver)
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Navigate to Departments page'):
        department.click_go_to_department()
    with allure.step('Assertion that navigation is completed'):
        assert driver.current_url == 'http://qa-admin.trado.co.il/#/departments'


@allure.epic('Test Departments')
@allure.id(44)
@allure.title("Create new department (no image)")
@allure.description('Creating a new department works as intended')
@allure.severity(allure.severity_level.NORMAL)
def test_create_department_valid(driver):
    department = BP(driver)
    login = LogIn(driver)
    request = R.MongoRequests()
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Navigating to branch area'):
        department.click_go_to_department()
    with allure.step('Navigating to the add new branch page'):
        department.go_to_create_department()
    with allure.step('Creating new branch'):
        test_branch = f'BananaDogDepartment{random.randint(1, 9999)}'
        department.create_department_without_image(test_branch, False)
    with allure.step('Asserting new branch has been created in '):
        name_in_db = request.find_existing_branch(test_branch)
        supposed_branch = department.get_text(department.CREATED_DEPARTMENT_NAME)
        assert supposed_branch == test_branch
        assert name_in_db == test_branch


@allure.epic('Test Departments')
@allure.id(45)
@allure.title("Create new department (with image)")
@allure.description('Creating a new department works as intended')
@allure.severity(allure.severity_level.NORMAL)
def test_create_department_with_image_valid(driver):
    department = BP(driver)
    login = LogIn(driver)
    request = R.MongoRequests()
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Navigating to branch area'):
        department.click_go_to_department()
    with allure.step('Navigating to the add new branch page'):
        department.go_to_create_department()
    with allure.step('Creating new branch name'):
        test_branch = f'BananaDogDepartment{random.randint(1, 9999)}'
        department.create_department_with_image(test_branch, False)
    with allure.step('Asserting new branch has been created in '):
        name_in_db = request.find_existing_branch(test_branch)
        supposed_branch = department.get_text(department.CREATED_DEPARTMENT_NAME)
        image_name = request.find_existing_image_branch(test_branch)
        assert image_name
        assert supposed_branch == test_branch
        assert name_in_db == test_branch


@allure.epic('Test Departments')
@allure.id(46)
@allure.title("Update branch name")
@allure.description('changing the branch to a new name')
@allure.severity(allure.severity_level.NORMAL)
def test_Update_a_Department_name(driver):
    department = BP(driver)
    login = LogIn(driver)
    request = R.MongoRequests()
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Navigating to branch area'):
        department.click_go_to_department()
    with allure.step('Navigating to the add new branch page'):
        department.go_to_create_department()
    with allure.step('Creating new branch'):
        test_branch = f'{random.randint(1, 9999)}'
        department.create_department_without_image(test_branch, False)
    with allure.step('Updating branch name'):
        department.Navigate_last_page()
        department.click((U.By.XPATH, f'//*[text()="{test_branch}"]'))
        updated_branch = department.insert_updated_name(f'avocado{random.randint(1, 9999)}')
    with allure.step('Asserting new branch has been created in '):
        name_in_db = request.find_existing_branch(updated_branch)
        supposed_branch = department.get_text(department.CREATED_DEPARTMENT_NAME)
        assert supposed_branch == updated_branch
        assert name_in_db == updated_branch


@allure.epic('Test Departments')
@allure.id(47)
@allure.title("Update branch Background picture")
@allure.description('updating branch background picture')
@allure.severity(allure.severity_level.NORMAL)
def test_Update_a_Department_Background_picture(driver):
    department = BP(driver)
    login = LogIn(driver)
    request = R.MongoRequests()
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Navigating to branch area'):
        department.click_go_to_department()
    with allure.step('Navigating to wert branch'):
        department.Navigate_to_wert_branch()
    with allure.step('Updating branch background picture'):
        department.changing_background_picture()
        department.Navigate_to_wert_branch()
        U.sleep(2)
    with allure.step('assert the background image'):
        branch_name = 'wert'
        background_image_name = request.find_existing_background_image_branch(branch_name)
        assert background_image_name

@allure.epic('Test Departments')
@allure.id(48)
@allure.title("Update branch picture")
@allure.description('updating branch picture')
@allure.severity(allure.severity_level.NORMAL)
def test_Update_a_Department_picture(driver):
    department = BP(driver)
    login = LogIn(driver)
    request = R.MongoRequests()
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Navigating to branch area'):
        department.click_go_to_department()
    with allure.step('Navigating to wert branch'):
        department.Navigate_to_wert_branch()
    with allure.step('Updating branch picture'):
        department.changing_image()
        department.Navigate_to_wert_branch()
        U.sleep(2)
    with allure.step('assert the background image'):
        branch_name = 'wert'
        image_name = request.find_existing_image_branch(branch_name)
        assert image_name
