import os
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, df, output_dir="data/reports"):
        self.df = df
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def create_all(self):
        self.monthly_sales_trend()
        self.category_sales_chart()

    def monthly_sales_trend(self):
        monthly = self.df.groupby("month")["total_amount"].sum()
        plt.figure(figsize=(8, 5))
        monthly.plot(kind="line", marker="o")
        plt.title("Monthly Sales Trend")
        plt.ylabel("Total Sales")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/monthly_sales.png")
        plt.close()

    def category_sales_chart(self):
        category = self.df.groupby("category")["total_amount"].sum()
        plt.figure(figsize=(8, 5))
        category.plot(kind="bar")
        plt.title("Sales by Category")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/category_sales.png")
        plt.close()
