import os
import pandas as pd

os.chdir(r"C:\Users\payal\Downloads\NBAStats")
# File path
file_path_advanced = os.path.join(os.getcwd(), "Advanced.csv")  # Replace with your file name

# Read the file into a DataFrame
df_advanced = pd.read_csv(file_path_advanced)

# Display the first 5 rows
print(df_advanced.head(5))

file_path_all_star_selection = os.path.join(os.getcwd(), "All-Star Selections.csv")  # Replace with your file name

df_all_star_selection = pd.read_csv(file_path_all_star_selection)
print(df_all_star_selection.head(5))