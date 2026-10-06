# Python for Machine Learning & Data Preprocessing

## Project Overview

This project demonstrates the basic steps involved in preparing a student dataset for machine learning using Python.

The dataset contains student information such as age, city, study hours, and marks.

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Dataset

The original dataset is stored in:

`students.csv`

The dataset contains 8 student records and 5 columns:

- Name
- Age
- City
- Study_Hours
- Marks

## Data Preprocessing Steps

### 1. Load the Dataset

The dataset was loaded using Pandas:

```python
df = pd.read_csv("students.csv")