n = int(input("Enter n: "))
for i in range(1,n+1): # Outer loop
    for j in range(i): # Inner loop
        print(i, end=" ") # Display number
    print()    # A new line after each row