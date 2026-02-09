import sys
from modules import interactive_menu, dependencies_check

if __name__ == "__main__":

    try:

        dependencies_check.check_psexec(raise_on_missing=True)

        interactive_menu.__init__()

    except KeyboardInterrupt:

        print("\n [!] Exiting...")
        sys.exit(0)