from src.logic import Esame, media_aritmetica

def test_media_aritmetica_semplice():
    lista_esami = [
        Esame(nome="Ingegneria del Software", voto=24, cfu=9),
        Esame(nome="Strutture Discrete", voto=30, cfu=6)
    ]
    assert media_aritmetica(lista_esami) == 27.0

from src.logic import Esame, calcola_media_ponderata

def test_media_ponderata_semplice():
    """Verifica il calcolo base della media ponderata"""
    lista_esami = [
        Esame(nome="Analisi 1", voto=30, cfu=12),
        Esame(nome="Inglese", voto=18, cfu=3)
    ]
    # Calcolo: ((30*12) + (18*3)) / (12+3) = (360 + 54) / 15 = 27.6
    assert calcola_media_ponderata(lista_esami) == 27.6

def test_media_ponderata_pesi_diversi():
    """Verifica che un esame con molti CFU influenzi di più la media"""
    # Caso A: 30 in un esame importante (12 CFU) e 18 in uno piccolo (6 CFU)
    esami_a = [
        Esame(nome="Esame Pesante", voto=30, cfu=12),
        Esame(nome="Esame Leggero", voto=18, cfu=6)
    ]
    media_a = calcola_media_ponderata(esami_a) # Risultato: 26.0

    # Caso B: 18 in un esame importante (12 CFU) e 30 in uno piccolo (6 CFU)
    esami_b = [
        Esame(nome="Esame Pesante", voto=18, cfu=12),
        Esame(nome="Esame Leggero", voto=30, cfu=6)
    ]
    media_b = calcola_media_ponderata(esami_b) # Risultato: 22.0

    # Il test passa se la media del caso A è maggiore della media del caso B
    assert media_a > media_b