import pandas as pd

df = pd.read_csv("students.csv")

print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())

print("Age median:", df["Age"].median())
print("City mode:", df["City"].mode()[0])

df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])
print(df.isnull().sum())

print("Duplicate rows:", df.duplicated().sum())

df = df.drop("Name", axis=1)

print(df.head())
print(df.columns)

df = pd.get_dummies(df, columns=["City"], dtype=int)

print(df.head())
print(df.columns)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[["Age", "Study_Hours", "Marks"]] = scaler.fit_transform(
    df[["Age", "Study_Hours", "Marks"]]
)

print(df)

print("Basic Statistics:")
print(df.describe())

import matplotlib.pyplot as plt

plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()


import os

os.makedirs("output", exist_ok=True)

df.to_csv("output/cleaned_students.csv", index=False)

print("Cleaned dataset saved successfully!")