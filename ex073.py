times = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Grêmio', 'Atlético-PR', 'Cuiabá', 'São Paulo', 'Atlético', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Corinthians', 'Goiás', 'Bahia', 'Santos', 'Coritiba', 'Vasco da Gama', 'América-MG')
print(f'Os cinco primeiros colocados são: {times[0:5]}.')
print(f'Os últimos quatro colocados são: {times[-4:]}')
print(f'Os times em ordem alfabéticas são: {sorted(times)}')
print('O Palmeiras está na posição {}'.format(times.index('Palmeiras') + 1))