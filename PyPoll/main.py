# Time to Import
import os
import csv

csv_path = (r'C:\Users\Sezy\OneDrive\python-challenge\PyPoll\Resources\election_data.csv')

# Creating Variables
one_votes = 0
two_votes = 0
three_votes = 0
Total_votes = 0 
ALL_Canidates = []
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
        
        if Canidate not in ALL_Canidates:
            ALL_Canidates.append(Canidate)
# First Canidate Data
        if Canidate == ALL_Canidates[0]:
            one_votes += 1 
        elif Canidate == ALL_Canidates[1]:
            two_votes += 1 
        else:
            three_votes += 1 
        
        DeGette_percentage = (two_votes / Total_votes)*100
        DeGette_percentage = "{:.3f}%".format(DeGette_percentage)
        Stockham_percentage = (one_votes / Total_votes)*100
        Stockham_percentage = "{:.3f}%".format(Stockham_percentage)
        Doane_percentage = (three_votes / Total_votes)*100
        Doane_percentage = "{:.3f}%".format(Doane_percentage)


        
Canidatelist = list(ALL_Canidates)
winner = max(one_votes, two_votes, three_votes)
if winner == one_votes:
    YOUWON = ALL_Canidates[0]
elif winner == two_votes:
    YOUWON = ALL_Canidates[1]
else:
    winner = ALL_Canidates[2]


    #    
print("Election Results")
print("====================")
print(f"{ALL_Canidates[0]}: {Stockham_percentage} ({one_votes})")
print(f"{ALL_Canidates[1]}: {DeGette_percentage} ({two_votes})")
print(f"{ALL_Canidates[2]}: {Doane_percentage} ({three_votes})")
print("======================")
print(f'Winner: {YOUWON}')

output = r"C:\Users\Sezy\OneDrive\python-challenge\PyPoll\analysis\something.txt"
with open(output, 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("====================\n")
    textfile.write(f"{ALL_Canidates[0]}: {Stockham_percentage} ({one_votes})\n")
    textfile.write(f"{ALL_Canidates[1]}: {DeGette_percentage} ({two_votes})\n")
    textfile.write(f"{ALL_Canidates[2]}: {Doane_percentage} ({three_votes})\n")
    textfile.write("======================\n")
    textfile.write(f'Winner: {YOUWON}\n')




    




