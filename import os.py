import os
import pandas as pd

# Change to your dataset folder
os.chdir(r"C:\Users\payal\Downloads\NBAStats")

# Read the CSV files
advanced = pd.read_csv("Advanced.csv")
all_star = pd.read_csv("All-Star Selections.csv")
player_totals = pd.read_csv("Player Totals.csv")

# Remove extra spaces
advanced.columns = advanced.columns.str.strip()
all_star.columns = all_star.columns.str.strip()
player_totals.columns = player_totals.columns.str.strip()

# Keep only the columns we need
#advanced = advanced[["player_id", "pos"]]

# Keep only ONE row per player
#advanced = advanced.drop_duplicates(subset="player_id")

# Keep only ONE All-Star row per player
#all_star = all_star.drop_duplicates(subset="player_id")

# Merge
result = pd.merge(
    all_star,
    advanced,
    on="player_id",
    how="left"
)
print(pd.read_csv("All_Star_With_Pos.csv").head(5))
# Save
#result.to_csv("All_Star_With_Pos.csv", index=False)

#print(f"\nUnique Players: {len(result)}")

result = pd.concat([advanced, all_star, player_totals], axis=0,)
print(result.head(30))