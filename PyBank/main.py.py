# Objective: Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

import os
import csv

#Set path for file
pybank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#Set Variables 
total_months= 0
total_profit_loss = 0
pre_pl = 0
pl_change = []
change_list = []
change_month = []
max_date = 0
min_date = 0

#Open the CSV
with open(pybank_csv) as data_file:   
    csv_data = csv.reader(data_file, delimiter=',')
    header = next(csv_data)
   
   #Loop through lines gathering data
    for line in csv_data:
    #Total Months calculation: 
        total_months += 1
    #Total Profit/Loss calculation:
        total_profit_loss += int(line[1])
    #Average Change calculation: 
    # current_revenue - previous_revenue = revenue_change
        pl_change = int(line[1]) - pre_pl
        pre_pl = int(line[1])
        change_list = change_list + [pl_change]
    #date for max change
        if pl_change == max(change_list): 
            max_date = line[0]
    #date for min change
        if pl_change == min(change_list):
            min_date = line[0]

#average change calcualtion 
pl_average = sum(change_list)/total_months


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(pl_average, 2)}")
print(f"Greatest Increase in Profits: {max_date} ${max(change_list)}")
print(f"Greatest Decrease in Profits: {min_date} ${min(change_list)}")

#create txt file
with open('puch_pybank.txt', 'w') as file:
    file.write("\nFinancial Analysis")
    file.write("\n----------------------------")
    file.write(f"\nTotal Months: {total_months}")
    file.write(f"\nTotal: ${total_profit_loss}")
    file.write(f"\nAverage Change: ${round(pl_average, 2)}")
    file.write(f"\nGreatest Increase in Profits: {max_date} ${max(change_list)}")
    file.write(f"\nGreatest Decrease in Profits: {min_date} ${min(change_list)}")