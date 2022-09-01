import fitz
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pdf_file', help='PDF file name')
parser.add_argument('start_page', help='Page to start from', type=int)
parser.add_argument('page_count', help='Number of pages to process', type=int, default=1)
parser.add_argument('-l', '--lang', 
                    help='Language files for tesseract. Use + sign to specify myltiple files: rus+eng',
                    default='rus')

args = parser.parse_args()

doc = fitz.open(args.pdf_file)

page_text = ''
for page_index in range(args.page_count):
    page = doc[args.start_page + page_index - 1] 
    full_tp = page.get_textpage_ocr(flags=0, dpi=300, full=True, language=args.lang)
    page_text = page_text + page.get_text(textpage=full_tp)

print(page_text)

