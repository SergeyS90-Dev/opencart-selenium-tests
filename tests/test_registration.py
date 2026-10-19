
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8081/en-gb?route=account/register")

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "h1")
        )
    )

    assert "Register" in heading.text, \
        "Не открылась страница регистрации"

    first_name = driver.find_element(By.ID, "input-firstname")
    last_name = driver.find_element(By.ID, "input-lastname")
    email = driver.find_element(By.ID, "input-email")

    assert first_name.is_displayed(), \
        "Поле имени не отображается"

    assert last_name.is_displayed(), \
        "Поле фамилии не отображается"

    assert email.is_displayed(), \
        "Поле электронной почты не отображается"

    print("Тест пройден: форма регистрации отображается")

finally:
    driver.quit()
