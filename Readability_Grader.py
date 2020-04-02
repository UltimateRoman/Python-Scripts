# Inputs text
text = str(input("Text: "))
l = len(text)
cl = sl = 0
wl = 1
for i in range(l):
    # Counts letters
    if text[i].isalpha():
        cl += 1
    # Counts words
    elif text[i] == ' ':
        wl += 1
    # Counts sentences
    elif text[i] in ['.', '!', '?']:
        sl += 1
L = cl/wl * 100
S = sl/wl * 100
# Calculates Coleman-Liau index
index = 0.0588*L - 0.296*S - 15.8
# Identifies corresponding grade
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    indexf = round(index)
    print("Grade", indexf)
