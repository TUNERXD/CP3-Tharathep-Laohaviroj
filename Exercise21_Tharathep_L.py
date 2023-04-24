from tkinter import *
import math

#อ้วนมาก 30.0 ขึ้นไป
#น้ำหนักเกิน 23.0 - 24.9
#น้ำหนักปกติ เหมาะสม 18.6 - 22.9
#ผอมเกินไป น้อยกว่า 18.5

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))

    bmiResult = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)

    numresult.configure(text =float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))

    if bmiResult <= 18.5:
        textresult.configure(text="ผอมเกินไป",fg="Yellow")
    elif bmiResult <= 22.9:
        textresult.configure(text="น้ำหนักปกติ, เหมาะสม",fg="Green")
    elif bmiResult <= 24.9:
        textresult.configure(text="น้ำหนักเกิน",fg="Orange")
    elif bmiResult <= 29.9:
        textresult.configure(text="อ้วน",fg="Red")
    elif bmiResult >= 30.0:
        textresult.configure(text="อ้วนมาก")


MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวน",)
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=3, column=0)

result = Label(MainWindow, text="ผลลัพธ์:",fg="Blue")
result.grid(row=2,column=1)

numresult = Label(MainWindow, text=" ")
numresult.grid(row=3,column=1)

textresult = Label(MainWindow, text = " ")
textresult.grid(row=4,column=1)

MainWindow.mainloop()