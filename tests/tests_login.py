import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators


class TestLogin:
    #Вход через кнопку "Войти"
    def test_login_main_page_button_email_password_successful_login(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.PAGE_LOGIN_BUTTON)).click()

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys('romanrubtsov_14@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        assert 'Личный Кабинет' in driver.page_source

    #Вход через личный кабинет
    def test_login_account_button_email_password_successful_login(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.GOTO_ACCOUNT_BUTTON)).click()

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(
            'romanrubtsov_14@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        assert 'Личный Кабинет' in driver.page_source

    # Вход по кнопке на форме регистрации
    def test_login_account_registration_button_email_password_successful_login(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.REGISTRATION_N_RECOVERY_GOTO_LOGIN_BUTTON)).click()

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(
            'romanrubtsov_14@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        assert 'Личный Кабинет' in driver.page_source

    # Вход через кнопку в форме восстановления пароля.
    def test_login_password_recovery_button_email_password_successful_login(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.REGISTRATION_N_RECOVERY_GOTO_LOGIN_BUTTON)).click()

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(
            'romanrubtsov_14@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        assert 'Личный Кабинет' in driver.page_source
