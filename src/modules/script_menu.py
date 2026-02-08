from runtime_state import runtime_state
from modules import executor, view_script, load_scripts, delete_script
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

    print(f"\n Selected target: {runtime_state.target}")
    print(f"\n === Script Menu ===\n")
    get_scripts()
    print(f"\n [load] Load additional scripts")
    print(f" [exit] Back to Main Menu")

    choice = input("\n Select an option: ")

    if choice == "exit":

        return

    elif choice == "load":

        load_scripts.load_scripts()
        get_scripts()

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

    print(f" [1] Execute script")
    print(f" [2] View script content")
    print(f" [3] Delete script")
    print(f" [0] Back to Script Menu")

    choice = input("\n Select an option: ")

    if choice in executes:

        executor.execute_script()

    elif choice in views:

        view_script.view_script()

    elif choice in deletes:

        delete_script.delete_script()

    elif choice in backs:

        display_menu()

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

            print(f" [{indexed_script['index']}] {indexed_script['filename']}")
            runtime_state.scripts.append(indexed_script)



def assign_file_index(input, index) -> FileIndex:
    return FileIndex(index=index, filename=input)