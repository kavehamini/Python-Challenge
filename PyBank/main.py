import os, csv
import itertools
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

diff = [int(Profit_Losses[i + 1]) - int(Profit_Losses[i]) for i in range(len(Profit_Losses)-1)]
s = 0
for n in diff:
    s = s + n
print(f'The average change:${s/len(diff)}')

maxindex = diff.index(max(diff)) + 1
print(f'Greatest Increase:{Months[maxindex]}, ${max(diff)}')
minindex = diff.index(min(diff)) + 1
print(f'Greatest Decrease:{Months[minindex]}, ${min(diff)}')

#for i in range(len(Months)):
    #mapped = zip(Months[i], diff[i]) 
#print(mapped)
#print(f'Greatest Increase:${max(diff)}')
#print(f'Greatest Increase:${min(diff)}')