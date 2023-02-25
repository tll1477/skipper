"""
GUI for the skipper
"""

import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# creating the window and setting the size
gui = customtkinter.CTk()
gui.geometry("800x600")

# creates a text label
label = customtkinter.CTkLabel(gui, text="Service Skipper")
label.pack()

my_image = customtkinter.CTkImage(light_image=Image.open("/Users/trislout/PycharmProjects/ServiceSkipper/myCoursesLogo.png"),
                                  dark_image=Image.open("/Users/trislout/PycharmProjects/ServiceSkipper/myCoursesLogo.png"),
                                  size=(30, 30))

# create myCourses button
myCoursesButton = customtkinter.CTkButton(master=gui, image=my_image)
myCoursesButton.pack(pady=12, padx=12)

def myCoursesClick():
    # call the code for opening myCourses credentials page
    myCoursesWindow = customtkinter.CTkToplevel(gui)
    myCoursesWindow.title("MyCourses")
    myCoursesWindow.geometry("600x400")

    myLabel = customtkinter.CTkLabel(myCoursesWindow, text="Enter MyCourses credentials")
    myLabel.pack()
    frame = customtkinter.CTkFrame(myCoursesWindow)
    frame.pack(pady=20, padx=40,
               fill='both', expand=True)

    # Create the text box for taking
    # username input from user
    user_entry = customtkinter.CTkEntry(frame, placeholder_text="Username")
    user_entry.pack(pady=12, padx=10)

    # Create a text box for taking
    # password input from user
    user_pass = customtkinter.CTkEntry(frame, placeholder_text="Password", show="*")
    user_pass.pack(pady=12, padx=10)

    # Create a login button to login
    button = customtkinter.CTkButton(frame, text='Save')
    button.pack(pady=12, padx=10)


myCoursesButton.configure(command=myCoursesClick)

# runs the application
gui.mainloop()
