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

def calcola_media_ponderata(esami: list[Esame]) -> float:
    if not esami:
        return 0.0
    totale_punti = sum(e.voto * e.cfu for e in esami)
    totale_cfu = sum(e.cfu for e in esami)
    return totale_punti / totale_cfu