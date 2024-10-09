import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, '//label[ text()="Email" ]/parent::div/input').send_keys('romanrubtsov_14@gmail.com')
    driver.find_element(By.XPATH, '//label[ text()="Пароль" ]/parent::div/input').send_keys('q1w2e3r4')

    driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > button").click()
    yield driver