from operator import index


tabela = 'Santos', 'Palmeiras', 'Corinthians', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Fluminense', 'São Paulo', 'Flamengo', 'Botafogo'

print(f'Os primeiros 5 colocados: {tabela[:5]}')
print(f'Os últimos 4 colocados: {tabela[-4:]}')
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print(f'O Santos está na {tabela.index("Santos") + 1} posição!')

