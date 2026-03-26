renda_fixa = input ('Informe sua Renda Mensal: ')
nome_status = input ('Seu nome está limpo? [S] ou [N]: ')
if nome_status == 'S' and int(renda_fixa) >= 2000 :
     print ("você está aprovado")
else:
     print ("você está reprovado")
