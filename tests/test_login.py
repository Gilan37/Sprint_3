from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_from_account_button(driver, register_user):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site")

    # Ищем кнопку «Войти в аккаунт» и нажимаем на нее
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]").click()

    # Заполняем поля Email и Пароль
    driver.find_element(By.XPATH, ".//fieldset[1]/div[1]/div[1]/input[1]").send_keys(register_user[1])
    driver.find_element(By.XPATH, ".//fieldset[2]/div[1]/div[1]/input[1]").send_keys(register_user[2])

    # Ищем кнопку «Войти» и нажимаем на нее
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    # Проверяем, что на странице отобразилась кнопка «Оформить заказ»
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains("
                                                                                                "text(),"
                                                                                                "'Оформить заказ')]")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_login_from_personal_area_button(driver, register_user):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site")

    # Ищем кнопку «Личный Кабинет» и нажимаем на нее
    driver.find_element(By.XPATH, ".//p[contains(text(),'Личный Кабинет')]").click()

    # Заполняем поля Email и Пароль
    driver.find_element(By.XPATH, ".//fieldset[1]/div[1]/div[1]/input[1]").send_keys(register_user[1])
    driver.find_element(By.XPATH, ".//fieldset[2]/div[1]/div[1]/input[1]").send_keys(register_user[2])

    # Ищем кнопку «Войти» и нажимаем на нее
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    # Проверяем, что на странице отобразилась кнопка «Оформить заказ»
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains("
                                                                                                "text(),"
                                                                                                "'Оформить заказ')]")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_login_from_register_form(driver, register_user):
    # Открываем страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ищем кнопку «Войти» и нажимаем на нее
    driver.find_element(By.XPATH, ".//a[contains(text(),'Войти')]").click()

    # Заполняем поля Email и Пароль
    driver.find_element(By.XPATH, ".//fieldset[1]/div[1]/div[1]/input[1]").send_keys(register_user[1])
    driver.find_element(By.XPATH, ".//fieldset[2]/div[1]/div[1]/input[1]").send_keys(register_user[2])

    # Ищем кнопку «Войти» и нажимаем на нее
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    # Проверяем, что на странице отобразилась кнопка «Оформить заказ»
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains("
                                                                                                "text(),"
                                                                                                "'Оформить заказ')]")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_login_from_recovery_form(driver, register_user):
    # Открываем страницу восстановления пароля
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    # Ищем кнопку «Войти» и нажимаем на нее
    driver.find_element(By.XPATH, ".//a[contains(text(),'Войти')]").click()

    # Заполняем поля Email и Пароль
    driver.find_element(By.XPATH, ".//fieldset[1]/div[1]/div[1]/input[1]").send_keys(register_user[1])
    driver.find_element(By.XPATH, ".//fieldset[2]/div[1]/div[1]/input[1]").send_keys(register_user[2])

    # Ищем кнопку «Войти» и нажимаем на нее
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    # Проверяем, что на странице отобразилась кнопка «Оформить заказ»
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains("
                                                                                                "text(),"
                                                                                                "'Оформить заказ')]")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()
