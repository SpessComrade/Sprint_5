import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from urls import URLs


class TestLogin:
    #Вход через кнопку "Войти"
    def test_login_main_page_button_email_password_successful_login(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.page_login_button)).click()

        driver.find_element(*TestLocators.email_input).send_keys('romanrubtsov_14@gmail.com')
        driver.find_element(*TestLocators.password_input).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.login_button).click()

        assert 'Личный Кабинет' in driver.page_source

    #Вход через личный кабинет
    def test_login_account_button_email_password_successful_login(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.goto_account_button)).click()

        driver.find_element(*TestLocators.email_input).send_keys(
            'romanrubtsov_14@gmail.com')
        driver.find_element(*TestLocators.password_input).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.login_button).click()

        assert 'Личный Кабинет' in driver.page_source

    # Вход по кнопке на форме регистрации
    def test_login_account_registration_button_email_password_successful_login(self, driver):
        driver.get(URLs.register_url)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.registration_n_recovery_goto_login_button)).click()

        driver.find_element(*TestLocators.email_input).send_keys(
            'romanrubtsov_14@gmail.com')
        driver.find_element(*TestLocators.password_input).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.login_button).click()

        assert 'Личный Кабинет' in driver.page_source

    # Вход через кнопку в форме восстановления пароля.
    def test_login_password_recovery_button_email_password_successful_login(self, driver):
        driver.get(URLs.forgot_password_url)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.registration_n_recovery_goto_login_button)).click()

        driver.find_element(*TestLocators.email_input).send_keys(
            'romanrubtsov_14@gmail.com')
        driver.find_element(*TestLocators.password_input).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.login_button).click()

        assert 'Личный Кабинет' in driver.page_source
