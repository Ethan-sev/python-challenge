# import things
import os
import csv

csv_path = (r"C:\Users\Sezy\onedrive\python-challenge\PyBank\Resources\budget_data.csv")

# Variable Names
total_months = 0
Max_increase = 0
Max_Decrease = 0
Last_p_and_L = 0
net_total_P_L = 0
D_Date = ""
I_Date = ""
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
# max increase in profits
        

        # change in P and L
        if Last_p_and_L != 0:
            change = Profit_Loss - Last_p_and_L
            changes_in_PnL.append(change)
            if change > Max_increase:
                Max_increase = change
                I_Date = Date
            if change < Max_Decrease:
                Max_Decrease = change
                D_Date = Date

                
        
        Last_p_and_L = Profit_Loss




    
# 85 because we are doing change so there are only 85 changes or len()
Average_change = sum(changes_in_PnL)/ len(changes_in_PnL)



Max_increase = "$" + str(Max_increase)
Max_Decrease = "$" + str(Max_Decrease)
net_total_P_L= "$" + str(net_total_P_L)
Average_change= "$" + str(round(Average_change,2))

print("Financial Analysis")
print("====================")
print(f"Total Months : {total_months} ")
print(f"Total: {net_total_P_L}")
print(f'Average Change: {Average_change}')
print(f"Greatest Increase in Profits: {I_Date} ({Max_increase})")
print(f"Greatest Decrease in Profits: {D_Date} ({Max_Decrease})")

output = r"C:\Users\Sezy\onedrive\python-challenge\PyBank\analysis\budget_analysis.txt"
with open(output,'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("====================\n")
    txtfile.write(f"Total Months : {total_months}\n")
    txtfile.write(f"Total: {net_total_P_L}\n")
    txtfile.write(f'Average Change: {Average_change}\n')
    txtfile.write(f"Greatest Increase in Profits: {I_Date} ({Max_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {D_Date} ({Max_Decrease})\n")