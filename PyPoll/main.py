# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:

# Read file 'election_data.csv'
import csv
file = open(r'./Resources/election_data.csv')
csvreader = csv.reader(file)
header = next(csvreader)

# The total number of votes cast
rows = []
rowcount = 0
# Create a individual Candidate list
Candidates = []      

for row in csvreader:
    rowcount+=1
    Candidates.append(row[-1])

# Create a complete list of candidates who received votes
CandidateCounter = 0
CandidateCounters = []   
Candidate = 0
CandidateList = [Candidates[Candidate]]
CandidatePercentage = 0
CandidatePercentages = []

# Sort the new created candidates list for calucation
Candidates.sort()

# Categorized Candidates by creating a python list for Candidate Categories
for Candidate in range(len(Candidates)-1):
    if Candidates[Candidate] != Candidates[Candidate + 1]:
        CandidateList.append(Candidates[Candidate+1])

# Calculate a total candidates for each candidate category
for x in range(len(CandidateList)):
    CandidateCounter = 0
    for Candidate in range(len(Candidates)):
        if Candidates[Candidate] == CandidateList[x]:
            CandidateCounter+=1
    CandidateCounters.append(CandidateCounter)

# The percentage of votes each candidate won
for y in range(len(CandidateCounters)):
    CandidatePercentage = round(CandidateCounters[y] / sum(CandidateCounters) * 100, 2)
    CandidatePercentages.append(CandidatePercentage)

# The winner of the election based on popular vote
WinnerCounter = max(CandidateCounters)

for z in range(len(CandidateCounters)):
    if CandidateCounters[z] == WinnerCounter:
        winner = CandidateList[z]

# Analysis result in terminal
print('Election Results')
print('-----------------------------')
print(f"Total Votes: {rowcount}")
for i in range(len(CandidateCounters)):
    print(f"{CandidateList[i]}:{CandidatePercentages[i]}% ({CandidateCounters[i]})")

print('-----------------------------')
print(f"Winner: {winner}")
print('-----------------------------')

# Write analysis result into PyPoll.txt
with open("./analysis/PyPoll.txt", "w") as text:
    text.write('Election Results')
    text.write('\n')
    text.write('-----------------------------')
    text.write('\n')
    text.write(f"Total Votes: {rowcount}")
    text.write('\n')
    for i in range(len(CandidateCounters)):
        text.write(f"{CandidateList[i]}:{CandidatePercentages[i]}% ({CandidateCounters[i]})")
        text.write('\n')
    text.write('-----------------------------')
    text.write('\n')
    text.write(f"Winner: {winner}")
    text.write('\n')
    text.write('-----------------------------')




