import os

class RuntimeState:
    def __init__(self):
        self.target = "127.0.0.1"
        self.selected_script = None
        self.scripts = []
        self.scripts_path = f"{os.getenv('LOCALAPPDATA')}\\RemoteScriptLauncher\\scripts"

runtime_state = RuntimeState()