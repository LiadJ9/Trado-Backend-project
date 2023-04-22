import Assets.Pages.Backend_utils as U
from Assets.Pages.Commons import Commons


class ProductPage(Commons):
    # Product Page Locators
    PRODUCT_PAGE_BRANCH = (
        U.By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/nav/div[2]/a[2]/span[2]')
    DOTS_SECTION = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_topRow > div > span > i')
    ADD_PRODUCT = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_topRow > div.dropMenu_dropMenu.table_dropMenu > div > div:nth-child(1)')
    NEXT_EDIT_BUTTON = (
        U.By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[4]/input')
    NEXT_EDIT_BUTTON2 = (
        U.By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[4]/input[2]')
    NEXT_EDIT_BUTTON3 = (
        U.By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[4]/input[2]')
    NEXT_EDIT_BUTTON4 = (
        U.By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[4]/input[2]')
    NEXT_EDIT_BUTTON5 = (
        U.By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[4]/input[2]')

    PREVIOUS_PAGE = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_tableScroll > div.paging_paging > div.paging_pagination > '
                           'span:nth-child(2) > i')
    BARCODE_FILTER = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_tableScroll > div.table_table > table > thead > tr > th:nth-child(1) '
                           '> span > i')
    NAME_FILTER = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_tableScroll > div.table_table > table > thead > tr > th:nth-child(2) >'
                           'span > i')
    PRICE_FILTER = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_tableScroll > div.table_table > table > thead > tr > th:nth-child('
                           '4) >'
                           'span > i')
    PROMOTION_FILTER = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div '
                           '> div.table_tableScroll > div.table_table > table > thead > tr > '
                           'th:nth-child(6) > span > i')
    PRODUCT_CLICK = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_tableScroll > div.table_table > table > tbody > tr:nth-child(5)')
    BARCODE_EDIT = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > span > '
                           'form > div.form_items > div.form_formItem.undefined.undefined.formItem_barcode > '
                           'span > div > input')
    CLICK_NEXT_BUTTON = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_tableScroll > div.paging_paging > div.paging_pagination > span:nth-child(2)')
    SEARCH_FIELD = (
        U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                           'div.table_topRow > span > span > div > input')
    RF_PRODUCT = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > div > '
                                     'div.table_tableScroll > div.table_table > table > tbody > tr:nth-child(1)')

    BIBI_83_PRODUCT = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.pages_pages > main > div.pages_children > '
                                          'div > div.table_tableScroll > div.table_table > table > tbody > '
                                          'tr:nth-child(15)')
    BUY_PRICE_FIELD = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div > '
                                          'span > form > div.form_items > '
                                          'div.form_formItem.undefined.undefined.formItem_salePrice > span > div > '
                                          'input')

    ADD_PRODUCT_BARCODE = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > '
                                              'div > span > form > div.form_items > '
                                              'div.form_formItem.undefined.undefined.formItem_barcode > span > div > '
                                              'input')

    ADD_PRODUCT_NAME = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div '
                                           '> span > form > div.form_items > '
                                           'div.form_formItem.undefined.undefined.formItem_name > span > div > input')
    ADD_PRODUCT_PRICE = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div '
                                            '> span > form > div.form_items > '
                                            'div.form_formItem.undefined.undefined.formItem_price > span > div > input')

    ADD_PRODUCT_BUY_PRICE = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > '
                                                'div > span > form > div.form_items > '
                                                'div.form_formItem.undefined.undefined.formItem_salePrice > span > '
                                                'div > input')

    ADD_PRODUCT_SUPREME_CATEGORY = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open '
                                                       '> div > div > span > form > div.form_items > '
                                                       'div.form_formItem.undefined.undefined.formItem_sectionId > '
                                                       'div.select_select')
    ADD_PRODUCT_SUPREME_CATEGORY_BEERS = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > '
                                                             'div.modal_modalWrapper.modal_open > div > div > span > '
                                                             'form > div.form_items > '
                                                             'div.form_formItem.undefined.undefined'
                                                             '.formItem_sectionId > div.select_select > '
                                                             'span.input_input > div.input_relative > div > '
                                                             'div:nth-child(3)')

    ADD_PRODUCT_STORE = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open > div > div '
                                            '> span > form > div.form_items > '
                                            'div.form_formItem.undefined.undefined.formItem_storeId > '
                                            'div.select_select > span.input_input > div.input_relative > input')

    ADD_PRODUCT_STORE_TELEPHONES = (U.By.CSS_SELECTOR, '#root > div:nth-child(1) > div.modal_modalWrapper.modal_open '
                                                       '> div > div > span > form > div.form_items > '
                                                       'div.form_formItem.undefined.undefined.formItem_storeId > '
                                                       'div.select_select > span.input_input > div.input_relative > '
                                                       'div > div:nth-child(21)')

    # Basic functions

    def click_on_product_branch(self):
        self.click(self.PRODUCT_PAGE_BRANCH)

    def click_on_dots_icon(self):
        self.click(self.DOTS_SECTION)

    def add_product(self):
        self.click(self.ADD_PRODUCT)

    def click_next_page(self):
        self.click(self.CLICK_NEXT_BUTTON)

    def click_previous_page(self):
        self.click(self.PREVIOUS_PAGE)

    def filtering_barcode(self):
        self.click(self.BARCODE_FILTER)

    def filtering_name(self):
        self.click(self.NAME_FILTER)

    def filtering_price(self):
        self.click(self.PRICE_FILTER)

    def filtering_promotion(self):
        self.click(self.PROMOTION_FILTER)

    def click_on_product(self):
        self.click(self.PRODUCT_CLICK)

    def edit_barcode(self):
        self.insert(self.BARCODE_EDIT, 'rf')

    def search_field(self):
        self.insert(self.SEARCH_FIELD, 'bibi83')

    def rf_product(self):
        self.wait_for(self.RF_PRODUCT)

    def click_next_edit_btn(self):
        self.click(self.NEXT_EDIT_BUTTON)

    def click_on_bibi83(self):
        self.click(self.BIBI_83_PRODUCT)

    def edit_buy_price(self):
        self.insert(self.BUY_PRICE_FIELD, '123')

    def click_next_edit_btn2(self):
        self.click(self.NEXT_EDIT_BUTTON2)

    def click_next_edit_btn3(self):
        self.click(self.NEXT_EDIT_BUTTON3)

    def click_next_edit_btn4(self):
        self.click(self.NEXT_EDIT_BUTTON4)

    def click_next_edit_btn5(self):
        self.click(self.NEXT_EDIT_BUTTON5)

    def get_buy_price(self):
        pass

    def get_buy_price_text(self):
        pass

    def check_product_price_order(self):
        pass

    def get_product_prices(self):
        pass

    def get_products_prices(self):
        pass

    def get_product_list(self):
        pass

    def add_product_barcode(self):
        self.click(self.ADD_PRODUCT_BARCODE)

    def add_product_insert_name(self):
        self.insert(self.ADD_PRODUCT_NAME, 'Maccabi')

    def add_product_price(self):
        self.insert(self.ADD_PRODUCT_PRICE, '14.5')

    def add_product_buy_price(self):
        self.insert(self.ADD_PRODUCT_BUY_PRICE, '5')

    def add_product_click_supreme_category_btn(self):
        self.click(self.ADD_PRODUCT_SUPREME_CATEGORY)

    def add_product_supreme_category_beers(self):
        self.click(self.ADD_PRODUCT_SUPREME_CATEGORY_BEERS)

    def add_product_store_btn(self):
        self.click(self.ADD_PRODUCT_STORE)

    def add_product_telephones_store_btn(self):
        self.click(self.ADD_PRODUCT_STORE_TELEPHONES)



