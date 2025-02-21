from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

c = canvas.Canvas("output-001.pdf")

data = [["Header1", "Header2"], ["Item1", "Item2"]]
table = Table(data)
table.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
table_width, table_height = table.wrap(0, 0)  # initialize table
table.drawOn(c, 100, 700)  # table at position (100, 700)

c.showPage()
c.save()
