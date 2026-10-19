
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://localhost:8081/en-gb/product/macbook")

    add_button = wait.until(
        EC.element_to_be_clickable((By.ID, "button-cart"))
    )
    add_button.click()

    cart_link = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href*='checkout/cart']")
        )
    )
    cart_link.click()

    wait.until(
        EC.url_contains("checkout/cart")
    )

    assert "MacBook" in driver.page_source, \
        "Товар не добавлен в корзину"

    remove_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[formaction*='remove']")
        )
    )
    remove_button.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "content"),
            "Your shopping cart is empty!"
        )
    )

    print("Тест пройден: товар успешно удалён из корзины")

finally:
    driver.quit()
