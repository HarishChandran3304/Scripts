<h1 align="center">AutoClearTemp</h1>

## About

A script for Windows to automatically terminate all instances of certain processes with the press of a hotkey

## Instructions

1. Open console, "type pip install -r requirements.txt" and hit enter (Installing required library)
2. In console, type "tasklist" and hit enter
3. Note down the "image names" of all the processes that you want to automatically terminate all instances of
4. Add them to the "termintelist" list on line 20 in the #SETUP section
5. Modify the hotkey combination according to your need by changing the "hotkey" list on line 21 in the #SETUP section
6. Right click on the ".pyw" file => Send to => Desktop (Create shortcut)
7. Go to desktop, find the shortcut, drag and drop into this folder: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" (Program auto starts every time PC boots)
8. Done! Use the hotkey (alt + e by default) whenever you wish to activate the script
