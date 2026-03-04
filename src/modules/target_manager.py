import ipaddress
from runtime_state import runtime_state



def set_target(value):

    if validate_target(value):

        print(f"[+] Target set to: {value}")
        runtime_state.target = value
        return True
    
    print(f"[!] Failed to set target.")
    return False



def validate_target(input):

    try:

        ipaddress.ip_address(input)
        return True
    
    except ValueError:

        print(f"[!] Invalid IP address. Please enter a valid IP address.")
        return None