# Objective: Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

import os
import csv

#Set path for file
pypoll_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#Set Variables 
total_votes = 0
ccs_votes = 0
ddg_votes = 0
rad_votes = 0
winner_name = 0
ccs_percent = 0
ddg_percent = 0
rad_percent = 0

#Open the CSV
with open(pypoll_csv) as data_file:   
    csv_data = csv.reader(data_file, delimiter=',')
    header = next(csv_data)
   
   #Loop through lines gathering data
    for line in csv_data:
        total_votes += 1
        if line[2] == "Charles Casper Stockham":
            ccs_votes += 1
        if line[2] == "Diana DeGette":
            ddg_votes += 1
        if line[2] == "Raymon Anthony Doane":
            rad_votes += 1

#determine winner
winner = max(ccs_votes, ddg_votes, rad_votes)
#determine winner name
if winner == ccs_votes:
    winner_name = "Charles Casper Stockham"
if winner == ddg_votes:
    winner_name = "Diana DeGette"
if winner == rad_votes:
    winner_name = "Raymon Anthony Doane"

#determine % of votes for each canidate 
ccs_percent = (ccs_votes / total_votes) * 100
ddg_percent = (ddg_votes / total_votes) * 100
rad_percent = (rad_votes / total_votes) * 100

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {round(ccs_percent, 3)}% ({ccs_votes})")
print(f"Diana DeGette: {round(ddg_percent, 3)}% ({ddg_votes})")
print(f"Raymon Anthony Doane: {round(rad_percent, 3)}% ({rad_votes})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

#create txt file
with open('puch_pypoll.txt', 'w') as file:
    file.write("\n Election Results")
    file.write("\n-------------------------")
    file.write(f"\nTotal Votes: {total_votes}")
    file.write("\n-------------------------")
    file.write(f"\nCharles Casper Stockham: {round(ccs_percent, 3)}% ({ccs_votes})")
    file.write(f"\nDiana DeGette: {round(ddg_percent, 3)}% ({ddg_votes})")
    file.write(f"\nRaymon Anthony Doane: {round(rad_percent, 3)}% ({rad_votes})")
    file.write("\n-------------------------")
    file.write(f"\nWinner: {winner_name}")
    file.write("\n-------------------------")