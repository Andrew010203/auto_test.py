import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "https://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    import math

    # ждем, пока цена дома не уменьшится до 100
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "$100")
    )

    # нажимаем на кнопку "Book"
    button = browser.find_element(By.XPATH, '//*[@id="book"]')
    button.click()


    # Считать значение для переменной x
    x_element: WebElement = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = int(x_element.text)

    # Посчитать математическую функцию от x
    result = str(math.log(abs(12 * math.sin(x))))

  # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(result)

    # находим кнопку "Submit" и нажимаем на неё
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()