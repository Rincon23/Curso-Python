n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2
if m >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')

#Simplificado

print('Aprovado' if m >= 6 else 'Reprovado')