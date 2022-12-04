# Your task is to create a Python script that analyses the records to calculate each of the following values:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period

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
  # printing the result
print("The total number of months included in the dataset is", rowcount-1)
budget_data.close()

import csv
file = open(r'c:/Users/Ina/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
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
    # print(row[-1])
    Pnl+= int(row[-1])
    PnlList.append(row[-1])
    PnlTotal = PnlTotal + int(row[-1])

# print(PnlList)
print(Pnl)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
PnlItem = 0
for PnlItem in range(len(PnlList)-1):
    PnlChange = int(PnlList[PnlItem+1]) - int(PnlList[PnlItem])
    PnlChanges.append(PnlChange)
    PnlChangeTotal = PnlChange + PnlChangeTotal

PnlChangeAverage = PnlChangeTotal / 85
PnlChangeAverage = round(PnlChangeAverage,2)

# The greatest increase in profits (date and amount) over the entire period
print(max(PnlChanges))
MaxPnlChange = max(PnlChanges)
MaxPnlChangeMonths = rows[PnlChanges.index(MaxPnlChange)+1]
print(f'{MaxPnlChangeMonths[0]}, {max(PnlChanges)}')

# The greatest decrease in profits (date and amount) over the entire period
print(min(PnlChanges))
print(max(PnlChanges))
MinPnlChange = min(PnlChanges)
MinPnlChangeMonths = rows[PnlChanges.index(MinPnlChange)+1]
print(f'{MinPnlChangeMonths[0]}, {min(PnlChanges)}')

file.close

with open('analysis/budget_data.txt','w') as text:
    text.write('Financial Analysis')
    text.write('\n')
    text.write('-----------------------------')
    text.write('\n')
    text.write(f'Total Months: {rowcount-1}')
    text.write('\n')
    text.write(f'Total: ${PnlTotal}')
    text.write('\n')
    text.write(f'Average Change: ${PnlChangeAverage}')
    text.write('\n')
    text.write(f'Greatest Increase in Profits: {MaxPnlChangeMonths[0]} (${max(PnlChanges)})')
    text.write('\n')
    text.write(f'Greatest Decrease in Profits: {MinPnlChangeMonths[0]} (${min(PnlChanges)})')


