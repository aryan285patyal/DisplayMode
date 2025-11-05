import customtkinter as ctk

#=======================classes for which pages are still to be made===============================
class welcome_page(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

class saved_page(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

class settings_page(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

class about_page(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.title = ctk.CTkLabel(self, text="About Page")
        self.title.pack(pady=40)
        about_label = ctk.CTkLabel(self, text="DisplayMode v1.0\nDeveloped by Aryan", font=("Arial", 14))
        about_label.pack(pady=40)

        about_close_button = ctk.CTkButton(self, text="Close", command=parent.show_main_view)
        about_close_button.pack(pady=10)
#======================create_mode_page=============================================================
class create_mode_window(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.title = ctk.CTkLabel(self, text = "Create Mode")
        self.title.pack(pady=40)
        self.subtitle = ctk.CTkLabel(self, text="Create your custom display mode here!", font=("Arial", 16))
        self.subtitle.pack(pady=40)
        
        # ============Orientation Selection=========================================================
        self.orientation_label = ctk.CTkLabel(self, text="Select Orientation:", font=("Arial", 14))
        self.orientation_label.pack(pady=10)
        self.orientation_optionmenu = ctk.CTkOptionMenu(self, values=["Landscape", "Portrait"])
        self.orientation_optionmenu.set("Landscape")
        self.orientation_optionmenu.pack(pady=10)

        # ============Resolution Selection===========================================================
        self.resolution_label = ctk.CTkLabel(self, text="Select Resolution:", font=("Arial", 14))
        self.resolution_label.pack(pady=10)
        self.resolution_optionmenu = ctk.CTkOptionMenu(self, values=["1920x1080", "1280x720", "800x600"])
        self.resolution_optionmenu.set("1920x1080")
        self.resolution_optionmenu.pack(pady=10)

        # ============Refresh Rate Selection=========================================================
        self.refresh_rate_label = ctk.CTkLabel(self, text="Select Refresh Rate:", font=("Arial", 14))
        self.refresh_rate_label.pack(pady=10)
        self.refresh_rate_optionmenu = ctk.CTkOptionMenu(self, values=["60Hz", "75Hz", "120Hz", "144Hz"])
        self.refresh_rate_optionmenu.set("60Hz")
        self.refresh_rate_optionmenu.pack(pady=10)

        #save mode button
        self.save_button = ctk.CTkButton(self, text="Save Mode", command=)
        self.save_button.pack(pady=20)

        #the close window button
        self.close_button = ctk.CTkButton(self,text="Close",command=parent.show_main_view)
        self.close_button.pack(pady=20)

    def action_save_mode(self):
        orientation = self.orientation_optionmenu.get()
        refresh = self.refresh_rate_optionmenu.get()
        resolution = self.resolution_optionmenu.get()
        print(f"Saved Mode with orientation:{orientation}, refresh rate:{refresh}Hz, and resolution:{resolution} ")

#________main_window_elements______

#====================main_window : sidebar============================================================
class sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side="left", fill="y")

        #About button
        self.button_about = ctk.CTkButton(self, text="About", command= lambda: master.show_frame("about_page"))
        self.button_about.grid(row=0, column=0, padx=10, pady=40)

        #Create Mode button
        self.button_create_mode = ctk.CTkButton(self, text="Create Mode", command=lambda: master.show_frame("create_mode"))
        self.button_create_mode.grid(row=1, column=0, padx=10, pady=40)

        #Saved Modes button
        self.button_saved_modes = ctk.CTkButton(self, text="Saved Modes")
        self.button_saved_modes.grid(row=2, column=0, padx=10 , pady=40)

        #exit button
        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.close_app)
        self.exit_button.grid(row=3, column=0, padx=10 , pady=40)
    
    # ########################use this as a template for alerts#####################
    # def show_about(self):
    #     about_window = ctk.CTkToplevel(self)
    #     about_window.title("About DisplayMode")
    #     about_window.geometry(f"{self.window_width//2}x{self.window_height//2}+{self.window_width//2}+{self.window_height//2}")
    #     about_window.transient(self)
    #     about_window.grab_set()
    #     about_window.focus_set()

    #     about_label = ctk.CTkLabel(about_window, text="DisplayMode v1.0\nDeveloped by Aryan", font=("Arial", 14))
    #     about_label.pack(pady=40)

    #     about_close_button = ctk.CTkButton(about_window, text="Close", command=about_window.destroy)
    #     about_close_button.pack(pady=10)
    # ########################use this as a template for alerts#####################


    # close_app: handels closing the app
    def close_app(self):
        self.destroy()  # 'destroy()' closes the current window


#========================The main window============================================================
class MainWindow(ctk.CTk):
    #constructor of the mainWindow
    def __init__(self):
        #calling the constructor of the ctk.CTk class in the constructor of the MainWindow
        super().__init__()

        # a dictionary to hold different frames
        self.frames = {
            "create_mode": create_mode_window,
            "welcome_page": welcome_page,
            "saved_page": saved_page,
            "settings_page": settings_page,
            "about_page": about_page
            }
        
        #window setup
        self.title("DisplayMode")
        self.window_height = self.winfo_screenheight()
        self.window_width = self.winfo_screenwidth()
        self.geometry(f"{self.window_width}x{self.window_height}+0+0")

        # Label at the top
        self.label = ctk.CTkLabel(self, text="Welcome to DisplayMode!", font=("Arial", 16))
        self.label.pack(pady=40)

        # making a sidebar instance and passing the MainWindow instance(self) to it so that the sidebar frame gets attached to the MainWindow
        self.sidebar = sidebar(self)
        

    # helper function which switches between frames(create, edit, saved)
    def show_frame(self, frame_name):

        # remove all current widgets from MainWindow instance's child list
        for widget in self.winfo_children():
            widget.pack_forget()

        # add the new frame
        frame = self.frames.get(frame_name) # get the frame class base on frame_name from the dictionary self.frames
        if(frame):frame(self).pack() #if frame exists in the dictionary then create an instance of the frame with MainFrame instance(self) as the parent. then pack
        else: print("no fram found in the dictionary")

    def show_main_view(self):
        print("in main view show")
        # Clear all widgets
        for widget in self.winfo_children():
            widget.pack_forget()

        # Rebuild your main UI
        self.label = ctk.CTkLabel(self, text="Welcome to DisplayMode!", font=("Arial", 16))
        self.label.pack(pady=40)

        self.sidebar = sidebar(self)






    
