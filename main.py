import sys
from modules import interactive_menu

if __name__ == "__main__":

    try:

        interactive_menu.__init__()

    except KeyboardInterrupt:

        print("\n[!] Exiting...")
        sys.exit(0)