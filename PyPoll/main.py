# Module for reading CSV files.
import os
import csv

# Set the path to the CSV file.
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

# Set the path to the text file for results.
output_file_path = "C:/Users/antho/python-challenge/PyPoll/Analysis.txt"

# Initialize variables to store election analysis results:
# Set the total votes count to start at zero and create new empty dictionaries to store the unique votes and percentage.
total_votes = 0
candidates_votes = {}
candidates_percentage = {}

# Specify the column targeted for the candidate count.
target_column = "Candidate"

# Open the CSV file and read its contents using csv.DictReader to skip the header row.
with open(csvpath, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    # Process the rows in the election_data CSV file with a for loop.
    for row in csv_reader:
        # Count total votes.
        total_votes = total_votes + 1

        # Extract the candidate information from the row by the Candidate column.
        candidate = row["Candidate"]

        # Update candidate votes count using the candidates_votes dictionary used to store the count of votes by candidate. 
        # Retrieves the current count of votes for the candidate using .get using a default value of 0 if the candidate it not already in the dictionary and adding + 1 for each new candidate.
        candidates_votes[candidate] = candidates_votes.get(candidate, 0) + 1
        # Calculate percentage of votes for each candidate using a for loop in the candidate's name and the count of votes they received.
        for candidate, votes in candidates_votes.items():
            # Use the candidates_percentage dictionary to store the calculated percentage for each candidate.
            candidates_percentage[candidate] = (votes / total_votes) * 100
    # Find the election winner based on most votes using max .get from candidate_votes dictionary.
    winner = max(candidates_votes, key=candidates_votes.get)

 # Open the Analysis text file using with open and the 'w' to write to the text file.
    with open(output_file_path, 'w') as output_file:
        # Redirect the print output to the Analysis text file.
        output_file.write("Election Results\n")
        output_file.write("------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("------------------\n")
        for candidate, votes in candidates_votes.items():
            output_file.write(f"{candidate}: {candidates_percentage[candidate]:.3f}% ({votes})")
        output_file.write("------------------\n")
        output_file.write(f"Winner: {winner}\n")
        output_file.write("------------------\n")
        
# Print the analysis results in the terminal.
print("Election Results")
print("------------------")
print(f"Total Votes: {total_votes}")
print("------------------")
# Use a for loop to iterate over the candidates_votes dictionary where each key is a candidate's name and the corresponding value is the candidate's vote count.
# Use .3f to get 3 decimal places for the percentage.
for candidate, votes in candidates_votes.items():
    print(f"{candidate}: {candidates_percentage[candidate]:.3f}% ({votes})")
print("------------------")
print(f"Winner: {winner}")
print("------------------")