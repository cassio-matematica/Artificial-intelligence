from flask import Blueprint, render_template, request, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
import os
from businnes_logic.PDFprocessor import PDFProcessor

import uuid

main_bp = Blueprint('main', __name__)

# Função para verificar arquivos permitidos
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('Nenhum arquivo foi selecionado.')
        return redirect(url_for('main.index'))

    file = request.files['file']
    
    if file.filename == '':
        flash('Nenhum arquivo foi selecionado.')
        return redirect(url_for('main.index'))

    if file and allowed_file(file.filename):
        # Cria o diretório "uploads" se ele não existir
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
            
        # Define um nome de arquivo único
        file_path = os.path.join('uploads', f'Documento_{uuid.uuid4().hex}.pdf')
        file.save(file_path)

        # Processa o PDF
        pdf_processor = PDFProcessor(file_path)
        try:
            # Processa o texto com tokenização e remoção de stop words
            processed_tokens = pdf_processor.process_pdf()

            # Gera nomes únicos para os arquivos de saída
            result_txt_path = os.path.join('uploads', f'Resultado_{uuid.uuid4().hex}.txt')
            result_json_path = os.path.join('uploads', f'Resultado_{uuid.uuid4().hex}.json')

            # Salva o texto processado em TXT
            pdf_processor.save_processed_content(processed_tokens, format_type='txt')

            # Salva o texto processado em JSON
            pdf_processor.save_processed_content(processed_tokens, format_type='json')

            # Renderiza a página de resultado com os dois links de download
            return render_template(
                'resultado.html', 
                output_txt=os.path.basename(result_txt_path),
                output_json=os.path.basename(result_json_path)
            )
        except Exception as e:
            flash(f'Erro ao processar o arquivo: {str(e)}')
            return render_template('erro.html')

    flash('Arquivo inválido.')
    return redirect(url_for('main.index'))

@main_bp.route('/uploads/<filename>')
def download_file(filename):
    file_path = os.path.join('uploads', filename)  # Caminho completo no diretório 'uploads'
    # Verifica se o arquivo existe
    if os.path.exists(file_path):
        # Envia o arquivo como um download para o usuário
        return send_file(file_path, as_attachment=True, download_name=filename)
    else:
        flash('Arquivo não encontrado.')
        return redirect(url_for('main.index'))
