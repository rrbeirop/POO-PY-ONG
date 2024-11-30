from classes import *
from views import *
from funcao import *


dog = []
rcs =["Vira-lata", "Shih Tzu", "Yorkshire", "Poodle", "Buldogue Francês", "Pinscher"]
hms = []

while True:
    print(menu())
    # print(menu_dog())
    op = input("INFORME SUA OPÇÃO:")
    # os.system("cls")
    if op == "1":
        dog.append(criar_cao(rcs))
       # print(dog())
    
    elif op == "2":
        hms.append(criar_humano(hms))

        
    elif op == "3":
         listar_dog(dog)
        #  print(menu_dog())
        #  print(listar_dog)

        #  listar_hms(
    elif op == "4":
         listar_hms(hms)

    elif op == "0":
         sair()
         break

