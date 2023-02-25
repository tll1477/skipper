from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from skipGUI import passwordDict

def main():
    driver = webdriver.Chrome()
    driver.get('https://mycourses.rit.edu/')
    signIn = driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[1]/d2l-html-block/div/div/table/tbody/tr[1]/td[1]/a').click()
    username = driver.find_element(By.XPATH, '/html/body/div/div/form/div/input[1]')
    user_passTuple = passwordDict["Mycourses"]
    username.send_keys(user_passTuple[0])
    password = driver.find_element(By.XPATH, '/html/body/div/div/form/div/input[2]')
    password.send_keys(user_passTuple[1])
    # time.sleep(10)
    login = driver.find_element(By.XPATH, '/html/body/div/div/form/div/span/button').click()
    time.sleep(10)

    notrust = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/div[4]/button').click()
    time.sleep(15)

    input("Press Enter to close the browser...")
    driver.close()
