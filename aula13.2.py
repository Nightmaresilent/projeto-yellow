numero_str = input ('Digite um número inteiro: ')
if numero_str.isdigit():
   numero_str = int(numero_str)
   print ('é um número inteiro')
   if numero_str % 2 == 1:
        print('é impar')
   else: 
        print('é par')

else:
   print('Não é um número inteiro.')
