import PyPDF2
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdfminer.high_level import extract_text

pdf_file_path = 'Chain-of-Thought-prompting.pdf'    # PDF 경로 ex) './abc.pdf'

class read_pdf:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path
    def pdf_read():        
        with open(pdf_file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            
            # 페이지 확인
            num_pages = reader.numPages            
            # 텍스트를 추출, 리스트 저장
            text_list = []
            splits = []
            for page_number in range(num_pages):
                page = reader.getPage(page_number)
                text = page.extractText()
                text_list.append(text)
            
            splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0)
            splits = splitter.split_documents(text_list)

        #return ' '.join(text_list)
        return text_list, splits

read_pdf.pdf_read(pdf_file_path)

# fyi
# module 'filesplit': read pdf -> split or merge to multiple chunk

'''
def extract_txt(pdf_file_path):
    text = extract_text(pdf_file_path)
    print(text)
'''