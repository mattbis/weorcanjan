import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")


# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("800x600")

class RunningProgramsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

class ArgumentsCheckListFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = RunningProgramsFrame(
            master=self,
            width=300,
            height=200,
            corner_radius=0,
            fg_color="transparent"
        )
        self.my_frame.grid(row=0, column=0, sticky="nsew")


app = App()
app.mainloop()
