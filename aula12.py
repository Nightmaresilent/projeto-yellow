nome = input ("Digite seu nome: ")
idade = input ("Digite sua idade: ")
if nome and idade:
    print (f'seu nome é {nome}')
    print ('seu nome invertido é', nome [ : :-1])
    if " " in nome:
        print ('seu nome contém espaços')
    else:
        print('seu nome não contém espaços')
    print ('seu nome tem no total de letras:', len(nome))
    print ('a primeira letra do seu nome é:', nome [0:1:1])
    print ('a ultima letra do seu nome é:', nome[ :-2:-1])
else:
    print('você não digitou um nome ou idade')
