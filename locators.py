from selenium.webdriver.common.by import By



class TestLocators:
    #Поля ввода
    registration_name_input = [By.XPATH, '//label[ text()="Имя" ]/parent::div/input']
    email_input = [By.XPATH, '//label[ text()="Email" ]/parent::div/input']
    password_input = [By.XPATH, '//label[ text()="Пароль" ]/parent::div/input']

    #Кнопки
    registration_button = [By.XPATH, "//button[text()='Зарегистрироваться']"]
    page_login_button = [By.XPATH, '//button[text()="Войти в аккаунт"]']
    goto_account_button = [By.XPATH, "//a[contains(@href, '/account')]"]
    registration_n_recovery_goto_login_button = [By.XPATH, '//a[@class="Auth_link__1fOlj" or @href="/login"]'] #Раньше тут были 2 разных локатора на кнопки перехода к логину из регистрации и из забытого пароля, но какой-либо разницы в вообще всех известных мне локаторах обнаружено не было. XPath сделал с оператором OR просто, чтобы попрактиковаться.
    login_button = [By.XPATH, "//button[text()='Войти']"]
    constructor_button = [By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" or contains(text(), "Конструктор")]'] #А тут практика использования or и contains в одном запросе.
    burgers_logo_button = [By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"]
    logout_button = [By.XPATH, "//button[text()='Выход']"]

    #Селекторы
    buns_selector = [By.XPATH, "//span[text()='Булки']/parent::div"]
    sauces_selector = [By.XPATH, "//span[text()='Соусы']/parent::div"]
    fillings_selector = [By.XPATH, "//span[text()='Начинки']/parent::div"]
    constructor_current_active_selector = [By.CSS_SELECTOR, "div.tab_tab_type_current__2BEPc"]

    #Параграфы и абзацы
    incorrect_password_paragraph = [By.XPATH, '//p[@class="input__error text_type_main-default" or contains(text(), "Некорректный пароль")]']
    assemble_burger_header = [By.CSS_SELECTOR, 'section.BurgerIngredients_ingredients__1N8v2']

    #Кнопки-ссылки
    hyperlink_profile = [By.XPATH, '//a[starts-with(text(),"Профиль")]']