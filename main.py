"""DISCLAIMER: Este app é um projeto pessoal do Wilson Mielke, qualquer uso profissional não está autorizado, com excessão de casos excepcionais com aprovação do mesmo.
App feito para organizar finanças pessoais
versão 0.1.21
(versão 0 = beta, .1 = build, .21 = teste com 1 bug)
"""
from typing import NamedTuple
import datetime
import pickle

  
mylist = []
today = datetime.date.today()
mylist.append(today)
print("Dia de hoje: ", mylist[0])


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
  with open('data_miner.pik', 'rb') as f:
    animals, population = pickle.load(f)
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

def in_dado():
	sal_liq_in = float(input("Salário deste mês: R$"))
	sal_desc_in = float(input("Desconto do salário: R$"))
	luz_pres_in = float(input("Custo de luz atual: R$"))
	agua_pres_in = float(input("Custo de água atual: R$"))
	internet_pres_in = float(input("Custo de internet atual: R$"))
	mercado_pres_in = float(input("Custo total do mercado atual: R$"))
	lazer_pres_in = float(input("Custo total de lazer atual: R$"))
  tot_Gast.tot_atual = (luz_pres_in + agua_pres_in + internet_pres_in +mercado_pres_in + lazer_pres_in)
  in_datas_pgto(luz)
	in_datas_pgto(agua)
	in_datas_pgto(internet)
	in_datas_pgto(mercado)
  Finan.perc_Dif = sal_liq_in - (sal_desc_in + Finan.tot_Gast) 
	rec = Finan(salario_Liq=sal_liq_in,salario_Desc=sal_desc_in,luz_Conta=luz(custo_Presente=luz_pres_in,custo_Passado=luz.custo_Passado,perc_Dif= luz.perc_Dif, data_Pag=in_datas_pgto(luz)),agua_Conta=agua(custo_Presente=agua_pres_in,custo_Passado=agua.custo_Passado,perc_Dif=agua.perc_Dif, data_Pag=in_datas_pgto(agua)),internet_Conta=internet(custo_Presente=internet_pres_in, custo_Passado=internet.custo_Passado, perc_Dif=internet.perc_Dif, data_Pag=in_datas_pgto(internet)),mercado_Conta=mercado(custo_Presente=mercado_pres_in, custo_Passado=mercado.custo_Passado,perc_Dif=mercado.perc_Dif, data_Pag=in_datas_pgto(mercado)),lazer_Conta=lazer(custo_Presente=lazer_pres_in,custo_Passado=lazer.custo_Passado,perc_Dif=mercado.perc_Dif))
	return rec


#end in_dado


def in_datas_pgto(serviço):
	print("Datas de pagamentos para ", serviço)
	in_dia = int(input("Dia do pagamento (número): "))
	serviço.data_Pag = data(dia=in_dia)
	return in_dia


#end in_datas_pgto

#rodando as datas de pagamento para os serviços
dados_Lista = [in_dado()]


def print_data(serviço, var):
	print("Custo atual: ", dados_Lista.serviço_Conta.custo_Presente)
	if var == 2:
		print("Data de pagamento: ", dados_Lista.serviço_Conta.data_Pag)


#end print_data
print_data(luz,2)
print_data(agua,2)
print_data(internet,2)
print_data(mercado,2)
print_data(lazer,1)
print("Salário Liquido: R$", dados_Lista.salario_Liq)
print("Salário com descontos: R$", dados_Lista.salario_Desc)
print("Efetivo não utilizado: R$",cap_Sobra)
with open('past_data.pik', 'wb') as f:
	pickle.dump(dados_lista, f, -1)
