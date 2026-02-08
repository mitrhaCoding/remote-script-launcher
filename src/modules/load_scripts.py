import shutil, os
from runtime_state import runtime_state
from tkinter import Tk, filedialog

def load_scripts():

    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    files = filedialog.askopenfilenames(title="Select script files", filetypes=[("scripts", "*.bat"), ("scripts", "*.cmd"), ("scripts", "*.ps1")], initialdir=os.path.join(os.getenv('USERPROFILE'), 'Downloads'))

    if not files:
        print(f"\n [!] No files selected. Returning to Script Menu.\n")
        root.destroy()
        return

    for file in files:

        print(f"Loading {file}...")
        try:
            shutil.copy(file, runtime_state.scripts_path)
            print(f"Success.")
        except Exception as e:
            print(f"Failed: {e}")

    root.destroy()
