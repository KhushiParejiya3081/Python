file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File Written Successfully")

print("*"*50)

file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*50)

file=open("tops1.txt","a")
file.write("\nNow This File Is Appended")
file.close()
print("File Appended Successfully")

print("*"*50)


file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*50)

file=open("tops2.txt","w+")
file.write("This is w+ Operation in file using Python.")
print("Current File Position : ", file.tell()) # Tell you where the curser is
file.seek(0)  # Print the data from which argument use pass if you pass 10 in place if 0 then output will print from 10 index
print("File Data : ", file.read())
file.close()

print("*"*50)
