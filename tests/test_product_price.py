
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081/en-gb/product/macbook")

    price = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#content .list-unstyled h2")
        )
    )

    assert price.text.strip() != "", \
        "Цена товара отсутствует"

    print("Тест пройден: цена MacBook отображается")
    print("Цена товара:", price.text)

finally:
    driver.quit()
