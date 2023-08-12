from tkinter import *
from tkcalendar import *
root = Tk()


def selectDate():
    myDate=mycal.get_date()
    selectDate=Label(text=myDate)
    selectDate.pack(padx=2,pady=2)


mycal=Calendar(root,setmode="Day",date_pattern="dd/mm/yyyy")
mycal.pack(padx=15,pady=15)


b1=Button(root,text="Select Date",command=selectDate)
b1.pack(padx=15,pady=15)


root.geometry("300x300")
root.title("Calendar")
root.configure(bg="yellow")
root.mainloop()