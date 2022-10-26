class Professor:
    def __init__(self, nome:str, matricula:int, subarea:str, campus_atual:str, campus_removido:str, tempo_de_ifce:int, idade:int, nota_concurso:int,):
        self.__nome = nome
        self.__matricula = matricula
        self.__subarea = subarea
        self.__campus_atual = campus_atual
        self.__campus_removido = campus_removido
        self.__tempo_de_ifce = tempo_de_ifce
        self.__idade = idade
        self.__nota_concurso = nota_concurso

    @property
    def tempo_de_ifce(self):
        return self.__tempo_de_ifce

    @tempo_de_ifce.setter
    def nome(self, valor):
        self.__tempo_de_ifce = valor

    def __str__(self):
        return '{}'.format(self.__tempo_de_ifce)



