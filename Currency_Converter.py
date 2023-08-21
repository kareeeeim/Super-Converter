from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ramsey currency  Converter")
root.minsize(width=700,height=500)
root.geometry("700x500")


Canvas1 = Canvas(root)
    
Canvas1.config(bg="#89807C")
Canvas1.pack(expand=True,fill=BOTH)

def quitroot():
    messagebox.showinfo("Thank you","Thank U for using Currency Converter Program")
    root.destroy()
#define a method to convert the currencies
currencies = {
    'dollar': 1.0,
    'ruble':93.87,
    'euros': 0.92,
    'naira': 760,
    'dinar ': 0.31,
    'rupees': 0.0124,
    'pounds': 0.79,
    'sar':3.79,
    'egp':31.16
    
}

def currency1():
    try:
        from_currency = f.get().lower()
        to_currency = t.get().lower()
        amount = float(a.get())

        if from_currency not in currencies or to_currency not in currencies:
            messagebox.showerror("Invalid input", "The currency you are converting is not possible or is not in our system. Please check our currency list and try again!")
        else:
            converted_amount = amount / currencies[from_currency] * currencies[to_currency]
            messagebox.showinfo("Conversion", f"{amount} {from_currency.capitalize()} = {converted_amount} {to_currency.capitalize()}")

    except ValueError:
        messagebox.showerror("Invalid input", "You can only convert numbers! Please try again.")

def clear():
    f.delete(0, "end")
    t.delete(0, "end")
    a.delete(0,"end")

        
headingFrame1 = Frame(root,bg="black",bd=3)
headingFrame1.place(relx=0.23,rely=0.1,relwidth=0.5,relheight=0.15)

#heading title 
headingLabel = Label(headingFrame1, text="Welcome to\n   Currency Conveter Program ", bg="#6E736E", fg='white', font=('Oswald',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

descrframe= Frame(root, bg='black',bd=3)
descrframe.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.1)

#label
descrlabel = Label(descrframe, text="We convert the following currencies \nDollars , Rouble , Naira , Pounds , Euros , Rupees , Dinar , EGP , SAR ", bg='#6E736E', fg='white', font=('Arial',10,'bold'))
descrlabel.place(relx=0,rely=0, relwidth=1, relheight=1)



labelFrame = Frame(root,bg='#C01E1E')
labelFrame.place(relx=0.1,rely=0.44,relwidth=0.8,relheight=0.4)

#currency froms
lb1 = Label(labelFrame,text="Currency From : ", fg='white', bg='#C01E1E',font=('Arial', 11, 'bold'))
lb1.place(relx=0.05,rely=0.2, relheight=0.1)

ff = StringVar()        
f = Entry(labelFrame, textvariable=ff)
f.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.1)
        
# currency to
lb2 = Label(labelFrame,text="Currency To: ",bg='#C01E1E', fg='white', font=('Arial', 11, 'bold'))
lb2.place(relx=0.05,rely=0.4, relheight=0.1)

tt = StringVar()        
t = Entry(labelFrame, textvariable=tt)
t.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.1)

#amount
lb3 = Label(labelFrame,text="Amount : ", bg='#C01E1E', fg='white',font=('Arial', 11, 'bold'))
lb3.place(relx=0.05,rely=0.6, relheight=0.1)


aa = StringVar()        
a = Entry(labelFrame, textvariable=aa)
a.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.1)

convertBtn = Button(root,text="Convert",bg='#C01E1E', fg='white',command=currency1,font=('Arial',11))
convertBtn.place(relx=0.1,rely=0.88, relwidth=0.18,relheight=0.05)

clearBtn = Button(root,text="Clear",bg='#C01E1E', fg='white', command=clear,font=('Arial',11))
clearBtn.place(relx=0.4,rely=0.88, relwidth=0.18,relheight=0.05)

quitBtn = Button(root,text="Quit",bg='#C01E1E', fg='white', command=quitroot,font=('Arial',11))
quitBtn.place(relx=0.7,rely=0.88, relwidth=0.18,relheight=0.05)
root.mainloop()
        