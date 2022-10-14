import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("--------------------")

candidates = []
candidate_votes = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_votes = 0
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    # print(candidate_votes)
    
    print(f"Total Votes: {total_votes}")
    print("-----------------------")

    sum1 = candidate_votes['Charles Casper Stockham']
    divisor = total_votes
    percentage_of_votes_1 = (sum1 / divisor) * 100
    print(f'Charles Casper Stockham: {percentage_of_votes_1:.3f}%')
    
    sum2 = candidate_votes['Diana DeGette']
    divisor = total_votes
    percentage_of_votes_2 = (sum2 / divisor) * 100
    print(f'Diana DeGette: {percentage_of_votes_2:.3f}%')

    sum3 = candidate_votes['Raymon Anthony Doane']
    divisor = total_votes
    percentage_of_votes_3 = (sum3 / divisor) * 100
    print(f'Raymon Anthony Doane: {percentage_of_votes_3:.3f}%')

outpath = os.path.join("analysis", "Summary_Voting_Results.csv")

with open(outpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results'])
    rows = [[f"Total Votes: {total_votes}"],[f'Charles Casper Stockham: {percentage_of_votes_1:.3f}%'],[f'Diana DeGette: {percentage_of_votes_2:.3f}%']
    ,[f'Raymon Anthony Doane: {percentage_of_votes_3:.3f}%']]
    for row in rows:
        csvwriter.writerow(row)