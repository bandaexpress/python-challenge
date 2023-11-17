# Module for reading CSV files.
import os
import csv

# Set the path to the CSV file.
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

# Set the path to the text file for results.
output_file_path = "C:/Users/antho/python-challenge/PyBank/Analysis.txt"

# Initialize variables to store analysis results:
# Set the total_month, net_total, and previous_profit_loss to zero to begin the calculation.
total_months = 0
net_total = 0
previous_profit_loss = 0

# Create a list to log the changes. 
changes = []

# Create two dictionaries to keep track of the date and amount associated with the greatest increase and greatest decrease.
# Create a floating-point representation of positive and negative infinity to find the maximum and minimum values in the set.
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}


# Open the CSV file and read its contents.
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip the header row.
    header = next(csv_reader)

    # Process the rows in the budget_data CSV file with a for loop.
    for row in csv_reader:
        # Extract date from starting value at index 0 (column 1) and extract profit/loss value at index 1 (column 2), using an integer conversion because the profit_loss value is numeric.
        date = row[0]
        profit_loss = int(row[1])

        # Update total months using +1 to count and calculate the net total.
        total_months = total_months + 1
        net_total = net_total + profit_loss

        # Calculate the change in profit/loss using previous_profit_loss and append the changes to the changes dictionary.
        change = profit_loss - previous_profit_loss
        changes.append(change)

        # Update greatest increase and decrease by using an if statement to check if each row has a change that is greater or less than the previously defined greatest increase and decrease. 
        # If the row has a change that is greater than the presently established greatest increase, then the selected row will be set as the greatest increase date, along with its corresponding change amount.
        if change > greatest_increase["amount"]:
            greatest_increase["date"] = date
            greatest_increase["amount"] = change
        # If the row has a change that is less than the presently established greatest decrease, then the selected row will be set as the greatest decrease date, along with its corresponding change amount.
        if change < greatest_decrease["amount"]:
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = change

        # Update previous profit/loss for the next iteration to enable the greatest increase and decrease calculation.
        previous_profit_loss = profit_loss

    # Calculate the average change from the changes list using the sum of the changes, excluding the first row, divided by total months -1 to exclude the first month which does not have a previous month for comparison.
    average_change = sum(changes[1:]) / (total_months - 1)


    # Open the Analysis text file using with open and the 'w' to write to the text file.
    with open(output_file_path, 'w') as output_file:
        # Redirect the print output to the Analysis text file.
        output_file.write("Financial Analysis\n")
        output_file.write("------------------\n")
        output_file.write(f"Total Months: {total_months}\n")
        output_file.write(f"Net Total: ${net_total}\n")
        output_file.write(f"Average Change: ${average_change:.2f}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

# Print the analysis results in the terminal.
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")