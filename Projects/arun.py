import tkinter as Tk

def callback():
    print('You clicked the button!')
    value=E1.get()
    a=value.split();
    print(a)
    for q in range(len(a)):
        l4=Label(top,bg='red',text=a[q]).grid(row=5,column=q,padx=50,pady=10)
               
    for i in range(len(a)):
        minm=1
        for j in range(i+1,len(a)):
            if(a[minm]>a[j]):
                minm=j;
        a[i],a[minm]=a[minm],a[i]
        for k in range(len(a)):
            l3=Label(top,bg='#03ade0',text=a[k]).grid(row=i+6,column=k,padx=50,pady=10)
       
           
           
       
top = Tk()

# heading=Label(top,text="Enter space seperated array elements",bg='green').grid(row=1,column=1);
L1 = Label(top, text="Enter space seperated array elements")
L1.grid(row=0, column=0)
E1 = Entry(top, bd = 9)
E1.grid(row=0, column=1)

MyButton1 = Button(top, text="Submit", width=10, command=callback)
MyButton1.grid(row=1, column=1)

top.mainloop()