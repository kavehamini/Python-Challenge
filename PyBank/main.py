import os, csv
Months = []
csvpath = os.path.join("Resources", "budget_data.csv")
with open (csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        Months.append(row)
        
a = set(Months)
Months_count = len(a)
print(Months_count)