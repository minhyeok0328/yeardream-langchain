import PyPDF2
from pdfminer.high_level import extract_text

# PDF 경로
pdf_file_path = 'Chain-of-Thought-prompting.pdf'

def pdf_read():        
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        
        # 페이지 확인
        num_pages = reader.numPages
        
        # 텍스트를 추출, 리스트 저장
        text_list = []
        for page_number in range(num_pages):
            page = reader.getPage(page_number)
            text = page.extractText()
            text_list.append(text)
        
        # 텍스트 출력 또는 원하는 정보 크롤링
        for text in text_list:
            # 예시: 특정 텍스트가 있는 부분을 찾아 출력
            if 'important information' in text:
                print(text)

pdf_read()
'''
def extract_txt(pdf_file_path):
    text = extract_text(pdf_file_path)
    print(text)

def '''