import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators import TestLocators


class TestConstructor:

    #Переход к разделу "Соусы"
    def test_constructor_sauces_section(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.SAUCES_SELECTOR)) #Проверка наличия селектора "Соусы"
        driver.find_element(*TestLocators.SAUCES_SELECTOR).click()
        active_sauces = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.CONSTRUCTOR_CURRENT_ACTIVE_SELECTOR)
        )
        assert active_sauces.text == 'Соусы'


    #Переход к разделу "Начинки"
    def test_constructor_fillings_section(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.FILLINGS_SELECTOR))

        driver.find_element(*TestLocators.FILLINGS_SELECTOR).click()
        active_fillings = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.CONSTRUCTOR_CURRENT_ACTIVE_SELECTOR)
        )
        assert active_fillings.text == 'Начинки'


    #Переход к разделу "Булки" (тк. раздел "Булки" стоит по умолчанию, сначала осуществляется клик в раздел Соусов)
    def test_constructor_buns_section(self, driver):
        #Предварительный переход в "Соусы". Можно было написать фикстуру, но она использовалась бы в 1-м тесте, поэтому счел нецелесообразным.
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.SAUCES_SELECTOR))
        driver.find_element(*TestLocators.SAUCES_SELECTOR).click()

        #Переход в "Булки"
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            TestLocators.BUNS_SELECTOR))
        driver.find_element(*TestLocators.BUNS_SELECTOR).click()

        active_buns = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.CONSTRUCTOR_CURRENT_ACTIVE_SELECTOR)
        )
        assert active_buns.text == 'Булки'


