# import things
import os
import csv

csv_path = (r"C:\Users\Sezy\onedrive\python-challenge\PyBank\Resources\budget_data.csv")

# Variable Names
total_months = 0

Last_p_and_L = 0
net_total_P_L = 0
# help store data
changes_in_PnL = []




with open (csv_path) as csvfile:
    csvreader= csv.reader(csvfile)

# pop to next line
    next(csvreader)

    for row in csvreader:

        Date = row[0]
        Profit_Loss = int(row[1])
        net_total_P_L += Profit_Loss
        # for each row in csv reader add 1 to total months
        total_months += 1
        # change in P and L
        if Last_p_and_L != 0:
            change = Profit_Loss - Last_p_and_L
            changes_in_PnL.append(change)
        Last_p_and_L = Profit_Loss
# 85 because we are doing change so there are only 85 changes or len()
Average_change = sum(changes_in_PnL)/ len(changes_in_PnL)



        
        
print(net_total_P_L)
print(total_months)
print(Average_change)

