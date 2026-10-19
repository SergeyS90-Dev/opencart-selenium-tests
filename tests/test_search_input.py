
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081")

    search = driver.find_element(By.NAME, "search")

    search.send_keys("iPhone")

    assert search.get_attribute("value") == "iPhone", \
        "Текст в поле поиска не совпадает"

    print("Тест пройден: текст успешно введён в поиск")

finally:
    driver.quit()
