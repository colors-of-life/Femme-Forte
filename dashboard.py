import customtkinter as ctk
from left_panel import LeftPanel
from right_panel import RightPanel

class InteractiveTableApp:
    def __init__(self, root):
        self.main_frame = root

        # Create a container frame to hold left and right panels
        container = ctk.CTkFrame(self.main_frame, corner_radius=10)
        container.pack(fill="both", expand=True, padx=10, pady=10)

        # Create the right panel first, as it contains the tksheet
        self.right_panel = RightPanel(container)

        # Pass the reference of the right panel to the left panel
        self.left_panel = LeftPanel(container, self.right_panel)

# Run the application
if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("900x600")
    app = InteractiveTableApp(root)
    root.mainloop()
