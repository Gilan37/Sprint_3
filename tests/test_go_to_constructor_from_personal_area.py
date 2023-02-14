from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_constructor_button_from_personal_area(driver, register_user):
    # Ищем кнопку «Личный Кабинет» и нажимаем на нее
    driver.find_element(By.XPATH, ".//p[contains(text(),'Личный Кабинет')]").click()

    # Заполняем поля Email и Пароль
    driver.find_element(By.XPATH, ".//fieldset[1]/div[1]/div[1]/input[1]").send_keys(register_user[1])
    driver.find_element(By.XPATH, ".//fieldset[2]/div[1]/div[1]/input[1]").send_keys(register_user[2])

    # Ищем кнопку «Войти» и нажимаем на нее
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    # Проверяем, что на странице отобразилась кнопка «Оформить заказ»
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains("
                                                                                                "text(),"
                                                                                                "'Оформить заказ')]")))

    # Ищем кнопку «Личный Кабинет» и нажимаем на нее
    driver.find_element(By.XPATH, ".//p[contains(text(),'Личный Кабинет')]").click()

    # Проверяем, что на странице отобразилась форма Личного кабинета
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[contains("
                                                                                                "@class, "
                                                                                                "'Account_account__vgk_w')]")))

    # Нажимаем на кнопку «Конструктор»
    driver.find_element(By.XPATH, ".//p[contains(text(),'Конструктор')]").click()

    assert 'Соберите бургер' in driver.find_element(By.XPATH, ".//h1[contains(text(),'Соберите бургер')]").text
    driver.quit()


def test_go_to_constructor_logo_from_personal_area(driver, register_user):
    # Ищем кнопку «Личный Кабинет» и нажимаем на нее
    driver.find_element(By.XPATH, ".//p[contains(text(),'Личный Кабинет')]").click()

    # Заполняем поля Email и Пароль
    driver.find_element(By.XPATH, ".//fieldset[1]/div[1]/div[1]/input[1]").send_keys(register_user[1])
    driver.find_element(By.XPATH, ".//fieldset[2]/div[1]/div[1]/input[1]").send_keys(register_user[2])

    # Ищем кнопку «Войти» и нажимаем на нее
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()

    # Проверяем, что на странице отобразилась кнопка «Оформить заказ»
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains("
                                                                                                "text(),"
                                                                                                "'Оформить заказ')]")))

    # Ищем кнопку «Личный Кабинет» и нажимаем на нее
    driver.find_element(By.XPATH, ".//p[contains(text(),'Личный Кабинет')]").click()

    # Проверяем, что на странице отобразилась форма Личного кабинета
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[contains("
                                                                                                "@class, "
                                                                                                "'Account_account__vgk_w')]")))

    # Нажимаем на лого «Stellar Burgers»
    driver.find_element(By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2").click()

    assert 'Соберите бургер' in driver.find_element(By.XPATH, ".//h1[contains(text(),'Соберите бургер')]").text
    driver.quit()
