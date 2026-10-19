
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081/en-gb/product/macbook")

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "button-cart")
        )
    )

    add_button.click()

    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href*='checkout/cart']")
        )
    )

    cart_link.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout/cart")
    )

    assert "MacBook" in driver.page_source, \
        "Товар MacBook отсутствует в корзине"

    print("Тест пройден: MacBook добавлен в корзину")

finally:
    driver.quit()
