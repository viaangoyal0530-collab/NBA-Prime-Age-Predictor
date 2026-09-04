import os
import pandas as pd

os.chdir(r"C:\Users\payal\Downloads\NBAStats")
# File path
file_path = os.path.join(os.getcwd(), "Team Totals.csv")  # Replace with your file name

# Read the file into a DataFrame
df = pd.read_csv(file_path)

# Display the first 5 rows
print(df.head(10))