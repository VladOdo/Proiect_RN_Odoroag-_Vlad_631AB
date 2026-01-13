# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** [Odoroaga Vlad-Ionut]  
**Link Repository GitHub**
**Data:** [Data]  
---

## Scopul Etapei 4

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Trebuie să livrați un SCHELET COMPLET și FUNCȚIONAL al întregului Sistem cu Inteligență Artificială (SIA). In acest stadiu modelul RN este doar definit și compilat (fără antrenare serioasă).**

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **CE TREBUIE SĂ FUNCȚIONEZE:**
- Toate modulele pornesc fără erori
- Pipeline-ul complet rulează end-to-end (de la date → până la output UI)
- Modelul RN este definit și compilat (arhitectura există)
- Web Service/UI primește input și returnează output

 **CE NU E NECESAR ÎN ETAPA 4:**
- Model RN antrenat cu performanță bună
- Hiperparametri optimizați
- Acuratețe mare pe test set
- Web Service/UI cu funcționalități avansate

**Scopul anti-plagiat:** Nu puteți copia un notebook + model pre-antrenat de pe internet, pentru că modelul vostru este NEANTRENAT în această etapă. Demonstrați că înțelegeți arhitectura și că ați construit sistemul de la zero.

---

##  Livrabile Obligatorii

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software 
|---------------------------------------------------------------------------------|----------------------------------------------------------|---------------------------------|
|                           **Nevoie reală concretă**                              |           **Cum o rezolvă SIA-ul vostru**                | **Modul software responsabil** |
|----------------------------------------------------------------------------------|----------------------------------------------------------|--------------------------------|
| Monitorizarea flotei: Operatorii nu au o vizibilitate clară asupra "sănătății"   | Dashboard grafic în timp real care afișează              |        Web Service / UI        |
| bateriei corelată cu efortul mecanic al motoarelor                               | tensiunea vs. efortul pe joncțiuni (joint_states)        |                                |
|----------------------------------------------------------------------------------|----------------------------------------------------------|--------------------------------|
| Managementul autonomiei: Roboții din flotă rămân fără baterie în mijlocul        | Predicție continuă a SoC (State of Charge) și RUL        |       Neural Network           |
| sarcinilor critice, blocând fluxul logistic                                      | (Remaining Useful Life) folosind date istorice de consum |      Module (CNN-LSTM)         |
|----------------------------------------------------------------------------------|----------------------------------------------------------|--------------------------------|
| Prevenirea descărcării critice: Robotul se oprește                               | Monitorizare predictivă și emitere alertă vizuală/log    |        Decision/Alert          |
| brusc în misiune din cauza scăderii tensiunii sub limită                         | când SoC prezis scade sub 20% (Warning)                  |     Module (Warning System)    |
|----------------------------------------------------------------------------------|----------------------------------------------------------|--------------------------------|

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

**Regula generală:** Din totalul de **N observații finale** în `data/processed/`, **minimum 40%** trebuie să fie **contribuția voastră originală**.

#### Cum se calculează 40%:

**Exemplu 1 - Dataset DOAR public în Etapa 3:**
```
Etapa 3: Ați folosit 10,000 samples dintr-o sursa externa (ex: Kaggle)
Etapa 4: Trebuie să generați/achiziționați date astfel încât:
  
Opțiune A: Adăugați 6,666 samples noi → Total 16,666 (6,666/16,666 = 40%)
Opțiune B: Păstrați 6,000 publice + 4,000 generate → Total 10,000 (4,000/10,000 = 40%)
```

**Exemplu 2 - Dataset parțial original în Etapa 3:**
```
Etapa 3: Ați avut deja 3,000 samples generate + 7,000 publice = 10,000 total
Etapa 4: 3,000 samples existente numără ca "originale"
        Dacă 3,000/10,000 = 30% < 40% → trebuie să generați încă ~1,700 samples
        pentru a ajunge la 4,700/10,000 = 47% > 40% ✓
```

**Exemplu 3 - Dataset complet original:**
```
Etapa 3-4: Generați toate datele (simulare, senzori proprii, etichetare manuală - varianta recomandata)
           → 100% original ✓ (depășește cu mult 40% - FOARTE BINE!)
```

#### Tipuri de contribuții acceptate (exemple din inginerie):

Alegeți UNA sau MAI MULTE dintre variantele de mai jos și **demonstrați clar în repository**:

