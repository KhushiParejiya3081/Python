print("Enter 10 numbers:")

even = []
odd = []
for i in range(10):
    n = int(input(f"Enter number {i+1}: "))
    
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("\nEven Numbers:", even)
print("Odd Numbers:", odd)
