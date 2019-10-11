import os, csv
Months=[] 
uniquelist=[]
Profit_Losses=[]
csvpath = os.path.join("Resources", "budget_data.csv")
with open (csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        Months.append(row[0])
        Profit_Losses.append(row[1])

    for x in Months:
        if x not in uniquelist:
            uniquelist.append(x)
print(f'Total Months:{len(uniquelist)}')
sum=0
for num in Profit_Losses:
    sum = sum + int(num)
print (f'Total:${str(sum)} ')




        
 