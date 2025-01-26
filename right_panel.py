import customtkinter as ctk
from tksheet import Sheet
import pickle
import os
import json

PICKLE_FILE = ".\\data\\table_data.pkl"

class RightPanel:
    def __init__(self, parent):
        """Create the right panel with tksheet and actions."""
        self.right_panel = ctk.CTkFrame(parent, corner_radius=10)
        self.right_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        with open(".\\data\\headers\\headers.json") as f :

            headers = json.load(f)
            self.custom_headers = headers["headers"]

        # Load data from pickle file or use default data
        data = self.load_from_pickle()

        # Create tksheet table
        self.sheet = Sheet(self.right_panel, data=data, header=self.custom_headers, width=600, height=400)
        self.sheet.pack(fill="both", expand=True)
        self.sheet.enable_bindings(("column_width_resize", "row_width_resize", "row_height_resize", "column_height_resize", "single_select", "copy"))

        # Set table customizations
        self.set_table_properties()

        # Create action buttons
        self.create_action_buttons()

    def load_from_pickle(self):
        """Load data from a pickle file."""
        if os.path.exists(PICKLE_FILE):
            with open(PICKLE_FILE, "rb") as file:
                data = pickle.load(file)
            print(f"hello world")
        else:
            # Default empty table data
            data = [["" for _ in self.custom_headers] for _ in range(1)]
        return data

    def save_to_pickle(self):
        """Save the current table data to a pickle file."""
        data = self.sheet.get_sheet_data()
        with open(PICKLE_FILE, "wb") as file:
            pickle.dump(data, file)
        print(f"Data saved to {PICKLE_FILE}")

    def set_table_properties(self):
        """Set properties for the table."""
        self.sheet.header_font(("Helvetica", 16, "bold"))
        self.sheet.header_align("c")
        self.sheet.font(("Arial", 14, "normal"))
        self.sheet.table_align("c")
        self.sheet.set_options(alternate_color="grey80")

    def create_action_buttons(self):
        """Create action buttons below the sheet."""
        button_frame = ctk.CTkFrame(self.right_panel)
        button_frame.pack(fill="x", pady=10)

        save_button = ctk.CTkButton(button_frame, text="Save", command=self.save_to_pickle, width=150)
        save_button.pack(side="left", padx=5)

        load_button = ctk.CTkButton(button_frame, text="Load", command=self.load_table_data, width=150)
        load_button.pack(side="left", padx=5)

    def load_table_data(self):
        """Load data from a pickle file into the table."""
        data = self.load_from_pickle()
        self.sheet.set_sheet_data(data)
