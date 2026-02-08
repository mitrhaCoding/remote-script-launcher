from runtime_state import runtime_state
import os

def delete_script():
    try:
        os.remove(os.path.join(runtime_state.scripts_path, runtime_state.selected_script["filename"]))
    except FileNotFoundError:
        print(f"\n [!] File not found: {runtime_state.selected_script['filename']}")
    except PermissionError:
        print(f"\n [!] Permission denied: {runtime_state.selected_script['filename']}")
    except Exception as e:
        print(f"\n [!] An error occurred while deleting the file: {e}")