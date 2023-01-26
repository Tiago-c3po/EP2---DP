def define_posicoes(linha, coluna, orientação, tamanho):
    posicao = []
    i=0
    while i < tamanho:
        if orientação == 'horizontal':
            posicao.append([linha,coluna+i])
        if orientação == 'vertical':
            posicao.append([linha+i, coluna])
        i+=1
    return posicao
print(define_posicoes(0, 0, 'horizontal', 1))