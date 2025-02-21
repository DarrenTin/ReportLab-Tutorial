# Guide on reportlab
- write a simple pdf and output
    ```python
    from reportlab.pdfgen import canvas
    c = canvas.Canvas("output-001.pdf")
    c.drawString(100, 750, "Hello pdf!")
    c.showPage()
    c.save() 