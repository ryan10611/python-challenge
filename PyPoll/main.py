import csv
import os
from collections import Counter

numvotes = Counter()
candidates = []
output = []    
pervote = []
# Reads in csv file
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    # Fills our list with candidates
    for row in csvreader:
        candidates.append(row[2])
    total = len(candidates)
    
    # Iterates through candidates for winner
    for can in candidates:
        numvotes[can] = numvotes[can] + 1
    votes = tuple(numvotes.values())
    canname = tuple(numvotes.keys())
    
    # Electorate determiner
    tempwinner = ""
    tempvote = 0
    for x in range(len(canname)):
        if votes[x] > tempvote:
            tempvote = votes[x]
            tempwinner = canname[x]
        
    # Vote percentages
    for vote in votes:
        pervote.append((int(vote)/total)*100)
            
# Post data-analysis output
print("Election Results:")
print(" ")
print("Total votes: " + str(total))
print("------------------------------------------")
for i in range(len(canname)):
        print(canname[i] + ': captured ' + str(round(pervote[i],1)) + "% of votes, with " + str(votes[i]))
print("------------------------------------------")
print("And the winner is: " + tempwinner)

# Output to txt
outputpath = os.path.join("data.txt")

with open(outputpath, 'w', newline = '') as txt:
    txt.write("Election Results:")
    txt.write(" ")
    txt.write("Total votes: " + str(total))
    txt.write("------------------------------------------")
    for i in range(len(canname)):
            txt.write(canname[i] + ': captured ' + str(round(pervote[i],1)) + "% of votes, with " + str(votes[i]))
    txt.write("------------------------------------------")
    txt.write("And the winner is: " + tempwinner)