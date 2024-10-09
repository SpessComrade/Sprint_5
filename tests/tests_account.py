import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators


class TestAccount:

    #Переход в профиль по кнопке "Личный кабинет
    def test_goto_account_account_button_login_password_account_page(self, login):
        WebDriverWait(login, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.GOTO_ACCOUNT_BUTTON)).click()

        WebDriverWait(login, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.HYPERLINK_PROFILE))

        assert 'Профиль' in login.page_source

    #Переход из аккаунта в Конструктор по кнопке "Конструктор"
    def test_goto_constructor_constructor_button_login_password_constructor_page(self, login):
        WebDriverWait(login, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.GOTO_ACCOUNT_BUTTON)).click()

        login.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(login, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.ASSEMBLE_BURGER_HEADER))

        assert 'Соберите бургер' in login.page_source


    #Переход из аккаунта в Конструктор по клику на логотип Stellar Burgers
    def test_goto_constructor_logo_login_password_constructor_page(self, login):
        WebDriverWait(login, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.GOTO_ACCOUNT_BUTTON)).click()

        login.find_element(*TestLocators.BURGERS_LOGO_BUTTON).click()

        WebDriverWait(login, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.ASSEMBLE_BURGER_HEADER))

        assert 'Соберите бургер' in login.page_source


    #Выход из аккаунта
    def test_account_logout_main_page(self, login):
        WebDriverWait(login, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.GOTO_ACCOUNT_BUTTON)).click()

        logout_button = WebDriverWait(login, 10).until(
            expected_conditions.element_to_be_clickable(TestLocators.LOGOUT_BUTTON))
        logout_button.click()

        WebDriverWait(login, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_BUTTON))
        assert "Войти" in login.page_source