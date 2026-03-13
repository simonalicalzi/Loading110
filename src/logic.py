from dataclasses import dataclass
from typing import List

@dataclass
class Esame:
    nome: str
    voto: int
    cfu: int
    lode: bool = False

def media_aritmetica(esami: List[Esame]) -> float:
    if not esami:
        return 0.0
    totale_voti = sum(esame.voto for esame in esami)
    return totale_voti / len(esami)
