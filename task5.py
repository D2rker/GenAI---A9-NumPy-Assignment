import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
mean_marks = np.mean(marks)
median_marks = np.median(marks)
variance_marks = np.var(marks)
standard_deviation_marks = np.std(marks)
minimum_marks = np.min(marks)
maximum_marks = np.max(marks)
range_marks = maximum_marks - minimum_marks

print(f"mean_marks: {mean_marks}")
print(f"median_marks: {median_marks}")
print(f"variance_marks: {variance_marks}")
print(f"standard_deviation_marks: {standard_deviation_marks}")
print(f"minimum_marks: {minimum_marks}")
print(f"maximum_marks: {maximum_marks}")
print(f"range_marks: {range_marks}")
