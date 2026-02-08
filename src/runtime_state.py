import os

if not os.path.exists(f"{os.getenv('LOCALAPPDATA')}\\RemoteScriptLauncher\\scripts"):
    os.makedirs(f"{os.getenv('LOCALAPPDATA')}\\RemoteScriptLauncher\\scripts")


class RuntimeState:
    def __init__(self):
        self.target = "127.0.0.1"
        self.selected_script = {"filename": str, "index": int}
        self.scripts = []
        self.scripts_path = f"{os.getenv('LOCALAPPDATA')}\\RemoteScriptLauncher\\scripts"
        self.executes = ["execute", "exec", "run", "start", "e", "1"]
        self.views = ["view", "content", "cat", "type", "v", "3"]
        self.deletes = ["delete", "del", "remove", "rm", "d", "4"]
        self.go_back = ["back", "b", "0", "exit", "quit", "q"]

runtime_state = RuntimeState()