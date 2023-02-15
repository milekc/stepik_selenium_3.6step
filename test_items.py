from conftest import *

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_add_to_basket(browser):
    browser.get(link)
    # time.sleep(30)
    basket = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert basket.text, 'Element not found'
    print(basket.text)
