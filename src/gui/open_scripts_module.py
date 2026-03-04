import customtkinter as ctk
from tkinter import Tk
from runtime_state import runtime_state
import os

# https://customtkinter.tomschimansky.com/documentation/windows/toplevel
class ScriptsFolder(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self.title = "Here are the scripts."
        
        root = Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        os.startfile(runtime_state.scripts_path)
        root.destroy()