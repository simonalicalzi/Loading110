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

def calcola_media_ponderata(esami: list) -> float:
    if not esami:
        return 0.0
    
    somma_pesata = 0
    totale_cfu = 0
    
    for esame in esami:
        # Gestione lode: se l'esame ha la lode, il voto vale 31
        voto_effettivo = 31 if (esame.voto == 30 and esame.lode) else esame.voto
        
        somma_pesata += voto_effettivo * esame.cfu
        totale_cfu += esame.cfu
        
    return somma_pesata / totale_cfu if totale_cfu > 0 else 0.0

def proiezione_voto_laurea(media_ponderata: float) -> float:
    
    if media_ponderata == 0:
        return 0.0
    
    # Formula: (Media * 110) / 30  =>  Media * 11 / 3
    voto_partenza = (media_ponderata * 11) / 3
    
    # Di solito il voto di partenza si tiene con due decimali
    return round(voto_partenza, 2)
