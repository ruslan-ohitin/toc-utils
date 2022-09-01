# pymupdf inport
import fitz

doc = fitz.open("1.pdf")

# Page Labels
# https://pymupdf.readthedocs.io/en/latest/document.html#Document.set_page_labels
# print(doc.get_page_labels())

# TOC Entries
# https://pymupdf.readthedocs.io/en/latest/document.html#Document.set_toc

# Read plain text file with TOC entries to toc_lines.
toc_file = open("index.txt", "r", encoding="utf8")
toc_lines = toc_file.readlines()
toc_file.close()

# String format "<Level>#<Title>#<Page>"
toc = []
for line in toc_lines:
    tokens = line.split("#")
    level = int(tokens[0])
    title = tokens[1].strip()
    page = int(tokens[2])

    toc.append([level, title, page])

doc.set_toc(toc, collapse=0)
doc.save("2.pdf")
