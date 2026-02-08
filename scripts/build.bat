@echo off
SETLOCAL

CALL "%~dp0..\.venv\Scripts\activate.bat"
IF %ERRORLEVEL% NEQ 0 (
    echo [!] Failed to activate virtual environment.
    exit /b 1
)

python -m pip install --upgrade pip
pip install pyinstaller

REM Build executable
pyinstaller --noconfirm --clean --onefile --name remote-script-launcher.exe --paths "%~dp0..\src" "%~dp0..\src\main.py"

ENDLOCAL