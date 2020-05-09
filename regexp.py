import re
message = input("Enter text:")
numregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
numsearch = numregex.findall(message)
print(numsearch)
