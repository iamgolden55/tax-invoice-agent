from tools.invoice_generator import generate_invoice

# Test the function
file = generate_invoice("Golden Nini", "2025-03-28", "250.00", "001")
print(f"✅ Invoice generated at: {file}")
