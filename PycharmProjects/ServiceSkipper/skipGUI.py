"""
GUI for the skipper
"""
from tkinter import PhotoImage

import tkinter
import customtkinter
from customtkinter import *
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
                                  size=(30,30))

myCoursesButton = customtkinter.CTkButton(master=gui, image=my_image)
myCoursesButton.pack(pady=12, padx=12)
# runs the application
gui.mainloop()