| **Tip contribuție** | **Exemple concrete din inginerie** | **Dovada minimă cerută** |
|---------------------|-------------------------------------|--------------------------|
| **Date generate prin simulare fizică** | • Traiectorii robot în Gazebo<br>• Vibrații motor cu zgomot aleator calibrat<br>• Consumuri energetice proces industrial simulat | Cod Python/LabVIEW funcțional + grafice comparative (simulat vs real din literatură) + justificare parametri |
| **Date achiziționate cu senzori proprii** | • 500-2000 măsurători accelerometru pe motor<br>• 100-1000 imagini capturate cu cameră montată pe robot<br>• 200-1000 semnale GPS/IMU de pe platformă mobilă<br>• Temperaturi/presiuni procesate din Arduino/ESP32 | Foto setup experimental + CSV-uri produse + descriere protocol achiziție (frecvență, durata, condiții) |
| **Etichetare/adnotare manuală** | • Etichetat manual 1000+ imagini defecte sudură<br>• Anotat 500+ secvențe video cu comportamente robot<br>• Clasificat manual 2000+ semnale vibrații (normal/anomalie)<br>• Marcat manual 1500+ puncte de interes în planuri tehnice | Fișier Excel/JSON cu labels + capturi ecran tool etichetare + log timestamp-uri lucru |
| **Date sintetice prin metode avansate** | • Simulări FEM/CFD pentru date dinamice proces | Cod implementare metodă + exemple before/after + justificare hiperparametri + validare pe subset real |

#### Declarație obligatorie în README:

Scrieți clar în acest README (Secțiunea 2):

```markdown
### Contribuția originală la setul de date:

**Total observații finale:** [10000] (după Etapa 3 + Etapa 4)
**Observații originale:** [40000] ([40]%)

**Tipul contribuției:**
[ ] Date generate prin simulare fizică  
[X] Date achiziționate cu senzori proprii  
[ ] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
Am creat un pipeline complet de procesare a datelor brute din ROS2. Deoarece datele provin din surse asincrone (/front_battery_state, /rear_battery_state, /joint_states), am dezvoltat scripturi personalizate în Python:
-mcap_to_csv.py: Extrage datele brute din formatul .mcap (ROS2 Bag) în fișiere CSV separate per topic.
-01_unify_and_average.py: Combină cele două baterii (față/spate) într-o singură metrică unificată și aplică o medie mobilă pentru reducerea zgomotului.
-02_sync_joint_states.py: Sincronizează temporal efortul mecanic de pe motoare cu starea bateriei folosind interpolare (pandas.merge_asof), rezultând fișierul final full_dataset_synchronized.csv gata de antrenare.

**Locația codului:** 'src/data_acquisition/mcap_to_csv.py', 'src/preprocessing/01_unify_and_average.py' si 'src/preprocessing/02_sync_joint_states.py'
**Locația datelor:** 'data/processed/full_dataset_synchronized.csv'

**Dovezi:**
-Structura folderului data/raw vs data/processed (vizibilă în repo).
-Fișierul rosbag2_2025_11_27... care demonstrează achiziția reală.
```

---

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

**Cerințe:**
- **Minimum 4-6 stări clare** cu tranziții între ele
- **Formate acceptate:** PNG/SVG, pptx, draw.io 
- **Locație:** `docs/state_machine.*` (orice extensie)
- **Legendă obligatorie:** 1-2 paragrafe în acest README: "De ce ați ales acest State Machine pentru nevoia voastră?"

**Stări tipice pentru un SIA:**
Locație diagramă: docs/state_machine.png
```
IDLE → INITIALIZING (Load Model & Params) → WAIT_FOR_DATA → 
BUFFERING (Accumulate 30s Window) → PREPROCESS (Normalize features) → 
INFERENCE (CNN-LSTM Forward Pass) → CHECK_THRESHOLD (User Input) →
  ├─ [Pred > Prag] → STATUS_OK (Green UI) → LOG_DATA → BUFFERING (Loop)
  └─ [Pred < Prag] → TRIGGER_WARNING (Red Alert UI) → LOG_WARNING → BUFFERING (Loop)
       ↓ [Eroare senzor]
     FAILSAFE (Stop Inference) → DISPLAY_ERROR
```

**Legendă obligatorie (scrieți în README):**
```markdown
### Justificarea State Machine-ului ales:

Am ales o arhitectură de tip Monitorizare Pasivă cu Alertare, nu una de control activ.

Stările principale:

BUFFERING: Stare critică pentru modelul CNN-LSTM. Rețeaua are nevoie de o secvență temporală (istoric), nu doar de o valoare instantanee. Sistemul acumulează datele procesate până se umple fereastra de timp.

CHECK_THRESHOLD (Input Utilizator): Sistemul citește în timp real pragul definit de utilizator în interfață (ex: "Alertează-mă la 20%"). Aceasta îndeplinește cerința de a avea input de la user.

TRIGGER_WARNING: Sistemul doar emite un avertisment vizual puternic (schimbare culoare interfață + log), lăsând decizia finală operatorului uman.

Starea ERROR este esențială pentru că bateria de la robot se poate deconecta sau driverele nu mai trimit date corect.
```
---

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

Toate cele 3 module trebuie să **pornească și să ruleze fără erori** la predare. Nu trebuie să fie perfecte, dar trebuie să demonstreze că înțelegeți arhitectura.

