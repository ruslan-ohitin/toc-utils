import fitz

doc = fitz.open("1.pdf")

page = doc[220]

full_tp = page.get_textpage_ocr(flags=0, dpi=300, full=True, language="rus-best+eng-best")

print(page.get_text(textpage=full_tp))

