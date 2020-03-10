from Tkinter import *
root=Tk()
root.title("welcome to PhoneBook")
root.geometry("800x800")
root.config(bg='light blue')
Label(root,text='Project title : PhoneBook',font='arial 18 bold',bg='light blue').grid(row=0,column=0)
Label(root,text='Project of Python and database',font='verdana 18 bold underline',bg='light blue').grid(row=3,column=0)
Label(root,text='Developed By: Vineet Raj Parashar',foreground='blue',font='Arial 16',bg='light blue').grid(row=4,column=0)
Label(root,text='Enrollment no: 181B242',foreground='blue',font='Arial 16',bg='light blue').grid(row=5,column=0)

Label(root,text='---------------------------------',foreground='red',font='16',bg='light blue').grid(row=6,column=0)
Label(root,text='',bg='light blue').grid(row=7)
Label(root,text='!!!"Make a mouse movement over this screen to close"!!!',foreground='red',bg='light blue',font='15').grid(row=8,column=0) 
i=PhotoImage(file='pblogo.gif')
Label(root,image=i).grid(row=9,column=0)
def close(e=1):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()
