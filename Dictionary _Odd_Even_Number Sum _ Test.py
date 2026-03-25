# dictionary with 10 key-value pairs
d = { "a": 10,"b": 15, "c": 8,"d": 21,"e": 6, "f": 13,"g": 4, "h": 9, "i": 12, "j": 7}

odd_sum = 0
even_sum = 0

for key, value in d.items():
    if value % 2 == 0:
        even_sum += value
       
    else:
        odd_sum += value
       

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
