from inspecao import inspecionar
from peca import Peca
CAPACIDADE_CAIXA = 10

class Producao:
    def __init__(self):
        self.pecas = []             
        self.caixas_fechadas = []  
        self.caixa_aberta = []      

    def buscar(self, id_peca):
        for peca in self.pecas:
            if peca.id == id_peca:
                return peca
        return None

    @property
    def aprovadas(self):
        return [p for p in self.pecas if p.aprovada]

    @property
    def reprovadas(self):
        return [p for p in self.pecas if not p.aprovada]

    @property
    def total_caixas_utilizadas(self):
        return len(self.caixas_fechadas) + (1 if self.caixa_aberta else 0)

    # Cadastrando as caixas
  
    def cadastrar_peca(self, id_peca, peso, cor, comprimento):
        if self.buscar(id_peca) is not None:
            raise ValueError(f"Já existe uma peça com o ID '{id_peca}'.")

        peca = Peca(id_peca, peso, cor, comprimento)
        inspecionar(peca)
        self.pecas.append(peca)
        self._reorganizar_caixas()
        return peca

    #Removendo as peças
    
    def remover_peca(self, id_peca):
        peca = self.buscar(id_peca)
        if peca is None:
            return False
        self.pecas.remove(peca)
        self._reorganizar_caixas()
        return True

    #Organizando as caixas
    
    def _reorganizar_caixas(self):
        self.caixas_fechadas = []
        self.caixa_aberta = []

        for peca in self.aprovadas:
            self.caixa_aberta.append(peca)
            if len(self.caixa_aberta) == CAPACIDADE_CAIXA:
                self.caixas_fechadas.append(self.caixa_aberta) 
                self.caixa_aberta = []                          