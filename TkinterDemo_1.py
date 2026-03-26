from tkinter import *
import mysql.connector

def create_conn():
    return mysql.connector.connect(
            database="tkinterdemo",
            user="root",
            password="",
            host="localhost"
        )

print(create_conn())

def insert_data():
    print("Insert Clicked")

def search_data():
    print("Search Clicked")

def update_data():
    print("Update Clicked")

def delete_data():
    print("Delete Clicked")

    
root=Tk()
root.geometry("500x500")
root.title("My Tkinter Example")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Arial",10))
l_id.place(x=50,y=50)

l_fname=Label(root,text="First Name",font=("Arial",10))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="Last Name",font=("Arial",10))
l_lname.place(x=50,y=150)

l_email=Label(root,text="Email",font=("Arial",10))
l_email.place(x=50,y=200)

l_mobile=Label(text="Mobile",font=("Arial",10))
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=200,y=50)

e_fname=Entry(root) 
e_fname.place(x=200,y=100)

e_lname=Entry(root)
e_lname.place(x=200,y=150)

e_email=Entry(root)
e_email.place(x=200,y=200)

e_mobile=Entry(root)
e_mobile.place(x=200,y=250)

insert=Button(root,text="INSERT",bg="Black",fg="white",font=("Arial",12),command=insert_data)
insert.place(x=50,y=300)
search=Button(root,text="SEARCH",bg="Black",fg="White",font=("Arial",12),command=search_data)
search.place(x=120,y=300)
update=Button(root,text="UPDATE",bg="Black",fg="White",font=("Arial",12),command=update_data)
update.place(x=201,y=300)
delete=Button(root,text="DELETE",bg="Black",fg="White",font=("Arial",12),command=delete_data)
delete.place(x=279,y=300)
