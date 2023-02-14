from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_success(driver, register_user):
    # Ожидаем страницу для авторизации
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('/login'))

    # Проверяем, что текущий url равен 'https://stellarburgers.nomoreparties.site/login'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()


def test_password_error(driver, create_wrong_password):
    # Открываем страницу с формой регистрации
    driver.get('https://stellarburgers.nomoreparties.site/register')

    # Вводим Пароль меньше 6 символов
    driver.find_element(By.NAME, "Пароль").send_keys(create_wrong_password)

    # Нажимаем кнопку «Зарегистрироваться»
    driver.find_element(By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]").click()

    # Проверяем, что класс input__error есть на странице и его видно
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__error")))

    # Проверяем текст ошибки для некорректного пароля
    assert driver.find_element(By.XPATH, ".//p[contains(@class, 'input__error')]").text == 'Некорректный пароль'
    driver.quit()
