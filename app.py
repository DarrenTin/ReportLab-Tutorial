from reportlab.pdfgen import canvas
from reportlab.lib.colors import red

c = canvas.Canvas("output-001.pdf")

# c.line(x-start, y-start, x-end, y-end)
c.line(100, 800, 300, 500)

c.showPage()
c.save()
