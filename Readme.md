# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

Protótipo em Python para controle de produção e qualidade de peças em uma linha de montagem.
O sistema recebe os dados de cada peça, decide automaticamente se ela está **aprovada** ou **reprovada**, armazena as aprovadas em **caixas de 10 peças** e gera um **relatório consolidado**.

> Trabalho da disciplina **Algoritmos e Lógica de Programação** – UniFECAF.

---

## Funcionamento

### Regras de qualidade

Uma peça só é aprovada se atender **às três** regras:

| Atributo    | Critério                          |
|-------------|-----------------------------------|
| Peso        | entre **95 g** e **105 g** (inclusive) |
| Cor         | **azul** ou **verde** (sem diferenciar maiúsculas/minúsculas) |
| Comprimento | entre **10 cm** e **20 cm** (inclusive) |

Se alguma regra falhar, a peça é reprovada e **todos** os motivos são registrados (uma peça pode ter mais de um).

### Caixas

- Somente peças **aprovadas** vão para as caixas.
- Cada caixa comporta **10 peças**. Ao atingir 10, ela é **fechada** e uma nova caixa é iniciada.
- Ao remover uma peça, as caixas são recalculadas automaticamente.

### Menu

| Opção | Ação |
|-------|------|
| 1 | Cadastrar nova peça (ID, peso, cor e comprimento) |
| 2 | Listar peças aprovadas/reprovadas (com os motivos das reprovadas) |
| 3 | Remover peça cadastrada (pelo ID) |
| 4 | Listar caixas fechadas (e situação da caixa aberta) |
| 5 | Gerar relatório final |
| 0 | Sair |

### Estrutura do projeto

```
Trabalho-Python/
├── main.py       # menu interativo e leitura/validação das entradas
├── peca.py       # dataclass Peca (id, peso, cor, comprimento, status, motivos)
├── inspecao.py   # regras de qualidade e inspeção das peças
├── producao.py   # classe Producao: cadastro, remoção e organização das caixas
├── relatorio.py  # geração do relatório final
└── README.md
```

---

## Como rodar

**Requisito:** Python 3.7 ou superior 

1. Verifique se o Python está instalado:
   ```bash
   python --version
   ```
2. Baixe ou clone o repositório:
   ```bash
   git clone <https://github.com/brunarcampos/Trabalho-Python>
   cd Trabalho-Python
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```
4. Use o menu digitando o número da opção e pressionando **Enter**.

---

## Exemplos de entradas e saídas

### 1) Cadastrar peça aprovada

```
Escolha uma opção: 1

--- Cadastrar nova peça ---
ID da peça: P001
Peso (g): 100
Cor: azul
Comprimento (cm): 15

✅ Peça P001 APROVADA e armazenada na caixa.
```

### 2) Cadastrar peça reprovada (vários motivos)

```
--- Cadastrar nova peça ---
ID da peça: P012
Peso (g): 110
Cor: vermelho
Comprimento (cm): 25

❌ Peça P012 REPROVADA:
   - Peso fora do padrão (110.0g; Peso esperado é de no mínimo 95g e no máximo 105g.)
   - Cor inválida (vermelho; Cor esperada: azul ou verde.)
   - Comprimento fora do padrão (25.0cm; Comprimento esperado é de no mínimo 10cm e no máximo 20cm.)
```

### 3) ID duplicado e entradas inválidas

```
ID da peça: P001
  ⚠ Já existe uma peça com o ID 'P001'.

Peso (g): abc
  ⚠ Digite um número válido (ex.: 50 ou 8.5).
```

### 4) Listar peças (opção 2)

```
APROVADAS (11):
  [P001] 100.0g | azul | 15.0cm
  [P002] 100.0g | verde | 15.0cm
  ...

REPROVADAS (2):
  [P012] 110.0g | vermelho | 25.0cm
        - Peso fora do padrão (...)
        - Cor inválida (...)
        - Comprimento fora do padrão (...)
  [P013] 90.0g | azul | 15.0cm
        - Peso fora do padrão (90.0g; Peso esperado é de no mínimo 95g e no máximo 105g.)
```

### 5) Listar caixas fechadas (opção 4)

```
--- Caixas fechadas ---
Caixa 1 (10/10): P001, P002, P003, P004, P005, P006, P007, P008, P009, P010

Caixa aberta atual: 1/10 peças
```

### 6) Remover peça (opção 3)

```
--- Remover peça cadastrada ---
ID da peça a remover: P013
✅ Peça P013 removida. Caixas recalculadas.
```

### 7) Relatório final (opção 5)

```
============================================
        RELATÓRIO FINAL DE PRODUÇÃO
============================================
Total de peças inspecionadas : 12
Total de peças aprovadas     : 11
Total de peças reprovadas    : 1

Motivos de reprovação (uma peça pode ter mais de um):
  - Peso: 1
  - Cor: 1
  - Comprimento: 1

Detalhe por peça reprovada:
  [P012] Peso fora do padrão (...); Cor inválida (...); Comprimento fora do padrão (...)

Caixas fechadas (10/10) : 1
Peças na caixa aberta        : 1/10
Quantidade de caixas utilizadas : 2
============================================
```

---

## Técnicas e boas práticas aplicadas

- Código dividido em módulos, cada um com uma responsabilidade.
- Constantes nomeadas para as regras (`PESO_MINIMO`, `CORES`, `CAPACIDADE_CAIXA`...).
- Validação de entrada (campo vazio, número inválido, valor ≤ 0, ID duplicado, vírgula decimal).
- `dataclass`, `@property` e `Counter` da biblioteca padrão.
- Menu com dicionário de funções em vez de vários `if/elif`.

## Limitações e próximos passos

- Os dados ficam apenas em memória (ao sair do programa, são perdidos).
- Possíveis evoluções: persistência em banco de dados, leitura de sensores, visão computacional, integração com sistemas industriais (MES/ERP).

## Autor

Bruna Regina de Campos de Almeida – UniFECAF + FTR