from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
    username_element = driver.find_element(By.ID, 'username')
    username_element.send_keys("devdog805@gmail.com")
    password_element = driver.find_element(By.ID, 'password')
    password_element.send_keys("dj101802")
    login_button = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')
    login_button.click()

    # Additional code to perform actions on the website
    # ...

    input("Press Enter to close the browser...")
    driver.close()

main()
