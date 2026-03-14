## 🎓 Loading110

Benvenuti in Loading110, lo strumento definitivo creato per gli studenti che vogliono smettere di fissare il libretto online con ansia e iniziare a pianificare la propria scalata verso la corona d'alloro. 🌿   


## 👥 Il Team 
Siamo due studentesse che hanno deciso di trasformare il calcolo della media da "trauma" a "utility":

Rosalia Maria Lombardo (@lialombardo)  

Simona Li Calzi (@simonalicalzi)  


## 🛠️ Cosa fa Loading110? (Spoiler: ti salva la vita)

📊 Medie: Aritmetica o ponderata? Le calcoliamo noi, tu pensa a studiare.

🔮 Leggiamo il futuro: Proietta il tuo voto di partenza alla laurea.

🎖️ Operazione Lode: Calcoliamo quanto pesano quelle sofferte lodi (0.5 punti alla volta!).

📉 110L, l'obiettivo di tutti: Ti diciamo esattamente quale media devi mantenere per raggiungere l'obiettivo dei tuoi sogni.

🛣️ Stato: Quanto manca alla fine? Ti mostriamo la barra di caricamento della tua carriera.

## 📂 Struttura del Progetto

```text
Loading110/
├── 🤖 .github/workflows/
│   └── python-app.yml          # Pipeline CI/CD (Actions)
├── 📦 src/
│   ├── __init__.py
│   └── logic.py                # Core logic del calcolatore
├── 🧪 tests/
│   ├── __init__.py
│   └── test_logic.py           # Test unitari (Pytest)
├── 📄 .gitignore               # File da escludere da Git
├── 📄 README.md                # Documentazione progetto
├── 📄 requirements.txt         # Dipendenze del progetto
└── 📄 setup.py                 # Configurazione installazione
```

## 📝 Unit-Tests

Abbiamo organizzato i test unitari per tutti i metodi utilizzati nell'app all'interno della cartella `tests/`. Per eseguire i test è necessario:

### 1. Installare le dipendenze:
```bash
pip install -r requirements.txt
```

I test possono essere eseguiti tutti insieme o singolarmente:

  Tutti insieme:
  ```bash
  pytest tests/
  pytest --cov=src/
  ```

  Singolarmente:
  ```bash
  pytest tests/test_logic.py
  ```

  ## 🏆 Code Coverage  
Il progetto ha una copertura del codice (code coverage) di 93% ! 

