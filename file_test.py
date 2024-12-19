import time 
import pdfplumber
# Определение кодировки
start_time = time.time()
with pdfplumber.open("Статьи для эссе.pdf") as pdf:
    with open("output.txt", "w", encoding="utf-8") as txt_file:
        for page in pdf.pages:
            text = page.extract_text()
            txt_file.write(text + "\n")
end_time = time.time()
all_time = end_time - start_time
print(all_time)