
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081")

    search = driver.find_element(By.NAME, "search")
    search.send_keys("iPhone")

    search_button = driver.find_element(
        By.CSS_SELECTOR, "#search button"
    )
    search_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("route=product/search")
    )

    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".product-thumb h4 a")
        )
    )

    assert any(product.text.strip() == "iPhone" for product in products), \
        "Товар iPhone не найден в результатах поиска"

    print("Тест пройден: iPhone найден в результатах поиска")

finally:
    driver.quit()
