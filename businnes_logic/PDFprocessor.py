import fitz  # PyMuPDF para manipulação de PDFs
import os
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time

# Certifique-se de baixar os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')

class PDFProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.stop_words = set(stopwords.words("portuguese"))  # Altere o idioma se necessário

    def process_pdf(self):
        content = []
        try:
            # Abrir o PDF com PyMuPDF
            with fitz.open(self.file_path) as pdf:
                for page_num in range(pdf.page_count):
                    page = pdf[page_num]
                    text = page.get_text("text")

                    # Limpeza de rodapé e cabeçalho
                    text_lines = text.splitlines()
                    text_lines = [line for line in text_lines if "cabeçalho" not in line.lower() and "rodapé" not in line.lower()]
                    content.append("\n".join(text_lines))

            full_text = "\n".join(content)

            # Tokenização e remoção de stop words
            tokens = word_tokenize(full_text, language="portuguese")
            filtered_tokens = [word for word in tokens if word.isalnum() and word.lower() not in self.stop_words]

            return filtered_tokens
        
        except Exception as e:
            print(f"Erro ao processar o arquivo PDF: {e}")
            raise  # Re-levanta o erro para ser tratado fora do método

    def save_processed_content(self, tokens, format_type='txt'):
        output_file = f"{os.path.splitext(self.file_path)[0]}.{format_type}"

        try:
            if format_type == 'txt':
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(" ".join(tokens))
            elif format_type == 'json':
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump({"tokens": tokens}, f, ensure_ascii=False, indent=4)

            return output_file
        except Exception as e:
            print(f"Erro ao salvar o arquivo {format_type}: {e}")
            raise  # Re-levanta o erro para ser tratado fora do método

# Exemplo de uso
if __name__ == "__main__":
    try:
        pdf_path = "seu_arquivo.pdf"
        processor = PDFProcessor(pdf_path)
        tokens = processor.process_pdf()

        # Salvar em JSON
        output_json = processor.save_processed_content(tokens, format_type='json')
        print(f"Arquivo JSON salvo em: {output_json}")

        # Salvar em TXT
        output_txt = processor.save_processed_content(tokens, format_type='txt')
        print(f"Arquivo TXT salvo em: {output_txt}")

    except Exception as e:
        print(f"Erro geral na execução do processo: {e}")

def cleanup_uploads(directory, max_age_minutes=30):
    """
    Remove arquivos do diretório que são mais antigos que o tempo permitido.
    
    Args:
        directory (str): Caminho para o diretório.
        max_age_minutes (int): Idade máxima dos arquivos em minutos.
    """
    now = time.time()
    max_age_seconds = max_age_minutes * 60

    if not os.path.exists(directory):
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > max_age_seconds:
                try:
                    os.remove(file_path)
                    print(f"Arquivo excluído: {file_path}")
                except Exception as e:
                    print(f"Erro ao excluir o arquivo {file_path}: {e}")
