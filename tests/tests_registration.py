import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators


class TestRegistration:

    #Проверка успешной регистрации (может падать, пока я не научусь не использовать уже существующие случайные переменные)
    def test_registration_name_email_password_successful_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        test_user_name = f'TestUser{random.randint(100, 999)}'
        test_user_email = f'romanrubtsov_{random.randint(100,999)}@gmail.com'

        WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(
            TestLocators.REGISTRATION_NAME_INPUT)
                                      ).send_keys(test_user_name)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(test_user_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        time.sleep(1)

        assert 'Вход' in driver.page_source

    #Проверка неуспешного входа при слишком коротком пароле (добавлена параметризация для покрытия диапазона от 1 до 5 символов)
    @pytest.mark.parametrize('password', [f'{random.randint(0, 99999)}'])
    def test_registration_name_email_shortpassword_error_message(self, driver, password):
        driver.get('https://stellarburgers.nomoreparties.site/register')

        test_user_name = f'TestUser{random.randint(100, 999)}'
        test_user_email = f'romanrubtsov_{random.randint(100, 999)}@gmail.com'
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.REGISTRATION_NAME_INPUT)
                                        ).send_keys(test_user_name)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(test_user_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        error_message = driver.find_element(*TestLocators.INCORRECT_PASSWORD_PARAGRAPH).text
        assert 'Некорректный пароль' in error_message

