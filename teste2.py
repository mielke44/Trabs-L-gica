from tkinter import *
from tkinter import ttk
import pickle
import os
import subprocess
import sys
import datetime
def NewFile():
    pickling_on = open("Ls.pickle", "wb")
    pickle.dump(ls, pickling_on)
    pickling_on.close()
    #cria no mesmo diretorio do .py

if sys.platform == 'darwin':
    def OpenFile():
        pass
elif sys.platform == 'win32':
    def OpenFile(path):
        subprocess.check_call(['explorer', path])


def SaveData():
    pickling_on = open("Ls.pickle", "wb")
    pickle.dump(ls, pickling_on)
    pickling_on.close()
def SaveDataAs(name):
    pickling_on = open(name, "wb")
    pickle.dump(ls, pickling_on)
    pickling_on.close()
def CallBack():
    pass
def About():
    window = Toplevel(master)
    Lb2 =Label(window, text='This app was made by X\nFor more info, go to Y\nFor contact info with X mail Z')
    Lb2.pack()
def onselect(event):
    w = event.widget
    idx = int(w.curselection()[0])
    value = w.get(idx)
    x=value
    return x
def CreateTab():
    window = Toplevel(master)
    w1 = StringVar()
    e1 = Entry(window, textvariable=w1).pack()
    w1.set('Título')
    s1=w1.get
    tab = ttk.Frame(note)

    note.add(s1,text=s1)
    lb1=Label(s1,text='Custo Atual:    ').grid(row=0,column=0)
    en1=Entry(s1,text='').grid(row=1, column=0)
    lb5=Label(s1,text='Data de pagamento:    ').grid(row=2,column=1)
    en3=Entry(s1,text='').grid(row=3,column=1)


master= Tk()
master.title('Finances App')
master.geometry('800x500')
list_mon = ['Janeiro','Fevereiro']
mylist = []
today = datetime.date.today()
mylist.append(today)

menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label='Open...',)
filemenu.add_separator()
filemenu.add_command(label='Save data',command=SaveData)
filemenu.add_command(label='Save data As...',command=SaveDataAs)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=master.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About...', command=About)

labelframe = LabelFrame(master, text="Mês")
labelframe.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)

note = ttk.Notebook(master)
note.place(x=100,y=300)
b1 = Button(master,text='Criar Aba', command=CreateTab).place(x=600, y=300)

v2 = StringVar()
e2 = Label(master, textvariable=v2,width=10).place(x=680,y=10)
v2.set(mylist[0])
s2 = v2.get()

lbl = Label(master,textvariable=v2).grid(row=0,column=4)
lbl_sal = Label(master,text='Salário:   ').place(x=120,y=10)
lbl_totg = Label(master,text='Total Gasto neste mês:    ').place(x=220,y=10)
lbl_jump = Label(master,text='                  ').grid(row=0,column=4)
lbl_Desc = Label(master,text='Desconto no Salário:  ').grid(row=2,column=2)
lbl_div = Label()

Lb2 = Listbox(labelframe,width=10)
for l in range(0,len(list_mon)):
    Lb2.insert(l,list_mon[l])
Lb2.grid(row=0,column=0)
Lb2.bind('<<ListboxSelect>>', onselect)
mainloop()
