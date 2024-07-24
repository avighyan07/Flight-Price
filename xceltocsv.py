import pandas as pd

# Load the Excel file
# excel_file = 'data\Data_Train.xlsx'

# # Read the first sheet of the Excel file into a DataFrame
# df = pd.read_excel(excel_file)

# # Save the DataFrame to a CSV file
# csv_file = 'data_flight.csv'


df = pd.read_csv('data_flight.csv')

# Select the first 50 rows
train = df.head(8548)

# Save the first 50 rows to a new CSV file
train.to_csv('train.csv', index=False)

test = df.tail(2000)

# Save the first 50 rows to a new CSV file
test.to_csv('test.csv', index=False)