class Animal():
    nome : str
    coracao : bool
    racional: bool

    def __init__(self, nome, coracao,):
        self.nome = nome
        self.coracao = coracao 


class Humano(Animal):
    def __init__(self, nome, sexo, idade):

        self.nome = nome
        self.sexo = sexo
        self.idade = idade

    # def hm(self):
    #     print(self.nome)
    #     print(self.sexo)    
    #     print(self.idade)

class Dog(Animal):

    def __init__(self, nome, tamanho, raca, cor):
        super ().__init__(nome, True)
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
        self.cor = cor
        
    
    # def latir():
    #     print('au, au')
    
    

    # def cachorro(self):
    #     print(self.nome)
    #     print(self.tamanho)
    #     print(self.raca)
    #     print(self.cor)


    


# cao = Dog('gordao', '70cm', 'Vira lata', 'PRETO')
# cao.cachorro()

# human = Humano("rafael","feminino", "10 anos")
# human.hm()

