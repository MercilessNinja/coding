from tkinter import *

root=Tk()
root.title("hello")
label1=Label(root,text="hello world").pack()
ent1=Entry(root).pack()
button1=Button(root,text="exit",command=root.destroy).pack()
root.mainloop()
