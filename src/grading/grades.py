#! /usr/bin/env python
import pandas as pd
from pandas.api.types import CategoricalDtype

grades = pd.read_csv("grades.csv", dtype="string")

assert "Sum" in grades.columns

assert "90" == input("Enter 90 to confirm that the exam has 90 points max")
assert "bonus" == input(
    "Type bonus to confirm that all exams are passed without the bonus points."
)

grades["Grade"] = ""

# 5% steps between 1.0 (90 points) and 4.0 (45 points)
for index, row in grades.iterrows():
    if int(row["Sum"]) >= 85.5:
        grades.at[index, "Grade"] = "1.0"
    elif int(row["Sum"]) >= 81:
        grades.at[index, "Grade"] = "1.3"
    elif int(row["Sum"]) >= 76.5:
        grades.at[index, "Grade"] = "1.7"
    elif int(row["Sum"]) >= 72:
        grades.at[index, "Grade"] = "2.0"
    elif int(row["Sum"]) >= 67.5:
        grades.at[index, "Grade"] = "2.3"
    elif int(row["Sum"]) >= 63:
        grades.at[index, "Grade"] = "2.7"
    elif int(row["Sum"]) >= 58.5:
        grades.at[index, "Grade"] = "3.0"
    elif int(row["Sum"]) >= 54:
        grades.at[index, "Grade"] = "3.3"
    elif int(row["Sum"]) >= 49.5:
        grades.at[index, "Grade"] = "3.7"
    elif int(row["Sum"]) >= 45:
        grades.at[index, "Grade"] = "4.0"
    # less than 4.0 -> 5.0
    else:
        grades.at[index, "Grade"] = "5.0"

grades.sort_values(by=["Grade"], inplace=True)

print("Grades:")
print(grades)

cat_dtype = CategoricalDtype(
    categories=[
        "1.0",
        "1.3",
        "1.7",
        "2.0",
        "2.3",
        "2.7",
        "3.0",
        "3.3",
        "3.7",
        "4.0",
        "4.3",
        "4.7",
        "5.0",
    ],
    ordered=True,
)
grades["Grade"] = grades["Grade"].astype(cat_dtype)

distribution = grades["Grade"].value_counts()[cat_dtype.categories]

print("\nDistribution:")
print(distribution)

print("\nAverage: %.2f\n" % grades["Grade"].astype(float).mean())

grades.to_csv("grades_updated.csv")

# TODO : should produce a report for Flexnow
