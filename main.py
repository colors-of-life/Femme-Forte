import customtkinter as ctk
from screeninfo import get_monitors
from sign_in import LogIn
from sign_up import SignUp
from log_state_check_client import log_state_check
from dashboard import InteractiveTableApp
from PIL import Image
from profile_page import *
from homepage import ManagementApp

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Initialize UI Properties
        self._init_window_properties()
        self._create_navigation_bar()
        self._create_main_panel()

        # Display the initial state
        self.display_home()
        self.after(0, lambda: self.state("zoomed"))
        self._check_login_state()

    def _init_window_properties(self):
        """Set up main window properties."""
        monitor = get_monitors()[0]
        self.geometry(f"{monitor.width}x{monitor.height}+0+0")
        self.title("Femme Forte")
        self.iconbitmap(".\\media\\icons\\femme_forte.ico")

    def _create_navigation_bar(self):
        """Create the navigation bar with a logo and centered navigation buttons."""
        self.nav_bar = ctk.CTkFrame(
            self,
            height=70,
            corner_radius=0,
            border_width=2
        )
        self.nav_bar.pack(fill="x", side="top")

        # Add logo to the left
        try:
            logo_image = ctk.CTkImage(Image.open("media/ff.png"), size=(100, 80))  # Update path and size as needed
        except FileNotFoundError:
            logo_image = None  # Handle missing logo gracefully

        self.logo_label = ctk.CTkLabel(
            self.nav_bar,
            text="",
            image=logo_image,
            fg_color="transparent"
        )
        self.logo_label.grid(row=0, column=0, padx=(300,0), pady=5, sticky = "e")

        # Create a frame for the navigation buttons to center them
        self.nav_buttons_frame = ctk.CTkFrame(
            self.nav_bar,
            fg_color="transparent"
        )
        self.nav_buttons_frame.grid(row=0, column=1, sticky = "w")

        # Add navigation buttons
        self.nav_options = [
            {"text": "Home", "icon": "media/nav_icons/home.png", "action": self.display_home},
            {"text": "Dashboard", "icon": "media/nav_icons/dashboard.png", "action": self.display_dashboard},
            {"text": "Sign in", "icon": "media/nav_icons/sign_in.png", "action": self.display_login},
            {"text": "Sign up", "icon": "media/nav_icons/sign_up.png", "action": self.display_sign_up},
            {"text": "Profile", "icon": "media/nav_icons/profile.png", "action": self.display_profile},
        ]

        for idx, option in enumerate(self.nav_options):
            self._create_nav_button(idx, option)

        # Adjust grid column weights to center buttons
        self.nav_bar.grid_columnconfigure(0, weight=1)  # Logo column
        self.nav_bar.grid_columnconfigure(1, weight=3)  # Buttons column
        self.nav_bar.grid_columnconfigure(2, weight=1)  # Right-side spacer

    def _create_nav_button(self, idx, option):
        """Create a single navigation button."""
        try:
            icon = ctk.CTkImage(Image.open(option["icon"]).resize((40, 40)))
        except FileNotFoundError:
            icon = None  # Handle missing icons gracefully

        btn = ctk.CTkButton(
            self.nav_buttons_frame,
            text=option["text"],
            width=120,
            fg_color="transparent",
            text_color="#4e54c8",
            hover_color="#eaeaea",
            font=("Helvetica", 14),
            image=icon,
            compound="left",
            command=option["action"],
        )
        btn.grid(row=0, column=idx, padx=10, pady=25)


    def _create_main_panel(self):
        """Create the main content panel."""
        self.main_panel = ctk.CTkFrame(self, fg_color="transparent")
        self.main_panel.pack(fill="both", expand=True)
        

    def _check_login_state(self):
        """Check the initial login state."""
        state_data = log_state_check()
        if state_data[0] == "false":
            self.after(0, self.display_login)


    def display_home(self):
        self._update_main_panel("Femme Forte")
        ManagementApp(self.main_panel)


    def display_dashboard(self):
        """Display the Dashboard."""
        self._update_main_panel("Femme Forte\\Dashboard")
        InteractiveTableApp(self.main_panel)


    def display_login(self):
        """Display the Login page."""
        self._update_main_panel("Femme Forte\\Sign in")
        self.display_home()
        self._manage_single_instance("login")


    def display_sign_up(self):
        """Display the Sign-Up page."""
        self._update_main_panel("Femme Forte\\sign up")
        self.display_home()
        self._manage_single_instance("signup")


    def display_profile(self):
        """Display the Profile page."""
        self._update_main_panel("Femme Forte\\Profile")
        ProfilePage(self.main_panel)


    def _manage_single_instance(self, page_type):
        """Handle single-instance pages (Login/Sign-Up)."""
        global login_instance_count, signup_instance_count

        if page_type == "login" and login_instance_count == 0:
            login_instance_count = 1
            LogIn().wait_window()
            login_instance_count = 0
            self.title("Femme Forte")

        elif page_type == "signup" and signup_instance_count == 0:
            signup_instance_count = 1
            SignUp().wait_window()
            signup_instance_count = 0
            self.title("Femme Forte")


    def _update_main_panel(self, title):
        """Clear and update the main panel with a message."""
        self.clear_main_panel()
        self.title(title)


    def clear_main_panel(self):
        """Remove all widgets from the main panel."""
        for widget in self.main_panel.winfo_children():
            widget.destroy()


# Run the application
if __name__ == "__main__":
    # Initialize CustomTkinter
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    login_instance_count = 0
    signup_instance_count = 0
    main_window = MainWindow()
    main_window.mainloop()
    
    