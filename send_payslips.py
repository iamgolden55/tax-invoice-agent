import pandas as pd
from tools.email_sender import send_invoice_email

# Load employee data
data = pd.read_csv("data/Employee_Salary_Dataset.csv")
print(data.columns)


for index, row in data.iterrows():
    # Simulate email
    employee_name = row['ID']
    receiver_email = f"{employee_name}@company.com"

    file_path = f"payslips/payslip_{index + 1}.pdf"

    subject = "Your Monthly Payslip"
    body = f"Hi {row['ID']},\n\nPlease find attached your payslip for this month.\n\nRegards,\nPayroll Team"

    result = send_invoice_email(receiver_email, subject, body, file_path)
    print(result)
