import fitz  # PyMuPDF para manipulação de PDFs
import os

class PDFProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process_pdf(self):
        content = []

        with fitz.open(self.file_path) as pdf:
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                text = page.get_text("text")

                # Limpeza de rodapé e cabeçalho
                text_lines = text.splitlines()
                text_lines = [line for line in text_lines if "cabeçalho" not in line.lower() and "rodapé" not in line.lower()]
                content.append("\n".join(text_lines))

        return "\n".join(content)

    def save_processed_content(self, content, format_type='txt'):
        output_file = f"{os.path.splitext(self.file_path)[0]}.{format_type}"

        if format_type == 'txt':
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
        elif format_type == 'csv':
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('Text\n')
                f.write(content.replace("\n", " "))

        return output_file
