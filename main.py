'''
1) Ler um conjunto aleatório de registros do teclado;

2) Em seguida, calcule a média de cada um ;

3) Por fim, imprimir a lista de estudantes com as três notas, média e se aprovado ou não (aprovado com média igual ou superior a 7.00).

OBS: Use Funções para cada ítem

Lembre-se use def para:

1) Ler os registros;

2) Calcular a média;

3) imprimir a lista de estudantes, média e se aprovado ou não.


ESTRUTURA REGISTRO DE ESTUDANTE

tipo Notas = Registro
                           Real Nota_1;
                           Real Nota_2;
                           Real Nota_3;
                      Fim-Registro;
tipo Estudante = Registro
                                 inteiro      Codigo
                                Caractere  Nome;
                                Avaliacao  Notas;
                                Real            Media;
                            Fim-Registro ;
 Lista Estudante Turma[ ] ;    
'''
from typing import NamedTuple

class Notas(NamedTuple):
    N1 : float
    N2 : float
    N3 : float
#end class Notas
class Estud(NamedTuple):
    Cod : int
    Nome : str
    Aval : Notas
    Med : float
#end class Estud
def in_data():
    Cod_in = int(input("Entre com o código do aluno: "))
    Nome_in = str(input("Entre com o nome do aluno: "))
    N1_in = float(input("Entre com a nota 1: "))
    N2_in = float(input("Entre com a nota 2: "))
    N3_in = float(input("Entre com a nota 3: "))
    rec = Estud(Cod=Cod_in, Nome=Nome_in, Aval=Notas(N1=N1_in, N2=N2_in, N3=N3_in), Med = med_Calc(N1_in,N2_in,N3_in))
    return rec
#end in_data

def med_Calc(nota1,nota2,nota3):
  Med = (nota1+nota2+nota3)/3
  return Med
#end med_Calc

Estud_List= []
exit = 's'
while exit != 'n' and exit != 'N':
    Estud_List.append(in_data())
    exit = str(input("Continuar (s ou n)?")) #Injetando os valores do in_data na lista nova
def print_data(Codigo,Nome,Media,nota1,nota2,nota3):
  for i in range(len(Estud_List)):
    rec=Estud_List[i]
    print("Código: ",Codigo)
    print("Nome: ",Nome)
    print("Média: ",Media)
    print("Notas: ","\n", nota1, "\n", nota2, "\n", nota3)
    if Media >= 7:
      print("Status: Aprovado")
    else:
      print("Status: Reprovado")
      print("\n")
#end print_data
print_data(rec.Cod,rec.Nome,rec.Med,rec.N1,rec.N2,rec.N3)