|             **Modul**             |          **Python**                     |                                ** Cerință minimă funcțională (la predare)**                                       |
|-----------------------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **1. Data Logging / Acquisition** |     rosbags, pandas                     |        **MUST:** Funcțional. Scripturile din src/preprocessing generează full_dataset_synchronized.csv.           |
| **2. Neural Network Module**      |    tensorflow/keras                     |                  **MUST:** Arhitectura CNN-LTSM definita si compilata                                             |
| **3. Web Service / UI**           | Streamlit, Gradio, FastAPI, Flask, Dash | **MUST:** Primește input de la user și afișează un output. **NOT required:** UI frumos, funcționalități avansate. |

#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition**

**Funcționalități obligatorii:**
- [ ] Cod rulează fără erori: `python src/data_acquisition/generate.py` sau echivalent LabVIEW
- [ ] Generează CSV în format compatibil cu preprocesarea din Etapa 3
- [ ] Include minimum 40% date originale în dataset-ul final
- [ ] Documentație în cod: ce date generează, cu ce parametri

#### **Modul 2: Neural Network Module**

**Funcționalități obligatorii:**
- [ ] Arhitectură RN definită și compilată fără erori
- [ ] Model poate fi salvat și reîncărcat
- [ ] Include justificare pentru arhitectura aleasă (în docstring sau README)
- [ ] **NU trebuie antrenat** cu performanță bună (weights pot fi random)


#### **Modul 3: Web Service / UI**

**Funcționalități MINIME obligatorii:**
- [X] Propunere Interfață ce primește input de la user (formular, file upload, sau API endpoint)
- [ ] Includeți un screenshot demonstrativ în `docs/screenshots/`

**Ce NU e necesar în Etapa 4:**
- UI frumos/profesionist cu grafică avansată
- Funcționalități multiple (istorice, comparații, statistici)
- Predicții corecte (modelul e neantrenat, e normal să fie incorect)
- Deployment în cloud sau server de producție

**Scop:** Prima demonstrație că pipeline-ul end-to-end funcționează: input user → preprocess → model → output.


## Structura Repository-ului la Finalul Etapei 4 (OBLIGATORIE)

**Verificare consistență cu Etapa 3:**

```
PROIECT_RN/
├──.venv/
├── config/
├── data/
│   ├── processed/
│   │   ├── full_dataset_synchronized.csv  # DATASET FINAL (Contribuție 100%)
│   │   └── unified_telemetry.csv
│   └── raw/
│       ├── rosbag2_2025_11_27.../         # Date brute de pe robot
│       │   ├── metadata.yaml
│       │   └── rosbag2_....mcap
│       ├── front_battery_state.csv
│       ├── joint_states.csv
│       └── rear_battery_state.csv
├── docs/
│   ├── state_machine.png                  # Diagrama obligatorie
│   └── datasets/
├── src/
│   ├── app/                               # Modul 3: UI/Dashboard
│   │   └── dashboard.py
│   ├── data_acquisition/                  # Modul 1 (Parte A): Extractie
│   │   └── mcap_to_csv.py
│   ├── neural_network/                    # Modul 2: Model RN
│   │   ├── __init__.py
│   │   └── model.py
│   └── preprocessing/                     # Modul 1 (Parte B): Procesare
│       ├── 01_unify_and_average.py
│       └── 02_sync_joint_states.py
├── dockerfile
├── link-github.txt
├── requirements.txt
└── README.md
```

**Diferențe față de Etapa 3:**
- Adăugat `data/generated/` pentru contribuția dvs originală
- Adăugat `src/data_acquisition/` - MODUL 1
- Adăugat `src/neural_network/` - MODUL 2
- Adăugat `src/app/` - MODUL 3
- Adăugat `models/` pentru model neantrenat
- Adăugat `docs/state_machine.png` - OBLIGATORIU

---

## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [ ] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [ ] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [ ] Cod generare/achiziție date funcțional și documentat
- [ ] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [ ] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [ ] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [ ] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [ ] Cod rulează fără erori (`python src/data_acquisition/...` sau echivalent LabVIEW)
- [ ] Produce minimum 40% date originale din dataset-ul final
- [ ] CSV generat în format compatibil cu preprocesarea din Etapa 3
- [ ] Documentație în `src/data_acquisition/README.md` cu:
  - [ ] Metodă de generare/achiziție explicată
  - [ ] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [ ] Justificare relevanță date pentru problema voastră
- [ ] Fișiere în `data/generated/` conform structurii

### Modul 2: Neural Network
- [ ] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [ ] README în `src/neural_network/` cu detalii arhitectură curentă

### Modul 3: Web Service / UI
- [ ] Propunere Interfață ce pornește fără erori (comanda de lansare testată)
- [ ] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [ ] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)

---

**Predarea se face prin commit pe GitHub cu mesajul:**  
`"Etapa 4 completă - Arhitectură SIA funcțională"`

**Tag obligatoriu:**  
`git tag -a v0.4-architecture -m "Etapa 4 - Skeleton complet SIA"`


