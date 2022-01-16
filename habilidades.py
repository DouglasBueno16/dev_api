"""
Arquivo para armazenar as habilidades dos programadores
"""

from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'PHP', 'C++']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
        