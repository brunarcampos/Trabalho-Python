from inspecao import CORES
from producao import CAPACIDADE_CAIXA, Producao
from relatorio import gerar_relatorio

def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("  ⚠ Este campo não pode ficar vazio.")
        

def ler_numero(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(texto)
        except ValueError:
            print("  ⚠ Digite um número válido (ex.: 50 ou 8.5).")
            continue
        if numero <= 0:
            print("  ⚠ O valor deve ser maior que zero.")
            continue
        return numero
      
#Cadastro das peças

def cadastrar_peca(producao):
    print("\n--- Cadastrar nova peça ---")
    id_peca = ler_texto("ID da peça: ")
    if producao.buscar(id_peca):
        print(f"  ⚠ Já existe uma peça com o ID '{id_peca}'.")
        return
    peso = ler_numero("Peso (g): ")
    cor = ler_texto("Cor: ")
    comprimento = ler_numero("Comprimento (cm): ")

    peca = producao.cadastrar_peca(id_peca, peso, cor, comprimento)
    if peca.aprovada:
        print(f"\n✅ Peça {peca.id} APROVADA e armazenada na caixa.")
    else:
        print(f"\n❌ Peça {peca.id} REPROVADA:")
        for motivo in peca.motivos:
            print(f"   - {motivo}")

#Listar as peças

def listar_pecas(producao):
    print("\n--- Peças cadastradas ---")
    if not producao.pecas:
        print("Nenhuma peça cadastrada.")
        return

    print(f"\nAPROVADAS ({len(producao.aprovadas)}):")
    for p in producao.aprovadas:
        print(f"  [{p.id}] {p.peso}g | {p.cor} | {p.comprimento}cm")
    if not producao.aprovadas:
        print("  (nenhuma)")

    print(f"\nREPROVADAS ({len(producao.reprovadas)}):")
    for p in producao.reprovadas:
        print(f"  [{p.id}] {p.peso}g | {p.cor} | {p.comprimento}cm")
        for motivo in p.motivos:
            print(f"        - {motivo}")
    if not producao.reprovadas:
        print("  (nenhuma)")
        
# Deletar as peças

def remover_peca(producao):
    print("\n--- Remover peça cadastrada ---")
    id_peca = ler_texto("ID da peça a remover: ")
    if producao.remover_peca(id_peca):
        print(f"✅ Peça {id_peca} removida. Caixas recalculadas.")
    else:
        print(f"⚠ Peça '{id_peca}' não encontrada.")

#Caixas quantidades

def listar_caixas(producao):
    print("\n--- Caixas fechadas ---")
    if not producao.caixas_fechadas:
        print("Nenhuma caixa fechada ainda "
              f"(cada caixa fecha com {CAPACIDADE_CAIXA} peças aprovadas).")
    for numero, caixa in enumerate(producao.caixas_fechadas, start=1):
        ids = ", ".join(p.id for p in caixa)
        print(f"Caixa {numero} ({len(caixa)}/{CAPACIDADE_CAIXA}): {ids}")
    print(f"\nCaixa aberta atual: {len(producao.caixa_aberta)}/{CAPACIDADE_CAIXA} peças")

# Relatório

def gerar_relatorio_final(producao):
    print()
    print(gerar_relatorio(producao))

# Menu

def exibir_menu():
    print("\n===== CONTROLE DE PRODUÇÃO E QUALIDADE =====")
    print("1 - Cadastrar nova peça")
    print("2 - Listar peças aprovadas/reprovadas")
    print("3 - Remover peça cadastrada")
    print("4 - Listar caixas fechadas")
    print("5 - Gerar relatório final")
    print("0 - Sair")


def main():
    producao = Producao()
    acoes = {
        "1": cadastrar_peca,
        "2": listar_pecas,
        "3": remover_peca,
        "4": listar_caixas,
        "5": gerar_relatorio_final,
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        acao = acoes.get(opcao)
        if acao:
            acao(producao)
        else:
            print("⚠ Opção inválida. Escolha de 0 a 5.")


if __name__ == "__main__":
    main()