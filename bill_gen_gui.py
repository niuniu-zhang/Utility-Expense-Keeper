import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pandas as pd

# Function to get numeric input with validation
def get_numeric_input(entry_widget, prompt):
    while True:
        value = entry_widget.get()
        try:
            float_value = float(value)
            return float_value
        except ValueError:
            # Display an error message and clear the input field
            messagebox.showerror("Invalid Input", "Please enter a numeric value.")
            entry_widget.delete(0, 'end')
            entry_widget.focus_set()
            entry_widget.wait_variable(entry_widget.get())

# Function to submit expenses
def submit_expense():
    # Get user input
    rent = get_numeric_input(rent_entry, "Rent: ")
    parking = get_numeric_input(parking_entry, "Parking: ")
    electricity = get_numeric_input(electricity_entry, "Electricity: ")
    water = get_numeric_input(water_entry, "Water: ")
    gas = get_numeric_input(gas_entry, "Gas: ")
    internet = get_numeric_input(internet_entry, "Internet: ")

    # Calculate the total expense
    total = rent + parking + electricity + water + gas + internet

    # Update the total label with the message
    total_label.config(text=f"Your monthly expense is ${total:.2f}")
    
    # Get the current date and time
    current_datetime = datetime.now()
    current_date = current_datetime.strftime('%Y-%m-%d')
    month_in_words = current_datetime.strftime('%B')

    # Inform the user about the file location and that it will be read in the future
    file_location = 'expenses.csv'  # Replace with the actual file path if needed
    message = f" Success! {month_in_words} bill updated to {file_location}.\n\n"
    messagebox.showinfo("Expense Saved", message)

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

    # Read the existing DataFrame from a CSV file (if it exists)
    try:
        df = pd.read_csv('expenses.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Date', 'Rent', 'Parking', 'Electricity', 'Water', 'Gas', 'Internet'])

    # Append the new row to the DataFrame
    new_row_df = pd.DataFrame([new_row], columns=df.columns)

    # Exclude empty columns from the DataFrame before concatenation
    df = df.dropna(axis=1, how='all')

    # Append the new row to the DataFrame
    df = pd.concat([df, new_row_df], ignore_index=True, sort=False)

    # Convert the numeric columns to float (excluding 'Date')
    numeric_columns = ['Rent', 'Parking', 'Electricity', 'Water', 'Gas', 'Internet']

    # Calculate the total expense column and add it to the DataFrame
    df['Total'] = df[numeric_columns].sum(axis=1)

    # Save the updated DataFrame to a CSV file
    df.to_csv('expenses.csv', index=False, date_format='%Y-%m-%d')

    # Clear input fields
    rent_entry.delete(0, 'end')
    parking_entry.delete(0, 'end')
    electricity_entry.delete(0, 'end')
    water_entry.delete(0, 'end')
    gas_entry.delete(0, 'end')
    internet_entry.delete(0, 'end')

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create input fields and labels
rent_label = tk.Label(root, text="Rent:")
rent_label.pack()
rent_entry = tk.Entry(root)
rent_entry.pack()

parking_label = tk.Label(root, text="Parking:")
parking_label.pack()
parking_entry = tk.Entry(root)
parking_entry.pack()

electricity_label = tk.Label(root, text="Electricity:")
electricity_label.pack()
electricity_entry = tk.Entry(root)
electricity_entry.pack()

water_label = tk.Label(root, text="Water:")
water_label.pack()
water_entry = tk.Entry(root)
water_entry.pack()

gas_label = tk.Label(root, text="Gas:")
gas_label.pack()
gas_entry = tk.Entry(root)
gas_entry.pack()

internet_label = tk.Label(root, text="Internet:")
internet_label.pack()
internet_entry = tk.Entry(root)
internet_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_expense)
submit_button.pack()

# Create a label to display the total expense message
total_label = tk.Label(root, text="")
total_label.pack()

# Inform the user about the file location and future reading
info_label = tk.Label(root, text="\nWarning: Don't delete expenses.csv, will be appended.")
info_label.pack()

# Start the GUI application
root.mainloop()
