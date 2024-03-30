from tkinter import *
root = Tk()
label = Label(root, text='Hello World', fg='blue', bg='white').grid(row=0,column=0)
label2 = Label(root, text='My name Ivan', fg='black', bg='white')
label2.grid(row=1,column=5)
root.configure(bg='blue')
root.mainloop()