import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators import TestLocators


class TestConstructor:

    #Переход к разделу "Соусы"
    def test_constructor_sauces_section(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            TestLocators.sauces_selector)) #Проверка наличия селектора "Соусы"
        driver.find_element(*TestLocators.sauces_selector).click()
        active_sauces = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.constructor_current_active_selector)
        )
        assert active_sauces.text == 'Соусы'


    #Переход к разделу "Начинки"
    def test_constructor_fillings_section(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.fillings_selector))

        driver.find_element(*TestLocators.fillings_selector).click()
        active_fillings = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.constructor_current_active_selector)
        )
        assert active_fillings.text == 'Начинки'


    #Переход к разделу "Булки" (тк. раздел "Булки" стоит по умолчанию, сначала осуществляется клик в раздел Соусов)
    def test_constructor_buns_section(self, driver):
        #Предварительный переход в "Соусы". Можно было написать фикстуру, но она использовалась бы в 1-м тесте, поэтому счел нецелесообразным.
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.sauces_selector))
        driver.find_element(*TestLocators.sauces_selector).click()

        #Переход в "Булки"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            TestLocators.buns_selector))
        driver.find_element(*TestLocators.buns_selector).click()

        active_buns = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.constructor_current_active_selector)
        )
        assert active_buns.text == 'Булки'


