def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    i=0
    while i < tamanho:
        if orientacao == 'horizontal':
            posicao.append([linha,coluna+i])
        if orientacao == 'vertical':
            posicao.append([linha+i, coluna])
        i+=1
    return posicao

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome not in frota:
        frota[nome] = [posicoes]
    else:
        frota[nome].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    for i in range(len(tabuleiro)):
        if i == linha:
            for j in range(len(tabuleiro[i])):
                if j == coluna:
                    if tabuleiro[i][j] == 1:
                        tabuleiro[i][j] = 'X'
                    elif tabuleiro[i][j] == 0:
                        tabuleiro[i][j] = '-'
                
    return tabuleiro

def posiciona_frota(frota):
    lista = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

    for posicao in frota.values():
        for quant in posicao:
            for info in quant:
                for i in range(len(lista)):
                    if i == info[0]:
                        for j in range(len(lista[i])):
                            if j == info[1]:
                                lista[i][j] = 1
    return lista
def afundados(frota, tabuleiro):
    cont = 0
    afundados = 0
    for posicao in frota.values():
        for quant in posicao:
            cont = 0 
            for info in quant:
                for i in range(len(tabuleiro)):
                    if i == info[0]:
                        for j in range(len(tabuleiro[i])):
                            if j == info[1]:
                                if tabuleiro[i][j] == 'X':
                                    cont += 1
            if len(quant) == cont:
                afundados += 1
    return afundados

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    valida = True
    if len(frota) == 0:
        for t in range(len(posicoes)):
            if posicoes[t][0] < 9:
                if posicoes[t][1] < 9:
                    valida = True
                elif posicoes [t][1] > 9:
                    return False
            elif posicoes[t][0]> 9 or posicoes[t][1]> 9:
                return False
        return valida

    for p in range(len(posicoes)):
        for posicao in frota.values():
            for quant in posicao:
                for info in quant:
                    if posicoes[p][0] > 9:
                        return False
                    if posicoes[p][1] > 9:
                        return False
                    if posicoes[p][0] == info[0]:
                        if posicoes[p][1] > 9:
                            return False
                        if posicoes[p][1] == info[1]:
                            return False
                        elif posicoes[p][1] != info[1]:
                            valida = True
    return valida
    