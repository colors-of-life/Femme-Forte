import customtkinter as ctk
def get_sys_txt_color():
    
    #Returns system text color based on appearance mode.
    if ctk.get_appearance_mode() == "Dark":
        return "#F0EAD6"
    else:
        return "black"