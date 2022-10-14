import os
import csv

print('Financial Analysis')
print('------------------------')

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_months = 0
    total_profit = 0
    for row in csvreader:
        total_months += 1
        total_profit += int(row[1])
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)
    previous_net = int(first_row[1])
    total_change = []
    month_of_change = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]
    for row in csvreader:
        difference = int(row[1]) - previous_net
        previous_net = int(row[1])
        total_change += [difference]
        month_of_change += [row[0]]
        if difference > greatest_increase[1]:
            greatest_increase[1] = difference
            greatest_increase[0] = row[0]
        elif difference < greatest_decrease[1]:
            greatest_decrease[1] = difference
            greatest_decrease[0] = row[0]
    sum = sum(total_change)
    divisor = len(total_change)
    net_average = sum / divisor
    print(f'Average Change: ${net_average:.2f}')
    print(f'The greatest increase in Profits: {greatest_increase}')
    print(f'The greatest decrease in Profits: {greatest_decrease}')
    

outpath = os.path.join("analysis", "Summary_budget_data.csv")

with open(outpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    rows = [[f'Total Months: {total_months}'],[f'Total: ${total_profit}'],[f'Average Change: ${net_average:.2f}']
    ,[f'The greatest increase in Profits: {greatest_increase}'],[f'The greatest decrease in Profits: {greatest_decrease}']]
    for row in rows:
        csvwriter.writerow(row)
