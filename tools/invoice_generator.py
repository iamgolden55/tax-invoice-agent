from fpdf import FPDF
import os

def generate_invoice(customer_name, invoice_date, amount, invoice_id):
    # Create Invoice Directory if not exist
    if not os.path.exists("invoices"):
        os.makedirs("invoices")

    file_name = f"invoices/invoice_{invoice_id}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Invoice content
    pdf.cell(200, 10, txt="Chase Bank - Invoice", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Invoice ID: {invoice_id}", ln=True)
    pdf.cell(200, 10, txt=f"Customer Name: {customer_name}", ln=True)
    pdf.cell(200, 10, txt=f"Invoice Date: {invoice_date}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: ${amount}", ln=True)

    pdf.output(file_name)
    return file_name
