# pymupdf inport
import fitz

doc = fitz.open("1.pdf")

print(doc.get_page_labels())

# Read plain text file with TOC entries.
# String format "<Level>#<Title>#<Page>"
toc_file = open('index.txt', 'r', encoding='utf8')
toc_lines = toc_file.readlines()
toc_file.close()

toc = []

for line in toc_lines:
    tokens = line.split('#')
    level = int(tokens[0])
    title = tokens[1].strip()
    page = int(tokens[2])

    toc.append([level, title, page])

doc.set_toc(toc, collapse=0)
doc.save("2.pdf")

