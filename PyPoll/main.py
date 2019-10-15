import os, csv

votecount = []
uniquelist= []
candidates = []

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        
        candidates.append(row[2])
    
    
khancount = candidates.count("Khan")
correycount = candidates.count("Correy")
licount = candidates.count("Li")
otooleycount = candidates.count("O'Tooley")

totalvotecount= khancount + correycount + licount + otooleycount




khanpercent = round((khancount/totalvotecount)*100,3)
correypercent = round((correycount/totalvotecount)*100,3)
lipercent = round((licount/totalvotecount)*100,3)
otooleypercent = round((otooleycount/totalvotecount)*100,3)

print("Election Results")
print(".........................")
print(f'Total votes:{totalvotecount}')
print(".........................")
print(f'Khan: {khanpercent}%, {(khancount)}')
print(f'Correy: {correypercent}%, {(correycount)}')
print(f'Li: {lipercent}%, {licount}')
print(f'O\'Tooley: {otooleypercent}%, {otooleycount}')
print(".........................")

if khanpercent > correypercent and khanpercent > lipercent and khanpercent > otooleypercent:
    print(f'Khan is the winner by {khanpercent}% of the votes')
elif correypercent > khanpercent and correypercent > lipercent and correypercent > otooleypercent:
    print(f'Coorey is the winner by {correypercent}% of the votes')
elif lipercent > khanpercent and lipercent > correypercent and lipercent > otooleypercent:
    print(f'Li is the winner by {lipercent}% of the votes')
elif otooleypercent > khanpercent and otooleypercent > correypercent and otooleypercent > lipercent:
    print(f'O\'Tooley is the winner by {otooleypercent}% of the votes')
else:
    print("Nobody wines the election")


finalresults = [ "Total votes: " + str(totalvotecount), " Khan: " + str(khanpercent)+"%" + " ("+str(khancount)+")",
                " Correy: " + str(correypercent)+"%" + " ("+str(correycount)+")",
                " Li: " + str(lipercent) +"%" + " ("+str(licount)+")", 
                " O\'Tooley: " + str(otooleypercent)+"%" +  " ("+str(otooleycount)+")"]
with open('Pypollresults.txt', 'w') as f:
    for item in finalresults:
        f.write(item)








