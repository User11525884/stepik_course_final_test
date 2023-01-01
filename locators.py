from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # теперь каждый селектор — это пара: как искать и что искать.#registration_link 


class LoginPageLocators():
    #URL_LOGIN = (By.CSS_SELECTOR, )

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")