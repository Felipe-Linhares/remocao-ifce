from professor import Professor


class Remocao:

    def __init__(self):

        self.__professor = []
        self.__tempo_de_ifce = []

    def push(self, professor):
        self.__tempo_de_ifce.append(professor.tempo_de_ifce)
        self.__tempo_de_ifce.sort(reverse = True)
        for element in range(0, len(self.__tempo_de_ifce)):
            if professor.tempo_de_ifce == self.__tempo_de_ifce[element]:
                self.__professor.insert(element, professor)


    def pop(self):
        self.__professor = self.__professor.pop()


    def empty(self):
        lista = self.__professor
        if(len(lista) == 0):
            return 'Error: Lista Está Vázia!!'
        else:
            return 'A Lista não Está Vázia: {}'.format(lista)

    def __str__(self):
        ret = ' '.join(str(element) for element in self.__professor)
        return ret
