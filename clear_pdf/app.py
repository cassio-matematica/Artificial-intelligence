from flask import Flask
from config import Config
from routes.views import main_bp

app = Flask(__name__)
app.config.from_object(Config)

# Registrar o blueprint das rotas
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
