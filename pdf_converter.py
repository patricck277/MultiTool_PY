from pdf2docx import Converter


# 1
def convert_pdf_to_docx(pdf_file, docx_file):
    # Utwórz konwerter i przekaż ścieżkę do pliku PDF
    cv = Converter(pdf_file)

    # Konwertuj PDF na DOCX
    cv.convert(docx_file, start=0, end=None)

    # Zamknij konwerter
    cv.close()


class PDFConverter:
    pass
