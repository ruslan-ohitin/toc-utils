# pymupdf inport
import fitz

doc = fitz.open("1.pdf")

print(doc.get_page_labels())

#print(doc.get_toc())

# Using readlines()
file1 = open('index.txt', 'r', encoding='utf8')
Lines = file1.readlines()
file1.close()

toc = []

for line in Lines:
    tokens = line.split('#')
    level = int(tokens[0])
    title = tokens[1].strip()
    page = int(tokens[2])

    toc.append([level, title, page])

doc.set_toc(toc, collapse=0)
doc.save("2.pdf")

