from flask import Blueprint, render_template, request, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
import os
from businnes_logic.PDFprocessor import PDFProcessor
import uuid

main_bp = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('Nenhum arquivo foi selecionado')
        return redirect(request.url)

    file = request.files['file']
    
    if file.filename == '':
        flash('Nenhum arquivo foi selecionado')
        return redirect(request.url)

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
            processed_text = pdf_processor.process_pdf()
            
            # Caminho para salvar o resultado
            result_path = os.path.join('uploads', f'Resultado_{uuid.uuid4().hex}.txt')
            with open(result_path, 'w', encoding='utf-8') as result_file:
                result_file.write(processed_text)

            # Extrai apenas o nome do arquivo para o template
            output_filename = os.path.basename(result_path)
            return render_template('resultado.html', output_file=output_filename)
        except Exception as e:
            flash(f'Erro ao processar o arquivo: {str(e)}')
            return render_template('erro.html')

    flash('Arquivo inválido')
    return redirect(url_for('main.index'))

@main_bp.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join('uploads', filename)  # Caminho completo no diretório 'uploads'
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        flash('Arquivo não encontrado')
        return redirect(url_for('main.index'))
