tempo = int(input('Quantos anos tem seu carro? '))

if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('---Fim---')

#Simplificado

print('Carro novo' if tempo <= 3 else 'Carro velho')
print('---Fim---')