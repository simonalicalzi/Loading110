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

## 🚀Setup
### 1. Clonare il progetto
Se il PC ha Git installato, apri il terminale e scarica la cartella direttamente da GitHub:

```bash
git clone https://github.com/simonalicalzi/Loading110.git
cd Loading110
```
Se non hai Git, scarica semplicemente il file .zip dal pulsante verde "Code" su GitHub ed estrailo.

### 2. Creare un Ambiente Virtuale 
Windows: 
```bash
python -m venv venv e poi venv\Scripts\activate
```
Mac/Linux:
```bash
python3 -m venv venv e poi source venv/bin/activate
```

### 3. Installare:
```bash
pip install -r requirements.txt
```

### 4. Eseguire il codice
Una volta dentro la cartella, lancia lo script principale:
```bash
python3 logic.py
```

## 📝 Unit-Tests
Abbiamo organizzato i test per tutti i metodi utilizzati all'interno della cartella `tests/`. 

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

