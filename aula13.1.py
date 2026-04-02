numero_str = input ('Digite um número inteiro: ')
numero_float = float(numero_str)
teste = numero_float.is_integer()
if teste:
   print ('é um número inteiro')
else:
   print('Não é um número inteiro.')
numero_int = int(numero_str)
if numero_int % 2 == 1:
   print('é impar')
else:
   print('é par')
