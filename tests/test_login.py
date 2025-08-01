import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.ID, "login").click()

    time.sleep(2)
    assert "Dashboard" in driver.title
    driver.quit()
