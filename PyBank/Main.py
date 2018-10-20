# import the os module
import os
#Module for reading csv files
import csv
#Declare Global Variables
TotalMonths = 0
month_of_change=[]
net_change_list=[]
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0


#Files to load 
file_to_load = os.path.join('budget_data.csv')
print(file_to_load)

with open(file_to_load, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
     reader = csv.reader(csvfile, delimiter=',')
# Set a variable to header and set that to next csv reader
     header=next(reader)
     first_row = next(reader)
     print(header)

# Extract row 1 to avoid appending to change values
     first_row = next(reader)
     TotalMonths = TotalMonths + 1
     total_net = total_net + int(first_row[1])
     prev_net = int(first_row[1])

     for row in reader:
      TotalMonths = TotalMonths + 1
      total_net = total_net + int(first_row[1])
# Track Changes
      net_change = int(row[1]) - prev_net
      prev_net = int(first_row[1])
     net_change_list = net_change_list + [net_change]
     month_of_change = month_of_change + [row[0]]
# Calculate the greatest increase
     if net_change < greatest_decrease[1]:
       greatest_decrease[0] = row[0]
       greatest_decrease[1] = net_change

 # Calculate the greatest increase
     if net_change > greatest_increase[1]:
      greatest_decrease[0] = row[0]
      greatest_decrease[1] = net_change

# Calculate avg net change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

#Generate Output Summary
output = (
          f"\n Financial Analysis \n"
          f"---------------------------------\n"
          f"Total Months: {TotalMonths}\n"
          f"Total: ${total_net}\n"
          f"Average Change : ${net_monthly_avg:.2f}\n"
          f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
          f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
   