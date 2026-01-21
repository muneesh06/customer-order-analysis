def total_revenue(df):
    return df["Price"].sum()

print("Total Revenue:", total_revenue(df))