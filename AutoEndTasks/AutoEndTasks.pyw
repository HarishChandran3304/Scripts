#INSTRUCTIONS
'''
1. Open console, "type pip install -r requirements.txt" and hit enter (Installing required library)
2. In console, type "tasklist" and hit enter
3. Note down the "image names" of all the processes that you want to automatically terminate all instances of
4. Add them to the "termintelist" list on line 20 in the #SETUP section
5. Modify the hotkey combination according to your need by changing the "hotkey" list on line 21 in the #SETUP section
6. Right click on the ".pyw" file => Send to => Desktop (Create shortcut)
7. Go to desktop, find the shortcut, drag and drop into this folder: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" (Program auto starts every time PC boots)
8. Done! Use the hotkey (alt + e by default) whenever you wish to activate the script
'''


#IMPORTS
import os
import keyboard


#SETUP
terminatelist = ["Spotify.exe"] # Process Image Names as strings [Use "tasklist" in shell to find it]
hotkey = ["alt", "e"] # Alt + e by default


#HELPER FUNCTION
def terminate(tasklist):
    for process in tasklist:
        while True:
            if os.system(f'cmd /c "Taskkill /IM {process} /F"'):
                break


#MAIN
def main(hotkey, tasklist):
    while True:
        if keyboard.is_pressed(hotkey):
            terminate(tasklist)


#MAIN CALL
if __name__ == "__main__":
    main(hotkey, terminatelist)
