from reportlab.pdfgen import canvas
from reportlab.lib.colors import red

c = canvas.Canvas("output-001.pdf")

c.setFillColor(red)
c.rect(100, 700, 100, 100, fill=1, stroke=1)

c.showPage()
c.save()
