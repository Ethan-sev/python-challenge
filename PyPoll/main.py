# Time to Import
import os
import csv

csv_path = (r'C:\Users\Sezy\OneDrive\python-challenge\PyPoll\Resources\election_data.csv')

# Creating Variables
one_votes = 0
two_votes = 0
three_votes = 0
Votes_per_canidate = 0
Total_votes = 0 
ALL_Canidates = set() 
last_canidate = ""
Stockham_percentage = 0 
DeGette_percentage = 0
Doane_percentage = 0

# Open CSV
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile)

    next(csv_reader)

    for row in csv_reader:
 # total votes 
        Total_votes += 1
        Canidate = str(row[2])
        County = row[1]
        
        if last_canidate != Canidate:
            ALL_Canidates.add(Canidate)
# First Canidate Data
        if Canidate == "Charles Casper Stockham":
            one_votes += 1 
        
        Stockham_percentage = (one_votes / Total_votes)*100
        Stockham_percentage = "{:.3f}%".format(Stockham_percentage)

        # if Canidate == "Diana DeGette":


        
Canidatelist = list(ALL_Canidates)



           





print(Canidatelist[0])
print(Total_votes)
print(one_votes)
print(list(ALL_Canidates)[0])
print(Stockham_percentage)
        



    




