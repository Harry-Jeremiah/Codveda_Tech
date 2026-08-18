import re
from pdfminer.high_level import extract_pages, extract_text

#identifying different elements in file 
# for page_layout in extract_pages("table.pdf"):
#     for element in page_layout:
#         print(element)

#extract text
# text = extract_text("FISHING.pdf")
# print(text)


text3 = extract_text("table.pdf")
print(text3)

