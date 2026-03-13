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

def analisi_avanzamento(esami: list, cfu_totali_percorso: int) -> dict:
    """
    Calcola i CFU acquisiti e la percentuale di completamento.
    """
    cfu_acquisiti = sum(esame.cfu for esame in esami)
    
    # Calcolo percentuale (evitiamo divisioni per zero)
    percentuale = (cfu_acquisiti / cfu_totali_percorso * 100) if cfu_totali_percorso > 0 else 0
    
    return {
        "cfu_acquisiti": cfu_acquisiti,
        "cfu_mancanti": max(0, cfu_totali_percorso - cfu_acquisiti),
        "percentuale_completamento": round(percentuale, 2)
    }

def stima_media_necessaria(esami_sostenuti: list, cfu_totali_percorso: int, obiettivo_voto: float = 110.0) -> float:
    """
    Calcola la media ponderata che lo studente deve mantenere negli esami rimanenti
    per raggiungere l'obiettivo (es. 110), considerando il bonus lodi.
    """
    cfu_acquisiti = sum(e.cfu for e in esami_sostenuti)
    cfu_mancanti = cfu_totali_percorso - cfu_acquisiti
    
    if cfu_mancanti <= 0:
        return 0.0

    # Calcolo bonus lodi attuali (0.5 punti per ogni lode)
    numero_lodi = sum(1 for e in esami_sostenuti if e.lode)
    bonus_lodi = numero_lodi * 0.5
    
    # Calcoliamo quanti punti "su 110" mancano per raggiungere l'obiettivo
    # Sottraiamo il bonus lodi e la proiezione attuale
    punti_attuali_su_110 = (calcola_media_ponderata(esami_sostenuti) * 11 / 3)
    
    # Formula inversa per capire la media necessaria sugli esami futuri
    # Per semplicità verso l'esame, calcoliamo la media totale necessaria:
    media_totale_necessaria = (obiettivo_voto - bonus_lodi) * 3 / 11
    
    return round(media_totale_necessaria, 2)