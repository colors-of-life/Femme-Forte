import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image  # Importing PIL for image handling
from screeninfo import get_monitors  # To get the screen dimensions
import utils
from login_auth_client import LoginAuthClient
from typing import Literal


class LogIn(ctk.CTkToplevel):  # Use Toplevel for a floating window
    def __init__(self):
        super().__init__()
        # Remove window decorations (title bar, borders, etc.)
        self.overrideredirect(True)  # Remove window decorations (no title bar, no borders)

        # Ensure the window stays on top
        self.attributes("-topmost", True)

        # Make the login window modal
        self.grab_set() 

        # Set the size of the window to a smaller dialog box size
        self.geometry("400x500")  # Smaller size for the dialog box

        # Get screen dimensions
        monitor = get_monitors()[0]  # Get primary monitor
        screen_width = monitor.width
        screen_height = monitor.height

        # Get window dimensions
        window_width = 400  # Reduced width
        window_height = 500  # Reduced height

        # Calculate the position to center the window
        x_pos = (screen_width - window_width) // 2
        y_pos = (screen_height - window_height) // 2

        # Position the window at the calculated position
        self.geometry(f"{window_width}x{window_height}+{x_pos-45}+{y_pos-85}")

        # Create a frame for the window with a square white border
        self.window_border = ctk.CTkFrame(
            self, 
            corner_radius=5, 
            fg_color="transparent", 
            border_width=1, 
            border_color="darkgrey"
        )
        self.window_border.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1) 

        # Initialize text_color
        self.text_color = utils.get_sys_txt_color()
        
        # Add the close button (X mark) on the top right corner
        self.close_button = ctk.CTkButton(
            self.window_border, 
            text="✕", 
            font=("Helvetica", 18), 
            width=30, 
            height=30, 
            fg_color="transparent", 
            text_color=self.text_color, 
            command=self.close_window, 
            hover=False
        )
        self.close_button.place(relx=1, rely=0, anchor="ne", x=-20, y=20)  # Move left and down by adjusting 'x' and 'y'

        # Start the appearance mode check (periodic)
        self.after(500, lambda:utils.update_text_color(window=self, root=self))

        # Central Login Card 
        self.login_frame = ctk.CTkFrame(
            self.window_border, 
            corner_radius=0, 
            fg_color="transparent"
        )
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center", relheight=0.8)

        self.create_widgets()
    
    def create_widgets(self):
        # Header frame for logo and title
        self.header_frame = ctk.CTkFrame(
            self.login_frame, 
            fg_color="transparent"
        )
        self.header_frame.pack(pady=(0, 0), padx=10, anchor="center")

        # Add logo
        logo_path = ".\\media\\ff.png"  # Update with your logo file path
        try:
            original_image = Image.open(logo_path)
            resized_image = original_image.resize((120, 110))  # Adjust size as needed
            logo_image = CTkImage(resized_image, size=(90, 80))
        except Exception as e:
            print(f"Error loading logo: {e}")
            logo_image = None

        if logo_image:
            self.logo_label = ctk.CTkLabel(
                self.header_frame, 
                image=logo_image, 
                text=""
            )
            self.logo_label.image = logo_image  # Keep reference to prevent garbage collection
            self.logo_label.pack(side="left", padx=(0, 10))  # Space between logo and title

        # Title
        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="Sign In", 
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(side="left")

        # Username Entry
        self.username_entry = ctk.CTkEntry(
            self.login_frame, 
            placeholder_text="Username", 
            width=280, font=("Helvetica", 12)
        )
        self.username_entry.pack(pady=(20, 10))

        # Password Entry
        self.password_frame = ctk.CTkFrame(self.login_frame, fg_color="transparent")
        self.password_frame.pack(pady=(0, 10))

        self.password_entry = ctk.CTkEntry(
            self.password_frame, 
            placeholder_text="Password", 
            show="●",
            width=240, 
            font=("Helvetica", 12)
        )
        self.password_entry.pack(side="left", padx=5)

        self.toggle_password_button = ctk.CTkButton(
            self.password_frame, 
            text="👁", 
            width=35, 
            command=self.toggle_password_visibility
        )
        self.toggle_password_button.pack(side="left")

        # "Remember Me" Checkbox
        self.remember_me_var = ctk.BooleanVar()
        self.remember_me_checkbox = ctk.CTkCheckBox(
            self.login_frame, 
            text="Remember Me", 
            variable=self.remember_me_var, 
            hover=None, 
            border_width=1, 
            font=("Helvetica", 12), 
            height=10, 
            width=10
        )
        self.remember_me_checkbox.pack(pady=(10, 10))

        # Forgot Password Link
        self.forgot_password_label = ctk.CTkLabel(
            self.login_frame, 
            text="Forgot Password?", 
            font=("Helvetica", 10, "underline"), 
            text_color="#4e54c8"
        )
        self.forgot_password_label.pack(pady=(0, 5))
        self.forgot_password_label.bind("<Button-1>", lambda e: print("Forgot Password clicked"))

        # Sign in Button
        self.login_button = ctk.CTkButton(
            self.login_frame, 
            text="Sign in", 
            command=self.login_action, 
            width=160, 
            hover_color="#ff9a9e", 
            font=("Helvetica", 12, "bold")
        )
        self.login_button.pack(pady=(0, 10))

        # Social Media Login
        self.social_label = ctk.CTkLabel(
            self.login_frame, 
            text="Or connect with", 
            font=("Helvetica", 12)
        )
        self.social_label.pack(pady=(10, 5))

        self.social_button_frame = ctk.CTkFrame(self.login_frame, fg_color="transparent")
        self.social_button_frame.pack(pady=(5, 0), padx=10)

        # Load the images for Google, Facebook, and Twitter
        self.google_logo = ctk.CTkImage(Image.open(".\\media\\google_logo.png"), size=(25, 25))
        self.facebook_logo = ctk.CTkImage(Image.open(".\\media\\facebook_logo.png"), size=(25, 25))
        self.twitter_logo = ctk.CTkImage(Image.open(".\\media\\twitter_logo.png"), size=(25, 25))

        self.google_button = ctk.CTkButton(
            self.social_button_frame, 
            image=self.google_logo, 
            text="Google", 
            fg_color="white", 
            hover_color="#FFFFE3", 
            width=100, 
            text_color="black"
        )
        self.google_button.grid(row=0, column=0, padx=10)

        self.facebook_button = ctk.CTkButton(
            self.social_button_frame, 
            image=self.facebook_logo, 
            text="Facebook", 
            fg_color="white", 
            hover_color="#FFFFE3", 
            width=100, 
            text_color="black"
        )
        self.facebook_button.grid(row=0, column=1, padx=10)

        self.twitter_button = ctk.CTkButton(
            self.social_button_frame, 
            image=self.twitter_logo, 
            text="Twitter", 
            fg_color="white", 
            hover_color="#FFFFE3", 
            width=100, 
            text_color="black")
        self.twitter_button.grid(row=0, column=2, padx=10)

        #'<Return>' bindings
        self.bind('<Return>', self.on_return)
        self.username_entry.bind('<Return>', self.on_return)
        self.password_entry.bind('<Return>', self.on_return)
        
    
    def on_return(self, event):
        if str(event.widget) == str(self.username_entry)+".!entry":
            self.password_entry.focus()
        elif str(event.widget) == str(self.password_entry)+".!entry":
            self.login_action()
        else:
            self.username_entry.focus()
        return None

    

    def toggle_password_visibility(self):
        if self.password_entry.cget("show") == "●":
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="●")
    
    def login_action(self):
        username = self.username_entry.get().strip().lower()
        password = self.password_entry.get().strip()
        rememberance = str(self.remember_me_var.get())

        log = LoginAuthClient()
        log.login(username, password, rememberance)

        if log.status == "failed-user-pass-missing":
            self.clear_entries("user")
            self.insert_error("Username must be entered", "user")
            self.insert_error("password must be entered", "pass")
            log.status = ""
        
        elif log.status == "verified":
            self.close_window()
            log.status = ""


        elif log.status == "failed-username":
            self.clear_entries(obj="user")
            self.insert_error("Username not found", "user")
            log.status = ""


        elif log.status == "failed-password":
            self.clear_entries(obj="pass")
            self.insert_error("Invalid password", "pass")
            log.status = ""

        else:
            lab = ctk.CTkLabel(
                self.login_frame, 
                text="Check your connection", 
                font=("Helvetica", 14, "normal")
            )
            lab.pack(pady = (10,0))
            log.status = ""
            lab.after(1500, lab.destroy)

    def clear_entries(self, obj: Literal["user", "pass"] = "user"):
        # Clear both username and password entries
        if obj == "user":
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
        elif obj == "pass":
            self.password_entry.delete(0, 'end')
        return None

    def insert_error(self, message:str, error: Literal["user" , "pass"] = "user"):
        if error == "user":
            self.username_entry.insert(0, message)
            self.username_entry.after(1000, lambda: self.username_entry.delete(0, 'end'))
            
        else:
            self.password_entry.insert(0, message)
            self.password_entry.configure(show = "")
            self.username_entry.after(1000, self.show_err)

    def show_err(self):
        self.password_entry.delete(0, 'end')
        self.password_entry.configure(show = "●")
        
    def close_window(self):
        self.destroy()  # Close the window
        return None


# Run the application
if __name__ == "__main__":
    test = LogIn()  # Now start the floating Toplevel window
    test.mainloop()
