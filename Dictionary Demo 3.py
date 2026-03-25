d={1:"Jigar" , 2:"Ajay", 3:"Vijay" , 4:"Kamal" , 5:"Ketan"}

key=int(input("Enter Existing Key : "))
value=input("Enter New Value : ")

if key in d:
    d[key]=value
else:
    print("Key Is Not Presented In Disctionary")
print(d)
