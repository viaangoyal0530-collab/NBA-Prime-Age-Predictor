import os

path = r"C:\Users\payal\.cache\kagglehub\datasets\wyattowalsh\basketball"

print("Folder exists:", os.path.exists(path))

if os.path.exists(path):
    for root, dirs, files in os.walk(path):
        print(root)
        for file in files:
            print("   ", file)