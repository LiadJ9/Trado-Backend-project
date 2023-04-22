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
        self.wait_for(locator)
        self.driver.find_element(*locator).click()

    def insert(self, locator, insertion):
        locator = self.driver.find_element(*locator)
        locator.send_keys(insertion)

    def clear(self, locator):
        locator = self.driver.find_element(*locator)
        locator.click()
        locator.send_keys(U.keys.CLEAR)

    def clear_department_name(self, locator):
        locator = self.driver.find_element(*locator)
        locator.clear()

    def get_class(self, locator):
        locator = self.driver.find_element(*locator)
        class_name = locator.get_attribute('class')
        return class_name

    def get_element_size(self, locator):
        div = self.driver.find_element(*locator)
        amount = list(div.find_elements(U.By.TAG_NAME, 'a'))
        size = len(amount)
        return size

    def get_css(self, locator, value):
        css = self.driver.find_element(*locator)
        val = css.value_of_css_property(value)
        return val

    def upload_image(self, locator, image_path):
        locator = self.driver.find_element(*locator)
        locator.send_keys(image_path)



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
    ORDERS = (U.By.CSS_SELECTOR, 'a.menu_menuItem:nth-child(5)')
    BRANCHES = (U.By.CSS_SELECTOR, 'a.menu_menuItem:nth-child(24)')
    # השלוש נקודות בצד שמאל
    PAGE_SETTING = (U.By.CSS_SELECTOR, '.fa-ellipsis-v')
    PAGE_SEARCH = (U.By.CSS_SELECTOR, '.input_iconInput > input:nth-child(2)')

    # ADVANCED FUNCTIONS #


class DashboardAndHeaders(Commons):
    BURGER_MENU = (U.By.CSS_SELECTOR, '.fa-bars')
    STORE_SELECTOR = (U.By.CSS_SELECTOR, 'a.loggedin_row')
    IS_MENU_OPEN = (U.By.CSS_SELECTOR, '.pages_pages > div:nth-child(1)')
    LOGO = (U.By.CSS_SELECTOR, '.logo_logo')
    DANI_MAMTAKIM = (U.By.CSS_SELECTOR, '.storesList_store')
    LOADING = (U.By.CSS_SELECTOR, '.loader_miniLoader')

    def click_burger_menu(self):
        self.click(self.BURGER_MENU)

    def click_logo(self):
        U.sleep(1)
        self.click(self.LOGO)

    def switch_store(self, store_locator):
        self.click(self.STORE_SELECTOR)
        U.sleep(1)
        self.click(store_locator)
        U.sleep(2)


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

    # phone number, code and remember me required (remember me is either True OR False

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
            U.sleep(1)
            self.wait_for(Commons.SELECT_TRADO).click()
            U.sleep(2)
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
