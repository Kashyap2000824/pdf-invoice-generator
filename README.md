# 🧾 PDF Invoice Generator

Hi! This is a Python script I built to generate professional PDF invoices from an Excel file. It reads client data, formats each invoice with proper layout, and saves them into a clean `invoices/` folder — perfect for freelancers, small businesses, or Fiverr delivery.

---

## 🔧 What It Does
- Reads client data from `clients.xlsx`
- Generates one invoice per client
- Adds:
  - Invoice number and date
  - Company and client blocks
  - Service table with borders
  - Footer message
- Saves each invoice as `invoice_1.pdf`, `invoice_2.pdf`, etc.

---

## 🛠️ Tools Used
- `pandas` for reading Excel
- `fpdf` for generating PDFs
- `os` and `datetime` for folder and date handling

---

## 🚀 How to Run It
1. Make sure you have Python installed
2. Install the required libraries:
    ```bash
    pip install pandas fpdf
    ```
3. Place your input file as `clients.xlsx` in the same folder
4. Run the script:
    ```bash
    python invoice_generator.py
    ```
5. Check the `invoices/` folder for your PDF files

---

## 📁 Sample Input

| Client Name | Email              | Service        | Amount |
|-------------|--------------------|----------------|--------|
| Raj Patel   | raj@example.com    | Web Design     | 5000   |
| Meera Shah  | meera@example.com  | SEO Audit      | 3000   |

---

## 📦 Sample Output

Each invoice includes:
    INVOICE

Invoice #: 1001
Date: 31-10-2025

From:
Kashyap Solutions
Rajkot, Gujarat
Email: support@kashyap.dev

Bill To:
Raj Patel
raj@example.com

Service Details:
| Web Design | Rs. 5000 |

Thank you for your business!
'


Saved as: `invoices/invoice_1.pdf`, `invoices/invoice_2.pdf`, etc.

---

## 📌 Use Cases
- Freelance billing
- Small business invoicing
- Fiverr automation gigs
- Client-ready PDF generation
