
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081")

    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "MacBook")
        )
    )

    product.click()

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "h1")
        )
    )

    assert heading.text == "MacBook", \
        "Название товара не совпадает"

    assert "/product/macbook" in driver.current_url, \
        "Открылась неправильная страница"

    print("Тест пройден: карточка MacBook открыта")

finally:
    driver.quit()
