Nome = input("Digite seu nome: ")
Quantidade_de_letras_Nome = len(Nome)
print (f'Seu nome tem, {Quantidade_de_letras_Nome} letras')
if Quantidade_de_letras_Nome <= 4:
    print('Seu nome é muito pequeno')
elif Quantidade_de_letras_Nome <= 6:
    print('Seu nome é normal')
elif Quantidade_de_letras_Nome >= 6:
    print('Seu nome é grande')
