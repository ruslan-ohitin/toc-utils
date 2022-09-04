# Page Labels
# https://pymupdf.readthedocs.io/en/latest/document.html#Document.set_page_labels
# print(doc.get_page_labels())

# TOC Entries
# https://pymupdf.readthedocs.io/en/latest/document.html#Document.set_toc

import fitz # pymupdf inport
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pdf_file', help='PDF file name')
parser.add_argument('-i', '--index', help='File name with TOC index', default='index.txt')
parser.add_argument('-o', '--out', help='Modified PDF file name', default='out.pdf')
parser.add_argument('-d', '--delta', help='Number to add to (or subtract from) page number in TOC index file', type=int, default=0)

args = parser.parse_args()

doc = fitz.open(args.pdf_file)

# Read plain text file with TOC entries to toc_lines.
toc_file = open(args.index, "r", encoding="utf8")
toc_lines = toc_file.readlines()
toc_file.close()

# String format "<Level>#<Title>#<Page>"
toc = []
for line in toc_lines:
    tokens = line.split("#")
    if len(tokens) < 3:
        print("Change format of this line as <Level>#<Title>#<Page>")
        print(line)
        break

    level = int(tokens[0])
    title = tokens[1].strip()
    page = int(tokens[2]) + args.delta

    toc.append([level, title, page])

doc.set_toc(toc, collapse=0)

if args.out:
    doc.save(args.out)

