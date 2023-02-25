from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from skipGUI import passwordDict

def main():
    driver = webdriver.Chrome()
    driver.get('https://github.com/login')
    username = driver.find_element(By.ID, 'login_field')

    username.send_keys("devdog805@gmail.com")
    password = driver.find_element(By.ID, 'password')
    password.send_keys("Akj645462016$")
    login = driver.find_element(By.NAME, 'commit').click()

    # Additional code to perform actions on GitHub
    # ...

    input("Press Enter to close the browser...")
    driver.close()

main()
