from reportlab.pdfgen import canvas
c = canvas.Canvas("output-001.pdf")
c.setFont("ZapfDingbats", 12)
c.drawString(100, 750, "Hello pdf!")
c.drawString(200, 750, "Right!")
c.drawString(100, 650, "Down!")
c.showPage()
c.save()