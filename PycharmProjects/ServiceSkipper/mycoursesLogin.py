from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from PIL import Image, ImageTk
import customtkinter
import time

from selenium.webdriver.support.wait import WebDriverWait

BACKGROUND_PATH = "background2.png"
passwordDict = {}

MY_COURSES_LOGO_PATH = "myCoursesLogo.png"
GITHUB_LOGO_PATH = "github-logo-300x300.png"
LINKEDIN_LOGO_PATH = "linkedin.png"

MY_COURSES = "MyCourses"
GITHUB = "Github"
LINKEDIN = "Link"

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

        self.create_button(self.gui, MY_COURSES, MY_COURSES_LOGO_PATH, (150, 100), MY_COURSES)
        self.create_button(self.gui, GITHUB, GITHUB_LOGO_PATH, (525, 100), GITHUB)
        self.create_button(self.gui, LINKEDIN, LINKEDIN_LOGO_PATH, (150, 300), LINKEDIN)
    def create_button(self, master, name, image_path, position, service_name):
        image = customtkinter.CTkImage(
            light_image=Image.open(image_path),
            dark_image=Image.open(image_path),
            size=(100, 100),
        )

        button = customtkinter.CTkButton(
            master=master,
            image=image,
            text="",
            width=0,
            height=0,
            hover_color="white",
            fg_color="white",
            border_width=5,
            border_color="white",
            corner_radius=10,
            command=lambda: self.open_credentials_window(service_name)
        )
        button.place(x=position[0], y=position[1])
        setattr(self, f"{name.lower()}Button", button)


    def open_credentials_window(self, service_name):
        window = customtkinter.CTkToplevel(self.gui)
        window.title(service_name)
        window.geometry("600x400")

        label_text = f"Enter {service_name} credentials"
        label = customtkinter.CTkLabel(window, text=label_text)
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
        save_button = customtkinter.CTkButton(frame, text='Save',
                                              command=lambda: self.save_credentials(service_name, user_entry.get(),
                                                                                    user_pass.get()))
        save_button.pack(pady=12, padx=10)

        run_button = customtkinter.CTkButton(frame, text='Run', command=lambda: self.run_login(service_name))
        run_button.pack(pady=12, padx=10)

    def save_credentials(self, service_name, username, password):
        passwordDict[service_name] = (username, password)
        print(passwordDict)

    def run_login(self, service_name):
        if service_name == "MyCourses":
            driver = webdriver.Chrome()
            driver.get('https://mycourses.rit.edu/')
            signIn = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div[1]/d2l-html-block/div/div/table/tbody/tr[1]/td[1]/a').click()
            username = driver.find_element(By.XPATH, '/html/body/div/div/form/div/input[1]').send_keys(passwordDict[service_name][0])

            password = driver.find_element(By.XPATH, '/html/body/div/div/form/div/input[2]').send_keys(passwordDict[service_name][1])

            # time.sleep(10)
            login = driver.find_element(By.XPATH, '/html/body/div/div/form/div/span/button').click()
            time.sleep(10)

            notrust = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/div[4]/button').click()
            time.sleep(15)



        elif service_name == "Github":
            driver = webdriver.Chrome()
            driver.get('https://github.com/login')
            driver.find_element(By.ID, 'login_field').send_keys(passwordDict[service_name][0])
            driver.find_element(By.ID, 'password').send_keys(passwordDict[service_name][1])
            driver.find_element(By.NAME, 'commit').click()

        elif service_name == "Link":
            driver = webdriver.Chrome()
            driver.get('https://www.linkedin.com/login')
            driver.find_element(By.ID, 'username').send_keys(passwordDict[service_name][0])
            driver.find_element(By.ID, 'password').send_keys(passwordDict[service_name][1])
            driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        try:
            # Wait for the browser to close
            WebDriverWait(driver, 3600).until(EC.number_of_windows_to_be(0))
        finally:
            driver.quit()

    def run(self):
        # runs the application
        self.gui.mainloop()


if __name__ == "__main__":
    skipper_gui = SkipperGUI()
    skipper_gui.run()
