all: c\:\\bin\\toc_set.py c\:\\bin\\toc_ocr.py

c\:\\bin\\toc_set.py: toc_set.py
	copy toc_set.py c:\\bin\\

c\:\\bin\\toc_ocr.py: toc_ocr.py
	copy toc_ocr.py c:\\bin\\

