print('------JOGO DO QUEIJO------')
print('Vamos ver quando o rato vai encontrar o queijo.')

tentativa = 0
local = 'ARMÁRIO'

opcao_local = ['GELADEIRA', 'FOGÃO', 'MESA', 'BALCÃO ','ARMÁRIO']

for loc in opcao_local:
    tentativa += 1
    if loc == local:
        print(f'Você achou o queijo no(a) {loc}, na tentativa {tentativa}')
        break
    else:
        continue
    


