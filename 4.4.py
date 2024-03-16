from tkinter import *
root = Tk()
e = Entry(root, width=50,fg='blue', bg='white')
e.pack()
e.insert(0,"Enter:")

def myClick():
    hello = "Hello"+e.get()
    label = Label(root, text= hello, fg='blue', bg='white')
    label.pack()
MButton = Button(root, text="Enter", command=myClick,fg='black', bg='white')
MButton.pack()
root.mainloop()