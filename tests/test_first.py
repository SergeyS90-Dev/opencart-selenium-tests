
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081")

    assert driver.title == "Your Store", "Заголовок страницы не совпадает"

    print("Тест пройден: заголовок страницы правильный")

finally:
    driver.quit()
