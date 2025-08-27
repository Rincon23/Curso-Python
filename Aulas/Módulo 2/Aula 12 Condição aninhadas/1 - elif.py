nome = input('Qual é seu nome? ')

if nome == 'enzo':
    print('mesmo nome do desenvolvedor!')
elif nome == 'gustavo':
    print('ganabara?')
elif nome in 'joâo pedro jose maria':
    print('Nome popular detectado!')
else:
    print('Olá {}!'.format(nome))