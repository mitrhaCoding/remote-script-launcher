import customtkinter as ctk

class ScriptFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0,column=0,pady=10,padx=20)