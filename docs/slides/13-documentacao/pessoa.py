'''
Módulo Pessoa.
Contém classes para se trabalhar com o
contexto de pessoas.

Autor: Bruno Silva
'''

class Pessoa:
    '''
    Representa uma Pessoa,
    que tem como atributos o seu nome
    e a sua idade.
    '''
    def __init__(self, nome, idade):
        '''Constroi um objeto pessoa.'''
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa{self.nome, self.idade}'

    def compara_idades(self, p2):
        '''Retorna verdadeiro se self for mais novo que p2.'''
        return self.idade <= p2.idade
    
    def cumprimenta(self, p):
        '''Cumprimenta um objeto p do tipo Pessoa.'''
        print(f'Olá {p.nome}, tudo bem?')

if __name__ == '__main__':
    p = Pessoa('Joao', 25)
    help(p)