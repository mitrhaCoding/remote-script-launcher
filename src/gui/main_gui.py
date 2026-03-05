import customtkinter as ctk
from modules import target_manager
from gui import open_scripts_module, scripts_frame

# https://customtkinter.tomschimansky.com/documentation/windows/window
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("470x365")
        self.title("Remote Script Launcher")
        self.grid_columnconfigure((0), weight=1)

        self.enter = ctk.CTkEntry(self, placeholder_text="IP, enter to confirm")
        self.enter.grid(row=0, column=0, pady=(20,0), padx=20, sticky="ew")
        self.enter.bind("<Return>", self.on_key_pressed)
        self.enter.focus()

        self.script_frame = scripts_frame.ScriptFrame(master=self, width=450, height=200)
        self.script_frame.grid(row=1, column=0, pady=(10,0), padx=20, sticky="ew")
        
        self.open_scripts_folder = ctk.CTkButton(self, 0, text="Open scripts folder", command=self.open_folder)
        self.open_scripts_folder.grid(row=2,column=0,pady=(10,0),padx=20,sticky="ew")

        self.refresh_scripts_button = ctk.CTkButton(self, 0, text="Refresh current scripts", command=self.refresh_scripts)
        self.refresh_scripts_button.grid(row=3,column=0,pady=(10,20),padx=20,sticky="ew")

    def refresh_scripts(self):
        pass

    def on_key_pressed(self, event=None):
        value = self.enter.get()
        target_manager.set_target(value)
    
    def open_folder(self):
        open_scripts_module.ScriptsFolder()

app = App()

def initiate():
    app.mainloop()