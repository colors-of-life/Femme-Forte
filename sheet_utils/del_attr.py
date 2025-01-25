from tksheet import Sheet
import customtkinter as ctk
import json

class DelAttr:
    def __init__(self, sheet: Sheet):
        self.win = ctk.CTkToplevel()
        self.flag = 0
        self.win.overrideredirect(True)
        self.win.geometry("300x200+850+400")
        self.win.grab_set()

        self.new_sheet = sheet

        self.f_1 = ctk.CTkFrame(self.win)
        self.f_1.pack(fill = "both", expand =True, anchor = "center")

        self.label = ctk.CTkLabel(
            self.f_1, 
            text= "Delete attribute", 
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

        self.btn_2 = ctk.CTkButton(self.f_1, text= "Delete", command= lambda: self.get_attr(self.entry_1), width=50)
        self.btn_2.pack(side = "right", padx = (0, 60), pady = (0, 0))
 
    def get_attr(self, entry: ctk.CTkEntry)-> None:
        if entry.get() == "":
            self.entry_1.insert(0, "Must enter an attribute")
            self.entry_1.configure(text_color = "red")
            self.entry_1.after(500, lambda: [self.entry_1.delete(0, 'end'), self.entry_1.configure(text_color = "white")])
            return None
        
        else:
            self.head = entry.get()
            with open("./data\\headers\\headers.json", 'r') as f:
                data = json.load(f)
                search_flag = 0
                for idx, head in enumerate(data["headers"]):
                    if head == self.head:
                        data["headers"].remove(head)
                        search_flag = 1
                        break

            if search_flag == 1:                
                with open("./data\\headers\\headers.json", 'w') as f: 
                    json.dump(data, f, indent=4)
                try:
                    self.new_sheet.delete_column(idx=idx)
                except Exception as e:
                    pass
                self.win.destroy()

            else:
                self.entry_1.delete(0, 'end')
                self.entry_1.insert(0, "No such attribute found")
                self.entry_1.configure(text_color = "yellow")
                self.entry_1.after(500, lambda: [self.entry_1.delete(0, 'end'), self.entry_1.configure(text_color = "white")])
                return

