from professor import Professor
from remocao import Remocao
def executar():
    professor = Professor(nome= 'Felipe',matricula=2020985,campus_atual='IFCE-JAGUARIBE',campus_removido='IFCE-CEDRO',tempo_de_ifce=2,nota_concurso=10,subarea='Metodologia',idade= 34)
    professor2 = Professor(nome= 'Paulo',matricula=2020985,campus_atual='IFCE-JAGUARIBE',campus_removido='IFCE-CEDRO',tempo_de_ifce=6,nota_concurso=10,subarea='Metodologia',idade= 34)

    remocao = Remocao()

    remocao.push(professor)
    remocao.push(professor2)
    # remocao.empty()
    print(remocao)
    # remocao.push(professor2, 2)
    # rint(remocao)?




if __name__ == '__main__':
    executar()

