from collections import Counter
from producao import CAPACIDADE_CAIXA
 
# Categoria

def _categoria(motivo):
    return motivo.split(" ")[0]

#Gerando relatório

def gerar_relatorio(producao):
    aprovadas = producao.aprovadas
    reprovadas = producao.reprovadas
    contagem = Counter()
    for peca in reprovadas:
        for motivo in peca.motivos:
            contagem[_categoria(motivo)] += 1
    linhas = [
        "=" * 44,
        "        RELATÓRIO FINAL DE PRODUÇÃO",
        "=" * 44,
        f"Total de peças inspecionadas : {len(producao.pecas)}",
        f"Total de peças aprovadas     : {len(aprovadas)}",
        f"Total de peças reprovadas    : {len(reprovadas)}",
    ]
    if reprovadas:
        linhas.append("")
        linhas.append("Motivos de reprovação (uma peça pode ter mais de um):")
        for categoria, qtd in contagem.most_common():
            linhas.append(f"  - {categoria}: {qtd}")
        linhas.append("")
        linhas.append("Detalhe por peça reprovada:")
        for peca in reprovadas:
            linhas.append(f"  [{peca.id}] " + "; ".join(peca.motivos))
    linhas += [
        "",
        f"Caixas fechadas ({CAPACIDADE_CAIXA}/{CAPACIDADE_CAIXA}) : {len(producao.caixas_fechadas)}",
        f"Peças na caixa aberta        : {len(producao.caixa_aberta)}/{CAPACIDADE_CAIXA}",
        f"Quantidade de caixas utilizadas : {producao.total_caixas_utilizadas}",
        "=" * 44,
    ]
    return "\n".join(linhas)