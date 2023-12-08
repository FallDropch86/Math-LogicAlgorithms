import win32ui
import win32con
import time
import sys

global zero
global one
global two
global three
global four
global five
global six
global seven
global eight
global nine

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

try:
    num = str(input("Input integer or decimal: "))

    for _ in num:
        if _ == "0":
            zero +=1
    
    print(f"Number of 0s: {zero}")

    for _ in num:
        if _ == "1":
            one +=1
    
    print(f"Number of 1s: {one}")

    for _ in num:
        if _ == "2":
            two +=1
    
    print(f"Number of 2s: {two}")

    for _ in num:
        if _ == "3":
            three +=1
    
    print(f"Number of 3s: {three}")

    for _ in num:
        if _ == "4":
            four +=1
    
    print(f"Number of 4s: {four}")

    for _ in num:
        if _ == "5":
            five +=1
    
    print(f"Number of 5s: {five}")

    for _ in num:
        if _ == "6":
            six +=1
    
    print(f"Number of 6s: {six}")

    for _ in num:
        if _ == "7":
            seven +=1
    
    print(f"Number of 7s: {seven}")

    for _ in num:
        if _ == "8":
            eight +=1
    
    print(f"Number of 8s: {eight}")

    for _ in num:
        if _ == "9":
            nine +=1
    
    print(f"Number of 9s: {nine}")
    
    time.sleep(1000)

except Exception as e:
    print(f"{e}")
    displaymsg = "Error: not a valid integer or decimal, perhaps maybe you are using a value that is incorrect?"
    title = "Error detected, failed to calculate number of number:"
    options = win32con.MB_OK
    icon = win32con.MB_ICONERROR
    errordisplay = win32ui.MessageBox(displaymsg, title, icon | options)
    if errordisplay == win32con.IDOK:
        sys.exit(0)
