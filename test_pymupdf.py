import fitz

doc = fitz.open("1.pdf")

print(doc.get_page_labels())

print(doc.get_toc())

