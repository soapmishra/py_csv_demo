import csv

FILE_PATH = "people.csv"
DELIM = ","

try:
    open(FILE_PATH, "x")
except:
    pass

with open(FILE_PATH, "r") as f:
    reader = csv.reader(f, delimiter=DELIM)
    for row in reader:
        print(",".join(row))
