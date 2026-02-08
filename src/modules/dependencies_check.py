import shutil
import sys


PS_EXEC_DOWNLOAD = "https://learn.microsoft.com/en-us/sysinternals/downloads/psexec"
SYSINTERNALS_SUITE = "https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite"
PYTHON_DOWNLOAD = "https://www.python.org/downloads/"


def find_psexec() -> str | None:
    """
    Return the full path to psexec if found in PATH, otherwise None.
    """
    # try common executable names
    for name in ("psexec.exe", "psexec"):
        path = shutil.which(name)
        if path:
            return path
    return None


def check_psexec(raise_on_missing: bool = False) -> bool:
    """
    Check for PsExec availability. If missing, print download links.
    Returns True if found, False otherwise. If raise_on_missing is True, raises SystemExit(1).
    """
    if sys.platform.startswith("win"):
        path = find_psexec()
        if path:
            return True
        msg = (
            "PsExec was not found in PATH.\n"
            f"Download PsExec: {PS_EXEC_DOWNLOAD}\n"
            f"Or get the full Sysinternals Suite: {SYSINTERNALS_SUITE}"
        )
        print(msg)
        if raise_on_missing:
            raise SystemExit(1)
        return False
    else:
        print("PsExec is a Windows utility; skipping check on non-Windows platform.")
        return False


def find_python() -> str | None:
    """
    Return the full path to a Python interpreter if found in PATH, otherwise None.
    """
    for name in ("python", "python3"):
        path = shutil.which(name)
        if path:
            return path
    return None


def check_python(raise_on_missing: bool = False) -> bool:
    """
    Check for a Python interpreter on PATH. If missing, print download link.
    Returns True if found, False otherwise. If raise_on_missing is True, raises SystemExit(1).
    """
    path = find_python()
    if path:
        return True
    msg = (
        "Python interpreter was not found in PATH.\n"
        f"Download Python: {PYTHON_DOWNLOAD}"
    )
    print(msg)
    if raise_on_missing:
        raise SystemExit(1)
    return False