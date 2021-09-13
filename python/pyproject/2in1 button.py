from tkinter import *
def prnt():
    print("hi")
def ext():
    root.destroy()
root=Tk()
button=Button(root,text="hi",command=lambda:[prnt(), ext()])
button.pack()
root.mainloop()
