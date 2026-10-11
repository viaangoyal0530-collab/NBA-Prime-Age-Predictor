import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor


# ============================================================
# SETUP
# ============================================================

os.chdir(r"C:\Users\payal\Downloads\NBAStats")

# Read Player Totals CSV
player_totals = pd.read_csv("Player Totals.csv")

# Remove extra spaces from column names
player_totals.columns = player_totals.columns.str.strip()

# Keep only the columns we need
player_totals = player_totals[
    ["player", "player_id", "season", "age", "g", "gs",
     "mp", "trb", "ast", "pts", "fg_percent"]
].copy()

# Make player names lowercase
player_totals["player"] = (
    player_totals["player"]
    .str.lower()
    .str.strip()
)


# ============================================================
# CLEAN DATA
# ============================================================

# Remove rows missing important information
player_totals = player_totals.dropna(
    subset=[
        "player",
        "player_id",
        "age",
        "g",
        "pts",
        "trb",
        "ast"
    ]
)

# Remove seasons where the player played zero games
player_totals = player_totals[player_totals["g"] > 0]


# ============================================================
# CALCULATE PER-GAME STATISTICS
# ============================================================

player_totals["ppg"] = (
    player_totals["pts"] / player_totals["g"]
)

player_totals["rpg"] = (
    player_totals["trb"] / player_totals["g"]
)

player_totals["apg"] = (
    player_totals["ast"] / player_totals["g"]
)


# ============================================================
# CREATE PRIME SCORE
# ============================================================

# We use several statistics to determine how good
# each season was.

player_totals["prime_score"] = (
    player_totals["ppg"] * 0.40 +
    player_totals["rpg"] * 0.20 +
    player_totals["apg"] * 0.20 +
    player_totals["fg_percent"] * 10 * 0.10 +
    (player_totals["g"] / 82) * 0.10
)


# ============================================================
# FIND EACH PLAYER'S HISTORICAL PRIME AGE
# ============================================================

# Find the season with the highest Prime Score
# for every player.

prime_seasons = player_totals.loc[
    player_totals.groupby("player_id")["prime_score"].idxmax()
].copy()


# Keep the player's ID and prime age
prime_ages = prime_seasons[
    ["player_id", "age"]
].rename(
    columns={"age": "prime_age"}
)


# ============================================================
# CREATE MACHINE LEARNING DATASET
# ============================================================

# Add each player's prime age to their season data

ml_data = player_totals.merge(
    prime_ages,
    on="player_id",
    how="left"
)


# Remove rows without a prime age
ml_data = ml_data.dropna(
    subset=["prime_age"]
)


# ============================================================
# RANDOM FOREST FEATURES
# ============================================================

features = [
    "age",
    "g",
    "gs",
    "mp",
    "ppg",
    "rpg",
    "apg",
    "fg_percent"
]


X = ml_data[features]

# Target = player's historical prime age
y = ml_data["prime_age"]


# ============================================================
# TRAIN RANDOM FOREST
# ============================================================

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=10,
    min_samples_leaf=3,
    random_state=42
)

model.fit(X, y)

print("\nRandom Forest model trained successfully!")


# ============================================================
# ASK USER WHICH PLAYER TO ANALYZE
# ============================================================

player_input = input(
    "\nWhich player do you want to analyze? "
    "(Press Enter to analyze LeBron James): "
).strip().lower()


# Default to LeBron James
if player_input == "":
    player_input = "lebron james"


# Check if player exists
if player_input not in player_totals["player"].values:

    print(f"\n{player_input} is not in the dataset.")
    print("Please check the spelling and try again.")

    raise SystemExit


print(f"\nAnalyzing stats for {player_input.title()}...")


# ============================================================
# GET PLAYER DATA
# ============================================================

player_data = player_totals[
    player_totals["player"] == player_input
].copy()

# Sort by season
player_data = player_data.sort_values("season")


# ============================================================
# CURRENT / MOST RECENT SEASON
# ============================================================

current_season = player_data.iloc[-1]


# ============================================================
# PREDICT PRIME AGE
# ============================================================

# Get the features from the player's most recent season

current_features = current_season[
    features
].to_frame().T


# Ask Random Forest to predict prime age

predicted_prime_age = model.predict(
    current_features
)[0]


