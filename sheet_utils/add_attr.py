from tksheet import Sheet
import customtkinter as ctk
import json

class AddAttr:
    def __init__(self, sheet: Sheet):
        self.win = ctk.CTkToplevel()
        self.flag = 0
        self.win.overrideredirect(True)
        self.win.geometry("300x200+850+400")
        self.win.grab_set()

        self.f_1 = ctk.CTkFrame(self.win)
        self.f_1.pack(fill = "both", expand =True, anchor = "center")

        self.label = ctk.CTkLabel(
            self.f_1, 
            text= "New attribute", 
            text_color="black", 
            font=('Helvetica', 16, "bold"), 
            bg_color="grey80", 
            width=300
            )
        self.label.pack()

        self.entry_1 = ctk.CTkEntry(self.f_1, placeholder_text="Enter the attribute", width=200, height=40)
        self.entry_1.pack(pady= (30,0))

        self.btn_1 = ctk.CTkButton(self.f_1, text= "Cancel", command= self.win.destroy, width=50)
        self.btn_1.pack(side = "left", padx = (60, 0), pady = (0, 0))

        self.btn_2 = ctk.CTkButton(self.f_1, text= "Add", command= lambda: self.get_attr(self.entry_1), width=50)
        self.btn_2.pack(side = "right", padx = (0, 60), pady = (0, 0))
 
        self.win.wait_window()

        if self.flag == 1:
            new_sheet = sheet
            with open("./data\\headers\\headers.json", 'r') as f:
                data = json.load(f)
                data["headers"].append(self.head)
            with open("./data\\headers\\headers.json", 'w') as f: 
                json.dump(data, f, indent=4)
            try:
                new_head = [self.head]
                new_sheet.insert_column(column= new_head, header=True)
            except Exception as e:
                pass
        

    def get_attr(self, entry: ctk.CTkEntry)-> str:
        if entry.get() == "":
            self.entry_1.configure(placeholder_text="Must enter a attribute", placeholder_text_color = "red")
            self.entry_1.after(500, lambda: self.entry_1.delete(0, 'end'))
            return None
        else:
            self.head = entry.get()
            self.flag = 1
            self.win.destroy()
            return self.head