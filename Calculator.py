import tkinter as tk
from tkinter import ttk, messagebox

# the main GUI
m=tk.Tk()
m.title('Calculator ➗✖️➕➖')
m.geometry('350x400')
m.configure(bg='grey')


result= tk.Entry(m, state="readonly", fg="blue",font=("Arial", 12))
result.grid(row=5, column=1, pady=5, padx=5)

#function (the main working body)
def calculate():
    global result
    try:
         c = float(e1.get())
         d = float(e2.get())
         oprator = options.get()
         if oprator == '+':
             a = c+d
         elif oprator =='-':
             a = c-d
             
         elif oprator =='/':
             a = c/d
             
         elif oprator =='*':
             a = c*d
             
         else:
            result = "Select operator"
         result.config(state="normal")
         result.delete(0, tk.END)
         result.insert(0, str(a))
         result.config(state="readonly")

    except ValueError:
        result.config(text='Enter a valid number!')
    except ZeroDivisionError:
        result.config(text="Error: Cannot divide by zero")
        

#Lables

tk.Label(m,text='Enter first number : ',fg='black',bg='grey',font=("Arial", 10)).grid(row=0)
tk.Label(m,text='Enter Second  number : ',fg='black',bg='grey',font=("Arial", 10)).grid(row=1)
e1 = tk.Entry(m,justify='center')
e2 = tk.Entry(m,justify='center')
e1.grid(row=0, column=1,padx=10,pady=10)
e2.grid(row=1, column=1,padx=10,pady=10)
# combobox

Label=tk.Label(m,text='Select operator :',justify='center',bg='grey',font=("Arial", 10)) 
Label.grid(pady=10,row=2)
options = ttk.Combobox(m,values=["+","-","*","/"])
options.grid(row=2,column=1,pady=5)



tk.Button(m, text="Calculate", bg="green", fg="white", command=calculate).grid(row=4, column=1,padx=10, pady=10)

#result 

tk.Label(m, text="Result :", bg="grey").grid(row=5, column=0, pady=5, padx=5, sticky="w")


m.mainloop()
