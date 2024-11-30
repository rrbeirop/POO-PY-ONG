from classes import ONG,Projeto
from api_client import *



def createOng(token):
    ong = ONG(input("Nome: "))
    nome = input("Informe nome:")
    descricao = input("Informe a descrição:")
    resposavel = input("Informe o responsavel ")
    status = input("Informe o status:")
    projeto = Projeto(nome, descricao ,resposavel,status)
    ong.adicionar_projeto(projeto)
    print(api_create(ong.to_json(),token))

def getOngs():  
    ongs=[]  
    ongs_json=api_read()
    for index, data in zip(range(len(ongs_json)),ongs_json):
        ong = ONG(_id=data['_id'],nome=data['nome'])
        print(f'{index} : Nome: {data['nome']}')
        for p in data['projetos']:
            projeto = Projeto(['nome'],p['descricao'],
                              p['responsavel'],p['status'],p['_id'])
            ong.adicionar_projeto(projeto)
            print(f'  Projeto ----> {p['nome']}')
        ongs.append(ong)
        print('\n')
    return ongs