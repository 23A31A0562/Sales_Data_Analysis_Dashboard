import pandas as pd

class SalesAnalyzer:
    def __init__(self, df):
        self.df = df

    def basic_stats(self):
        return {
            "total_sales": self.df["total_amount"].sum(),
            "average_order": self.df["total_amount"].mean(),
            "total_orders": len(self.df),
            "unique_customers": self.df["customer_id"].nunique()
        }

    def monthly_trends(self):
        self.df["month"] = self.df["order_date"].dt.to_period("M")
        return self.df.groupby("month")["total_amount"].sum()

    def sales_by_category(self):
        return self.df.groupby("category")["total_amount"].sum().sort_values(ascending=False)
