
from views import*
from classes import*
import os

# def rc():
#     for i in(rcs):
#        print()

def criar_cao(rcs):
        nome = input("DEFINA UM NOME AO CÃO:")
        # rc()
        cont = 1
        for i in rcs:
            print (f"{cont}: {i} ")
            cont += 1 
        
        rk = int(input("ESCOLHA UMA RAÇA:"))
        rk -= 1 
        raca = rcs[rk]
        tamanho = input("QUAL TAMANHO:")
        cor = input("DEFINA UMA COR:")
        cao = Dog(nome,tamanho, raca, cor)
        os.system("cls")
        return cao
        dog.append(cao) 
       
      
def criar_humano(hm):
    
        nome = input("DEFINA UM NOME:")
        sexo = input("DEFINA O SEXO:")
        idade = input("DEFINA UMA IDADE:")
        hm = Humano(nome, sexo, idade)
        # hms.append(hm)

        return hm

def listar_dog(var):
     for i in var:
        os.system("cls")
        #   print(f"NOME DO CÃO: {i.nome}\nRACA DO CÃO: {i.raca}\nTAMANHO DO CÃO: {i.tamanho}\nCOR DO CÃO:{i.cor}")
        print(f"NOME DO CÃO: {i.nome}")
        print(f"RACA DO CÃO: {i.raca}")
        print(f"TAMANHO DO CÃO:{i.tamanho}")
        print(f"COR DO CÃO: {i.cor}")
        print("↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")



def listar_hms(var1):
     
     for i in var1:
        os.system("cls")
        print(f"NOME DO HUMANO: {i.nome}")
        print(f"SEXO DO HUMANO: {i.sexo}")
        print(f"IDAIDE DO HUMANO:{i.idade}")
        print("↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")



def editar_dog():
      
      pass

def editar_human():
      

      pass
def sair():
         print("ACABOU")
    