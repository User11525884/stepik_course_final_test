from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button_add_to_basket()
        self.add_to_product_basket()
        # self.go_to_begining_page()
        self.coincidence_of_names()
        self.go_to_back_page() # возвращаемся на back страницу 
        self.prices_are_equal()
        self.go_to_back_page() # возвращаемся на back страницу 

    #     self.should_be_register_form()
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket is not presented"    	
    
    def add_to_product_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)  
        button.click()
        self.solve_quiz_and_get_code()

    def coincidence_of_names(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_GO_TO_BASKET)
        button_basket.click()
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BASKET).text == name_product, f"In basket not product with name - {name_product}"
        
    def prices_are_equal(self):
        price_product = float(self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text.split("&")[0][1:])
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_GO_TO_BASKET)
        button_basket.click()
        assert float(self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_BASKET).text.split("&")[0][1:]) == price_product, f"In basket other price {str(price_product)}"

    def go_to_begining_page(self):
        button = self.browser.find_element(*ProductPageLocators.BEGINING_LINK)  
        button.click()

    def go_to_back_page(self):
        self.browser.back()
