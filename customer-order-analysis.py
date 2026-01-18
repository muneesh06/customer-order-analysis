# ==========================================
# Customer Order Analysis Project
# ==========================================

from collections import defaultdict

# ----------------------------
# Sample Dataset
# ----------------------------
orders = [
    {"customer": "Alice", "product": "Laptop", "category": "Electronics", "price": 1200},
    {"customer": "Bob", "product": "T-Shirt", "category": "Clothing", "price": 25},
    {"customer": "Alice", "product": "Headphones", "category": "Electronics", "price": 150},
    {"customer": "Charlie", "product": "Shoes", "category": "Clothing", "price": 80},
    {"customer": "Bob", "product": "Watch", "category": "Accessories", "price": 200},
    {"customer": "Alice", "product": "Mouse", "category": "Electronics", "price": 50},
    {"customer": "David", "product": "Keyboard", "category": "Electronics", "price": 100},
    {"customer": "Charlie", "product": "Jacket", "category": "Clothing", "price": 120},
]

# ----------------------------
# 1. Total Revenue
# ----------------------------
def total_revenue(data):
    return sum(order["price"] for order in data)

# ----------------------------
# 2. Revenue by Category
# ----------------------------
def revenue_by_category(data):
    category_revenue = defaultdict(int)
    for order in data:
        category_revenue[order["category"]] += order["price"]
    return dict(category_revenue)

# ----------------------------
# 3. Top Customer
# ----------------------------
def top_customer(data):
    customer_spend = defaultdict(int)
    for order in data:
        customer_spend[order["customer"]] += order["price"]
    return max(customer_spend, key=customer_spend.get)

# ----------------------------
# 4. Most Popular Product
# ----------------------------
def most_popular_product(data):
    product_count = defaultdict(int)
    for order in data:
        product_count[order["product"]] += 1
    return max(product_count, key=product_count.get)

# ----------------------------
# 5. Average Order Value
# ----------------------------
def average_order_value(data):
    return total_revenue(data) / len(data)

# ----------------------------
# 6. Customer Segmentation
# ----------------------------
def customer_segmentation(data):
    customer_spend = defaultdict(int)
    for order in data:
        customer_spend[order["customer"]] += order["price"]

    segmentation = {}
    for customer, spend in customer_spend.items():
        if spend > 1000:
            segmentation[customer] = "High Value"
        elif spend > 300:
            segmentation[customer] = "Medium Value"
        else:
            segmentation[customer] = "Low Value"
    return segmentation

# ----------------------------
# 7. Display Results
# ----------------------------
def generate_report(data):
    print("\n====== Customer Order Analysis Report ======\n")

    print(f"Total Revenue: ${total_revenue(data)}")

    print("\nRevenue by Category:")
    for category, revenue in revenue_by_category(data).items():
        print(f"  {category}: ${revenue}")

    print(f"\nTop Customer: {top_customer(data)}")

    print(f"Most Popular Product: {most_popular_product(data)}")

    print(f"Average Order Value: ${average_order_value(data):.2f}")

    print("\nCustomer Segmentation:")
    for customer, segment in customer_segmentation(data).items():
        print(f"  {customer}: {segment}")

    print("\n===========================================\n")

# ----------------------------
# Run Program
# ----------------------------
if __name__ == "__main__":
    generate_report(orders)