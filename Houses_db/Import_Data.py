from sys import argv, exit
from cs50 import SQL
import csv
# Checks for number of arguments
if len(argv) != 2:
    print("Usage: python import.py characters.csv")
    exit(0)
# Opens csv file in read mode
file = open(argv[1], 'r')
# Reads data in csv into a list of dictionaries
read = csv.DictReader(file)
# Sets up db connection
db = SQL("sqlite:///students.db")
# Stores data in dictionary into db
for row in read:
    n = row['name'].split()
    if len(n) == 2:
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?,?,?,?,?)",
                   n[0], None, n[1], row['house'], row['birth'])
    else:
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?,?,?,?,?)",
                   n[0], n[1], n[2], row['house'], row['birth'])
file.close()
