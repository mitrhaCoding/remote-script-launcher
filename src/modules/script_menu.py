from runtime_state import runtime_state
from modules import executor, view_script
import os



def display_menu():

    print(f"\n Selected target: {runtime_state.target}")
    print(f"\n === Script Menu ===\n")
    get_scripts()
    print(f"\n [0] Back to Main Menu")

    choice = input("\n Select an option: ")

    if choice == "0":

        return

    elif any(script for script in runtime_state.scripts if script.startswith(choice)):

        runtime_state.selected_script = next(script for script in runtime_state.scripts if script.startswith(choice))
        print(f"\n [+] Selected script: {runtime_state.selected_script}")
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

    if choice == "1":

        executor.execute_script()

    elif choice == "2":

        view_script.view_script()

    elif choice == "3":

        print(f"--- Not yet implemented ---")

    elif choice == "0":

        display_menu()

    else:

        print(f"\n [!] Invalid option. Please select a valid option.")



def get_scripts():

    for script in os.listdir(runtime_state.scripts_path):

        if script.endswith(".ps1"):

            print(f" [*] {script}")
            runtime_state.scripts.append(script)

        elif script.endswith(".bat" or ".cmd"):

            print(f" [*] {script}")
            runtime_state.scripts.append(script)