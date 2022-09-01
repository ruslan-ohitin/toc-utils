import fitz
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pdf_file', help='PDF file name')
parser.add_argument('start_page', help='Page number to start from. Don\'t mix it with page label!', type=int)
parser.add_argument('page_count', help='Number of pages to process', type=int, default=1)
parser.add_argument('-o', '--out', help='Output file name', default='index.txt')
parser.add_argument('-l', '--lang', 
                    help='Language files for tesseract. Use + sign to specify myltiple files: rus+eng',
                    default='rus')
parser.add_argument('-d', '--dpi', help='Resolution in dpi to render PDF page', type=int, default=300)

args = parser.parse_args()

doc = fitz.open(args.pdf_file)

page_text = '' # Var to collect text from ocr
for page_index in range(args.page_count):
    # Pages starts from 0, we expext page number 1 based in user input 
    page = doc[args.start_page - 1 + page_index] 
    full_tp = page.get_textpage_ocr(flags=0, dpi=args.dpi, full=True, language=args.lang)
    page_text = page_text + page.get_text(textpage=full_tp)

toc_file = open(args.out, "w", encoding="utf8")
toc_lines = toc_file.write(page_text)
toc_file.close()

