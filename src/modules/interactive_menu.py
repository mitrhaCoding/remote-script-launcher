from modules import target_manager, script_menu
from runtime_state import runtime_state

def __init__():

    while True:

        print(f"\n === Remote Script Launcher ===")
        print(f"\n [1] Set Target")
        print(f" [2] Select Script")
        print(f" [0] Exit")

        choice = input("\n Select an option: ")

        if choice == "1":

            target_manager.set_target(input(" Enter target IP address: "))

        elif choice == "2":

            if runtime_state.target is None:

                print("\n [!] Please set a target before selecting a script.")
                continue

            script_menu.display_menu()

        elif choice in runtime_state.go_back:

            print("\n[!] Exiting...")
            break

        else:

            print("\n[!] Invalid option. Please select a valid option.")