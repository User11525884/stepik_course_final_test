from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link1 = "https://suninjuly.github.io/selects1.html"
    link2 = "https://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link2)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # #начало------------------- первый вариант---------------------------
    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(str(int(num1) + int(num2)))
    # #конец-------------------- второй вариант---------------------------
    # browser.find_element(By.ID, "dropdown").click()  # рабочий вариант

    browser.find_element(By.CSS_SELECTOR, "select.custom-select").click()

    # как вариант>   browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    ss = f"[value='{str(int(num1) + int(num2))}']"
    browser.find_element(By.CSS_SELECTOR, ss).click()
    #конец-------------------- ыторой вариант---------------------------

    # Ваш код, который заполняет обязательные поля
    # x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    # print(x)

    # otv = browser.find_element(By.ID,  "answer")
    # otv.send_keys(calc(x))


    # checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    # checkbox.click()

    # radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    # radio.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()