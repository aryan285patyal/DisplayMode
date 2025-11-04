import customtkinter as ctk
ctk.set_default_color_theme("dark-blue")

class checkbox_frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.checkbox_1 = ctk.CTkCheckBox(self, text="Option 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=10)
        self.checkbox_2 = ctk.CTkCheckBox(self, text="Option 2")
        self.checkbox_2.grid(row=0, column=1, padx=10, pady=10)
        self.checkbox_3 = ctk.CTkCheckBox(self, text="Option 3")
        self.checkbox_3.grid(row=0, column=2, padx=10, pady=10)

class main_window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("DisyplayMode")
        self.geometry("400x300")
        self.grid_columnconfigure((0, 1), weight=1, pad=10)
        self.grid_rowconfigure(0, weight=1, pad=10)
        cb_frame = checkbox_frame(self)
        cb_frame.grid(row=0, column=0)

        apply_button = ctk.CTkButton(self, text="Apply")
        apply_button.grid(row=1, column=0, pady=20)

app = main_window()
app.mainloop()