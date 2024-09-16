import pandas as pd
from math import ceil

# Load the CSV file
file_path = 'E:\\Amazon_ML\\dataset\\test.csv'  # Update with the correct path if needed
data = pd.read_csv(file_path)

# Calculate the number of rows for each split
total_rows = len(data)
split_size = ceil(total_rows / 3)  # Use ceil to handle cases where rows don't divide evenly

# Split the data into three parts
part1 = data.iloc[:split_size]
part2 = data.iloc[split_size:split_size * 2]
part3 = data.iloc[split_size * 2:]

# Save each part into a separate CSV file
part1.to_csv('part1.csv', index=False)
part2.to_csv('part2.csv', index=False)
part3.to_csv('part3.csv', index=False)

print("CSV files created: part1.csv, part2.csv, part3.csv")


