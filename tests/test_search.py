
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081")

    search = driver.find_element(By.NAME, "search")

    assert search.is_displayed(), "Поле поиска не отображается"

    print("Тест пройден: поле поиска отображается")

finally:
    driver.quit()
