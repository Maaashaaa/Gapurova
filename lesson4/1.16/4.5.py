from tkinter import *
room = Tk()
room.title("Калькулятор")

def button_click(number)
    global f_num
    global math

e = Entry(room, command = button_click, width=50, fg="black", bg="white", borderwidth=5).grid(row=0, column=0, columnspan=4)


#первая строка
clear = Button(room,command = button_click, text="Очистить", fg="black", bg="white", width=30, height=2).grid(row=1,column=0, padx=1, columnspan=3)
delenie = Button(room, command = button_click, text="/", fg="black", bg="white", width=8, height=2).grid(row=1,column=3, padx=1, pady=5)


#вторая строка
seven = Button(room, command = button_click, text="7",fg="black", bg="white", width=8, height=2).grid(row=2,column=0, padx=1, pady=5)
eight = Button(room, command = button_click, text="8",fg="black", bg="white", width=8, height=2).grid(row=2,column=1, padx=1, pady=5)
nine = Button(room, command = button_click, text="9",fg="black", bg="white", width=8, height=2).grid(row=2,column=2, padx=1, pady=5)
multiply = Button(room, command = button_click, text="*",fg="black", bg="white", width=8, height=2).grid(row=2,column=3, padx=1, pady=5)

#третья строка
four = Button(room, command = button_click, text="4",fg="black", bg="white", width=8, height=2).grid(row=3,column=0, padx=1, pady=5)
five = Button(room, command = button_click, text="5",fg="black", bg="white", width=8, height=2).grid(row=3,column=1, padx=1, pady=5)
six = Button(room, command = button_click, text="6",fg="black", bg="white", width=8, height=2).grid(row=3,column=2, padx=1, pady=5)
minus = Button(room, command = button_click, text="-",fg="black", bg="white", width=8, height=2).grid(row=3,column=3, padx=1, pady=5)

#Четвертая строка
one = Button(room, command = button_click, text="1",fg="black", bg="white", width=8, height=2).grid(row=4,column=0, padx=1, pady=5)
two = Button(room, command = button_click, text="2",fg="black", bg="white", width=8, height=2).grid(row=4,column=1, padx=1, pady=5)
three = Button(room, command = button_click, text="3",fg="black", bg="white", width=8, height=2).grid(row=4,column=2, padx=1, pady=5)
plus = Button(room, command = button_click, text="+",fg="black", bg="white", width=8, height=2).grid(row=4,column=3, padx=1, pady=5)

#Пятая строка
zero = Button(room, command = button_click, text="0", fg="black", bg="white", width=30, height=2).grid(row=5,column=0, padx=1, columnspan=3)
equal = Button(room, command = button_click, text="=", fg="black", bg="white", width=8, height=2).grid(row=5,column=3, padx=1, pady=5)

room.mainloop()