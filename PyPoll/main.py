#importing os and csv modules
import os, csv
#creating votecount list to convert the votes column of csv to a list and count the votes cast
votecount = []
#creating candidates list to get a list of all candidates from the candidates csv column 
candidates = []
#creating uniquelist to get a list of unique candidate names to avoid repetition
uniquelist= []

#creating csvpath to locate the csv file and read it
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skipping the header
    next(csvreader)
    #converting the csv column of candidates to a list
    for row in csvreader:
        
        candidates.append(row[2])
    #getting the unique candidate names
    for x in candidates:
        if x not in uniquelist:
            uniquelist.append(x)
    
#getting the vote count for each candidate    
khancount = candidates.count("Khan")
correycount = candidates.count("Correy")
licount = candidates.count("Li")
otooleycount = candidates.count("O'Tooley")
#getting the total votes cast
totalvotecount= khancount + correycount + licount + otooleycount


#calculating the percentage of votes for each candidate and rounding it to three decimal places

khanpercent = round((khancount/totalvotecount)*100,3)
correypercent = round((correycount/totalvotecount)*100,3)
lipercent = round((licount/totalvotecount)*100,3)
otooleypercent = round((otooleycount/totalvotecount)*100,3)

#printing the values obtained
print("Election Results")
print(".........................")
print(f'Total votes:{totalvotecount}')
print(".........................")
print("The list of the candidates who received votes:")
print(" ")
for item in uniquelist:
    print(item)
print(".........................")
print(f'Khan: {khanpercent}%, {(khancount)}')
print(f'Correy: {correypercent}%, {(correycount)}')
print(f'Li: {lipercent}%, {licount}')
print(f'O\'Tooley: {otooleypercent}%, {otooleycount}')
print(".........................")
# getting the winner by popular vote and printing it
if khanpercent > correypercent and khanpercent > lipercent and khanpercent > otooleypercent:
    winner = "Khan"
elif correypercent > khanpercent and correypercent > lipercent and correypercent > otooleypercent:
    winner = "Coorey"
elif lipercent > khanpercent and lipercent > correypercent and lipercent > otooleypercent:
    winner = "Li"
elif otooleypercent > khanpercent and otooleypercent > correypercent and otooleypercent > lipercent:
    winner = "O\'Tooley"
else:
    print("Nobody wines the election")
print(winner +" is the winner!" )
print(".........................")


#exporting the results as a text file
finalresults = [ "Total votes: " + str(totalvotecount), ", Khan: " + str(khanpercent)+"%" + " ("+str(khancount)+")",
                ", Correy: " + str(correypercent)+"%" + " ("+str(correycount)+")",
                ", Li: " + str(lipercent) +"%" + " ("+str(licount)+")", 
                ", O\'Tooley: " + str(otooleypercent)+"%" +  " ("+str(otooleycount)+")", 
                ", " +winner +" is the winner!"]
with open('Pypollresults.txt', 'w') as f:
    for item in finalresults:
        f.write(item)








