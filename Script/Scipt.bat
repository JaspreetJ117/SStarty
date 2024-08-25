@echo off
start "" "C:\Program Files (x86)\Steam\steam.exe"
TIMEOUT /T 10
TASKLIST | FINDSTR steamwebhelper.exe && start "" "C:\Users\jaspr\Documents\SStarty\Script\Main.py"
exit
