"""
GUI for the skipper
"""
import customtkinter
from customtkinter import *
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# creating the window and setting the size
gui = CTk()
gui.geometry("800x600")

# creates a text label
label = customtkinter.CTkLabel(gui, text="Service Skipper")
label.pack()

# runs the application
gui.mainloop()
