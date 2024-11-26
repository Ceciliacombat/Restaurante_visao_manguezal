# criar a estrutura do banco de dados
from restaurante import database

class Marmita(database.Model):
    __tablename__ = 'marmitas'  # Nome da tabela no banco de dados

    id = database.Column(database.Integer, primary_key=True)
    responsavel = database.Column(database.String(120), nullable=False)
    opcoes_de_carne = database.Column(database.String(120))
    arroz = database.Column(database.Boolean, default=False)
    feijao = database.Column(database.Boolean, default=False)
    salada = database.Column(database.Boolean, default=False)
    farofa = database.Column(database.Boolean, default=False)
    adicional = database.Column(database.String(120))
    observacao = database.Column(database.String(500))

    def __repr__(self):
        return f'<Marmita {self.id} - {self.responsavel}>'
    
class RespostaPrato(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    tipo_casquinha = database.Column(database.String(50), nullable=False)
    tipo_feijao = database.Column(database.String(50), nullable=False)
    observacao = database.Column(database.Text, nullable=True)

    
class Eventos(database.Model):
    __tablename__ = 'eventos'
    
    id = database.Column(database.Integer, primary_key=True)
    data_evento = database.Column(database.Date, nullable=False)
    responsavel = database.Column(database.String, nullable=False)
    quantidade_pessoas = database.Column(database.Integer, nullable=False)
    horario_evento = database.Column(database.String, nullable=False)  # Armazenado como string
    observacao = database.Column(database.Text)

    def __repr__(self):
        return f'<Evento {self.responsavel} - {self.data_evento}>'
    