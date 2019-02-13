import os
import csv
import statistics

monthlist = []
moneylist = []
avgchange = 0
csvpath = os.path.join ('Resources', 'budget_data.csv')

# Loads in and reads our Excel data
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
# Skips over header
    next(csvreader)

# Reads in our values
    for column in csvreader:
        months, money = column
        monthlist.append(str(months))
        moneylist.append(int(money))

# Totals
nummonths = (len(monthlist))
totalmoney = (sum(moneylist))

# Average change
netchange = []
for x,y in zip(moneylist[:-1], moneylist[1:]):
    netchange.append((y)-(x))
temp = 0.0       
for num in netchange:
    temp += float(num)
avgchange = (temp/(len(netchange)))
print(avgchange)

# Greatest increase in profits
changelist = list(zip(netchange, monthlist))
grincmonth = max(changelist)[1]
grincval = max(changelist)[0]

# Greatest decrease in losses
grdecmonth = min(changelist)[1]
grdecval = min(changelist)[0]

# Post saved-data analysis:
print("Financial Analysis:")
print(" ")
print("Total Months: " + str(nummonths))
print("Total: " + "$" + str(totalmoney))
print("Average Change: " + "$" + str(avgchange))
print("Greatest increase in profit: " + str(grincmonth) + ": $" + str(grincval))
print("Greatest decrease in losses: " + str(grdecmonth) + ": $" + str(grdecval))

# Writes output to txt file
outputpath = os.path.join("data.txt")

with open(outputpath, 'w', newline = '') as txt:
    txt.write("Financial Analysis:")
    txt.write(" ")
    txt.write("Total Months: " + str(nummonths))
    txt.write("Total: " + "$" + str(totalmoney))
    txt.write("Average Change: " + "$" + str(avgchange))
    txt.write("Greatest increase in profit: " + str(grincmonth) + ": $" + str(grincval))
    txt.write("Greatest decrease in losses: " + str(grdecmonth) + ": $" + str(grdecval))