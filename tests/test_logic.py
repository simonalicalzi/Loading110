"""
Unit tests for the graduation utility logic functions.
"""

import pytest

from src.logic import (
    Esame,
    analisi_avanzamento,
    calcola_media_ponderata,
    media_aritmetica,
    proiezione_voto_laurea,
    stima_media_necessaria,
)


def test_media_aritmetica_semplice():
    lista_esami = [
        Esame(nome="Ingegneria del Software", voto=24, cfu=9),
        Esame(nome="Strutture Discrete", voto=30, cfu=6),
    ]
    assert media_aritmetica(lista_esami) == 27.0


def test_media_ponderata_semplice():
    lista_esami = [
        Esame(nome="Analisi 1", voto=30, cfu=12),
        Esame(nome="Inglese", voto=18, cfu=3),
    ]
    assert calcola_media_ponderata(lista_esami) == 27.6


def test_media_ponderata_pesi_diversi():
    esami_a = [
        Esame(nome="Esame Pesante", voto=30, cfu=12),
        Esame(nome="Esame Leggero", voto=18, cfu=6),
    ]
    media_a = calcola_media_ponderata(esami_a)
    esami_b = [
        Esame(nome="Esame Pesante", voto=18, cfu=12),
        Esame(nome="Esame Leggero", voto=30, cfu=6),
    ]
    media_b = calcola_media_ponderata(esami_b)
    assert media_a > media_b


def test_media_ponderata_e_lode():
    esami = [
        Esame(nome="Analisi", voto=30, cfu=12, lode=True),
        Esame(nome="Chimica", voto=18, cfu=6, lode=False),
    ]
    risultato = calcola_media_ponderata(esami)
    assert round(risultato, 2) == 26.67


def test_proiezione_voto_laurea():
    assert proiezione_voto_laurea(27.0) == 99.0
    assert proiezione_voto_laurea(30.0) == 110.0
    assert proiezione_voto_laurea(25.5) == 93.5


def test_analisi_avanzamento():
    esami = [
        Esame(nome="Esame 1", voto=24, cfu=12),
        Esame(nome="Esame 2", voto=30, cfu=6),
    ]
    risultato = analisi_avanzamento(esami, 180)
    assert risultato["cfu_acquisiti"] == 18
    assert risultato["cfu_mancanti"] == 162
    assert risultato["percentuale_completamento"] == 10.0


def test_stima_media_necessaria():
    esami = [
        Esame(nome="Esame 1", voto=30, cfu=12, lode=True),
        Esame(nome="Esame 2", voto=30, cfu=12, lode=True),
    ]
    risultato = stima_media_necessaria(esami, 180, 110.0)
    assert risultato == 29.73
