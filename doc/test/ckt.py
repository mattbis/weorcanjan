import customtkinter as ctk

# Modes: system (default), light, dark
ctk.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
ctk.set_default_color_theme("blue")


# app = ctk.CTk()  # create CTk window like you do with the Tk window
# app.geometry("800x600")

class RunningProgramsFrame(ctk.CTkScrollableFrame):
    """
    If the user clicks on the check box it will appear in the list with save these
    args. In the sister frame.
    """
    def __init__(
        self,
        master,
        **kwargs
    ):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=0)

        # add widgets onto the frame...
        self.label = ctk.CTkLabel(self, text="Running Programs")
        self.label.grid(row=0, column=0, padx=20, pady=20)


class ArgumentsCheckListFrame(ctk.CTkScrollableFrame):
    def __init__(
        self,
        master,
        **kwargs
    ):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(1, weight=1)

        # add widgets onto the frame...
        self.label = ctk.CTkLabel(self, text="Arguments")
        self.label.grid(row=0, column=1, padx=20, pady=20)

        # self.checkbox_list = []
        # for i, item in enumerate(item_list):
        #     self.populate_program_list(item)


class ControlPanelFrame(ctk.CTkFrame):
    def __init__(
        self,
        master,
        **kwargs
    ):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(2, weight=0)

        self.label = ctk.CTkLabel(self, text="Control Panel")
        self.label.grid(row=1, column=0, padx=20, pady=20)

        # self.done_button = ctk.CTkButton(
        #     app,
        #     text="Done",
        #     command=button_event
        # )

        # self.cancel_button = customkinter.CTkButton(
        # )

    # def exit_event(self):
    #     print("exit!!!")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Weorcanjan")

        # https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
        # In the simplest terms possible, a non-zero weight causes a row or column to
        # grow if there's extra space. The default is a weight of zero, which means the
        # column will not grow if there's extra space.

        # row for the columns
        self.grid_rowconfigure(0, weight=1)

        # row for the control panel
        self.grid_rowconfigure(1, weight=0)

        # expanding column of arg configuration
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.running_programs_frame = RunningProgramsFrame(
            master=self,
            corner_radius=0,
            width=300,
        )
        self.arguments_checkbox_frame = ArgumentsCheckListFrame(
            master=self,
            corner_radius=0,
            width=500
        )
        self.control_panel_frame = ControlPanelFrame(
            master=self,
            corner_radius=0,
            width=800,
            height=100
        )

        self.running_programs_frame.grid(row=0, column=0, sticky="nsew")
        self.arguments_checkbox_frame.grid(row=0, column=1, sticky="nsew")
        self.control_panel_frame.grid(row=1, column=0, sticky="nsew", columnspan="2")

        # add controls here to reference the subcomponents
        self.btn_checkbox = ctk.CTkButton(
            self.control_panel_frame,
            text="Done",
            command=self._on_done()
        )

    def _on_done(self):
        pass


app = App()
app.mainloop()
