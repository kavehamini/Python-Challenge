#importing os and csv modules
import os, csv
#creating Months list to convert the Months and years column of csv to a list
Months=[]
#creating uniquelist to get the unique values in the Months and Years list created 
uniquelist=[]
#creating profit_loss list to convert the profit_loss column of csv to a list
Profit_Losses=[]
#creating csvpath to locate the csv file and read it
csvpath = os.path.join("Resources", "budget_data.csv")
with open (csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    #skipping the header
    next(csvreader)
    #converting the Months and Profil_loss columns of csv to lists
    for row in csvreader:
        Months.append(row[0])
        Profit_Losses.append(row[1])
    #getting unique values for the Months and years to avoid repetition
    for x in Months:
        if x not in uniquelist:
            uniquelist.append(x)
#printing the results
print("Financial Analysis")
print("..........................")
print(f'Total Months:{len(uniquelist)}')
sum=0
for num in Profit_Losses:
    sum = sum + int(num)
print (f'Total:${str(sum)}')

#geting the average difference and priting it after rounding it up to two decimal places
diff = [int(Profit_Losses[i + 1]) - int(Profit_Losses[i]) for i in range(len(Profit_Losses)-1)]
s = 0
for n in diff:
    s = s + n
print(f'The average change:${round(s/len(diff),2)}')

#getting the indecies for max and min values in the list of differences and printing the max and min differences
maxindex = diff.index(max(diff)) + 1
print(f'Greatest Increase:{Months[maxindex]}, ${max(diff)}')
minindex = diff.index(min(diff)) + 1
print(f'Greatest Decrease:{Months[minindex]}, ${min(diff)}')
#exporting the results as a text file
finalresults = [ "Total Months: " + str(len(uniquelist)), " Total: $" + str(sum)," The average change: $" + str(round(s/len(diff),2)),
                " Greatest Increase: " + str(Months[maxindex]) + ", $" + str(max(diff)), 
                " Greatest Decrease: " + str(Months[minindex]) + ", $" + str(min(diff))]
with open('Pybankresults.txt', 'w') as f:
    for item in finalresults:
        f.write(item)