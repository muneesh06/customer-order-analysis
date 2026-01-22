def revenue_by_category(df):
    return df.groupby("Category")["Price"].sum()

print(revenue_by_category(df))