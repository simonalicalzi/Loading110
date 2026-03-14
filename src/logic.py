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
    esami_sostenuti: list[Esame], _cfu_totali: int, obiettivo: float = 110.0
) -> float:
    numero_lodi = sum(1 for e in esami_sostenuti if e.lode)
    bonus_lodi = numero_lodi * 0.5
    media_necessaria = (obiettivo - bonus_lodi) * 3 / 11
    return round(media_necessaria, 2)


# --- INTERFACCIA DI INPUT UTENTE ---

if __name__ == "__main__":
    print("=" * 40)
    print("   BENVENUTA IN LOADING 110! 🎓")
    print("=" * 40)

    miei_esami = []

    try:
        cfu_totali_corso = int(
            input("Inserisci i CFU totali del tuo corso (es. 180): ")
        )
        obiettivo_laurea = float(
            input("Qual è il tuo obiettivo di voto finale? (es. 110): ")
        )
    except ValueError:
        print(
            "Errore: Inserisci solo numeri. Userò i valori predefiniti (180 CFU, obiettivo 110)."
        )
        cfu_totali_corso = 180
        obiettivo_laurea = 110.0

    print("\n--- Inserimento Esami (scrivi 'stop' nel nome per terminare) ---")

    while True:
        nome = input("\nNome esame: ")
        if nome.lower() == "stop":
            break

        try:
            voto = int(input(f"Voto per {nome}: "))
            cfu = int(input(f"CFU per {nome}: "))
            lode_input = input("Ha la lode? (s/n): ").lower()
            lode = True if lode_input == "s" else False

            nuovo_esame = Esame(nome=nome, voto=voto, cfu=cfu, lode=lode)
            miei_esami.append(nuovo_esame)

        except ValueError:
            print("⚠️ Dati non validi per questo esame. Riprova.")
            continue

    if miei_esami:
        media_a = media_aritmetica(miei_esami)
        media_p = calcola_media_ponderata(miei_esami)
        proiezione = proiezione_voto_laurea(media_p)
        info_progresso = analisi_avanzamento(miei_esami, cfu_totali_corso)
        media_necessaria = stima_media_necessaria(
            miei_esami, cfu_totali_corso, obiettivo_laurea
        )
        lodi = sum(1 for e in miei_esami if e.lode)

        print("\n" + "=" * 40)
        print("      --- IL TUO REPORT ---")
        print("=" * 40)
        print(f"📊 Medie: Aritmetica: {media_a:.2f} | Ponderata: {media_p:.2f}")
        print("   Le abbiamo calcolate noi, tu pensa a studiare!")

        print("-" * 40)
        print(f"🔮 Leggiamo il futuro: Il tuo voto di partenza è {proiezione}/110")

        print("-" * 40)
        print(f"🎖️ Operazione Lode: Hai collezionato {lodi} lode/i.")
        print(f"   Peso totale bonus: +{lodi * 0.5} punti sulla base laurea.")

        print("-" * 40)
        print(f"📉 {obiettivo_laurea}, l'obiettivo di tutti:")
        print(f"   Devi mantenere una media di {media_necessaria}")
        print(f"   nei restanti {info_progresso['cfu_mancanti']} CFU.")

        print("-" * 40)
        print(
            f"✅ Avanzamento: {info_progresso['percentuale_completamento']}% completato."
        )
        print("=" * 40 + "\n")
    else:
        print("\nNessun esame inserito. Alla prossima!")
