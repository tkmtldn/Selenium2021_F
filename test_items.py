import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestMain():

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        time.sleep(3)
        add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket')
        assert add_to_basket, 'Please add button!'
