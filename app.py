"""
1 - Aplicação em Flask
"""
import json
from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Douglas',
        'habilidades':['Python', 'C ++']
    },

    {
        'id':'1',
        'nome':'Ze',
        'habilidades':['Python', 'PHP']
    }   
]


class Desenvolvedor(Resource):
    """Classe para retornar os desenvolvedores"""
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor com ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido! Favor consultar o serviço de suporte'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response
    
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores [id] = dados 
        return dados


    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status": "sucesso", "mensagem": "Registro excluido!"}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores


    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

# Add route to web application
api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')


if __name__ == '__main__':
    app.run(debug=True)