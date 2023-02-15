import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site')
    return driver


@pytest.fixture
def create_login():
    login = 'Gilan'
    return login


@pytest.fixture
def create_email():
    name = 'gilansuleimenov'
    kogorta = '6'
    email = name + kogorta + str(random.randint(100, 999)) + '@yandex.ru'
    return email


@pytest.fixture
def create_password():
    password = random.randint(100000, 999999)
    return password


@pytest.fixture
def create_wrong_password():
    wrong_password = random.randint(10000, 99999)
    return wrong_password


@pytest.fixture
def register_user(driver, create_login, create_email, create_password):
    email = create_email
    password = create_password
    driver.get('https://stellarburgers.nomoreparties.site/register')
    # Вводим Имя, Email и Пароль
    driver.find_element(By.XPATH, ".//fieldset[1]/div[1]/div[1]/input[1]").send_keys(create_login)
    driver.find_element(By.XPATH, ".//fieldset[2]/div[1]/div[1]/input[1]").send_keys(create_email)
    driver.find_element(By.XPATH, ".//fieldset[3]/div[1]/div[1]/input[1]").send_keys(create_password)

    # Нажимаем кнопку Зарегистрироваться
    driver.find_element(By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]").click()
    return register_user, email, password
