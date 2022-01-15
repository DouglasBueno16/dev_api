"""
1 - Aplicação em Flask
"""

import re
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

devs = [
    {
        'id':'0',
        'nome':'Douglas',
        'habilidades':['Python', 'C ++']
    },

    {
        'id':'1',
        'nome':'Gabriel',
        'habilidades':['Python', 'Data Science']
    }   
]

class Desenvolvedor(Resource, id):
    def get(self):
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Desenvolvedor com ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido! Favor consultar o serviço de suporte'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response
    
    
    def put(self):

        return

# Add route to web application
api.add_resource(Desenvolvedor, '/dev/int:<id>/')

if __name__ == '__main__':
    app.run(debug=True)