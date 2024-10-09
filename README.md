# Sprint_5
---
# Проект автоматизации тестирования сервиса Stellar Burgers
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — Shift + F10.

---
# Поля ввода
### REGISTRATION_NAME_INPUT = [By.XPATH, '//label[ text()="Имя" ]/parent::div/input'] - Поле ввода Имени
### EMAIL_INPUT = [By.XPATH, '//label[ text()="Email" ]/parent::div/input'] - Поле ввода Email
### PASSWORD_INPUT = [By.XPATH, '//label[ text()="Пароль" ]/parent::div/input'] - Поле ввода Пароля

---

# Кнопки
### REGISTRATION_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"] - кнопка "Регистрация"
### PAGE_LOGIN_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'] - кнопка "Войти" на главной странице
### GOTO_ACCOUNT_BUTTON = [By.XPATH, '//*[@id="root"]/div/header/nav/a'] - кнопка "Личный Кабинет"
### REGISTRATION_N_RECOVERY_GOTO_LOGIN_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/div/p/a'] -кнопка перехода на форме авторизации на формах регистрации и восстановления пароля.
    Раньше тут были 2 разных локатора на кнопки перехода к логину из регистрации и из забытого пароля, но какой-либо разницы в вообще всех известных мне локаторах обнаружено не было.
### LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"] - кнопка "Войти" на форме авторизации
### CONSTRUCTOR_BUTTON = [By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p'] - кнопка "Конструктор"
### BURGERS_LOGO_BUTTON = [By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"] - кнопка-логотип "Stellar Burgers"
### LOGOUT_BUTTON = [By.XPATH, "//button[text()='Выход']"] - кнопка "Выйти" в Личном Кабинете

---

# Селекторы
### BUNS_SELECTOR = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]"] - селектор "Булки"
### SAUCES_SELECTOR = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]"] - селектор "Соусы"
### FILLINGS_SELECTOR = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]"] - селектор "Начинки"
### CONSTRUCTOR_CURRENT_ACTIVE_SELECTOR = [By.CSS_SELECTOR, "div.tab_tab_type_current__2BEPc"] - текущий выбранный селектор в конструкторе бургеров

---

# Параграфы и абзацы
### INCORRECT_PASSWORD_PARAGRAPH = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p'] - параграф с надписью "Некорректный пароль" на форме регистрации
### ASSEMBLE_BURGER_HEADER = [By.CSS_SELECTOR, '#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > h1'] - абзац "Соберите бургер" в конструкторе

---

# Ссылки
### HYPERLINK_PROFILE = [By.CSS_SELECTOR, '#root > div > main > div > nav > ul > li:nth-child(1) > a'] - кнопка-гиперссылка "Профиль"