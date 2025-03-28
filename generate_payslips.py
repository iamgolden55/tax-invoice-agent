import pandas as pd
from fpdf import FPDF
import os

# Load dataset
data = pd.read_csv("data/Employee_Salary_Dataset.csv")

# Create directory to store payslips
if not os.path.exists("payslips"):
    os.makedirs("payslips")

# Loop through employees and generate PDF
for index, row in data.iterrows():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Company - Employee Payslip", ln=True, align="C")
    pdf.ln(10)

    # Auto-load all columns
    for col in data.columns:
        pdf.cell(200, 10, txt=f"{col}: {row[col]}", ln=True)

    file_path = f"payslips/payslip_{index + 1}.pdf"
    pdf.output(file_path)

    print(f"✅ Payslip generated for {row[0]} → {file_path}")

