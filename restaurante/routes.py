# criar as rotas do site (os links)
# restaurante/routes.py
# restaurante/routes.py
from flask import render_template, redirect, url_for, flash
from .forms import Formeventos, FormMarmita,  Formprato
from .models import Marmita, Eventos, RespostaPrato
from . import app, database


@app.route("/")
def homepage():
    return render_template ("homepage.html")

@app.route("/cardapio")
def cardapio():
    return render_template ("cardapio.html")

@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
   
    return render_template('pedidos.html')


@app.route('/eventos', methods=['GET', 'POST'])
def eventos():
    form = Formeventos()

    if form.validate_on_submit():
        # Converta o horário_evento para string
        horario_evento_str = form.horario_evento.data.strftime('%H:%M:%S') if form.horario_evento.data else None

        # Criar um novo evento a partir dos dados do formulário
        novo_evento = Eventos(
            data_evento=form.data_evento.data,
            responsavel=form.responsavel.data,
            quantidade_pessoas=form.quantidade_pessoas.data,
            horario_evento=horario_evento_str,  # Aqui salva como string
            observacao=form.observacao.data
        )

        # Adicionar o evento ao banco de dados
        database.session.add(novo_evento)
        database.session.commit()

        # Redirecionar para a página de sucesso
        return redirect(url_for('evento_sucesso'))

    return render_template('eventos.html', form=form)

@app.route('/evento_sucesso', methods=['GET'])
def evento_sucesso():
    return render_template('evento_sucesso.html')



@app.route("/adm")
def adm():
    return render_template("adm.html")


@app.route('/marmitas', methods=['GET', 'POST'])
def marmita():
    form = FormMarmita()
    if form.validate_on_submit():
        # Criar uma nova instância de Marmita com os dados do formulário
        nova_marmita = Marmita(
            responsavel=form.responsavel.data,
            opcoes_de_carne=form.opcoes_carnes.data,
            arroz=form.arroz.data,
            feijao=form.feijao.data,
            salada=form.salada.data,
            farofa=form.farofa.data,
            adicional=form.adicional.data,
            observacao=form.observacao.data
        )
        
        # Adicionar a marmita ao banco de dados
        database.session.add(nova_marmita)
        database.session.commit()
        
        # Redireciona para a página de sucesso (Pedido Enviado com Sucesso)
        return redirect(url_for('pedido_sucesso'))
    
    return render_template('marmitas.html', form=form)


# Rota de Pedido Enviado com Sucesso
@app.route('/pedido-sucesso')
def pedido_sucesso():
    return render_template('pedido_sucesso.html')

@app.route('/pratofeito', methods=['GET', 'POST'])
def questionario():
    form = Formprato()  # Corrigido: adicionando os parênteses
    if form.validate_on_submit():
        # Criar uma nova resposta para o banco de dados
        nova_resposta = RespostaPrato(
            tipo_casquinha=form.tipo_casquinha.data,
            tipo_feijao=form.tipo_feijao.data,
            observacao=form.observacao.data
        )
        
        # Adicionar e salvar a nova resposta no banco de dados
        database.session.add(nova_resposta)
        database.session.commit()
        
        # Redirecionar para a página de sucesso
        return redirect(url_for('pedido_sucesso'))
    
    
    return render_template('pratofeito.html', form=form)

if __name__ == '__main__':
    database.create_all()  # Garante que as tabelas estão criadas
    app.run(debug=True)

@app.route('/admin/marmitas')
def admin_marmitas():
    pedidos_marmitas = Marmita.query.all()  # Consulta os pedidos de marmitas
    return render_template('admin_marmitas.html', pedidos=pedidos_marmitas)

@app.route('/admin/pratofeito')
def admin_prato_feito():
    pedidos_prato_feito =  RespostaPrato.query.all()  # Consulta os pedidos de prato feito
    return render_template('admin_pratofeito.html', pedidos=pedidos_prato_feito)

@app.route('/admin/eventos')
def admin_eventos():
    eventos = Eventos.query.all()  # Consulta eventos cadastrados
    return render_template('admin_eventos.html', eventos=eventos)


@app.route('/admin/pedido/excluir_prato/<int:id>', methods=['GET', 'POST'])
def excluir_pedido_prato(id):
    pedido = RespostaPrato.query.get(id)  # Obtém o pedido a partir do banco de dados
    if pedido:
        database.session.delete(pedido)  # Exclui o pedido
        database.session.commit()  # Commit para confirmar a exclusão
    return redirect(url_for('admin_prato_feito'))  # Redireciona de volta para a lista de pedidos

@app.route('/admin/pedido/excluir_marmita/<int:id>', methods=['GET', 'POST'])
def excluir_pedido_marmita(id):
    pedido = Marmita.query.get(id)  # Obtém o pedido de Marmita do banco de dados
    if pedido:
        database.session.delete(pedido)  # Exclui o pedido
        database.session.commit()  # Commit para confirmar a exclusão
    return redirect(url_for('admin_marmitas'))  # Redireciona de volta para a lista de marmitas

@app.route('/admin/evento/excluir_evento/<int:id>', methods=['GET', 'POST'])
def excluir_evento(id):
    evento = Eventos.query.get(id)  # Obtém o evento do banco de dados
    if evento:
        database.session.delete(evento)  # Exclui o evento
        database.session.commit()  # Commit para confirmar a exclusão
    return redirect(url_for('admin_eventos'))  # Redireciona de volta para a lista de eventos
