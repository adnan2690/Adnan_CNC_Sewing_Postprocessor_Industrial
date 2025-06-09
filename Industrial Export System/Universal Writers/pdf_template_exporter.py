from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class PDFExporter:
    def export(self, template, filename):
        c = canvas.Canvas(filename, pagesize=A4)
        c.setTitle("Adnan CNC Template")
        
        # Add title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 800, "Industrial Sewing Template")
        
        # Add template content
        c.setFont("Helvetica", 12)
        c.drawString(100, 770, f"Material: {template.material}")
        c.drawString(100, 750, f"Dimensions: {template.width}x{template.height} mm")
        
        # Draw template outline
        c.rect(100, 100, template.width/10, template.height/10)
        
        c.save()