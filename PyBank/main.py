# The python script is to analyse the following values:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase & decrease in profits (date and amount) over the entire period

# Open & read budget_data.csv
import os
import csv

budget_data = open ("./Resources/budget_data.csv")
budget_data_reader = csv.reader(budget_data, delimiter=",")

# Setting initial value of the counter to zero
rowcount  = 0

# iterating through the whole file
for row in budget_data_reader:
  rowcount+= 1
# printing the total number of months included in the dataset
print("The total number of months included in the dataset is", rowcount-1)
budget_data.close()

import csv
file = open(r'./Resources/budget_data.csv')
csvreader = csv.reader(file)
#Store the header row
header = next(csvreader)
rows = []
Pnl = 0
PnlTotal = 0
PnlChange = 0
PnlList = []
PnlList2 = []
PnlChangeTotal = 0
PnlChangeAverage = 0
PnlChanges = []

for row in csvreader:
    rows.append(row)
    # Total Months
    Pnl+= int(row[-1])
    PnlList.append(row[-1])
    # The net total amount of "Profit/Losses" over the entire period
    PnlTotal = PnlTotal + int(row[-1])

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
PnlItem = 0
for PnlItem in range(len(PnlList)-1):
    PnlChange = int(PnlList[PnlItem+1]) - int(PnlList[PnlItem])
    PnlChanges.append(PnlChange)
    PnlChangeTotal = PnlChange + PnlChangeTotal

PnlChangeAverage = PnlChangeTotal / 85
PnlChangeAverage = round(PnlChangeAverage,2)

# The greatest increase in profits (date and amount) over the entire period
MaxPnlChange = max(PnlChanges)
MaxPnlChangeMonths = rows[PnlChanges.index(MaxPnlChange)+1]


# The greatest decrease in profits (date and amount) over the entire period
MinPnlChange = min(PnlChanges)
MinPnlChangeMonths = rows[PnlChanges.index(MinPnlChange)+1]

file.close

# print analysis result to terminal
print('Financial Analysis')
print('-----------------------------')
print(f'Total Months: {rowcount-1}') # Total months
print(f'Total: ${PnlTotal}') # Total amount of "Profit/Losses" over the entire period
print(f'Average Change: ${PnlChangeAverage}') # Total Average Change
print(f'Greatest Increase in Profits: {MaxPnlChangeMonths[0]} (${max(PnlChanges)})') # Greatest Increase
print(f'Greatest Decrease in Profits: {MinPnlChangeMonths[0]} (${min(PnlChanges)})') # Greatest Decrease

# Export analysis result to text file
with open('analysis/budget_data.txt','w') as text:
    text.write('Financial Analysis')
    text.write('\n')
    text.write('-----------------------------')
    text.write('\n')
    text.write(f'Total Months: {rowcount-1}') # Total months
    text.write('\n')
    text.write(f'Total: ${PnlTotal}') # Total amount of "Profit/Losses" over the entire period
    text.write('\n')
    text.write(f'Average Change: ${PnlChangeAverage}') # Total Average Change
    text.write('\n')
    text.write(f'Greatest Increase in Profits: {MaxPnlChangeMonths[0]} (${max(PnlChanges)})') # Greatest Increase
    text.write('\n')
    text.write(f'Greatest Decrease in Profits: {MinPnlChangeMonths[0]} (${min(PnlChanges)})') # Greatest Decrease