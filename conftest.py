from Assets.Pages.Backend_utils import pytest
import Assets.Pages.Backend_utils as U


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'C'


@pytest.fixture
def driver(selection):
    url = 'http://qa-admin.trado.co.il'
    if selection == 'F':
        driver = U.Firefox()
    elif selection == 'C':
        driver = U.Chrome()
    elif selection == 'E':
        driver = U.Edge()
    else:
        print('invalid selection ---- selecting default:: Firefox')
        driver = U.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()
