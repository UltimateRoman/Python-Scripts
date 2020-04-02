# Inputs the card number
cno = str(input("Number: "))
cn = int(cno)
cs = 0
# Length of card number
c = len(cno)
# 1st check for valid card number
if c in [13, 15, 16]:
    cnn = cn
    while cnn > 9:
        scn = str(cnn)
        i = int(scn[-2])
        i = i*2
        while i:
            j = i % 10
            cs += j
            i //= 10
        cnn //= 100
    cn = int(cno)
    while cn:
        i = cn % 10
        cs += i
        cn //= 100
    # 2nd check for valid card number
    if cs % 10 == 0:
        # Check for VISA
        if c == 13:
            t = str(cn)
            fn = t[0]
            if fn == '4':
                print("VISA")
            else:
                print("INVALID")
        # Check for AMEX
        elif c == 15:
            t = cno
            fn = t[0:2]
            if fn in ['34', '37']:
                print("AMEX")
            else:
                print("INVALID")
        # Check for MASTERCARD and VISA
        elif c == 16:
            t = cno
            fn = t[0:2]
            if fn in ['51', '52', '53', '54', '55']:
                print("MASTERCARD")
            else:
                if t[0] == '4':
                    print("VISA")
                else:
                    print("INVALID")
    else:
        print("INVALID")
else:
    print("INVALID")
