from tkinter import *
root = Tk()
def myClick():
    label = Label(root, text='Hello World', fg='blue', bg='white')
    label.pack()
MButton = Button(root, text='My name Ivan', command=myClick,fg='black', bg='white')
MButton.pack()
root.mainloop()