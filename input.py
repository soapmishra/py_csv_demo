import csv

DELIM = ","
FILE_PATH = "people.csv"

try:
    open(FILE_PATH, "x")
    with open(FILE_PATH, "w") as f:
        writer = csv.writer(f, delimiter=DELIM)
        writer.writerow(("first_name", "last_name", "email"))
except:
    pass
with open(FILE_PATH, "a") as f:
    writer = csv.writer(f, delimiter=DELIM)
    c = "Y"
    while c in "Yy":
        writer.writerow(
            (
                input("Enter first name:\t"),
                input("Enter last name:\t"),
                input("Enter email:\t\t"),
            )
        )
        c = input("Continue? [y/N]\t\t")
