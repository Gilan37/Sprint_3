from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_open_souses(driver):
    # Находим раздел Соусы и нажимаем на него
    driver.find_element(By.XPATH, ".//span[contains(text(),'Соусы')]").click()

    # Проверяем, что видно раздел Соусы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text("
                                                                                                "),'Соусы')]")))

    assert 'Соусы' in driver.find_element(By.XPATH, ".//h2[contains(text(),'Соусы')]").text
    driver.quit()


def test_open_toppings(driver):
    # Находим раздел Начинки и нажимаем на него
    driver.find_element(By.XPATH, ".//span[contains(text(),'Начинки')]").click()

    # Проверяем, что видно Начинки
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text("
                                                                                                "),'Начинки')]")))

    assert 'Начинки' in driver.find_element(By.XPATH, ".//h2[contains(text(),'Начинки')]").text
    driver.quit()


def test_open_buns(driver):
    # Находим раздел Начинки и нажимаем на него
    driver.find_element(By.XPATH, ".//span[contains(text(),'Начинки')]").click()

    # Проверяем, что видно Начинки
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text("
                                                                                                "),'Начинки')]")))

    # Находим раздел Булки и нажимаем на него
    driver.find_element(By.XPATH, ".//span[contains(text(),'Булки')]").click()

    # Проверяем, что видно Булки
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text("
                                                                                                "),'Булки')]")))

    assert 'Булки' in driver.find_element(By.XPATH, ".//h2[contains(text(),'Булки')]").text
    driver.quit()
