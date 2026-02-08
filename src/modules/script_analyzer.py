import re
import os
from runtime_state import runtime_state

def requires_arguments(script_filename):
    """
    Analyzes a script file to determine if it requires arguments.
    
    Returns:
        bool: True if the script requires arguments, False otherwise
    """
    script_path = os.path.join(runtime_state.scripts_path, script_filename)
    
    try:
        with open(script_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Warning: Could not read {script_filename}: {e}")
        return False
    
    if script_filename.endswith('.ps1'):
        return _check_powershell_args(content)
    elif script_filename.endswith('.bat') or script_filename.endswith('.cmd'):
        return _check_batch_args(content)
    
    return False


def _check_powershell_args(content):
    """
    Checks if a PowerShell script uses arguments.
    Looks for:
    - param() blocks
    - $args variable usage
    - $PSBoundParameters
    """
    # Check for param block (case insensitive)
    if re.search(r'\bparam\s*\(', content, re.IGNORECASE):
        return True
    
    # Check for $args usage (not in comments)
    lines = content.split('\n')
    for line in lines:
        # Skip comment lines
        if line.strip().startswith('#'):
            continue
        # Check for $args usage
        if re.search(r'\$args\b', line, re.IGNORECASE):
            return True
        # Check for $PSBoundParameters
        if re.search(r'\$PSBoundParameters\b', line, re.IGNORECASE):
            return True
    
    return False


def _check_batch_args(content):
    """
    Checks if a batch script uses arguments.
    Looks for:
    - %1, %2, ... %9 (positional parameters)
    - %* (all parameters)
    - %~1, %~2, etc. (parameter modifiers)
    """
    # Remove comment lines (lines starting with REM or ::)
    lines = content.split('\n')
    code_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith('REM ') and not stripped.startswith('::'):
            code_lines.append(line)
    
    code = '\n'.join(code_lines)
    
    # Check for %1 through %9 (with optional modifiers like %~1)
    if re.search(r'%~?[1-9]\b', code):
        return True
    
    # Check for %* (all parameters)
    if '%*' in code:
        return True
    
    return False


def get_script_info(script_filename):
    """
    Returns a dictionary with information about a script.
    
    Returns:
        dict: Contains 'requires_args' boolean and 'arg_indicator' string
    """
    requires_args = requires_arguments(script_filename)
    
    return {
        'requires_args': requires_args,
        'arg_indicator': '[ARGS]' if requires_args else ''
    }
