from reportlab.pdfgen import canvas
c = canvas.Canvas("output-001.pdf")
c.drawString(100, 750, "Hello pdf!")
c.drawString(100, 650, "Down!")
c.showPage()
c.save()