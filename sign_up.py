import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
from screeninfo import get_monitors
import utils
from sign_up_client import send_sign_up_data

class SignUp(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """Setup window properties and initial position."""
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.grab_set()

        # Set dimensions and center the window
        window_width, window_height = 400, 600
        monitor = get_monitors()[0]
        screen_width, screen_height = monitor.width, monitor.height
        x_pos = (screen_width - window_width) // 2 - 45
        y_pos = (screen_height - window_height) // 2 - 35
        self.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        # Add border frame
        self.window_border = ctk.CTkFrame(
            self,
            corner_radius=5,
            fg_color="transparent",
            border_width=1,
            border_color="darkgrey",
        )
        self.window_border.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        self.text_color = utils.get_sys_txt_color()

        # Close button
        self.close_button = ctk.CTkButton(
            self.window_border,
            text="✕",
            font=("Helvetica", 18),
            width=30,
            height=30,
            fg_color="transparent",
            text_color=self.text_color,
            command=self.close_window,
            hover=False,
        )
        self.close_button.place(relx=1, rely=0, anchor="ne", x=-20, y=20)
        self.after(500, lambda: utils.update_text_color(window=self, root=self))

    def create_widgets(self):
        """Create all widgets in the SignUp window."""
        self.signup_frame = ctk.CTkFrame(self.window_border, corner_radius=0, fg_color="transparent")
        self.signup_frame.place(relx=0.5, rely=0.5, anchor="center", relheight=0.9)

        self.create_header()
        self.create_input_fields()
        self.create_signup_button()

    def create_header(self):
        """Create the header with a logo and title."""
        header_frame = ctk.CTkFrame(self.signup_frame, fg_color="transparent")
        header_frame.pack(pady=(10, 10))

        # Logo
        logo_image = self.load_resized_image(".\\media\\ff.png", (90, 80))
        logo_label = ctk.CTkLabel(header_frame, image=logo_image, text="")
        logo_label.image = logo_image  # Prevent garbage collection
        logo_label.pack(side="left", padx=(0, 10))

        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="Sign Up",
            font=("Helvetica", 24, "bold"),
        )
        title_label.pack(side="left")

    def create_input_fields(self):
        """Create input fields for user details."""
        self.input_fields = {
            "Full Name": None,
            "Designation": None,
            "Phone Number": None,
            "Email ID": None,
            "Create Username": None,
            "Create Password": {"show": "●"},
            "Confirm Password": {"show": "●"},
        }

        self.entries = {}
        for placeholder, options in self.input_fields.items():
            show_char = options.get("show") if options else ""
            entry = ctk.CTkEntry(
                self.signup_frame,
                placeholder_text=placeholder,
                width=280,
                font=("Helvetica", 12),
                show=show_char,
            )
            entry.pack(pady=(10, 10))
            self.entries[placeholder] = entry

    def create_signup_button(self):
        """Create the Sign Up button."""
        signup_button = ctk.CTkButton(
            self.signup_frame,
            text="Sign Up",
            command=self.signup_action,
            width=160,
            hover_color="#ff9a9e",
            font=("Helvetica", 12, "bold"),
        )
        signup_button.pack(pady=(20, 10))

    def load_resized_image(self, path, size):
        """Load and resize an image."""
        image = Image.open(path)
        resized_image = image.resize(size)
        return CTkImage(resized_image, size=size)

    def signup_action(self) -> None:
        """Handle the Sign Up action."""
        #data = {key: entry.get().strip() for key, entry in self.entries.items()}
        data = {"username" : self.entries["Create Username"].get().strip(),
                "password" : self.entries["Confirm Password"].get(),
                "name": self.entries["Full Name"].get().strip()
                }
        send_sign_up_data(data = data)
        self.close_window()
        return None

    def show_error(self, message):
        """Display an error message."""
        error_label = ctk.CTkLabel(
            self.signup_frame,
            text=message,
            font=("Helvetica", 12),
            text_color="red",
        )
        error_label.pack(pady=(5, 0))
        error_label.after(1500, error_label.destroy)

    def close_window(self):
        """Close the SignUp window."""
        self.destroy()


# Run the application
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")
    root = ctk.CTk()
    SignUp()
    root.mainloop()
