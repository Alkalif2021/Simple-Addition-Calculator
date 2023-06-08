from tkinter import *

root=Tk()

input=Entry(root,width=50)
input.grid(row=0,column=0,columnspan=3,padx=15,pady=15)

def click(num):
    current_n=input.get()
    input.delete(0,END)
    input.insert(0,str(current_n)+str(num))
    return
def addi():
    current_n=input.get()
    global fnum
    fnum=int(current_n)
    input.delete(0,END)
    return
def clear():
    input.delete(0,END)
    return
def equal():
    current_n=input.get()
    sec_n=int(current_n)
    input.delete(0,END)
    input.insert(0,int(fnum+sec_n))
    return

Button_1=Button(root,text='1',bg='antique white',padx=50,pady=25,command=lambda:click(1))
Button_2=Button(root,text='2',bg='antique white',padx=50,pady=25,command=lambda:click(2))
Button_3=Button(root,text='3',bg='antique white',padx=50,pady=25,command=lambda:click(3))
Button_4=Button(root,text='4',bg='antique white',padx=50,pady=25,command=lambda:click(4))
Button_5=Button(root,text='5',bg='antique white',padx=50,pady=25,command=lambda:click(5))
Button_6=Button(root,text='6',bg='antique white',padx=50,pady=25,command=lambda:click(6))
Button_7=Button(root,text='7',bg='antique white',padx=50,pady=25,command=lambda:click(7))
Button_8=Button(root,text='8',bg='antique white',padx=50,pady=25,command=lambda:click(8))
Button_9=Button(root,text='9',bg='antique white',padx=50,pady=25,command=lambda:click(9))
Button_0=Button(root,text='0',bg='antique white',padx=50,pady=25,command=lambda:click(0))
add=Button(root,text='+',bg='antique white',padx=105,pady=25,command=addi)
dele=Button(root,text='AC',bg='antique white',padx=45,pady=25,command=clear)
equ=Button(root,text='=',bg='pale green',padx=105,pady=25,command=equal)

Button_7.grid(row=2,column=0)
Button_8.grid(row=2,column=1)
Button_9.grid(row=2,column=2)

Button_4.grid(row=3,column=0)
Button_5.grid(row=3,column=1)
Button_6.grid(row=3,column=2)

Button_1.grid(row=4,column=0)
Button_2.grid(row=4,column=1)
Button_3.grid(row=4,column=2)


Button_0.grid(row=5,column=0)
add.grid(row=5,column=1,columnspan=2)
dele.grid(row=6,column=0)
equ.grid(row=6,column=1,columnspan=2)


root.mainloop()