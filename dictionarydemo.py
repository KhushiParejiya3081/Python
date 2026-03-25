d={101:"Khushi",899:"Riddhi",767:"Anshu",545:"Shivani",323:"Zeel",122:"Chaitanya"}

print(d)
print(d[323])
#print(d["Zeel"])
print(d.get(101))
print(d.items())
print(d.keys())
print(d.pop(767))
print(d)
d.popitem()
print(d)
d1={767:"Anshu",122:"Chaitanya"}
d.update(d1)
print(d)
print(d.values())

for i in d:
    print(i," : ",d[i])  # first way to use for loop

for key,value in d.items():
    print(key," : " ,value)  # second way to use for loop

if 899 in d:
    print("899 Is Available in Dictionary")
else:
    print ("899 Is Not Available In Dictionary")
   
