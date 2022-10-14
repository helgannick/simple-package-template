from   package_vendas.calc_preco import aumento, reducao
from   package_vendas.formata import formatacao

preco = 59.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata= True)
print (preco_com_aumento)


preco_com_reducao = reducao(valor=preco, porcentagem=15, formata= True)
print (preco_com_reducao)

