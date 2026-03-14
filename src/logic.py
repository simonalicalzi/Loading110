# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring

"""
Logic functions for university grade management and graduation projection.
"""

from dataclasses import dataclass


@dataclass
class Esame:
    nome: str
    voto: int
    cfu: int
    lode: bool = False


def media_aritmetica(esami: list[Esame]) -> float:
    if not esami:
        return 0.0
    return sum(e.voto for e in esami) / len(esami)


def calcola_media_ponderata(esami: list[Esame]) -> float:
    if not esami:
        return 0.0
    totale_punti = sum((e.voto + (1 if e.lode else 0)) * e.cfu for e in esami)
    totale_cfu = sum(e.cfu for e in esami)
    return totale_punti / totale_cfu


def proiezione_voto_laurea(media: float) -> float:
    return media * 11 / 3


def analisi_avanzamento(esami: list[Esame], cfu_totali: int) -> dict:
    cfu_acquisiti = sum(e.cfu for e in esami)
    percentuale = (cfu_acquisiti / cfu_totali) * 100 if cfu_totali > 0 else 0
    return {
        "cfu_acquisiti": cfu_acquisiti,
        "cfu_mancanti": max(0, cfu_totali - cfu_acquisiti),
        "percentuale_completamento": round(percentuale, 2),
    }


def stima_media_necessaria(
    esami_sostenuti: list[Esame], cfu_totali: int, obiettivo: float = 110.0
) -> float:
    numero_lodi = sum(1 for e in esami_sostenuti if e.lode)
    bonus_lodi = numero_lodi * 0.5
    media_necessaria = (obiettivo - bonus_lodi) * 3 / 11
    return round(media_necessaria, 2)
