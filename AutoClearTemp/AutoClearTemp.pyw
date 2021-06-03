#INSTRUCTIONS:
'''
1) Open console, "type pip install -r requirements.txt" and hit enter (Installing required library)
2) Change the name of user by changing the username variable (Make sure it is a string!) on line 18 in the #SETUP section
3) Right click on the ".pyw" file => Send to => Desktop (Create shortcut) 
4) Go to desktop, find the shortcut, drag and drop into this folder: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" (Program auto starts every time PC boots)
5) Done!
'''


#IMPORTS
import os
import winshell
import shutil


#SETUP
username = ""
temp1path = "C:\\Windows\\Temp"
temp2path = f'C:\\Users\\{username}\\AppData\\Local\\Temp'


#HELPER FUNCTIONS
def cleartemp1():
    '''
    Clears the files in the first temporary file dump location
    '''
    for file in os.listdir(temp1path):
        if os.path.isfile(f"{temp1path}\\{file}"):
            try:
                os.remove(f"{temp1path}\\{file}")
            except:
                pass
        elif os.path.isdir(f"{temp1path}\\{file}"):
            try:
                shutil.rmtree(f"{temp1path}\\{file}")
            except:
                pass

def cleartemp2():
    '''
    Clears the files in the second temporary file dump location
    '''
    for file in os.listdir(temp2path):
        if os.path.isfile(f"{temp2path}\\{file}"):
            try:
                os.remove(f"{temp2path}\\{file}")
            except:
                pass
        elif os.path.isdir(f"{temp2path}\\{file}"):
            try:
                shutil.rmtree(f"{temp2path}\\{file}")
            except:
                pass

def clearrecyclebin():
    '''
    Clears the recycle bin
    '''
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except:
        pass


#MAIN
def main():
    cleartemp1()
    cleartemp2()
    # Comment out the next line if you dont want the recycle bin to be cleared!
    clearrecyclebin()


#MAIN CALL
if __name__ == "__main__":
    main()