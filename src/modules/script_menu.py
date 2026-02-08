from tkinter import Tk
from runtime_state import runtime_state
from modules import executor, view_script, load_scripts, delete_script, script_analyzer
import os
from dataclasses import dataclass

@dataclass
class FileIndex:
    index : int
    filename : str



executes = runtime_state.executes
views = runtime_state.views
deletes = runtime_state.deletes
backs = runtime_state.go_back



def display_menu():

    while True:

        print(f"\n === Script Menu ===\n")
        print(f" Selected target: {runtime_state.target}\n")
        get_scripts()
        print(f"\n [l] Load additional scripts")
        print(f" [o] Open scripts folder")
        print(f" [q] Back to Main Menu")

        choice = input("\n Select an option: ")

        if choice in backs:

            break

        elif choice in ["load", "l"]:

            load_scripts.load_scripts()
            get_scripts()

        elif choice in ["open", "o"]:

            print(f"\n Opening scripts folder...")
            # let's open it and bring it to the front
            root = Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            os.startfile(runtime_state.scripts_path)
            root.destroy()

        elif any(script for script in runtime_state.scripts if script["filename"].startswith(choice)):

            runtime_state.selected_script = next(script for script in runtime_state.scripts if script["filename"].startswith(choice))
            print(f"\n [+] Selected script: {runtime_state.selected_script['filename']}")
            print(f"\n What to do with the selected script?\n")
            script_choice()

        elif choice in [str(script["index"]) for script in runtime_state.scripts]:

            runtime_state.selected_script = next(script for script in runtime_state.scripts if str(script["index"]) == choice)
            print(f"\n [+] Selected script: {runtime_state.selected_script['filename']}")
            print(f"\n What to do with the selected script?\n")
            script_choice()


        else:

            print(f"\n [!] Invalid option. Please select a valid option.")



def script_choice():

    script_info = script_analyzer.get_script_info(runtime_state.selected_script['filename'])
    requires_args = script_info['requires_args']
    
    while True:

        print(f" [1] Execute script")
        if requires_args:
            print(f" [2] Execute script with arguments (recommended)")
        else:
            print(f" [2] Execute script with arguments")
        print(f" [3] View script content")
        print(f" [4] Delete script")
        print(f" [q] Back to Script Menu")

        choice = input("\n Select an option: ")

        if choice in executes:

            if requires_args:
                print(f"\n [!] Warning: This script appears to require arguments.")
                confirm = input(" Execute without arguments anyway? (y/n): ")
                if confirm.lower() not in ['y', 'yes']:
                    continue
            
            executor.execute_script()
            break

        elif choice in ["execute with arguments", "exec with arguments", "run with arguments", "start with arguments", "e with arguments", "2"]:

            arguments = input("\n Enter arguments to pass to the script: ")
            executor.execute_script_with_arguments(arguments)
            break

        elif choice in views:

            view_script.view_script()

        elif choice in deletes:

            delete_script.delete_script()

        elif choice in backs:

            break

        else:

            print(f"\n [!] Invalid option. Please select a valid option.")



def get_scripts():

    if not os.listdir(runtime_state.scripts_path):

        print(f" [!] No scripts found.")
        return

    for index, script in enumerate(os.listdir(runtime_state.scripts_path)):

        indexed_script = {"filename": script, "index": index + 1}
        indexed_script["filename", "index"] = assign_file_index(script, index + 1)

        if script.endswith(".bat") or script.endswith(".cmd") or script.endswith(".ps1"):

            script_info = script_analyzer.get_script_info(script)
            arg_indicator = f" {script_info['arg_indicator']}" if script_info['arg_indicator'] else ""
            
            print(f" [{indexed_script['index']}] {indexed_script['filename']}{arg_indicator}")
            runtime_state.scripts.append(indexed_script)



def assign_file_index(input, index) -> FileIndex:
    return FileIndex(index=index, filename=input)