# ==========================================
# Sales Data Analysis Project
# ==========================================

import pandas as pd

# ----------------------------
# Load CSV Data
# ----------------------------
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!\n")
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None

# ----------------------------
# Total Revenue
# ----------------------------
def total_revenue(df):
    return df["Price"].sum()

# ----------------------------
# Revenue by Category
# ----------------------------
def revenue_by_category(df):
    return df.groupby("Category")["Price"].sum().sort_values(ascending=False)

# ----------------------------
# Top Customers
# ----------------------------
def top_customers(df):
    return df.groupby("Customer")["Price"].sum().sort_values(ascending=False).head(5)

# ----------------------------
# Most Sold Products
# ----------------------------
def most_sold_products(df):
    return df["Product"].value_counts().head(5)

# ----------------------------
# Save Report
# ----------------------------
def save_report(df):
    report = {
        "Total Revenue": total_revenue(df),
        "Top Customers": top_customers(df).to_dict(),
        "Revenue by Category": revenue_by_category(df).to_dict(),
        "Most Sold Products": most_sold_products(df).to_dict(),
    }

    report_df = pd.DataFrame.from_dict(report, orient='index')
    report_df.to_csv("report_output.csv")
    print("Report saved to report_output.csv")

# ----------------------------
# Main Function
# ----------------------------
def main():
    df = load_data("sales_data.csv")

    if df is not None:
        print("===== SALES ANALYSIS =====\n")

        print("Total Revenue:", total_revenue(df), "\n")

        print("Top Customers:\n", top_customers(df), "\n")

        print("Revenue by Category:\n", revenue_by_category(df), "\n")

        print("Most Sold Products:\n", most_sold_products(df), "\n")

        save_report(df)

# ----------------------------
# Run
# ----------------------------
if __name__ == "__main__":
    main()