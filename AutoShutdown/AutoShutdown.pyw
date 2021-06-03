#INSTRUCTIONS
'''
1. Open console, "type pip install -r requirements.txt" and hit enter (Installing required library)
2. Fill in the shutdown timings for each day in the #SETUP section and save the file
3. Right click on the ".pyw" file => Send to => Desktop (Create shortcut)
4. Go to desktop, find the shortcut, drag and drop into this folder: "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp" (Program auto starts every time PC boots)
5. Done! Your PC will automatically shutdown at the specified times from here on
'''


#IMPORTS
import os
import schedule


#SETUP
'''
Enter the shutdown time for each day in the format {"HH:MM"} else leave it empty {""} to not auto-shutdown on a particular day.
'''
mon_shutdown_time = ""
tue_shutdown_time = ""
wed_shutdown_time = ""
thu_shutdown_time = ""
fri_shutdown_time = ""
sat_shutdown_time = ""
sun_shutdown_time = ""


#HELPER FUNCTIONS
def shutdown():
    os.system("shutdown /s /t 1")


#MAIN
def main():
    if mon_shutdown_time:
        schedule.every().monday.at(mon_shutdown_time).do(shutdown)
    if tue_shutdown_time:
        schedule.every().tuesday.at(tue_shutdown_time).do(shutdown)
    if wed_shutdown_time:
        schedule.every().wednesday.at(wed_shutdown_time).do(shutdown)
    if thu_shutdown_time:
        schedule.every().thursday.at(thu_shutdown_time).do(shutdown)
    if fri_shutdown_time:
        schedule.every().friday.at(thu_shutdown_time).do(shutdown)
    if sat_shutdown_time:
        schedule.every().saturday.at(sat_shutdown_time).do(shutdown)
    if sun_shutdown_time:
        schedule.every().sunday.at(sun_shutdown_time).do(shutdown)


#MAIN CALL
if __name__ == "__main__":
    main()