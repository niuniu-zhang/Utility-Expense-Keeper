import pandas as pd
from datetime import datetime

# Try to read the existing DataFrame from a CSV file (if it exists)
try:
    df = pd.read_csv('expenses.csv')
except FileNotFoundError:
    # If the file doesn't exist, create an empty DataFrame
    df = pd.DataFrame(columns=['Date', 'Rent', 'Parking', 'Electricity', 'Water', 'Gas', 'Internet'])

# Get the current date and time
current_datetime = datetime.now()

# Extract only the year, month, and day portion
current_date = current_datetime.strftime('%Y-%m-%d')

month_to_word = current_datetime.strftime('%B')

# Function to get numeric input with validation
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Get user input for the current month's expenses
print(f"Enter expenses for Month {current_datetime.month}")
rent = get_numeric_input("Rent: ")
parking = get_numeric_input("Parking: ")
electricity = get_numeric_input("Electricity: ")
water = get_numeric_input("Water: ")
gas = get_numeric_input("Gas: ")
internet = get_numeric_input("Internet: ")

# Create a dictionary for the new row
new_row = {
    'Date': current_date,
    'Rent': rent,
    'Parking': parking,
    'Electricity': electricity,
    'Water': water,
    'Gas': gas,
    'Internet': internet
}

new_row_df = pd.DataFrame([new_row], columns=df.columns)

# Exclude empty columns from the DataFrame before concatenation
df = df.dropna(axis=1, how='all')

# Append the new row to the DataFrame
df = pd.concat([df, new_row_df], ignore_index=True, sort=False)

# Calculate the total expense column and add it to the DataFrame
df['Total'] = df[['Rent', 'Parking', 'Electricity', 'Water', 'Gas', 'Internet']].sum(axis=1)

# Save the updated DataFrame to a CSV file
df.to_csv('expenses.csv', index=False, date_format='%Y-%m-%d')

# Calculate the total expenses for the current month
total_expense = df[df['Date'].str.startswith(current_date[:7])]['Total'].sum()

# Print the total expense for the current month
print(f"Your total expense for {month_to_word} is ${total_expense:.2f}")


# Print the resulting DataFrame
print("Here's the summary of your utility bill:")
print(df)
