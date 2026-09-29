from dataclasses import dataclass, field

@dataclass
class Peca:
    id: str
    peso: float
    cor: str
    comprimento: float
    aprovada: bool = False
    motivos: list = field(default_factory=list)
    
    @property
    def status(self):
      return "APROVADA" if self.aprovada else "REPROVADA"