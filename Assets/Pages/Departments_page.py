import os
import Assets.Pages.Backend_utils as U
from Assets.Pages.Commons import Commons
import pyautogui


class DepartmentsPage(Commons):
    ADD_DEPARTMENT = (U.By.CSS_SELECTOR, 'div.dropMenu_option:nth-child(1) > span:nth-child(2)')
    DEPARTMENT_NAME = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > form > div.form_items > div.form_formItem.undefined.undefined.formItem_name > span > div > input')
    ACTIVE_DEPARTMENT = (U.By.CSS_SELECTOR, '.checkbox_checkboxCircle')
    ADD_NEW_DEPARTMENT = (U.By.CSS_SELECTOR, '.form_submitBtn')
    SORT_BY_DATE = (
    U.By.CSS_SELECTOR, '.table_table > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(6)')
    CREATED_DEPARTMENT_NAME = (
    U.By.CSS_SELECTOR, '.table_table > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')
    UPLOAD_IMAGE = (U.By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[2]/div[1]')
    UPLOAD_BACKGROUND_IMAGE = (U.By.XPATH, '//*[@id="root"]/div[1]/div[4]/div/div/form/div[1]/div[3]/div[1]')
    LAST_PAGE = (U.By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]/span[5]/i')
    wert_branch = (U.By.XPATH, '/html/body/div/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[3]')
    def click_go_to_department(self):
        self.wait_for(self.BRANCHES)
        self.click(self.BRANCHES)
        # Buffer for stupid site
        self.wait_for(self.SORT_BY_DATE)

    def go_to_create_department(self):
        self.wait_for(self.PAGE_SETTING)
        self.click(self.PAGE_SETTING)
        self.wait_for(self.ADD_DEPARTMENT)
        self.click(self.ADD_DEPARTMENT)

    def create_department_without_image(self, name, active):
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        if active:
            self.click(self.ACTIVE_DEPARTMENT)
        self.insert(self.DEPARTMENT_NAME, name)
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        self.click(self.ADD_NEW_DEPARTMENT)
        U.sleep(2)

    def create_department_with_image(self, name, active):
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        if active:
            self.click(self.ACTIVE_DEPARTMENT)
        self.insert(self.DEPARTMENT_NAME, name)
        self.click(self.UPLOAD_IMAGE)
        U.sleep(2)
        script_dir = os.path.dirname(os.path.abspath('Trado-Backend-project'))
        file_path = os.path.join(script_dir, 'Assets', 'Photos', 'cat_image.jpg')
        pyautogui.write(file_path)
        pyautogui.press('enter')
        U.sleep(2)
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        self.click(self.ADD_NEW_DEPARTMENT)
        U.sleep(2)

    def insert_updated_name(self, name):
        self.clear_department_name(self.DEPARTMENT_NAME)
        self.insert(self.DEPARTMENT_NAME, name)
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        U.sleep(5)
        self.click(self.ADD_NEW_DEPARTMENT)
        U.sleep(5)
        return name

    def changing_image(self):
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        self.click(self.UPLOAD_IMAGE)
        U.sleep(2)
        script_dir = os.path.dirname(os.path.abspath('Trado-Backend-project'))
        file_path = os.path.join(script_dir, 'Assets', 'Photos', 'cat_image.jpg')
        pyautogui.write(file_path)
        pyautogui.press('enter')
        U.sleep(2)
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        self.click(self.ADD_NEW_DEPARTMENT)

    def changing_background_picture(self):
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        self.click(self.UPLOAD_BACKGROUND_IMAGE)
        U.sleep(2)
        script_dir = os.path.dirname(os.path.abspath('Trado-Backend-project'))
        file_path = os.path.join(script_dir, 'Assets', 'Photos', 'cat_image.jpg')
        pyautogui.write(file_path)
        pyautogui.press('enter')
        U.sleep(2)
        self.wait_for(self.ADD_NEW_DEPARTMENT)
        self.click(self.ADD_NEW_DEPARTMENT)


    def last_page(self):
        self.click(self.LAST_PAGE)

    def sort_by_date(self):
        self.wait_for(self.SORT_BY_DATE)
        self.click(self.SORT_BY_DATE)

    def Navigate_last_page(self):
        self.click(self.LAST_PAGE)

    def Navigate_to_wert_branch(self):
        U.sleep(2)
        self.click(self.wert_branch)



