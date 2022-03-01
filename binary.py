

BinaryVar = []
print("Enter Your number to Convert to Binary number:")
Number = input("> ")

while True:
    if Number.isnumeric():
        print()
        if int(Number) // 2 != 1:
            BinaryVar.append(int(Number) % 2)
            Number = int(Number) // 2
            Number = str(Number)
        else: 
            BinaryVar.append(int(Number) % 2)
            BinaryVar.append(int(Number) // 2)
            print(BinaryVar[::-1])
            break
        
    else:
        print("You Can only Enter Number!")

    
