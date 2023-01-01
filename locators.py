from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # теперь каждый селектор — это пара: как искать и что искать.#registration_link 


class LoginPageLocators():
    #URL_LOGIN = (By.CSS_SELECTOR, )

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BEGINING_LINK = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > ul > li:nth-child(1) > a")
    # BACK_LINK = (By.CSS_SELECTOR, "#basket_formset > div:nth-child(7) > div > div.col-sm-4 > h3 > a")

    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-4 > h3 > a")
#basket_formset > div > div > div.col-sm-4 > h3 > a
    PRICE_PRODUCT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRICE_PRODUCT_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-1 > p")


    #browse > li > ul > li.dropdown-submenu > a