# Round prediction
predicted_prime_age = round(
    predicted_prime_age,
    1
)


# ============================================================
# DETERMINE PRIME STATUS
# ============================================================

current_age = current_season["age"]

years_until_prime = (
    predicted_prime_age - current_age
)


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n" + "=" * 60)
print("                 NBA PRIME PREDICTOR")
print("=" * 60)

print(f"\nPlayer: {player_input.title()}")


# ------------------------------------------------------------
# CURRENT SEASON
# ------------------------------------------------------------

print("\nCURRENT / MOST RECENT SEASON")
print("-" * 40)

print(
    f"Season:       {current_season['season']}"
)

print(
    f"Age:          {current_age}"
)

print(
    f"PPG:          {current_season['ppg']:.2f}"
)

print(
    f"RPG:          {current_season['rpg']:.2f}"
)

print(
    f"APG:          {current_season['apg']:.2f}"
)

print(
    f"FG%:          {current_season['fg_percent']:.3f}"
)


# ------------------------------------------------------------
# RANDOM FOREST PREDICTION
# ------------------------------------------------------------

print("\nRANDOM FOREST PREDICTION")
print("-" * 40)

print(
    f"Predicted Prime Age: "
    f"{predicted_prime_age}"
)


# ------------------------------------------------------------
# PRIME STATUS
# ------------------------------------------------------------

if predicted_prime_age > current_age:

    print(
        "\nPrime Status: "
        "PRIME IS PROJECTED TO BE AHEAD"
    )

    print(
        f"Approximate years until prime: "
        f"{years_until_prime:.1f}"
    )

elif predicted_prime_age < current_age:

    print(
        "\nPrime Status: "
        "PRIME IS PROJECTED TO HAVE PASSED"
    )

    print(
        f"Predicted prime age: "
        f"{predicted_prime_age}"
    )

else:

    print(
        "\nPrime Status: "
        "PLAYER IS AROUND THEIR PREDICTED PRIME"
    )


# ============================================================
# HISTORICAL PRIME
# ============================================================

historical_prime = player_data.loc[
    player_data["prime_score"].idxmax()
]


print("\nHISTORICAL BEST SEASON")
print("-" * 40)

print(
    f"Season:       "
    f"{historical_prime['season']}"
)

print(
    f"Age:          "
    f"{historical_prime['age']}"
)

print(
    f"PPG:          "
    f"{historical_prime['ppg']:.2f}"
)

print(
    f"RPG:          "
    f"{historical_prime['rpg']:.2f}"
)

print(
    f"APG:          "
    f"{historical_prime['apg']:.2f}"
)

print(
    f"FG%:          "
    f"{historical_prime['fg_percent']:.3f}"
)

print(
    f"Prime Score:  "
    f"{historical_prime['prime_score']:.2f}"
)


# ============================================================
# CAREER TOTALS
# ============================================================

career_games = player_data["g"].sum()

career_points = player_data["pts"].sum()

career_rebounds = player_data["trb"].sum()

career_assists = player_data["ast"].sum()

career_minutes = player_data["mp"].sum()


# ============================================================
# CAREER AVERAGES
# ============================================================

ppg = career_points / career_games

rpg = career_rebounds / career_games

apg = career_assists / career_games


print("\nCAREER TOTALS")
print("-" * 40)

print(
    f"Games:        {career_games:,.0f}"
)

print(
    f"Points:       {career_points:,.0f}"
)

print(
    f"Rebounds:     {career_rebounds:,.0f}"
)

print(
    f"Assists:      {career_assists:,.0f}"
)

print(
    f"Minutes:      {career_minutes:,.0f}"
)


print("\nCAREER AVERAGES")
print("-" * 40)

print(
    f"PPG:          {ppg:.2f}"
)

print(
    f"RPG:          {rpg:.2f}"
)

print(
    f"APG:          {apg:.2f}"
)


# ============================================================
# SEASON-BY-SEASON DATA
# ============================================================

print("\nSEASON-BY-SEASON STATS")
print("-" * 60)

print(
    player_data[
        [
            "season",
            "age",
            "g",
            "ppg",
            "rpg",
            "apg",
            "fg_percent",
            "prime_score"
        ]
    ].to_string(index=False)
)