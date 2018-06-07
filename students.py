# ler infos (nome, codigo, 3 notas), calcular a media das 3 notas, imprimir lista de estudantes com as medias e se
# foi aprovado (media => 7) ou não.
# def para ler registros, calcular media e imprimir os tchans.
# ESTRUTURA REGISTRO DE ESTUDANTE
# tipo Notas = Registro
#        Real Nota_1;
#        Real Nota_2;
#        Real Nota_3;
#    Fim-Registro;
# tipo Estudante = Registro
#        int  Codigo;
#        str  Nome;
#        int  Notas;
#        flt  Media;
#    Fim-Registro;
# Lista Estudante Turma[];


from typing import NamedTuple


class Notas(NamedTuple):
    nota1: int
    nota2: int
    nota3: int
# end_Notas_class


class EstudanteInfo(NamedTuple):
    nome: str
    notas: Notas
    codigo: int
# end_EstudanteInfo_class


def input_data():
    nome_in = str(input("Insira o nome do estudante: "))
    codigo_in = int(input("Insira o código: "))
    nota_1_in = int(input("Insira a primeira nota: "))
    nota_2_in = int(input("Insira a segunda nota: "))
    nota_3_in = int(input("Insira a terceira nota: "))
    recordestudante = EstudanteInfo(nome=nome_in, codigo=codigo_in)
    recordnotas = Notas(notas=Notas(nota1=nota_1_in, nota2=nota_2_in, nota3=nota_3_in))
    return recordestudante and recordnotas
# end input_data


def media_calculator():
    Estudante_list = (Notas.nota1, Notas.nota2, Notas.nota3)/3

# end media_calculator


Estudante_list = []
sair = 'S'
while (sair != 'n') and (sair != 'N'):
    Estudante_list.append(input_data())
    sair = str(input("Inserir mais estudantes? (S ou N)?"))
for i in (range(len(Estudante_list))):
    record = Estudante_list[i]
    if record == ():
        print("Estudante: ", record.nome)
        print("Código: ", record.codigo)
        print("Média: ", record.media)
        print("Aprovado ou não: ", record.aprovado)

# def dados_imprimeitor():

# end dados_imprimeitor
