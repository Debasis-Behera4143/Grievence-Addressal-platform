import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(ticket_id: str, data: dict):
    """
    Generate PDF report for grievance complaint.
    
    Args:
        ticket_id (str): Unique ticket identifier
        data (dict): Complaint details dictionary
        
    Returns:
        str: File path of generated PDF
    """

    # Create reports folder if not exists
    os.makedirs("reports", exist_ok=True)

    file_path = f"reports/Grievance_{ticket_id}.pdf"

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50

    # ================= HEADER =================
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, y, "GOVERNMENT OF INDIA")
    y -= 25

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width / 2, y, "AI-POWERED GRIEVANCE REDRESSAL SYSTEM")
    y -= 40

    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Ticket ID: {ticket_id}")
    y -= 30

    # ================= BODY =================
    for key, value in data.items():
        if y < 80:
            c.showPage()
            c.setFont("Helvetica", 11)
            y = height - 50

        c.setFont("Helvetica-Bold", 11)
        c.drawString(50, y, f"{key}:")
        c.setFont("Helvetica", 11)
        c.drawString(180, y, str(value))
        y -= 20

    # ================= FOOTER =================
    y -= 30
    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(
        width / 2,
        y,
        "National AI Redressal Framework | 2026"
    )

    c.save()
    return file_path
