import os
import pandas as pd

class Reporter:
    def __init__(self, df, summary, monthly, category):
        self.df = df
        self.summary = summary
        self.monthly = monthly
        self.category = category

    def generate_excel_report(self, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        report_path = os.path.join(output_dir, "sales_report.xlsx")

        with pd.ExcelWriter(report_path, engine="openpyxl") as writer:
            # Summary sheet
            pd.DataFrame([self.summary]).to_excel(
                writer, sheet_name="Summary", index=False
            )

            # Monthly trends
            self.monthly.to_excel(writer, sheet_name="Monthly Trends")

            # Category analysis
            self.category.to_excel(writer, sheet_name="Category Analysis")

            # Raw sample data
            self.df.head(1000).to_excel(
                writer, sheet_name="Sample Data", index=False
            )

        print(f"📊 Excel report generated at: {report_path}")
