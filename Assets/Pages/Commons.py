import Assets.Pages.Backend_utils as U


class Commons(object):
    def __init__(self, driver):
        self.driver = driver
        self._wait = U.wdw(self.driver, 10)
        self._qwait = U.wdw(self.driver, 2)

    def wait_for(self, locator):
        return self._wait.until(U.ec.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self._wait.until(U.ec.element_to_be_clickable(locator))

    def wait_for_invisibility(self, locator):
        return self._wait.until(U.ec.invisibility_of_element(locator))

    def quick_wait_for_invisibility(self, locator):
        return self._qwait.until(U.ec.invisibility_of_element(locator))

    def wait_for_window_number_to_change(self, num):
        return self._wait.until(U.ec.number_of_windows_to_be(num))

    def switch_tabs(self, tab_to_switch):
        self.wait_for_window_number_to_change(2)
        for tab in self.driver.window_handles:
            if tab != tab_to_switch:
                self.driver.switch_to.window(tab)
                break

    def wait_for_url_change(self, url):
        return self._wait.until(U.ec.url_to_be(url))

    def wait_for_alert(self):
        return self._wait.until(U.ec.alert_is_present())

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_many(self, locator):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        temp = self.driver.find_element(*locator)
        return temp.text

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def insert(self, locator, insertion):
        locator = self.driver.find_element(*locator)
        locator.send_keys(insertion)

    def clear(self, locator):
        locator = self.driver.find_element(*locator)
        locator.click()
        locator.send_keys(U.keys.CLEAR)

    def get_element_size(self, locator):
        div = self.driver.find_element(*locator)
        amount = list(div.find_elements(U.By.TAG_NAME, 'a'))
        size = len(amount)
        return size

    def get_css(self, locator, value):
        css = self.driver.find_element(*locator)
        val = css.value_of_css_property(value)
        return val

    def get_element_color(self, locator):
        element = self.driver.find_element(*locator)
        colour_rgb = element.getCssValue("color")
        colour_hex = U.Color.from_string(colour_rgb).hex
        return colour_hex

    # LOGIN LOCATORS #

    LOGIN = (U.By.CSS_SELECTOR, '.input_relative > input:nth-child(1)')
    CLICK_LOGIN = (U.By.CSS_SELECTOR, '.form_submitBtn')
    PASSWORD = (U.By.CSS_SELECTOR, '.input_relative > input:nth-child(1)')
    SELECT_TRADO = (U.By.CSS_SELECTOR, 'div.storesList_store:nth-child(2)')
    REMEMBER_ME = (U.By.CSS_SELECTOR, 'div.form_formItem:nth-child(2)')
    NO_SUCH_USER_ERROR = (U.By.CSS_SELECTOR, '.form_message')
    CODE_VISIBILITY = (U.By.CSS_SELECTOR, '.fa-eye')
    LOGOUT = (U.By.CSS_SELECTOR, '.loggedin_hello > a:nth-child(1)')

    # MENU LOCATORS #

    PRODUCTS = (U.By.CSS_SELECTOR, 'a.menu_menuItem:nth-child(2)')
    USERS = (U.By.CSS_SELECTOR, 'a.menu_menuItem:nth-child(27)')
    DEPARTMENTS = (U.By.CSS_SELECTOR, 'a.menu_menuItem:nth-child(24)')
    ORDERS = (U.By.CSS_SELECTOR, 'a.menu_menuItem:nth-child(5)')
    PAGE_SETTING = (U.By.CSS_SELECTOR, '.fa-ellipsis-v')
    PAGE_SEARCH = (U.By.CSS_SELECTOR, '.input_iconInput > input:nth-child(2)')

    # USERS LOCATORS #

    SEARCH_BAR = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                                     'div.table_topRow > span > span > div > input')
    USER_FIRST_NAME = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                          'div > div.table_tableScroll > div.table_table > table > tbody > '
                                          'tr:nth-child(1) > td:nth-child(1)')
    USER_LAST_NAME = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                         'div > div.table_tableScroll > div.table_table > table > tbody > '
                                         'tr:nth-child(1) > td:nth-child(2)')
    USER_EMAIL = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                                     'div.table_tableScroll > div.table_table > table > tbody > tr:nth-child(1) > '
                                     'td:nth-child(3)')
    USER_PHONE_NUMBER = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                            'div > div.table_tableScroll > div.table_table > table > tbody > '
                                            'tr:nth-child(1) > td:nth-child(4)')
    USER_ADDRESS = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div '
                                       '> div.table_tableScroll > div.table_table > table > tbody > tr:nth-child(1) >'
                                       ' td:nth-child(6)')
    USER_MARKETING_LIST = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children '
                                              '> div > div.table_tableScroll > div.table_table > table > tbody > tr >'
                                              ' td:nth-child(7)')
    USER_ETRADO_APPROVED = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > '
                                               'div.pages_children > div > div.table_tableScroll > div.table_table > '
                                               'table > tbody > tr > td:nth-child(8)')
    USER_ACTIVE = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                                      'div.table_tableScroll > div.table_table > table > tbody > tr > td:nth-child(9)')
    USER_LAST_SEEN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                         'div > div.table_tableScroll > div.table_table > table > tbody > tr > '
                                         'td:nth-child(10)')
    USER_CREATED_AT = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                          'div > div.table_tableScroll > div.table_table > table > tbody > tr > '
                                          'td:nth-child(11)')
    FIRST_NAME_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                            'div > div.table_tableScroll > div.table_table > table > thead > tr > '
                                            'th:nth-child(1) > span')
    LAST_NAME_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                           'div > div.table_tableScroll > div.table_table > table > thead > tr > '
                                           'th:nth-child(2) > span')
    EMAIL_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div '
                                       '> div.table_tableScroll > div.table_table > table > thead > tr > '
                                       'th:nth-child(3) > span')
    PHONE_NUMBER_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children '
                                              '> div > div.table_tableScroll > div.table_table > table > thead > tr >'
                                              ' th:nth-child(4) > span')
    ADDRESS_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                         'div > div.table_tableScroll > div.table_table > table > thead > tr > '
                                         'th:nth-child(6) > span')
    MARKETING_LIST_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > '
                                                'div.pages_children > div > div.table_tableScroll > div.table_table > '
                                                'table > thead > tr > th:nth-child(7) > span')
    ETRADO_APPROVED_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > '
                                                 'div.pages_children > div > div.table_tableScroll > div.table_table '
                                                 '> table > thead > tr > th:nth-child(8) > span')
    ACTIVE_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div '
                                        '> div.table_tableScroll > div.table_table > table > thead > tr > '
                                        'th:nth-child(9) > span')
    LAST_SEEN_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                           'div > div.table_tableScroll > div.table_table > table > thead > tr > '
                                           'th:nth-child(10) > span')
    CREATED_AT_COLUMN = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                            'div > div.table_tableScroll > div.table_table > table > thead > tr > '
                                            'th:nth-child(11) > span')
    page_number_1 = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div '
                                        '> div.table_tableScroll > div.paging_paging > div.paging_pagination > '
                                        'span.paging_paginationNum.paging_active')
    page_number_2 = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div '
                                        '> div.table_tableScroll > div.paging_paging > div.paging_pagination > '
                                        'span:nth-child(2)')
    page_number_3 = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div '
                                        '> div.table_tableScroll > div.paging_paging > div.paging_pagination > '
                                        'span:nth-child(3)')
    one_page_forwards = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                            'div > div.table_tableScroll > div.paging_paging > div.paging_pagination '
                                            '> span:nth-child(6) > i')
    last_page = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                                    'div.table_tableScroll > div.paging_paging > div.paging_pagination > '
                                    'span:nth-child(7) > i')
    one_page_backwards = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children '
                                             '> div > div.table_tableScroll > div.paging_paging > '
                                             'div.paging_pagination > span:nth-child(2) > i')
    first_page = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                                     'div.table_tableScroll > div.paging_paging > div.paging_pagination > '
                                     'span:nth-child(1) > i')
    display_amount = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                         'div > div.table_tableScroll > div.paging_paging > div.paging_rowsNum > div '
                                         '> span.input_input > div > input')
    credit_score = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                       'div.index_scoreContainer > div')
    id_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > form > '
                                 'div.form_items > div.form_formItem.undefined.undefined.formItem_userId > span > div'
                                 ' > input')
    first_name_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                         'form > div.form_items > '
                                         'div.form_formItem.undefined.undefined.formItem_firstName > span > div > '
                                         'input')
    last_name_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                        'form > div.form_items > '
                                        'div.form_formItem.undefined.undefined.formItem_lastName > span > div > input')
    email_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > form '
                                    '> div.form_items > div.form_formItem.undefined.undefined.formItem_email > span >'
                                    ' div > input')
    phone_number_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div '
                                           '> form > div.form_items > '
                                           'div.form_formItem.undefined.undefined.formItem_phone > span > div > input')
    additional_phone_number_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > '
                                                      'div > div > form > div.form_items > '
                                                      'div.form_formItem.undefined.undefined.formItem_phone2 > span > '
                                                      'div > input')
    city_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > form > '
                                   'div.form_items > div.form_formItem.form_group.undefined.formItem_address > '
                                   'div.form_formGroup > div.form_formItem.undefined.undefined.formItem_city > span > '
                                   'div > input')
    street_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > form '
                                     '> div.form_items > div.form_formItem.form_group.undefined.formItem_address > '
                                     'div.form_formGroup > div.form_formItem.undefined.undefined.formItem_street > '
                                     'span > div > input')
    building_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                       'form > div.form_items > '
                                       'div.form_formItem.form_group.undefined.formItem_address > div.form_formGroup '
                                       '> div.form_formItem.undefined.undefined.formItem_building > span > div > input')
    apartment_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                        'form > div.form_items > '
                                        'div.form_formItem.form_group.undefined.formItem_address > div.form_formGroup '
                                        '> div.form_formItem.undefined.undefined.formItem_apartment > span > div > '
                                        'input')
    floor_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > form '
                                    '> div.form_items > div.form_formItem.form_group.undefined.formItem_address > '
                                    'div.form_formGroup > div.form_formItem.undefined.undefined.formItem_floor > span '
                                    '> div > input')
    comment_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                      'form > div.form_items > '
                                      'div.form_formItem.form_group.undefined.formItem_address > div.form_formGroup > '
                                      'div.form_formItem.undefined.undefined.formItem_comment > textarea')
    account_owner_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div '
                                            '> form > div.form_items > '
                                            'div.form_formItem.form_group.undefined.formItem_paymentBillInfo > '
                                            'div.form_formGroup > '
                                            'div.form_formItem.undefined.undefined.formItem_acountOwner > span > div '
                                            '> input')
    number_account_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > '
                                             'div > form > div.form_items > '
                                             'div.form_formItem.form_group.undefined.formItem_paymentBillInfo > '
                                             'div.form_formGroup > '
                                             'div.form_formItem.undefined.undefined.formItem_numberAcount > span > '
                                             'div > input')
    number_branch_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div '
                                            '> form > div.form_items > '
                                            'div.form_formItem.form_group.undefined.formItem_paymentBillInfo > '
                                            'div.form_formGroup > '
                                            'div.form_formItem.undefined.undefined.formItem_numberBranch > span > div '
                                            '> input')
    bank_name_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                        'form > div.form_items > '
                                        'div.form_formItem.form_group.undefined.formItem_paymentBillInfo > '
                                        'div.form_formGroup > div.form_formItem.undefined.undefined.formItem_bankName '
                                        '> span > div > input')
    credit_score_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div '
                                           '> form > div.form_items > '
                                           'div.form_formItem.undefined.undefined.formItem_creditScore > span > div > '
                                           'input')
    balance_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                      'form > div.form_items > '
                                      'div.form_formItem.form_group.undefined.formItem_etradoBalance > '
                                      'div.form_formGroup > div.form_formItem.undefined.undefined.formItem_balance > '
                                      'span > div > input')
    income_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > form '
                                     '> div.form_items > '
                                     'div.form_formItem.form_group.undefined.formItem_etradoBalance > '
                                     'div.form_formGroup > div.form_formItem.undefined.undefined.formItem_income > '
                                     'span > div > input')
    outcome_box = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                      'form > div.form_items > '
                                      'div.form_formItem.form_group.undefined.formItem_etradoBalance > '
                                      'div.form_formGroup > div.form_formItem.undefined.undefined.formItem_outcome > '
                                      'span > div > input')
    marketing_list_button = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > '
                                                'div > form > div.form_items > '
                                                'div.form_formItem.undefined.undefined.formItem_marketingList > span > '
                                                'span')
    Takanon_button = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                         'form > div.form_items > '
                                         'div.form_formItem.undefined.undefined.formItem_takanon > span > span')
    ETrado_approved_button = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div '
                                                 '> div > form > div.form_items > '
                                                 'div.form_formItem.undefined.undefined.formItem_eTradoApproved > '
                                                 'span > span')
    update_button = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                        'form > input')

    # USER DETAILS #

    FIRST_NAME = 'Jace'
    LAST_NAME = 'Parker'
    EMAIL = 'gocew82872@lieboe.com'
    PHONE = '0552992042'
    CITY = 'Sunrise, Arizona'
    STREET = 'air base'
    BUILDING = '3'
    CREDIT_SCORE = '600'
    LAST_SEEN = '07/04/23, 17:30'
    CREATED_AT = '22/03/23, 09:55'

    # ADVANCED FUNCTIONS #


