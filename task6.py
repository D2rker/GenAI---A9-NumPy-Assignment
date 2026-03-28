import numpy as np

marks = np.array([50, 80, 25, 0, 24, 7, 19, 99, 56, 88])
sorted_marks = np.sort(marks)
print(F"sorted_marks: {sorted_marks}")

# Find Percentiles
P25 = np.percentile(marks, 25)
P50 = np.percentile(marks, 50)
P75 = np.percentile(marks, 75)

print(f"25 percentile : {P25}")
print(f"75 percentile : {P50}")
print(f"75 percentile : {P75}")

# count how many students scored above average marks.
average_marks = np.mean(marks)
above_average_marks = np.mean(marks > average_marks)
print(f"{above_average_marks} students scored above average marks")
