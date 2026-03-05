import customtkinter as ctk
from tkinter import Tk, ttk
from runtime_state import runtime_state
from pathlib import Path
import os, subprocess

# https://customtkinter.tomschimansky.com/documentation/windows/toplevel
class ScriptsFolder(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self.title("Here are the scripts.")
        
        self.current_path = Path(runtime_state.scripts_path)

        self.path_label = ctk.CTkLabel(self, text=str(self.current_path), anchor="w")
        self.path_label.pack(fill="x",padx=10,pady=(10,5))

        self.tree = ttk.Treeview(self,columns=("type",),show="tree headings")
        self.tree.heading("#0",text="Name")
        self.tree.heading("type",text="Type")
        self.tree.column("type",width=120,anchor="center")
        self.tree.pack(fill="both",expand=True,padx=10,pady=10)

        self.tree.bind("<Double-1>", self.on_button_click)

        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(fill="x",padx=10,pady=(0,10))

        ctk.CTkButton(btn_frame,text="Up",command=self.go_up).pack(side="left",padx=(0,10))
        ctk.CTkButton(btn_frame,text="Open in Explorer",command=self.open_external).pack(side="left")

        self.refresh()

    def refresh(self):
        self.path_label.configure(text=str(self.current_path))
        self.tree.delete(*self.tree.get_children())

        try:
            entries = sorted(self.current_path.iterdir(),key=lambda p: (p.is_file(),p.name.lower()))
            for p in entries:
                kind = "Folder" if p.is_dir() else "File"
                self.tree.insert("","end",iid=str(p),text=p.name,values=(kind,))
        except Exception as e:
            self.tree.insert("","end",text=f"Error: {e}",values=("Error",))

    def go_up(self):
        parent = self.current_path.parent
        if parent != self.current_path:
            self.current_path = parent
            self.refresh()
        
    def open_external(self):
        os.startfile(str(self.current_path))

    def on_button_click(self, _event):
        selected = self.tree.selection()
        if not selected:
            return
        path = Path(selected[0])

        if path.is_dir():
            self.current_path = path
            self.refresh()
        else:
            subprocess.Popen(["notepad.exe", str(path)])
        
    