import os
import time

def cleanup_uploads(directory, max_age_minutes=30):
    """
    Remove arquivos antigos do diretório especificado.
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
                os.remove(file_path)
                print(f"Arquivo excluído: {file_path}")
