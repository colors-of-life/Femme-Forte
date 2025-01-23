import customtkinter as ctk
from tkcalendar import Calendar
import datetime

class ManagementApp():
    def __init__(self, root: ctk.CTk):
        # Create a CTkFrame as the main frame
        self.main_frame = ctk.CTkFrame(root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Grid configuration for the root window to make the frame expand
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Grid configuration for the main frame to make widgets inside it expand
        self.main_frame.grid_rowconfigure((0, 1), weight=1)  # Allow rows 0 and 1 to expand
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)  # Allow columns to expand

        # Calendar widget using tkcalendar
        self.calendar_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.calendar_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.calendar_frame, text="Calendar", font=("Arial", 18)).pack(pady=10)

        # tkcalendar widget
        self.calendar = Calendar(self.calendar_frame, selectmode='day', date_pattern='yyyy-mm-dd', showothermonthdays = False)
        self.calendar.pack(expand=True, fill="both", padx=5, pady=5)

        # Notifications widget
        self.notifications_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.notifications_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.notifications_frame, text="Notifications", font=("Arial", 18)).pack(pady=10)
        self.notification_text = ctk.CTkTextbox(self.notifications_frame, height=200, font=('Helvetica', 16))
        self.notification_text.pack(expand=True, fill="both")
        self.notification_text.insert("0.0", "No new notifications.")

        # Notes widget
        self.notes_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.notes_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.notes_frame, text="Notes", font=("Arial", 18)).pack(pady=10)
        self.notes_entry = ctk.CTkTextbox(self.notes_frame, height=200, font=('Helvetica', 16))
        self.notes_entry.pack(expand=True, fill="both")

        # Clock widget
        self.clock_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.clock_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.clock_frame, text="Clock", font=("Arial", 18)).pack(pady=10)
        self.clock_label = ctk.CTkLabel(self.clock_frame, text="", font=("Arial", 72, "bold"))
        self.clock_label.pack(fill="both", expand =True)
        self.update_clock()

        # Inventory level indicator
        self.inventory_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.inventory_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.inventory_frame, text="Inventory Level", font=("Arial", 18)).pack(pady=10)
        self.inventory_level = ctk.CTkProgressBar(self.inventory_frame, orientation="horizontal", height=20)
        self.inventory_level.pack(expand=True, fill="x", padx=20, pady=10)
        self.inventory_level.set(1)  # Example value, 70%

        # Placeholder for additional widgets
        self.extra_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.extra_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.extra_frame, text="Additional Widgets", font=("Arial", 18)).pack(pady=10)
        ctk.CTkLabel(self.extra_frame, text="(Feature coming soon)", font=("Arial", 14)).pack(pady=10)

    def update_clock(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.clock_label.configure(text=current_time)
        self.main_frame.after(1000, self.update_clock)  # Update every second

# Run the application
if __name__ == "__main__":
    root = ctk.CTk()  # Create a root Tkinter window
    app = ManagementApp(root)  # Pass root to the ManagementApp class
    root.mainloop()  # Start the Tkinter main loop
