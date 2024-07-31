from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
            screen.update()
        except Exception as e:
            scvalue.set("Error")
            screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root =Tk()

root.geometry("444x644")
root.title("Calculator")
scvalue=StringVar()
scvalue.set("")
screen= Entry(root,textvar=scvalue,font=" lucida 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f1= Frame(root,bg="grey")
b=Button(f1,text="9", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5) 
b.bind("<Button-1>", click)
b=Button(f1,text="8", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="7", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f1.pack()

f1= Frame(root,bg="grey")
b=Button(f1,text="6", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5) 
b.bind("<Button-1>", click)
b=Button(f1,text="5", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="4", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f1.pack()

f1= Frame(root,bg="grey")
b=Button(f1,text="3", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5) 
b.bind("<Button-1>", click)
b=Button(f1,text="2", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="1", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f1.pack()

f1= Frame(root,bg="grey")
b=Button(f1,text="0", padx=29,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5) 
b.bind("<Button-1>", click)
b=Button(f1,text="-", padx=29,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="*", padx=30,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f1.pack()

f1= Frame(root,bg="grey")
b=Button(f1,text="/", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5) 
b.bind("<Button-1>", click)
b=Button(f1,text="%", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="=", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f1.pack()

f1= Frame(root,bg="grey")
b=Button(f1,text="C", padx=28,pady=18,font="lucida,35,bold")
b.pack(side=LEFT,padx=5,pady=5) 
b.bind("<Button-1>", click)

f1.pack()
root.mainloop()