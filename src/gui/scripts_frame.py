import customtkinter as ctk
from runtime_state import runtime_state
from modules.script_menu import get_scripts

# https://customtkinter.tomschimansky.com/documentation/widgets/frame
# https://customtkinter.tomschimansky.com/tutorial/spinbox
class ScriptObject(ctk.CTkFrame):
    def __init__(self, master, script):
        super().__init__(master, script)
        self.label = script
        self.label.grid(row=0,column=0,pady=0,padx=0)

# https://customtkinter.tomschimansky.com/documentation/widgets/scrollableframe
class ScriptFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text="Script")
        self.label.grid(row=0,column=0,pady=10,padx=20)

        get_scripts(print_items=False)
        
        for script in runtime_state.scripts:
            print(f"Found script as dict: {script}")
            #self.script_o = ScriptObject(script=script)