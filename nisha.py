from tkinter import*
top=Tk()
top.geometry("500x200")
top['bg']="#51E1DC"
label=Label(top,text="First Number",).place(x=50,y=50)
ent=Entry(top).place(x=150,y=50)
top.mainloop()