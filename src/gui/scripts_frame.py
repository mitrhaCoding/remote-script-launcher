import customtkinter as ctk
from runtime_state import runtime_state
from modules.script_menu import get_scripts
from modules import executor, script_analyzer

# https://customtkinter.tomschimansky.com/documentation/widgets/frame
# https://customtkinter.tomschimansky.com/tutorial/spinbox
class ScriptObject(ctk.CTkFrame):
    def __init__(self, master, script, on_delete=None, on_launch=None):
        super().__init__(master)

        self.script = script
        self.on_delete = on_delete
        self.on_launch = on_launch

        # https://customtkinter.tomschimansky.com/documentation/widgets/label
        self.label = ctk.CTkLabel(self,text=script["filename"])
        self.label.grid(row=0,column=0,pady=0,padx=0,sticky="w")
        self.grid_columnconfigure(0, weight=1)

        # https://customtkinter.tomschimansky.com/documentation/widgets/button    
        self.launch_button = ctk.CTkButton(
            self,
            text="Launch",
            command=self._launch_command,
            width=0
        )
        self.launch_button.grid(row=0,column=1,pady=0,padx=5)

        # https://customtkinter.tomschimansky.com/documentation/widgets/button
        self.delete_button = ctk.CTkButton(
            self,
            text="Delete",
            command=self._delete_command,
            width=0
        )
        self.delete_button.grid(row=0,column=2,pady=0,padx=5)

    def _delete_command(self):
        if callable(self.on_delete):
            self.on_delete(self.script)

    def _launch_command(self):
        if callable(self.on_launch):
            self.on_launch(self.script)

class ArgBox(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x150")

        self.arguments = ctk.CTkEntry(self, placeholder_text="Arguments:")

# https://customtkinter.tomschimansky.com/documentation/widgets/scrollableframe
class ScriptFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text="Script")
        self.label.grid(row=0,column=0,pady=10,padx=20)

        get_scripts(print_items=False)
        
        for row, script in enumerate(runtime_state.scripts):
            if isinstance(script, str):
                script = {"filename": script, "index": row}

            script_box = ScriptObject(
                self,
                script=script,
                on_delete=self.handle_delete_button,
                on_launch=self.handle_launch_button
            )
            script_box.grid(row=row+1,column=0,padx=5,pady=5,sticky="ew")

        self.grid_columnconfigure(0, weight=1)

    def handle_launch_button(self,script):
        print(f"Issued launch request for {script["filename"]}")
        script_info = script_analyzer.get_script_info(script['filename'])
        requires_args = script_info['requires_args']

        if requires_args:
            pass
        
    def handle_delete_button(self,script):
        print(f"Issued delete request for {script["filename"]}")
    