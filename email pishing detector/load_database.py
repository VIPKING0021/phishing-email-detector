# import os

# folder_path = "D:\dataset"
# files = os.listdir(folder_path)

# for file in files:
#     if file.endswith(".csv"):
#         print(file)


import pandas as pd

data = pd.read_csv(r"D:\dataset\Phishing_Email.csv")
print(data.head())
