from flask import Flask
from config import Config
from routes.views import main_bp
from businnes_logic.file_menagers import cleanup_uploads



app = Flask(__name__)
app.config.from_object(Config)

# Registrar o blueprint das rotas
app.register_blueprint(main_bp)

UPLOAD_FOLDER = "uploads"
@app.before_request
def before_request():
    cleanup_uploads(UPLOAD_FOLDER)

if __name__ == '__main__':
    app.run(debug=True)

