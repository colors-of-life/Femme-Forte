import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
import utils
from tkinter import filedialog  # Import filedialog to open file selection dialog

class ProfilePage:
    def __init__(self, root: ctk.CTk):
        self.text_color = utils.get_sys_txt_color()  # Get text color from utils
        self.body_frame = ctk.CTkFrame(
            master=root,
            width=700,  # Smaller width
            height=500,  # Smaller height
            fg_color="transparent"
        )
        self.body_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Profile picture
        size = (90, 90)
        self.profile_image = Image.open(".\\media\\profiles\\profile.png").resize(size)  # Initial image
        self.profile_CTkimage = CTkImage(self.profile_image, size=size)
        self.profile_picture = ctk.CTkLabel(
            self.body_frame, 
            image=self.profile_CTkimage, 
            text=""
            )
        self.profile_picture.place(x=80, y=70)

        # Update image button
        self.update_button = ctk.CTkButton(
            self.body_frame, 
            text="Upload Image", 
            command=self.update_image,width=40
            )
        self.update_button.place(x=80, y=170)

        self.labels = [
            {
                "text":"Name:",
                "x":80,
                "y":210
            },
            {
                "text":"Username:",
                "x":80,
                "y":245
            },
            {
                "text":"Designation:",
                "x":80,
                "y":280
            },
            {
                "text":"Mobile:",
                "x":80,
                "y":315
            },
            {
                "text":"Email:",
                "x":80,
                "y":350
            },
            {
                "text":"Address:",
                "x":80,
                "y":385

            }
        ]
        for options in self.labels:
            self.create_labels(options= options)

        self.entry_boxes = [
            {
                "placeholder":"Muhammed Ibrahim Rabbani M N",
                "x":100,
                "y":210
            },
            {
                "placeholder":"username@123",
                "x":100,
                "y":245
            },
            {
                "placeholder":"Developer/technician",
                "x":100,
                "y":280
            },
            {
                "placeholder":"8139824398",
                "x":100,
                "y":315
            },
            {
                "placeholder":"mnmircse@gmail.com",
                "x":100,
                "y":350
            },
            {
                "placeholder":"maliyekkal(H), thevakkal, thrikkakara, pin:682021, Ernakulam ,kerala, India, thrikkakara p.o",
                "x":100,
                "y":385
            }
        ]
        for options in self.entry_boxes:
            self.create_entry_boxes(options=options)
        
        btn_edit = ctk.CTkButton(self.body_frame, text="edit", command= self.enable_edit)
        btn_edit.place(x = 300, y=440)

        btn_save = ctk.CTkButton(self.body_frame, text="save", command=self.save)
        btn_save.place(x = 450, y=440)

        t_label = ctk.CTkLabel(self.body_frame, text="Profile", font = ("Helvetica", 38))
        t_label.place(x = 380, y = 100)
        
        # Update text color after a small delay
        self.body_frame.after(
            ms=500, 
            func=lambda: utils.update_text_color(
                window=self, 
                root=self.body_frame
                )
            )
        
    # self-Methods    
    def create_labels(self,options):
        labls = ctk.CTkLabel(
            self.body_frame, 
            text=options["text"], 
            font=('Helvetica', 18), 
            text_color=self.text_color
            )
        labls.place(x = options["x"], y = options["y"])
    
    def create_entry_boxes(self, options):
        entry_box = ctk.CTkEntry(
            master=self.body_frame,
            placeholder_text=options["placeholder"],
            placeholder_text_color=self.text_color,
            font=('Helvetica', 18),
            width=500
            )
        entry_box.place(x= options["x"]+100, y = options["y"])
        entry_box.configure(state="disabled")
    
    def enable_edit(self):
        for child in self.body_frame.winfo_children():
            if isinstance(child, ctk.CTkEntry):
                child.configure(state = "normal")
    
    def save():
        pass


    def update_image(self):
        # Open a file dialog to select a new image
        file_path = filedialog.askopenfilename(
            title="Select a Profile Image", 
            filetypes=[(
                "Image files", 
                "*.png;*.jpg;*.jpeg;*.bmp"
                )]
            )
        
        if file_path:  # If a file was selected
            # Open and resize the selected image
            new_image = Image.open(file_path).resize((90, 90))
            new_CTkimage = CTkImage(new_image, size=(90, 90))
            
            # Update the label with the new image
            self.profile_picture.configure(image=new_CTkimage)
            self.profile_picture.image = new_CTkimage  # Keep a reference to avoid garbage collection

if __name__ == '__main__':
    root = ctk.CTk()
    ProfilePage(root=root)
    root.mainloop()
