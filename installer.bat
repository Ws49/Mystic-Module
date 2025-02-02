@echo off
cls


python --version
if %errorlevel% equ 1 ( 
    echo O python nao esta instalado!
    pause
    exit
)

pip install pyinstaller
pip install pynput
pip install pywin32
pip install requests
pip install pyzipper


move "%~dp0scripts" "C:\mystic_exploit"
setx PATH "%PATH%;C:\mystic_exploit"
pause