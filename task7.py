import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

# total weekly sales
total_sales = np.sum(sales)
print(f"{total_sales} total sales")

# average daily sales
average_sales= np.mean(sales)
print(f"{average_sales} average sales")

# highest & lowest sales day
max_sales = np.max(sales)
min_sales = np.min(sales)
print(f"sales range highest/lowest sales: {max_sales} / {min_sales}")

# standard deviation of sales
standard_deviation = np.std(sales)
print(f"{standard_deviation} standard deviation")

# identify days where sales are above average
above_average_marks = sales > average_sales
average_sales_values = sales[above_average_marks]
print(f"{average_sales_values} average sales values")