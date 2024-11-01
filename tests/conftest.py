import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import TestLocators
from urls import URLs

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(URLs.main_page_url)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    driver.get(URLs.login_url)

    driver.find_element(*TestLocators.email_input).send_keys('romanrubtsov_14@gmail.com')
    driver.find_element(*TestLocators.password_input).send_keys('q1w2e3r4')

    driver.find_element(*TestLocators.login_button).click()
    yield driver