par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n%2 == 0:
            par += 1
        else:
            impar += 1
print('Foram contados\nPares: {}\nImpares {}'.format(par,impar))