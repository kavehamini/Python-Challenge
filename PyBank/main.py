import os, csv
Months=[] 
uniquelist=[] 
csvpath = os.path.join("Resources", "budget_data.csv")
with open (csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        Months.append(row[0])   
    for x in Months:
        if x not in uniquelist:
            uniquelist.append(x)
print(f'The total number of months in the database is {len(uniquelist)}')



        
 