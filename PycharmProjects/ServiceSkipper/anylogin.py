from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def main(url, username, password):
    driver = webdriver.Chrome()
    driver.get(url)
    username_element = driver.find_element(By.ID, 'username')
    username_element.send_keys(username)
    password_element = driver.find_element(By.ID, 'password')
    password_element.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    # Additional code to perform actions on the website
    # ...

    input("Press Enter to close the browser...")
    driver.close()

if __name__ == '__main__':
    # Prompt the user for input
    url = input("Enter website URL: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Call the main function with the user input
    main(url, username, password)
