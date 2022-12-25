from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link1 = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME,  "lastname")
    last_name.send_keys("Ivanov")
    email = browser.find_element(By.NAME,  "email")
    email.send_keys("Ivanov@ivan.ru")

    file = browser.find_element(By.ID, "file")

    # browser.execute_script("return arguments[0].scrollIntoView(true);", file)
    # file.click()

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()