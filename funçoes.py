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