import customtkinter as ctk
from sheet_utils import add_attr

class LeftPanel:
    def __init__(self, parent, right_panel):
        """Create a left panel for navigation options."""
        self.right_panel = right_panel  # Store the reference to the right panel
        self.left_panel = ctk.CTkFrame(parent, corner_radius=10, width=200)
        self.left_panel.pack(side="left", fill="y", padx=10, pady=10)

        # Add navigation dropdowns
        options = {
            "Tenants": ["Add attribute", "Manage Tenants"],
            "Employee": ["Add Employee", "View Employees", "Remove Employee"],
            "Expenses": ["Add Expense", "View Expenses", "Generate Report"],
            "Notes": ["Add Note", "View Notes", "Delete Note"],
        }

        for key, values in options.items():
            label = ctk.CTkLabel(self.left_panel, text=key, font=("Arial", 14, "bold"))
            label.pack(pady=5)

            dropdown = ctk.CTkOptionMenu(
                self.left_panel,
                values=values,
                command=lambda selection, 
                category=key: self.handle_dropdown_selection(category, selection)
            )
            dropdown.pack(pady=5, fill="x", padx=10)

    def handle_dropdown_selection(self, category, selection):
        """Handle dropdown menu selection."""
        print(f"Category: {category}, Selected: {selection}")

        # Example: Update tksheet data based on dropdown selection
        if category == "Tenants" and selection == "Add attribute":
            add_attr.AddAttr(sheet= self.right_panel.sheet)
            
        elif category == "Tenants" and selection == "Manage Tenants":
            self.add_sample_row("v")

    def add_sample_row(self, passas):
        """Add a sample row to the tksheet in the right panel."""
        if self.right_panel.sheet and passas == "h":
            indx = 1
            self.right_panel.sheet.insert_column(column = ["name"], header = True)
            print("Row added to tksheet.")
        elif self.right_panel.sheet and passas == "v":
            self.right_panel.sheet.insert_row(row = ["test", "test", "test", "test", "test", "test", "test", ])
