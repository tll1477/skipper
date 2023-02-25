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
#backgroundImg = customtkinter.CTkImage(Image.open("background.png"),size=(800,600))
#backgroundLabel = customtkinter.CTkLabel(master=gui, image=backgroundImg,text="")
#backgroundLabel.pack()
# creates a text label
label = customtkinter.CTkLabel(gui, text="Service Skipper")
label.pack()

my_image = customtkinter.CTkImage(light_image=Image.open("myCoursesLogo.png"),
                                  dark_image=Image.open("myCoursesLogo.png"),
                                  size=(100, 100))

myCoursesButton = customtkinter.CTkButton(master=gui, image=my_image, text="", width=0, height=0,
                                          hover_color="white",
                                          fg_color="white",
                                          border_width=5,
                                          border_color="white",
                                          corner_radius=10)
#myCoursesButton.tkraise(backgroundLabel)
myCoursesButton.pack(pady=600 / 3, padx=800 / 3)

# runs the application
gui.mainloop()
