# file: order_analysis.py

orders = [120, 340, 560, 230, 150]

def total_sales(data):
    return sum(data)

def average_sales(data):
    return sum(data) / len(data)

print("Total Sales:", total_sales(orders))
print("Average Sales:", average_sales(orders))