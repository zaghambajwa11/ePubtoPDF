
# Import the required modules
import ebooklib
from ebooklib import epub
from reportlab.pdfgen import canvas

# Define a function that converts epub file to pdf
def epub_to_pdf(epub_file, pdf_file):
    # Open the epub file
    book = epub.read_epub(epub_file)
    # Create a canvas object
    c = canvas.Canvas(pdf_file)
    # Loop through the items in the book
    for item in book.get_items():
        # Check if the item is an html document
        if item.get_type() == ebooklib.ITEM_DOCUMENT and item.get_name().endswith(".html"):
            # Get the item content as a string
            html = item.get_content().decode("utf-8")
            # Draw the html content on the canvas
            c.drawCentredString(300, 700, html)
            # Create a new page
            c.showPage()
    # Save the canvas to the pdf file
    c.save()

# Example usage
epub_to_pdf("r.epub", "r.pdf")