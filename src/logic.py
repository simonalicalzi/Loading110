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


# --- INTERFACCIA DI INPUT E OUTPUT ---

if __name__ == "__main__":  # pragma: no cover
    print("\n" + "=" * 40)
    print("   BENVENUTA IN LOADING 110! 🎓")
    print("=" * 40)

    miei_esami = []

    try:
        CFU_TOTALI_CORSO = int(input("Inserisci i CFU totali del corso (es. 180): "))
        OBIETTIVO_LAUREA = float(input("Qual è il tuo obiettivo di voto? (es. 110): "))
    except ValueError:
        print("⚠️ Errore: Inserisci solo numeri. Uso valori standard (180, 110).")
        CFU_TOTALI_CORSO = 180
        OBIETTIVO_LAUREA = 110.0

    print("\n--- Inserimento Esami (scrivi 'stop' per terminare) ---")

    while True:
        nome_input = input("\nNome esame: ")
        if nome_input.lower() == "stop":
            break

        try:
            v_voto = int(input(f"Voto per {nome_input}: "))
            v_cfu = int(input(f"CFU per {nome_input}: "))
            lode_prompt = input("Ha la lode? (s/n): ").lower()

            ha_lode = lode_prompt == "s"

            miei_esami.append(
                Esame(nome=nome_input, voto=v_voto, cfu=v_cfu, lode=ha_lode)
            )

        except ValueError:
            print("⚠️ Dati non validi per questo esame. Riprova.")

    if miei_esami:
        res_media_a = media_aritmetica(miei_esami)
        res_media_p = calcola_media_ponderata(miei_esami)
        res_proiezione = proiezione_voto_laurea(res_media_p)
        res_progresso = analisi_avanzamento(miei_esami, CFU_TOTALI_CORSO)
        res_media_req = stima_media_necessaria(
            miei_esami, CFU_TOTALI_CORSO, OBIETTIVO_LAUREA
        )
        n_lodi = sum(1 for e in miei_esami if e.lode)

        print("\n" + "=" * 40)
        print("      --- LOADING 110 STATUS ---")
        print("=" * 40)

        print(f"📊 Medie: Aritmetica: {res_media_a:.2f} | Ponderata: {res_media_p:.2f}")
        print("   Le abbiamo calcolate noi, tu pensa a studiare!")

        print("-" * 40)
        print(f"🔮 Leggiamo il futuro: Il tuo voto di partenza è {res_proiezione}/110")

        print("-" * 40)
        print(f"🎖️ Operazione Lode: Hai collezionato {n_lodi} lode/i.")
        print(f"   Peso totale bonus: +{n_lodi * 0.5} punti sulla base laurea.")

        print("-" * 40)
        print(f"📉 {OBIETTIVO_LAUREA}, l'obiettivo di tutti:")
        print(f"   Devi mantenere una media di {res_media_req}")
        print(f"   nei restanti {res_progresso['cfu_mancanti']} CFU.")

        print("-" * 40)
        print(
            f"✅ Avanzamento: {res_progresso['percentuale_completamento']}% del percorso fatto."
        )
        print("=" * 40 + "\n")
    else:
        print("\nNessun dato inserito. Arrivederci!")
