import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Change to correct directory
os.chdir(r"C:\Users\payal\Downloads\NBAStats")

# Read Player Totals CSV
player_totals = pd.read_csv("Player Totals.csv")

# Remove extra spaces from column names
player_totals.columns = player_totals.columns.str.strip()

# Keep only the columns we need
player_totals = player_totals[
    ["player", "player_id", "season", "age", "g", "gs",
     "mp", "trb", "ast", "pts", "fg_percent"]
]

player_totals["player"] = player_totals["player"].str.lower()





# Ask the user which player they want to analyze
player_input = input(
    "Which player do you want to analyze? "
    "(Press Enter to analyze LeBron James): "
).strip().lower()

# Default to LeBron James
if player_input == "":
    player_input = "lebron james"

# Check if player exists
if player_input not in player_totals["player"].values:
    print(f"\n{player_input} is not in the dataset.")
    print("Please check the spelling and try again.") 
    exit().lower()

print(f"\nAnalyzing stats for {player_input}...")

# Get all data for that player
player_data = player_totals[
    player_totals["player"] == player_input
].copy()

# Sort by season
player_data = player_data.sort_values("season")

# -----------------------------------------
# CAREER TOTALS
# -----------------------------------------

career_games = player_data["g"].sum()
career_points = player_data["pts"].sum()
career_rebounds = player_data["trb"].sum()
career_assists = player_data["ast"].sum()
career_minutes = player_data["mp"].sum()

# -----------------------------------------
# CAREER AVERAGES
# -----------------------------------------

ppg = career_points / career_games
rpg = career_rebounds / career_games
apg = career_assists / career_games

# Weighted field-goal percentage
total_fg_made = (
    player_data["fg_percent"] * player_data["mp"]
).sum()

average_fg = total_fg_made / player_data["mp"].sum()

# -----------------------------------------
# BEST SCORING SEASON
# -----------------------------------------

# Calculate points per game for every season
player_data["ppg"] = player_data["pts"] / player_data["g"]

best_scoring_season = player_data.loc[
    player_data["ppg"].idxmax()
]

# -----------------------------------------
# DISPLAY RESULTS
# -----------------------------------------

print("\n" + "=" * 50)
print("             NBA PLAYER ANALYZER")
print("=" * 50)

print(f"\nPlayer: {player_input}")

print("\nCAREER TOTALS")
print("-" * 30)
print(f"Games:       {career_games:,.0f}")
print(f"Points:      {career_points:,.0f}")
print(f"Rebounds:    {career_rebounds:,.0f}")
print(f"Assists:     {career_assists:,.0f}")
print(f"Minutes:     {career_minutes:,.0f}")

print("\nCAREER AVERAGES")
print("-" * 30)
print(f"PPG:         {ppg:.2f}")
print(f"RPG:         {rpg:.2f}")
print(f"APG:         {apg:.2f}")
print(f"FG%:         {average_fg:.3f}")

print("\nBEST SCORING SEASON")
print("-" * 30)
print(f"Season:      {best_scoring_season['season']}")
print(f"Age:         {best_scoring_season['age']}")
print(f"PPG:         {best_scoring_season['ppg']:.2f}")
print(f"Points:      {best_scoring_season['pts']:,.0f}")

# -----------------------------------------
# SEASON-BY-SEASON DATA
# -----------------------------------------

print("\nSEASON-BY-SEASON STATS")
print("-" * 50)

print(
    player_data[
        ["season", "age", "g", "pts", "trb", "ast",
         "fg_percent", "ppg"]
    ].to_string(index=False)
)

# -----------------------------------------
# CREATE GRAPH
# -----------------------------------------

# plt.figure(figsize=(12, 7))

# plt.plot(
#     player_data["season"],
#     player_data["ppg"],
#     marker="o",
#     label="PPG"
# )

# plt.plot(
#     player_data["season"],
#     player_data["trb"] / player_data["g"],
#     marker="o",
#     label="RPG"
# )

# plt.plot(
#     player_data["season"],
#     player_data["ast"] / player_data["g"],
#     marker="o",
#     label="APG"
# )

# plt.title(f"{player_input} - Career Statistics")
# plt.xlabel("Season")
# plt.ylabel("Per Game Statistics")

# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Change to correct directory
os.chdir(r"C:\Users\payal\Downloads\NBAStats")

# Read Player Totals CSV
player_totals = pd.read_csv("Player Totals.csv")

# Remove extra spaces from column names
player_totals.columns = player_totals.columns.str.strip()

# Keep only the columns we need
player_totals = player_totals[
    ["player", "player_id", "season", "age", "g", "gs",
     "mp", "trb", "ast", "pts", "fg_percent"]
]

player_totals["player"] = player_totals["player"].str.lower()





# Ask the user which player they want to analyze
player_input = input(
    "Which player do you want to analyze? "
    "(Press Enter to analyze LeBron James): "
).strip().lower()

# Default to LeBron James
if player_input == "":
    player_input = "lebron james"

# Check if player exists
if player_input not in player_totals["player"].values:
    print(f"\n{player_input} is not in the dataset.")
    print("Please check the spelling and try again.") 
    exit().lower()

print(f"\nAnalyzing stats for {player_input}...")

# Get all data for that player
player_data = player_totals[
    player_totals["player"] == player_input
].copy()

# Sort by season
player_data = player_data.sort_values("season")

# -----------------------------------------
# CAREER TOTALS
# -----------------------------------------

career_games = player_data["g"].sum()
career_points = player_data["pts"].sum()
career_rebounds = player_data["trb"].sum()
career_assists = player_data["ast"].sum()
career_minutes = player_data["mp"].sum()

# -----------------------------------------
# CAREER AVERAGES
# -----------------------------------------

ppg = career_points / career_games
rpg = career_rebounds / career_games
apg = career_assists / career_games

# Weighted field-goal percentage
total_fg_made = (
    player_data["fg_percent"] * player_data["mp"]
).sum()

average_fg = total_fg_made / player_data["mp"].sum()

# -----------------------------------------
# BEST SCORING SEASON
# -----------------------------------------

# Calculate points per game for every season
player_data["ppg"] = player_data["pts"] / player_data["g"]

best_scoring_season = player_data.loc[
    player_data["ppg"].idxmax()
]

# -----------------------------------------
# DISPLAY RESULTS
# -----------------------------------------

print("\n" + "=" * 50)
print("             NBA PLAYER ANALYZER")
print("=" * 50)

print(f"\nPlayer: {player_input}")

print("\nCAREER TOTALS")
print("-" * 30)
print(f"Games:       {career_games:,.0f}")
print(f"Points:      {career_points:,.0f}")
print(f"Rebounds:    {career_rebounds:,.0f}")
print(f"Assists:     {career_assists:,.0f}")
print(f"Minutes:     {career_minutes:,.0f}")

print("\nCAREER AVERAGES")
print("-" * 30)
print(f"PPG:         {ppg:.2f}")
print(f"RPG:         {rpg:.2f}")
print(f"APG:         {apg:.2f}")
print(f"FG%:         {average_fg:.3f}")

print("\nBEST SCORING SEASON")
print("-" * 30)
print(f"Season:      {best_scoring_season['season']}")
print(f"Age:         {best_scoring_season['age']}")
print(f"PPG:         {best_scoring_season['ppg']:.2f}")
print(f"Points:      {best_scoring_season['pts']:,.0f}")

# -----------------------------------------
# SEASON-BY-SEASON DATA
# -----------------------------------------

print("\nSEASON-BY-SEASON STATS")
print("-" * 50)

print(
    player_data[
        ["season", "age", "g", "pts", "trb", "ast",
         "fg_percent", "ppg"]
    ].to_string(index=False)
)

# -----------------------------------------
# CREATE GRAPH
# -----------------------------------------

# plt.figure(figsize=(12, 7))

# plt.plot(
#     player_data["season"],
#     player_data["ppg"],
#     marker="o",
#     label="PPG"
# )

# plt.plot(
#     player_data["season"],
#     player_data["trb"] / player_data["g"],
#     marker="o",
#     label="RPG"
# )

# plt.plot(
#     player_data["season"],
#     player_data["ast"] / player_data["g"],
#     marker="o",
#     label="APG"
# )

# plt.title(f"{player_input} - Career Statistics")
# plt.xlabel("Season")
# plt.ylabel("Per Game Statistics")

# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()