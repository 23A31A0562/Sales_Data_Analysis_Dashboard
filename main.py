from sales_analyzer.data_loader import DataLoader
from sales_analyzer.data_cleaner import DataCleaner
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.visualizer import Visualizer
from sales_analyzer.reporter import Reporter
import os

DATA_PATH = "sales_analyzer/data/raw/sales_data.csv"
OUTPUT_DIR = "data/reports"

def main():
    loader = DataLoader(DATA_PATH)
    df = loader.load_data()

    cleaner = DataCleaner()
    df = cleaner.clean(df)

    analyzer = SalesAnalyzer(df)
    summary = analyzer.basic_stats()
    monthly = analyzer.monthly_trends()
    category = analyzer.sales_by_category()

    visualizer = Visualizer(df, OUTPUT_DIR)
    visualizer.create_all()

    reporter = Reporter(df, summary, monthly, category)
    reporter.generate_excel_report(OUTPUT_DIR)

    print("✅ Sales analysis completed successfully")
    print("\n📊 SALES DATA ANALYSIS REPORT")
    print("=" * 30)
    print(f"💰 Total Sales: ${summary['total_sales']:.2f}")
    print(f"📈 Average Order Value: ${summary['average_order']:.2f}")
    print(f"🏆 Top Category: {category.index[0]}")


if __name__ == "__main__":
    main()
