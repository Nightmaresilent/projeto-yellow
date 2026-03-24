cliente = float(input('Digite quanto você quer investir de 0 a 100: '))

if cliente < 0:
    print("Valor invalido") 
elif cliente <= 20:
    print("Você é um investidor conservador")
elif cliente <= 50:
    print("Você é um investidor moderado")
elif cliente <= 100:
    print("Você é um investidor arrojado")
else: 
    print("Valor invalido") 
