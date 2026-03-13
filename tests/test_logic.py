from src.logic import Esame, media_aritmetica

def test_media_aritmetica_semplice():
    lista_esami = [
        Esame(nome="Ingegneria del Software", voto=24, cfu=9),
        Esame(nome="Strutture Discrete", voto=30, cfu=6)
    ]
    assert media_aritmetica(lista_esami) == 27.0

    