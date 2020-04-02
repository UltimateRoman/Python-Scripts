from sys import argv, exit
import csv

# Checks for required no: of arguments
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(0)
# Opens csv and dna files
file1 = open(argv[1], 'r')
file2 = open(argv[2], 'r')
read1 = csv.DictReader(file1)
fnames = read1.fieldnames
read1 = csv.reader(file1)
read2 = file2.read()
dictr = []
dnal = {}
# Creates a dictionary with csv data
for i in read1:
    l = {}
    for j in range(len(fnames)):
        l[fnames[j]] = i[j]
    dictr.append(l)
# Checks for matching STRs in DNA and takes count
for c in range(1, len(fnames)):
    dnal[fnames[c]] = 0
    for k in range(len(read2)):
        count = 0
        while fnames[c] == read2[k:(k+len(fnames[c]))]:
            count += 1
            k += len(fnames[c])
        if dnal[fnames[c]] < count:
            dnal[fnames[c]] = count
file1.close()
file2.close()
# Checks for a matching person
for p in dictr:
    dc = 0
    for d in range(1, len(dnal)+1):
        if int(p[fnames[d]]) == int(dnal[fnames[d]]):
            dc += 1
        if dc == len(dnal):
            print(p['name'])
            exit(0)
print("No Match")