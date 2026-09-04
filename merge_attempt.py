import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Change to correct directory
os.chdir(r"C:\Users\payal\Downloads\NBAStats")

# Read the CSV files
advanced = pd.read_csv("Advanced.csv")
draft_pick_history = pd.read_csv("Draft Pick History.csv")
player_totals = pd.read_csv("Player Totals.csv")

# Remove extra spaces
advanced.columns = advanced.columns.str.strip()
draft_pick_history.columns = draft_pick_history.columns.str.strip()
player_totals.columns = player_totals.columns.str.strip()

# Keep only the columns needed
advanced = advanced[["player_id", "pos", "player", "season", "per", "bpm"]]
draft_pick_history = draft_pick_history[["season", "overall_pick", "player", "player_id"]]
player_totals = player_totals[[ "player", "player_id", "season", "age", "g", "gs", "mp", "trb", "ast", "pts", "fg_percent"]]

# Keep only ONE row per player_id
# advanced = advanced.drop_duplicates(subset="player_id")
# draft_pick_history = draft_pick_history.drop_duplicates(subset="player_id")
# player_totals = player_totals.drop_duplicates(subset="player_id")

# # First merge
# result_1 = pd.merge(player_totals, draft_pick_history, on="player_id", how="left")

# # # Second merge
# result_2 = pd.merge(result_1, advanced, on="player_id", how="left")

# First merge
result_1 = pd.merge(
    player_totals,
    draft_pick_history,
    on=["player_id", "season"],
    how="left"
)

# Second merge
result_2 = pd.merge(
    result_1,
    advanced,
    on=["player_id", "season"],
    how="left"
)

result_2 = result_2.drop(columns=["player_x", "player_y"])


# delete duplicate rows based on player_id and season
result_2 = result_2.drop_duplicates(subset=["player_id", "season"])

print(result_2.head(500))

# Lebron Check
# player_name = input("Which player do you want to check for in the dataset? (Press Enter to check for LeBron James) ")
# if player_name == "":
#     player_name = "LeBron James"PP

# if result_2.loc[result_2['player'] == player_name].shape[0] > 0:
#     print(f"{player_name} is in the dataset.")
#     player_data = result_2.loc[result_2['player'] == player_name]
#     print(player_data)
# elif result_2.loc[result_2['player'] == player_name].shape[0] == 0:
#     print(f"{player_name} is not in the dataset.")
# else:
#     print("Error: Could not determine if the player is in the dataset.")




# Cleaning Data Lines
# print(np.shape(result_2))                    # Check the shape of the DataFrame
# result_2 = result_2.dropna()                    # Drop all rows containing any missing value
# result_2.dropna(axis=1)              # Drop any column containing a missing value
# result_2.fillna(0)                   # Replace all missing values with 0
# result_2['Age'] = result_2['Age'].fillna(result_2['Age'].mean()) # Fill NaNs with the column average
# result_2 = result_2.dropna(subset=["age", "pts"])  # Drop rows where age or pts is missing  



#print(result_2.head())

#concat attempt
#result_2 =  pd.concat([advanced, draft_pick_history, player_totals], axis=1, ignore_index=True)

# Drop duplicates based on player_id
#result_2 = result_2.drop_duplicates(subset="player_id")

#result_2['player']                      # Select a single column as a Series
#print(result_2[['player', 'player_id']])            # Select multiple columns as a new DataFrame

# Specific rows and columns
#print(result_2.loc[10])                      # Select the first row by label index
#print(result_2.loc[100:105, ['player', 'player_id']])   # Select rows 0 to 5 for specific columns
#print(result_2.iloc[100:101, 8:9])              # Select rows 0-2 and columns 0-1 by position

#result_2.to_csv("lebron_check", index=False)

#print(result_2.head(50))

#ibfuhbeaiufhuHfj
#print(result_2)



# lebron_check = result_2.loc[result_2['player'] == "LeBron James"]

# print(lebron_check)


# #new csv
# result_2.to_csv(r"C:\Users\payal\Downloads\NBAStats\lebron_check.csv", index=False)
#result_2.to_csv("lebron_check.csv", index=False)


# #lebron_check = player_totals.player.str.contains("LeBron James", case=False, na=False)

# # if lebron_check == True:
# #     print("LeBron James is in the dataset.")
# # elif lebron_check == False:
# #     print("LeBron James is not in the dataset.")


# # if player == "LeBron James":
# #     print("LeBron James is in the dataset.")

# # print("df.columns below:")
# # print(result_2.columns.tolist())

# # print("df.shape below:")
# # print(result_2.shape)
# # Remove rows where age or PER is missing
# # plot_data = result_2.dropna(subset=["age", "pts"])

# # #Create the scatter plot

# # plt.figure(figsize=(25, 25))
# # plt.scatter(plot_data["age"], plot_data["pts"], alpha=0.7)

# # #Add labels and title
# # plt.title("Age vs Points")
# # plt.xlabel("Age")
# # plt.ylabel("Points")

# # #Optional: Add grid
# # plt.grid(True)

# # #Display the graph
# # plt.show()