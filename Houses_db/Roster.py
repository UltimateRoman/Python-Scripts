from sys import argv, exit
from cs50 import SQL
# Checks for number of arguments
if len(argv) != 2:
    print("Usage: python roster.py house_name")
    exit(0)
# Sets up db connection
db = SQL("sqlite:///students.db")
# Executes SQL query and stores data into a list of dictionaries
s = db.execute("SELECT first,middle,last,birth FROM students WHERE house = ? ORDER BY last, first", argv[1])
# Displays required data 
for a in s:
    if a['middle'] == None:
        print(a['first'], a['last'] + ", born", a['birth'])
    else:
        print(a['first'], a['middle'], a['last'] + ", born", a['birth'])