import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

class PlaceHolder:
    def __init__(self, root):
        image  = Image.open(".\\media\\ff.png")
        bg_image = ctk.CTkImage(image, size = (500, 450))

        label = ctk.CTkLabel(root, image=bg_image, text= "")
        label.place(relx=0.5, rely= 0.5, anchor="center")