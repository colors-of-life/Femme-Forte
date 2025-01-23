from .get_sys_txt_color import get_sys_txt_color
import customtkinter  as ctk

def update_text_color(window, root):
        """ Update the text color dynamically every 500ms. """
        new_text_color = get_sys_txt_color()
        if window.text_color != new_text_color:
            window.text_color = new_text_color
            try:
                window.close_button.configure(text_color=window.text_color)
            except Exception:
                 for child in root.winfo_children():
                    if isinstance(child, ctk.CTkLabel):
                        child.configure(text_color = window.text_color)
                    if isinstance(child, ctk.CTkEntry):
                        child.configure(placeholder_text_color= window.text_color)   
        root.after(500, lambda: update_text_color(window= window, root=root))