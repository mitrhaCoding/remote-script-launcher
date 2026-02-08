from runtime_state import runtime_state
import os

def view_script():

    current_script = os.path.join(runtime_state.scripts_path, runtime_state.selected_script['filename'])

    with open(current_script, 'r') as f:
        script_content = f.read()

    print(script_content)
