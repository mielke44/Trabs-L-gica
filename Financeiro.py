"""DISCLAIMER: Este app é um projeto pessoal do Wilson Mielke, qualquer uso profissional não está autorizado, com excessão de casos excepcionais com aprovação do mesmo.
App feito para organizar finanças pessoais
versão 0.1.23
(versão 0 = beta, .1 = build, .21 = teste com 1 bug)
"""
from typing import NamedTuple
import datetime
import pickle

mylist = []
today = datetime.date.today()
mylist.append(today)
print("Dia de hoje:", mylist[0])


class data(NamedTuple):
	dia: int


class luz(NamedTuple):
	custo_Presente: float
	custo_Passado: float
	perc_Dif: float
	data_Pag: data


#end Luz class


class agua(NamedTuple):
	custo_Presente: float
	custo_Passado: float
	perc_Dif: float
	data_Pag: data


#end Agua class


class internet(NamedTuple):
	custo_Presente: float
	custo_Passado: float
	perc_Dif: float
	data_Pag: data


#end Internet class


class mercado(NamedTuple):
	custo_Presente: float
	custo_Passado: float
	perc_Dif: float
	data_Pag: data


#end Mercado class


class lazer(NamedTuple):
	custo_Presente: float
	custo_Passado: float
	perc_Dif: float


#end lazer class


class tot_Gast(NamedTuple):
	tot_atual: float
	tot_passado: float
	perc_Dif: float


class Finan(NamedTuple):
	salario_Liq: float
	salario_Desc: float
	luz_Conta: luz
	agua_Conta: agua
	internet_Conta: internet
	mercado_Conta: mercado
	lazer_Conta: lazer
	cap_Sobra: float
	tot_Gasto: tot_Gast


#end Financeiro class
try:
	with open('past_data.pik', 'rb') as f:
		dados_Lista2 = pickle.load(f)
  with open('last_date.pik', 'rb') as f:
    last_date = pickle.load(f)
	print("sucesso")
	print(dados_Lista2)
	luz.custo_Passado = dados_Lista2[0]
	agua.custo_Passado = dados_Lista2[1]
	internet.custo_Passado = dados_Lista2[2]
	mercado.custo_Passado = dados_Lista2[3]
	lazer.custo_Passado = dados_Lista2[4]
	tot_Gast.tot_passado = dados_Lista2[5]
except FileNotFoundError:
	luz.perc_Dif = 0
	luz.custo_Passado = 0
	agua.perc_Dif = 0
	agua.custo_Passado = 0
	internet.perc_Dif = 0
	internet.custo_Passado = 0
	mercado.perc_Dif = 0
	mercado.custo_Passado = 0
	lazer.perc_Dif = 0
	lazer.custo_Passado = 0
	tot_Gast.tot_passado = 0
	tot_Gast.perc_Dif = 0

def calc_Perc(serviço,serviço2):
  x = 100 * (serviço2//(serviço2 + serviço.custo_Passado))
  return x

#end calc_Perc

def in_dado():
  sal_liq_in = float(input("Salário deste mês: R$"))
  sal_desc_in = float(input("Desconto do salário: R$"))
  luz_pres_in = float(input("Custo de luz atual: R$"))
  agua_pres_in = float(input("Custo de água atual: R$"))
  internet_pres_in = float(input("Custo de internet atual: R$"))
  mercado_pres_in = float(input("Custo total do mercado atual: R$"))
  lazer_pres_in = float(input("Custo total de lazer atual: R$"))

  tot_atual_in = (luz_pres_in + agua_pres_in + internet_pres_in + mercado_pres_in + lazer_pres_in)
  cap_sobra_in = sal_liq_in - (sal_desc_in + luz_pres_in + agua_pres_in + internet_pres_in +mercado_pres_in + lazer_pres_in)
  tot_Gast.perc_Dif = 100 * tot_atual_in // (tot_atual_in + tot_Gast.tot_passado) 

  luz.perc_Dif=calc_Perc(luz,luz_pres_in)
  agua.perc_Dif=calc_Perc(agua,agua_pres_in)
  internet.perc_Dif=calc_Perc(internet,internet_pres_in)
  mercado.perc_Dif=calc_Perc(mercado,mercado_pres_in)
  lazer.perc_Dif=calc_Perc(lazer,lazer_pres_in)
  rec = Finan(
	    salario_Liq=sal_liq_in,
	    salario_Desc=sal_desc_in,
	    luz_Conta=luz(
	        custo_Presente=luz_pres_in,
	        custo_Passado=luz.custo_Passado,
	        perc_Dif=luz.perc_Dif,
	        data_Pag=in_datas_pgto(luz)),
	    agua_Conta=agua(
	        custo_Presente=agua_pres_in,
	        custo_Passado=agua.custo_Passado,
	        perc_Dif=agua.perc_Dif,
	        data_Pag=in_datas_pgto(agua)),
	    internet_Conta=internet(
	        custo_Presente=internet_pres_in,
	        custo_Passado=internet.custo_Passado,
	        perc_Dif=internet.perc_Dif,
	        data_Pag=in_datas_pgto(internet)),
	    mercado_Conta=mercado(
	        custo_Presente=mercado_pres_in,
	        custo_Passado=mercado.custo_Passado,
	        perc_Dif=mercado.perc_Dif,
	        data_Pag=in_datas_pgto(mercado)),
	    lazer_Conta=lazer(
	        custo_Presente=lazer_pres_in,
	        custo_Passado=lazer.custo_Passado,
	        perc_Dif=mercado.perc_Dif),
	    cap_Sobra=cap_sobra_in,
	    tot_Gasto=tot_Gast(
	        tot_atual=tot_atual_in,
	        tot_passado=tot_Gast.tot_passado,
	        perc_Dif=tot_Gast.perc_Dif))
  return rec


#end in_dado


def in_datas_pgto(serviço):
	print("Data de pagamentos para",serviço.__name__,":")
	in_dia = int(input("Dia do pagamento (número): "))
	serviço.data_Pag = data(in_dia)
	return in_dia


#end in_datas_pgto

#rodando as datas de pagamento para os serviços
dados_Lista = (in_dado())

def change_List(serviço,x):
  serviço.custo_Passado = dados_Lista[x][0]
  lista_Nova.append(serviço.custo_Passado)
#end change_List

def print_data(serviço, var,x):
  print(serviço.__name__,":")
  print("Custo atual: R$", dados_Lista[x][0])
  if var == 2:
    print("Data de pagamento: dia ", dados_Lista[x][3],"\n")


#end print_data
print("------------------------------------ \n")
print_data(luz, 2,2)
print_data(agua, 2,3)
print_data(internet, 2,4)
print_data(mercado, 2,5)
print_data(lazer, 1,6)
print("Salário Liquido: R$", dados_Lista.salario_Liq)
print("Desconto do salário: R$", dados_Lista.salario_Desc)
print("Efetivo não utilizado: R$", dados_Lista.cap_Sobra)
print("Percentual de diferença de custo com o mês anterior:", dados_Lista.tot_Gasto[2], "%")
lista_Nova=[]
total_passado=dados_Lista[8][0]
change_List(luz,2)
change_List(agua,3)
change_List(internet,4)
change_List(mercado,5)
change_List(lazer,6)
lista_Nova.append(total_passado)
tuple(lista_Nova)
with open('past_data.pik', 'wb') as f:
  pickle.dump(lista_Nova, f, -1)
with open('last_date.pik', 'wb') as f:
  pickle.dump(mylist,f,-1)