
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081")

    category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#menu a[href*='/catalog/desktops']")
        )
    )

    category_url = category.get_attribute("href")
    assert category_url, "Ссылка на категорию отсутствует"

    driver.get(category_url)

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#content h2")
        )
    )

    assert heading.text == "Desktops", \
        "Открылась неправильная категория"

    assert "/catalog/desktops" in driver.current_url, \
        "Адрес категории не совпадает"

    print("Тест пройден: категория Desktops открыта")

finally:
    driver.quit()
