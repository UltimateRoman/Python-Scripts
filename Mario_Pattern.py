while True:
    # Inputs height of pyramid
    height = int(input("Height: "))
    # Checks for valid input otherwise reprompts user
    if height >= 1 and height <= 8:
        break
    
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    print("  ", end="")
    for j in range(i + 1):
        print("#", end="")
    print()
