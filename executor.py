from runtime_state import runtime_state
import subprocess

def execute_script():

    script = runtime_state.selected_script
    target = runtime_state.target

    if script.endswith(".bat" or ".cmd"):

        copy_command = f"copy {runtime_state.scripts_path}\\{script} \\\\{target}\\C$\\Windows\\System32"
        execute_command = f"psexec -nobanner \\\\{target} {script}"
        delete_command = f"del \\\\{target}\\C$\\Windows\\System32\\{script}"

        try:
            
            print(f"Copying script to target...")
            subprocess.run(copy_command, shell=True, check=True)
            print(f"Success.")
            
            print(f"Executing script on target...")
            subprocess.run(execute_command, shell=True, check=True)
            print(f"\nSuccess.")

            print(f"\nDeleting script from target...")
            subprocess.run(delete_command, shell=True, check=True)
            print(f"\nSuccess.")

        except subprocess.CalledProcessError as e:

            print(f"\n [!] An error occurred while executing the script: {e}")
