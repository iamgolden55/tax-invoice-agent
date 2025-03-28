from tools.email_sender import send_invoice_email

result = send_invoice_email(
    receiver_email="eruwagolden@gmail.com",
    subject="Your Invoice from Chase Bank",
    body="Hi, please find attached your invoice.",
    attachment_path="invoices/invoice_001.pdf"
)

print(result)
