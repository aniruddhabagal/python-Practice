from tkinter import *

def callback():
    print('You clicked the button!')
    value=E1.get()
    a=value.split();
    print(a)
    for q in range(len(a)):
        l4=Label(top,bg='red',text=a[q],width=10,height=4).grid(row=6,column=q,padx=50,pady=10)
                
    for i in range(len(a)):
        minm=1
        for j in range(i+1,len(a)):
            if(a[minm]>a[j]):
                minm=j;
        a[i],a[minm]=a[minm],a[i]
        for k in range(len(a)):
            print(a)
            l3=Label(top,bg='#3754B0',text=a[k],width=10,height=4).grid(row=i+7,column=k,padx=50,pady=10)
    
#     heading=Label(top,text="Sorted Using Selection SOrt",bg='green').grid(row=i+8,column=1);
        
            
            
        
top = Tk()
#03ade0

L1 = Label(top, text="Enter space seperated array elements")
L1.grid(row=0, column=0)
E1 = Entry(top, bd = 9)
E1.grid(row=0, column=1)

MyButton1 = Button(top, text="Submit", width=10, command=callback)
MyButton1.grid(row=1, column=1)

top.mainloop()
