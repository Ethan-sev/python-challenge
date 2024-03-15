# import things
import os
import csv

csv_path = (r"C:\Users\Sezy\onedrive\python-challenge\PyBank\Resources\budget_data.csv")

# Variable Names
total_months = 0


net_total_P_L = 0

changes_in_PnL = []

dates=[]









with open (csv_path) as csvfile:
    csvreader= csv.reader(csvfile)

# pop to next line
    next(csvreader)

    for row in csvreader:
        Date = row[0]
        Profit_Loss = int(row[1])
        net_total_P_L += Profit_Loss
        print(net_total_P_L)


