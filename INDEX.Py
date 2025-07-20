import pandas as pd
from fpdf import FPDF

# Load data
data = pd.read_csv('sample_data.csv')

# Analyze
average_value = data['Sales'].mean()
total_entries = len(data)
category_summary = data.groupby('Category')['Sales'].sum()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Sales Report", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, f"Total Entries: {total_entries}", ln=True)
pdf.cell(200, 10, f"Average Sales: 'Rs'{average_value:.2f}", ln=True)

pdf.ln(10)
pdf.cell(200, 10, "Sales by Category:", ln=True)
for category, sales in category_summary.items():
    pdf.cell(200, 10, f"{category}: 'Rs'{sales:.2f}", ln=True)

# Save PDF
pdf.output("sales_report.pdf")
