from selenium.webdriver.common.by import By



class TestLocators:
    #Поля ввода
    REGISTRATION_NAME_INPUT = [By.XPATH, '//label[ text()="Имя" ]/parent::div/input']
    EMAIL_INPUT = [By.XPATH, '//label[ text()="Email" ]/parent::div/input']
    PASSWORD_INPUT = [By.XPATH, '//label[ text()="Пароль" ]/parent::div/input']

    #Кнопки
    REGISTRATION_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"]
    PAGE_LOGIN_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button']
    GOTO_ACCOUNT_BUTTON = [By.XPATH, '//*[@id="root"]/div/header/nav/a']
    REGISTRATION_N_RECOVERY_GOTO_LOGIN_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/div/p/a'] #Раньше тут были 2 разных локатора на кнопки перехода к логину из регистрации и из забытого пароля, но какой-либо разницы в вообще всех известных мне локаторах обнаружено не было.
    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"]
    CONSTRUCTOR_BUTTON = [By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p']
    BURGERS_LOGO_BUTTON = [By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"]
    LOGOUT_BUTTON = [By.XPATH, "//button[text()='Выход']"]

    #Селекторы
    BUNS_SELECTOR = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]"]
    SAUCES_SELECTOR = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]"]
    FILLINGS_SELECTOR = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]"]
    CONSTRUCTOR_CURRENT_ACTIVE_SELECTOR = [By.CSS_SELECTOR, "div.tab_tab_type_current__2BEPc"]

    #Параграфы и абзацы
    INCORRECT_PASSWORD_PARAGRAPH = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p']
    ASSEMBLE_BURGER_HEADER = [By.CSS_SELECTOR, '#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > h1']

    #Ссылки
    HYPERLINK_PROFILE = [By.CSS_SELECTOR, '#root > div > main > div > nav > ul > li:nth-child(1) > a']