class LogIn(Commons):
    def eye_visibility(self, phone_number, code):
        U.sleep(4)
        self.wait_for(Commons.LOGIN)
        self.insert(Commons.LOGIN, phone_number)
        self.click(Commons.CLICK_LOGIN)
        self.wait_for(Commons.PASSWORD)
        self.insert(Commons.PASSWORD, code)
        self.click(Commons.CODE_VISIBILITY)
        psd = self.get_text(Commons.PASSWORD)
        return psd

    def log_in(self, phone_number, code, remember):
        logging = True
        while logging:
            self.wait_for(Commons.LOGIN)
            self.insert(Commons.LOGIN, phone_number)
            self.click(Commons.CLICK_LOGIN)
            U.sleep(1)
            err = self.find(Commons.NO_SUCH_USER_ERROR)
            if err.is_displayed():
                break
            self.wait_for(Commons.PASSWORD)
            self.insert(Commons.PASSWORD, code)
            U.sleep(1)
            if remember:
                self.click(Commons.REMEMBER_ME)
            self.click(Commons.CLICK_LOGIN)
            try:
                err = self.find(Commons.NO_SUCH_USER_ERROR)
                if err.is_displayed():
                    break
            except:
                pass
            U.sleep(2)
            self.wait_for(Commons.SELECT_TRADO).click()
            logging = False

    def find_logout(self):
        invis = self.wait_for_invisibility(Commons.LOGOUT)
        return invis

    # STATIC METHODS #

    @staticmethod
    def random_phone_number():
        nums = U.string.digits
        phone_number = (''.join(U.random.choice(nums) for _ in range(7)))
        return f'057{phone_number}'
