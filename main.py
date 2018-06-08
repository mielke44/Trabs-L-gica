from typing import NamedTuple
import datetime

mylist = []
today = datetime.date.today()
mylist.append(today)
print ("Dia de hoje: ",mylist[0])

class data(NamedTuple):
  dia:int

class luz(NamedTuple):
  custo_Presente:float
  custo_Passado:float
  perc_Dif:float
  data_Pag:data

#end Luz class

class agua(NamedTuple):
  custo_Presente:float
  custo_Passado:float
  perc_Dif:float
  data_Pag:data

#end Agua class

class internet(NamedTuple):
  custo_Presente:float
  custo_Passado:float
  perc_Dif:float
  data_Pag:data

#end Internet class

class mercado(NamedTuple):
  custo_Presente:float
  custo_Passado:float
  perc_Dif:float
  data_Pag:data

#end Mercado class

class lazer(NamedTuple):
  custo_Presente:float
  custo_Passado:float
  perc_Dif:float

#end lazer class

class tot_Gast(NamedTuple):
  tot_atual:float
  tot_passado:float
  perc_Dif:float

class Finan(NamedTuple):
  salario_Liq:float
  salario_Desc:float
  luz_Conta:luz
  agua_Conta:agua
  internet_Conta:internet
  mercado_Conta:mercado
  lazer_Conta:lazer
  cap_Sobra:float
  tot_Gasto:tot_Gast

#end Financeiro class

def in_dado():
  sal_liq_in=float(input("Salário deste mês: "))
  sal_desc_in=float(input("Desconto do salário: "))
  luz_pres_in=float(input("Custo de luz atual: "))
  agua_pres_in=float(input("Custo de água atual: "))
  internet_pres_in=float(input("Custo de internet atual: "))
  mercado_pres_in=float(input("Custo total do mercado atual: "))
  lazer_pres_in=float(input("Custo total de lazer atual: "))
  in_datas_pgto(luz)
  in_datas_pgto(agua)
  in_datas_pgto(internet)
  in_datas_pgto(mercado)
  rec=Finan(salario_Liq=sal_liq_in, salario_Desc=sal_desc_in, luz_Conta=luz(custo_Presente=luz_pres_in, data_Pag=in_datas_pgto(luz)), agua_Conta=agua(custo_Presente=agua_pres_in, data_Pag=in_datas_pgto(agua)),internet_Conta=internet(custo_Presente=internet_pres_in, data_Pag=in_datas_pgto(internet)),mercado_Conta=mercado(custo_Presente=mercado_pres_in, data_Pag=in_datas_pgto(mercado)),lazer_Conta=lazer(custo_Presente=lazer_pres_in))
  return rec
#end in_dado

def in_datas_pgto(serviço):
  print("Datas de pagamentos para ",serviço)
  in_dia = int(input("Dia do pagamento (número): "))
  serviço.data_Pag=data(dia=in_dia)
  return in_dia

#end in_datas_pgto

in_dado()

#rodando as datas de pagamento para os serviços
dados_Lista = [in_dado]
def print_data(serviço,var):
  print("Custo atual: ",dados_Lista.serviço_Conta.custo_Presente)
  if var == 2:
    print("Data de pagamento: ",dados_Lista.serviço_Conta.data_Pag)
#end print_data
print("Salário Liquido: ",dados_Lista.salario_Liq)
print("Salário com descontos: ",dados_Lista.salario_Desc)