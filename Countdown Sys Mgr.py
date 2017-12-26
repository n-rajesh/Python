"""
This is a program to perform hibernate,shutdown or restart after the specified countdown time.
Use powercfg /h on in Command prompt to enable hibernation. Replace on with off to disable it.
"""

import msvcrt
import os
import time

print(__doc__)

t = 1
c = int(input('\t1-Hibernate 2-Shutdown 3-Restart 4-Exit.Enter the desired option '))
if c == 4:
    quit()

m = int(input('\tEnter countdown time in minutes '))

for i in range(m * 60, 0, -1):
    os.system('cls')
    print(i, "seconds remaining.Press any key to cancel.")
    time.sleep(1)

    if msvcrt.kbhit():
        os.system('cls')
        print("Task Cancelled")
        t = 0
        break

if t != 0:
    if c == 1:
        os.system('cls')
        os.system("shutdown /h")
    elif c == 2:
        os.system("shutdown /s")
    else:
        os.system("shutdown /r")
    print("Press any key to abort")
    if msvcrt.kbhit():
        os.system("shutdown /a")
        print("Task Cancelled")

msvcrt.getch().decode()
time.sleep(3)
os.system('cls')
quit()
