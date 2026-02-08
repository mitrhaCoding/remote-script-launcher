:: filepath: setup.bat
@echo off
SETLOCAL

:: 1. Checking for python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo '[!] Python is not installed. Please install Python 3.12.3 ^(or newer^) from https://www.python.org/downloads/.'
    echo     During installation make sure to check the box "Add Python to PATH".
    pause
    exit /b 1
)
echo [+] Python is installed.

:: 2. Setting up virtual environment
IF EXIST "%~dp0..\.venv" (
    echo [+] Virtual environment already exists.
) ELSE (
    echo [+] Creating virtual environment...
    python -m venv "%~dp0..\.venv"
    IF ERRORLEVEL 1 (
        echo [!] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo [+] Virtual environment created.
)

:: 3. Activating virtual environment
echo [+] Activating virtual environment...
CALL "%~dp0..\.venv\Scripts\activate.bat"
IF %ERRORLEVEL% NEQ 0 (
    echo [!] Failed to activate virtual environment.
    pause
    exit /b 1
)
echo [+] Virtual environment activated.

echo.
echo === Setup Complete ===
ENDLOCAL