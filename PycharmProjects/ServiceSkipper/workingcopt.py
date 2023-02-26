import tkinter
from tkinter import LEFT

import customtkinter
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


from PIL import Image, ImageTk

passwordDict = {"Mycourses": (),"Github":(),"Link":()}
BACKGROUND_PATH= "background2.png"
class SkipperGUI:
    def __init__(self):

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        # creating the window and setting the size
        self.gui = customtkinter.CTk()
        self.gui.geometry("800x600")
        bg_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH))

        # Create a Label widget with the background image and place it at (0, 0)
        bg_label = customtkinter.CTkLabel(self.gui, image=bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.label = customtkinter.CTkLabel(self.gui, text="Service Skipper")
        self.label.pack()

        self.create_button('myCoursesLogo.png', self.my_courses_click, 150, 100)
        self.create_button('github-logo-300x300.png', self.git_click, 525, 100)
        self.create_button('linkedin.png', self.link_click, 150, 300)

    def my_courses_click(self):
        self.create_credentials_window("MyCourses", self.MyCourserunLogin)

    def git_click(self):
        self.create_credentials_window("GitHub", self.git_login)

    def link_click(self):
        self.create_credentials_window("LinkedIn", self.link_login)

    def create_button(self, image_path, command, x, y):
        # Create an image for button
        image = customtkinter.CTkImage(light_image=Image.open(image_path),
                                       dark_image=Image.open(image_path),
                                       size=(100, 100))

        # Create a button
        button = customtkinter.CTkButton(master=self.gui, image=image, text="", width=0, height=0,
                                         hover_color="white",
                                         fg_color="white",
                                         border_width=5,
                                         border_color="white",
                                         corner_radius=10)
        button.place(x=x, y=y)
        button.configure(command=self.my_courses_click)

    def create_credentials_window(self, title, command):
        window = customtkinter.CTkToplevel(self.gui)
        window.title(title)
        window.geometry("600x400")

        label = customtkinter.CTkLabel(window, text=f"Enter {title} credentials")
        label.pack()
        frame = customtkinter.CTkFrame(window)
        frame.pack(pady=20, padx=40, fill='both', expand=True)

        # Create the text box for taking username input from user
        user_entry = customtkinter.CTkEntry(frame, placeholder_text="Username")
        user_entry.pack(pady=12, padx=10)

        # Create a text box for taking password input from user
        user_pass = customtkinter.CTkEntry(frame, placeholder_text="Password", show="*")
        user_pass.pack(pady=12, padx=10)

        # Create a login button to login
        save_button = customtkinter.CTkButton(frame, text='Save', command=self.save_credentials(title))
        save_button.pack(pady=12, padx=10)

        run_button = customtkinter.CTkButton(frame, text='Run', command=command)
        run_button.pack(pady=12, padx=10)

    def save_credentials(self, title):
        username = self.user_entry.get()
        password = self.user_pass.get()
        passwordDict[title] = (username, password)
        print(passwordDict)

    """""
    def saveMycoures(self):
        username = self.user_entry.get()
        password = self.user_pass.get()
        passwordDict["Mycourses"] = (username,password)
        print(passwordDict)

    def saveGit(self):
        username = self.user_entry.get()
        password = self.user_pass.get()
        passwordDict["Github"] = (username,password)
        print(passwordDict)

    def saveLink(self):
        username = self.user_entry.get()
        password = self.user_pass.get()
        passwordDict["Link"] = (username,password)
        print(passwordDict)
        """""


    def MyCourserunLogin(self):
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


    def gitrunLogin(self):
        driver = webdriver.Chrome()
        driver.get('https://github.com/login')
        username = driver.find_element(By.ID, 'login_field')
        user_passTuple = passwordDict["Github"]
        username.send_keys(user_passTuple[0])
        password = driver.find_element(By.ID, 'password')
        password.send_keys(user_passTuple[1])
        login = driver.find_element(By.NAME, 'commit').click()

        # Additional code to perform actions on GitHub
        # ...

        input("Press Enter to close the browser...")
        driver.close()


    def LinkrunLogin(self):
        driver = webdriver.Chrome()
        driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
        username_element = driver.find_element(By.ID, 'username')
        user_passTuple = passwordDict["Link"]
        username_element.send_keys(user_passTuple[0])
        password = driver.find_element(By.ID, 'password')
        password.send_keys(user_passTuple[1])
        login_button = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')
        login_button.click()

        # Additional code to perform actions on the website
        # ...

        input("Press Enter to close the browser...")
        driver.close()


    def run(self):
        # runs the application
        self.gui.mainloop()


if __name__ == "__main__":
    skipper_gui = SkipperGUI()
    skipper_gui.run()
