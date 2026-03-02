import customtkinter as ctk
from modules import target_manager
from gui import scripts_frame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Remote Script Launcher")

        self.enter = ctk.CTkEntry(self, placeholder_text="IP, enter to confirm")
        self.enter.grid(row=0, column=0, pady=10, padx=20)
        self.enter.bind("<Return>", self.on_key_pressed)
        self.enter.focus()

        self.script_frame = scripts_frame.ScriptFrame(master=self, width=450, height=200)
        self.script_frame.grid(row=1,column=0,pady=10,padx=20)

    def on_key_pressed(self, event=None):
        value = self.enter.get()
        target_manager.set_target(value)

app = App()

def initiate():
    app.mainloop()