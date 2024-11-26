# criar os formulários do site
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, BooleanField, SubmitField, FieldList, DateField, IntegerField,  TimeField, RadioField
from wtforms.validators import DataRequired

class FormMarmita(FlaskForm):
    responsavel = StringField('Responsável', validators=[DataRequired()])
    opcoes_carnes = SelectField('Opções de Carnes', choices=[
        ('', 'Não quero carne'),
        ('carne-de-sol', 'Carne de Sol'),
        ('carne-de-fumeiro', 'Carne de Fumeiro')
    ], validators=[DataRequired()])
    arroz = BooleanField('Arroz')
    feijao = BooleanField('Feijão')
    salada = BooleanField('Salada')
    farofa = BooleanField('Farofa')
    adicional = StringField('Adicional')
    observacao = TextAreaField('Observação')
    submit = SubmitField('Enviar')

class Formprato(FlaskForm):
    tipo_casquinha = RadioField(
        'Escolha o tipo de casquinha:',
        choices=[
            ('Casquinha de Siri', 'Casquinha de Siri'),
            ('Casquinha de Caranguejo', 'Casquinha de Caranguejo'),
            ('Casquinha de Aratu', 'Casquinha de Aratu')
        ],
        validators=[DataRequired()]
    )
    tipo_feijao = RadioField(
        'Escolha o tipo de feijão:',
        choices=[
            ('Feijão de Caldo', 'Feijão de Caldo'),
            ('Feijão Fradinho', 'Feijão Fradinho')
        ],
        validators=[DataRequired()]
    )
    observacao = TextAreaField('Observações:', validators=[DataRequired()])
    submit = SubmitField('Enviar Pedido')  # Defina uma única vez


class Formeventos(FlaskForm):
    data_evento = DateField('Data do Evento', format='%Y-%m-%d', validators=[DataRequired()])
    responsavel = StringField('Nome do Responsável pela Reserva', validators=[DataRequired()])
    quantidade_pessoas = IntegerField('Quantidade de Pessoas', validators=[DataRequired()])
    horario_evento = TimeField('Horário do Evento', validators=[DataRequired()])
    observacao = TextAreaField('Observação')
    submit = SubmitField('Enviar')