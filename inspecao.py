#REGRAS DE QUALIDADE
PESO_MINIMO = 95
PESO_MAXIMO = 105
CORES = ("azul", "verde")
COMPRIMENTO_MINIMO = 10
COMPRIMENTO_MAXIMO = 20

#Validando se as peças estão no padrão
def verificar_peca(peca):
    motivos = []
    
    if not (PESO_MINIMO <= peca.peso <= PESO_MAXIMO):
        motivos.append(f"Peso fora do padrão ({peca.peso}g; Peso esperado é de no mínimo {PESO_MINIMO}g e no máximo {PESO_MAXIMO}g.)")
        
    if peca.cor.strip().lower() not in CORES:
        motivos.append(f"Cor inválida ({peca.cor}; Cor esperada: azul ou verde.)")
        
    if not (COMPRIMENTO_MINIMO <= peca.comprimento <= COMPRIMENTO_MAXIMO):
        motivos.append(f"Comprimento fora do padrão ({peca.comprimento}cm; "
                       f"Comprimento esperado é de no mínimo {COMPRIMENTO_MINIMO}cm e no máximo {COMPRIMENTO_MAXIMO}cm.)")
    return motivos

#Última verificação se foi aprovada ou reprovada
def inspecionar(peca):
    peca.motivos = verificar_peca(peca)
    peca.aprovada = len(peca.motivos) == 0
    return peca.aprovada