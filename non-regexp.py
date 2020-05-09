def isPhoneNumber(num):
    if len(num) != 12:
        return False
    for i in range(3):
        if not num[i].isdecimal():
            return False
    if num[3] != '-':
        return False
    for i in range(4,7):
        if not num[i].isdecimal():
            return False
    if num[7] != '-':
        return False
    for i in range(8,12):
        if not num[i].isdecimal():
            return False
    return True

message = input("Enter text:")
foundnum = False
for i in range(len(message)):
    num = message[i:i+12]
    if isPhoneNumber(num):
        print("Number found:", num)
        foundnum = True
if not foundnum:
    print("Numbers not found")