from typing import NamedTuple


class InfoNotas(NamedTuple):
    nota1: int
    nota2: int
    nota3: int


class InfoEstudante(NamedTuple):
    nome: str
    codigo: int
    media: float
    passou: InfoNotas


def input_data():
    nome_in = str(input("Insira o nome do estudante: "))
    codigo_in = int(input("Insira o código: "))
    nota_1_in = int(input("Insira a primeira nota: "))
    nota_2_in = int(input("Insira a segunda nota: "))
    nota_3_in = int(input("Insira a terceira nota: "))
    recinfo = InfoEstudante(nome=nome_in, codigo=codigo_in, media=media_calculator(nota_1_in, nota_2_in, nota_3_in),
                            passou=InfoNotas(nota1=nota_1_in, nota2=nota_2_in, nota3=nota_3_in))
    recnotas = InfoNotas(nota1=nota_1_in, nota2=nota_2_in, nota3=nota_3_in)
    return recinfo, recnotas


def media_calculator(nota1, nota2, nota3):
    media = (nota1+nota2+nota3)/3
    return media


lista_estudantes = []
sair = 's'
while sair != 'n' and sair != 'N':
    lista_estudantes.append(input_data())
    sair = str(input("Inserir outro estudante? (S ou N) \n"))


def print_data():
    for i in range(len(lista_estudantes)):
        rec = lista_estudantes[i]
        print("Nome: ", rec.nome)
        print("Código: ", rec.codigo)
        print("Notas:", rec.nota1, rec.nota2, rec.nota3)
        print("Média: ", rec.media)
        if rec.media >= 7:
            print("Aprovado.")
            print("\n")
        else:
            print("Reprovado.")
            print("\n")


print_data()
