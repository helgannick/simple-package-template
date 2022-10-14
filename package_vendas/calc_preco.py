from package_vendas.formata import formatacao

def aumento(valor, porcentagem, formata=False):
    res = valor +(valor * (porcentagem / 100))
    
    if formata:
     return formatacao.real(res)

    else:
     return res

def reducao(valor,  porcentagem, formata=False):
   res = valor - (valor * (porcentagem / 100))
   
   if formata:
    return  formatacao.real(res)       

 