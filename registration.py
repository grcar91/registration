import sqlite3
import tkinter as tk
from tkinter import *



windo=tk.Tk()
windo.geometry("500x450")
windo.title("Registration")
windo.configure(bg="silver")

       
table=sqlite3.connect("nove_stranke.db")
con=table.cursor()
con.execute('''CREATE TABLE IF NOT EXISTS nove_stranke(id INTEGER PRIMARY KEY AUTOINCREMENT, 
            ime TEXT NOT NULL,priimek TEXT NOT NULL,naslov TEXT,e_mail TEXT)''')
table.commit()

windo.resizable(False,False)
windo.grid_columnconfigure(2, weight=1)


text1=tk.Label(windo,text="Welcome!",bg="silver")
text1.pack()


text2 = tk.Label(windo,text="We need you too trust us some data!",bg="silver")
text2.pack()

insertet = tk.Label(windo,text="Please enter your first name",bg="silver")
insertet.pack()

name1 = tk.Entry(windo,width=15,justify="center")
name1.pack()

insertet2 = tk.Label(windo,text="Please enter your last name",bg="silver")
insertet2.pack()

lastname = tk.Entry(windo,width=15)
lastname.pack()

text3 = tk.Label(windo,text="Please enter your address",bg="silver")
text3.pack()

addres= tk.Entry(windo,width=15)
addres.pack()

text4=tk.Label(windo,text="Please enter your e-mail",bg="silver")
text4.pack()

e_mail1= tk.Entry(windo,width=15)
e_mail1.pack()

text5=tk.Label(windo,text="Thank you to trust us your data.",bg="silver")
text5.pack()



def save():
    ime = name1.get()
    priimek = lastname.get()
    naslov = addres.get()
    e_mail = e_mail1.get()

    sql="INSERT INTO nove_stranke(ime, priimek, naslov, e_mail) VALUES(?,?,?,?)"
    podatki1=(ime,priimek,naslov,e_mail)
    con.execute(sql,podatki1)
    table.commit()
    saved = tk.Toplevel(windo)
    saved.geometry("150x100")
    saved.title("SAVE")
    saved.resizable(False,False)
    saved.grid_rowconfigure(2,weight=2)

    pis=tk.Label(saved,text="The data is save!")
    pis.pack()

    ok = tk.Button(saved,text="OK",width=10,command=saved.destroy)
    ok.pack()


def delete():
        name1.delete(0,tk.END)
        lastname.delete(0,tk.END)
        addres.delete(0,tk.END)
        e_mail1.delete(0,tk.END) 

def save_delete():
     save()
     delete()

    
  
def show_customer():
   con.execute("SELECT * FROM nove_stranke")
   vsi= con.fetchall()
   
   customer = tk.Toplevel(windo)
   customer.geometry("300x300")
   customer.title("Stranke")
   lista = tk.Listbox(customer,width=40,height=50)
   lista.grid(pady=20,sticky="nsew",column=0)

   delete = tk.Button(customer,text="Delete",width=5)
   delete.grid(sticky="nsew")

   for st in vsi:
       lista.insert(0,st)
       table.commit()

def uredi():
     pass
            

      

tipka1 = tk.Button(windo,text="SAVE",width= 10, bg="gold2",command=save_delete)
tipka1.pack()

tipka2 = tk.Button(windo,text="Show clients",width= 10,fg="white", bg="blue1", command=show_customer)
tipka2.pack()

tipka3 = tk.Button(windo,text="Delete",width= 10,fg="white", bg="red1", command=delete)
tipka3.pack()


windo.mainloop()
