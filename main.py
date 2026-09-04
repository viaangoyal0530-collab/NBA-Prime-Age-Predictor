import os
import pandas as pd

BASE_PATH = r"C:\Users\payal\Downloads\archive"

advanced = pd.read_csv(os.path.join(BASE_PATH, "Player Advanced.csv"))
all_star = pd.read_csv(os.path.join(BASE_PATH, "All-Star Selections.csv"))
draft = pd.read_csv(os.path.join(BASE_PATH, "Draft History.csv"))

print(advanced.head())
print(all_star.head())
print(draft.head())