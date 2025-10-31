import pandas as pd
from fpdf import FPDF
import os
from datetime import datetime

# Create output folder
output_folder = "invoices"
os.makedirs(output_folder, exist_ok=True)

# Read and clean input
df = pd.read_excel("clients.xlsx")
df.columns = df.columns.str.strip()

# Generate invoices
for index, row in df.iterrows():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "INVOICE", ln=True, align="C")
    pdf.ln(5)

    # Invoice metadata
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, f"Invoice #: {1000 + index}", ln=True)
    pdf.cell(100, 10, f"Date: {datetime.today().strftime('%d-%m-%Y')}", ln=True)
    pdf.ln(5)

    # Company info
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "From:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 8, "Kashyap Solutions", ln=True)
    pdf.cell(100, 8, "Rajkot, Gujarat", ln=True)
    pdf.cell(100, 8, "Email: support@kashyap.dev", ln=True)
    pdf.ln(5)

    # Client info
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "Bill To:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 8, f"{row['Client Name']}", ln=True)
    pdf.cell(100, 8, f"{row['Email']}", ln=True)
    pdf.ln(10)

    # Service table
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "Service Details", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(120, 10, "Service", border=1, fill=True)
    pdf.cell(40, 10, "Amount (Rs.)", border=1, ln=True, fill=True)

    pdf.cell(120, 10, row['Service'], border=1)
    pdf.cell(40, 10, str(row['Amount']), border=1, ln=True)

    # Footer
    pdf.ln(15)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, "Thank you for your business!", ln=True, align="C")

    filename = f"{output_folder}/invoice_{index+1}.pdf"
    pdf.output(filename)

print(f"✅ {len(df)} professional invoices saved in '{output_folder}/'")