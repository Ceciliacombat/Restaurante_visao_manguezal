from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurante.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita um aviso de depreciação
app.secret_key = 'sua_chave_secreta'  # Defina uma chave secreta para sessões

database = SQLAlchemy(app)


from restaurante import routes  # Importa as rotas após a inicialização
