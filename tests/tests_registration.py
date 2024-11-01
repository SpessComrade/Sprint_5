import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from urls import URLs


class TestRegistration:

    #Проверка успешной регистрации (может падать, пока я не научусь не использовать уже существующие случайные переменные)
    def test_registration_name_email_password_successful_registration(self, driver):
        driver.get(URLs.register_url)

        test_user_name = f'TestUser{random.randint(100, 999)}'
        test_user_email = f'romanrubtsov_{random.randint(100,999)}@gmail.com'

        WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(
            TestLocators.registration_name_input)
                                      ).send_keys(test_user_name)
        driver.find_element(*TestLocators.email_input).send_keys(test_user_email)
        driver.find_element(*TestLocators.password_input).send_keys('q1w2e3r4')

        driver.find_element(*TestLocators.registration_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.login_button)
        )

        assert 'Вход' in driver.page_source

    #Проверка неуспешного входа при слишком коротком пароле (добавлена параметризация для покрытия диапазона от 1 до 5 символов)
    @pytest.mark.parametrize('password', [f'{random.randint(0, 99999)}'])
    def test_registration_name_email_shortpassword_error_message(self, driver, password):
        driver.get(URLs.register_url)

        test_user_name = f'TestUser{random.randint(100, 999)}'
        test_user_email = f'romanrubtsov_{random.randint(100, 999)}@gmail.com'
        (WebDriverWait(driver, 10).until
             (expected_conditions.presence_of_element_located(
            TestLocators.registration_name_input)
                                        ).send_keys(test_user_name))
        driver.find_element(*TestLocators.email_input).send_keys(test_user_email)
        driver.find_element(*TestLocators.password_input).send_keys(password)

        driver.find_element(*TestLocators.registration_button).click()

        error_message = driver.find_element(*TestLocators.incorrect_password_paragraph).text
        assert 'Некорректный пароль' in error_message

