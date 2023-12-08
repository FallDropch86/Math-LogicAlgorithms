# Simple Calculator app in Python

from tkinter import *

# App Config

root = Tk()
root.title("Simple calculator app in Python")
root.geometry("400x400")
root.config(bg="Black")
root.resizable(False, False)

# App functionality

ResultVal = 0

def AddBtnFunc():
    num1Val = FirstNum_TextEntry.get()
    try:
        num1 = int(num1Val)
    except ValueError:
        try:
            num1 = float(num1Val)

        except ValueError:
            num1 = None

    num2Val = SecondNum_TextEntry.get()
    try:
        num2 = int(num2Val)
    except ValueError:
        try:
            num2 = float(num2Val)
        except ValueError:
            num2 = None
    
    ResultVal = num1 + num2
    Result_Label.config(text = f"Result = {ResultVal}")

def SubBtnFunc():
    num1Val = FirstNum_TextEntry.get()
    try:
        num1 = int(num1Val)
    except ValueError:
        try:
            num1 = float(num1Val)

        except ValueError:
            num1 = None

    num2Val = SecondNum_TextEntry.get()
    try:
        num2 = int(num2Val)
    except ValueError:
        try:
            num2 = float(num2Val)
        except ValueError:
            num2 = None
    
    ResultVal = num1 - num2
    Result_Label.config(text = f"Result = {ResultVal}")

def MultBtnFunc():
    num1Val = FirstNum_TextEntry.get()
    try:
        num1 = int(num1Val)
    except ValueError:
        try:
            num1 = float(num1Val)

        except ValueError:
            num1 = None

    num2Val = SecondNum_TextEntry.get()
    try:
        num2 = int(num2Val)
    except ValueError:
        try:
            num2 = float(num2Val)
        except ValueError:
            num2 = None
    
    ResultVal = num1 * num2
    Result_Label.config(text = f"Result = {ResultVal}")

def DivideBtnFunc():
    num1Val = FirstNum_TextEntry.get()
    try:
        num1 = int(num1Val)
    except ValueError:
        try:
            num1 = float(num1Val)

        except ValueError:
            num1 = None

    num2Val = SecondNum_TextEntry.get()
    try:
        num2 = int(num2Val)
    except ValueError:
        try:
            num2 = float(num2Val)
        except ValueError:
            num2 = None
    
    ResultVal = num1 / num2
    print(ResultVal)
    Result_Label.config(text = f"Result = {ResultVal}")

# Design

FirstNum_Label = Label(root, text="Enter first number : ", bg="Black", fg="White", 
                    font=("Cambria", 14))
FirstNum_Label.place(x=10, y=10)

FirstNum_TextEntry = Entry(root, fg="White", bg="#242424", font=("Cambria", 14), 
                        width=19)
FirstNum_TextEntry.place(x=180, y=10)

SecondNum_Label = Label(root, text="Enter second number : ", bg="Black", fg="White", 
                    font=("Cambria", 14))
SecondNum_Label.place(x=10, y=50)

SecondNum_TextEntry = Entry(root, fg="White", bg="#242424", font=("Cambria", 14), 
                        width=17)
SecondNum_TextEntry.place(x=204, y=50)

Ask_Label = Label(root, text="What would you like to do?", fg="White", bg="Black", 
                font=("Script MT Bold", 20))
Ask_Label.place(x=50, y=140)

Add_Button = Button(root, text="Add", fg="White", bg="#242424", font=("Script MT Bold", 20), 
                    command=AddBtnFunc)
Add_Button.place(x=11, y=200, width=70, height=70)

Sub_Button = Button(root, text="Subtract", fg="White", bg="#242424", font=("Script MT Bold", 20), 
                    command=SubBtnFunc)
Sub_Button.place(x=81, y=200, width=100, height=70)

Mult_Button = Button(root, text="Multiply", fg="White", bg="#242424", font=("Script MT Bold", 20), 
                    command=MultBtnFunc)
Mult_Button.place(x=181, y=200, width=105, height=70)

Divide_Button = Button(root, text="Divide", fg="White", bg="#242424", font=("Script MT Bold", 20), 
                    command=DivideBtnFunc)
Divide_Button.place(x=287, y=200, width=100, height=70)

Result_Label = Label(root, text=f"Result = {ResultVal}", fg="White", bg="Black", 
                font=("Courier New", 20))
Result_Label.place(x=50, y=300)

root.mainloop()
root.quit