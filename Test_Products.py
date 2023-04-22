import allure
import pytest
from Assets.Pages.Commons import LogIn
from Assets.Pages.Product_Page import ProductPage
import time


@allure.epic('Product Page')
@allure.id(1)
@allure.title("Click on Product Branch and verify URL")
@allure.description('Verify if user can click on Product Branch and URL is updated')
@allure.severity(allure.severity_level.NORMAL)
def test_click_on_product_branch_and_verify_url(driver):
    login = LogIn(driver)
    product = ProductPage(driver)

    with allure.step('Logging in with valid credentials'):
        login.log_in('1951111111', '1234', False)

    with allure.step('Clicking on Product Branch'):
        product.click_on_product_branch()

    with allure.step('Verifying that we are in the products section'):
        assert "products" in driver.current_url.lower(), "Not in the products section"


@allure.epic('Product Page')
@allure.id(2)
@allure.title("Moving to the next product page")
@allure.description('Verify if user can move to the next page')
@allure.severity(allure.severity_level.NORMAL)
def test_click_on_next_page(driver):
    login = LogIn(driver)
    product = ProductPage(driver)

    with allure.step('Logging in with valid credentials'):
        login.log_in('1951111111', '1234', False)

    with allure.step('Clicking on Product Branch'):
        product.click_on_product_branch()
        time.sleep(4)
    with allure.step('Moving to the next page'):
        product.click_next_page()

    # Verify that the user moved to the next page
    expected_text = 'rf'
    assert expected_text in driver.page_source, f"Expected text '{expected_text}' not found on the page"


@allure.epic('Product Page')
@allure.id(3)
@allure.title("Editing a product")
@allure.description('Verify if user can edit a product')
@allure.severity(allure.severity_level.NORMAL)
def test_edit_product(driver):
    login = LogIn(driver)
    product = ProductPage(driver)

    with allure.step('Logging in with valid credentials'):
        login.log_in('1951111111', '1234', False)

    with allure.step('Clicking on Product Branch'):
        product.click_on_product_branch()
        time.sleep(5)
    with allure.step('Selecting a product'):
        product.click_on_bibi83()
        time.sleep(2)
    with allure.step('Editing the details'):
        product.edit_buy_price()
        time.sleep(2)
    with allure.step('clicking the next button'):
        product.click_next_edit_btn()
        time.sleep(2)

    with allure.step('clicking the next button'):
        product.click_next_edit_btn2()
        time.sleep(2)

    with allure.step('clicking the next button'):
        product.click_next_edit_btn3()
        time.sleep(2)

    with allure.step('clicking the next button'):
        product.click_next_edit_btn4()
        time.sleep(2)

    with allure.step('clicking the next button'):
        product.click_next_edit_btn5()
        time.sleep(2)

    with allure.step('Verifying that the buy price has been changed'):
        buy_price_text = product.get_buy_price_text()
        assert buy_price_text == "123123321123123123", f"Expected buy price: '123123321123123123', but got:" \
                                                       f" '{buy_price_text}'"


@allure.epic('Product Page')
@allure.id(4)
@allure.title("Filtering the products")
@allure.description('Verify if user can filter the products')
@allure.severity(allure.severity_level.NORMAL)
def test_product_filtering(driver):
    login = LogIn(driver)
    product = ProductPage(driver)

    with allure.step('Logging in with valid credentials'):
        login.log_in('1951111111', '1234', False)

    with allure.step('Clicking on Product Branch'):
        product.click_on_product_branch()
        time.sleep(5)

    with allure.step('Filtering the products'):
        product.filtering_price()

    with allure.step('Verifying that the products are filtered by price'):
        with allure.step('Filtering the products'):
            product.filtering_price()

        with allure.step('Verifying that the products are filtered by price'):
            filtered_products_prices = product.get_products_prices()
            sorted_prices = sorted(filtered_products_prices)
            assert filtered_products_prices == sorted_prices, f"Filtered products prices are not in ascending order. " \
                                                              f"Actual prices: {filtered_products_prices}"


@allure.epic('Product Page')
@allure.id(5)
@allure.title("Sorting the products")
@allure.description('Verify if user can Sort the products')
@allure.severity(allure.severity_level.NORMAL)
def test_product_filtering(driver):
    login = LogIn(driver)
    product = ProductPage(driver)

    with allure.step('Logging in with valid credentials'):
        login.log_in('1951111111', '1234', False)

    with allure.step('Clicking on Product Branch'):
        product.click_on_product_branch()
        time.sleep(5)

    with allure.step('Sorting the products'):
        product.filtering_name()

    with allure.step('Verifying that the products are sorted by price'):
        sorted_products_names = product.get_product_list()
        sorted_prices = sorted(sorted_products_names)
        assert sorted_products_names == sorted_prices, f"Sorted products prices are not sorted by the right name order. " \
                                                       f"names: {sorted_products_names}"


@allure.epic('Product Page')
@allure.id(6)
@allure.title("Searching through the search bar")
@allure.description('Verify if user can Sort the products')
@allure.severity(allure.severity_level.NORMAL)
def test_product_filtering(driver):
    login = LogIn(driver)
    product = ProductPage(driver)

    with allure.step('Logging in with valid credentials'):
        login.log_in('1951111111', '1234', False)

    with allure.step('Clicking on Product Branch'):
        product.click_on_product_branch()
        time.sleep(5)

    with allure.step('Searching for an item using the search bar'):
        searched_product_name = "bibi83"
        product.search_field()
        assert searched_product_name in driver.page_source, f"{searched_product_name} not found on the page"


@allure.epic('Product Page')
@allure.id(7)
@allure.title("Adding a product")
@allure.description('Verify if user can add a product')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product(driver):
    login = LogIn(driver)
    product = ProductPage(driver)

    with allure.step('Logging in with valid credentials'):
        login.log_in('1951111111', '1234', False)

    with allure.step('Clicking on Product Branch'):
        product.click_on_product_branch()
        time.sleep(5)

    with allure.step('Clicking on the 3 dots btn and add product'):
        product.click_on_dots_icon()
        product.add_product()

    with allure.step('Inserting the product barcode'):
        product.add_product_barcode()

    with allure.step('Inserting the product price'):
        product.add_product_price()

    with allure.step('Inserting the product buy price'):
        product.add_product_buy_price()

    with allure.step('Clicking on the next button'):
        product.click_next_edit_btn()

    with allure.step('Choosing the supreme category'):
        product.add_product_click_supreme_category_btn()
        product.add_product_supreme_category_beers()

    with allure.step('Choosing the store'):
        product.add_product_store_btn()
        product.add_product_telephones_store_btn()
        product.click_next_edit_btn2()
        product.click_next_edit_btn3()
        product.click_next_edit_btn4()
        product.click_next_edit_btn5()
