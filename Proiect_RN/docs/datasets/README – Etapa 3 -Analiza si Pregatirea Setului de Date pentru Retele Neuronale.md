# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** [Odoroaga Vlad]  
**Data:** [25 nov. 2025]  

---

## Introducere

Acest document descrie activitățile realizate în **Etapa 3**, în care se analizează și se preprocesează setul de date necesar proiectului „Rețele Neuronale". Scopul etapei este pregătirea corectă a datelor pentru instruirea modelului RN, respectând bunele practici privind calitatea, consistența și reproductibilitatea datelor.

---

##  1. Structura Repository-ului Github (versiunea Etapei 3)

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

---

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Platforma robotică mobilă autonomă **EduBot Xplorer
* **Modul de achiziție:** ☐ Senzori reali
* **Perioada / condițiile colectării:** [Ex: Noiembrie 2024 - Ianuarie 2025, condiții experimentale specifice]

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** [Se va completa după conversia din ROS bag, estimare: **~10,000 – 15,000** mostre/ciclu complet]
* **Număr de caracteristici (features):** **6** (brute) – se vor extinde prin *feature engineering* (lag/timp).
* **Tipuri de date:** ☐ Numerice / ☐ Temporale
* **Format fișiere:** ☐ CSV

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Sursă** |
|-------------------|---------|-------------|---------------|--------------------|
| **timestamp** | temporal | secunde | Momentul colectării datelor. | ROS Header |
| **voltage\_v** | numeric | V | Tensiunea de intrare a bateriei (3S LiPo). | [cite_start]RoboClaw (via Driver) [cite: 144] |
| **current\_a** | numeric | A | Curentul total consumat de motoarele de bază. | [cite_start]RoboClaw (via Driver) [cite: 159, 166] |
| **speed\_linear\_mps** | numeric | m/s | Viteza liniară a robotului (pe axa x). | [cite_start]Odometry (Topic `/odom`) [cite: 169] |
| **speed\_angular\_rads** | numeric | rad/s | Viteza unghiulară a robotului (pe axa z). | [cite_start]Odometry (Topic `/odom`) [cite: 169] |
| **temperature\_c** | numeric | °C | [cite_start]Temperatura bateriei sau a controlerelor (dacă este disponibilă)[cite: 134, 156]. | BMS/RoboClaw (Dacă e citit) |
| **target\_RUL\_min** | numeric | min | **Eticheta (Label)**: Timpul real rămas de funcționare până la pragul critic de decuplare. | Calculat post-procesare (Total Time - Current Time) |

**Fișier recomandat:**  `data/README.md`

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

* **Tensiunea (voltage\_v):** Se așteaptă o distribuție grupată în jurul valorii nominale (11.1V), cu o coadă către valoarea minimă de descărcare (de ex., 9.9V).
* **Curentul (current\_a):** Se așteaptă o deviație standard mare, reflectând natura dinamică a consumului (curent mare în accelerație/viraje, mic în staționare).
* **target\_RUL\_min:** Distribuția va fi uniformă (de la max la 0) pe măsură ce timpul de funcționare crește.

### 3.2 Analiza calității datelor

* **Detectarea valorilor lipsă:** Se va verifica dacă există *timestamps* lipsă sau goluri în datele de curent și viteză, cauzate de eventuale erori de sincronizare între topic-urile ROS.
* **Detectarea valorilor inconsistente:** Se vor identifica valorile de curent negative în timpul descărcării și valorile de tensiune peste maximul bateriei LiPo.
* **Identificarea corelației:** Se așteaptă o corelație puternică între `current_a` și `speed_linear_mps`.

### 3.3 Probleme identificate

* **Valori Lipsă (Interpolare):** Înregistrări ocazionale pierdute din fluxul de date `RoboClaw`. Acestea vor trebui interpolate sau tratate ca *NaN*.
* **Nivel de zgomot ridicat:** Datele de curent și viteză vor avea variații rapide (zgomot) care necesită o *smoothing* preliminar (ex: media mobilă) înainte de a fi introduse în LSTM.
* **Dezechilibru de clasă (implicat):** Deși este o problemă de regresie, modelul va avea mai puține date în scenariul critic (ultimele 5 minute de autonomie).

---

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

* **Tratarea sincronizării:** Alinierea *timestamps*-urilor topic-urilor de intrare (`/odom`, `/roboclaw/voltage`) folosind o tehnică de *interpolation* sau *nearest neighbor* (în funcție de rata de eșantionare).
* **Tratarea outlierilor:** Aplicarea unei filtre (ex: Z-score) pe coloana `current_a` pentru a limita vârfurile excesive de curent care nu sunt relevante pentru comportamentul general al bateriei.

### 4.2 Transformarea caracteristicilor

* **Generarea etichetei (Label Engineering):** Calcularea coloanei **`target_RUL_min`** (Timpul Rămas Utile) ca diferență între timpul total de rulare și timpul curent.
* **Crearea Caracteristicilor Secvențiale (Sequence Engineering):** Setul de date va fi transformat în secvențe temporale (ex: ferestre de 20-50 de pași de timp) pentru a alimenta modelul LSTM. Aceasta implică utilizarea funcțiilor de *lag* pe coloanele de intrare (`voltage_v`, `current_a`, etc.).
* **Normalizare:** Aplicarea **Min–Max Scaling** pe toate caracteristicile numerice de intrare (inclusiv pe secvențele generate) pentru a aduce valorile între 0 și 1, optimizând performanța rețelei neuronale.

### 4.3 Structurarea seturilor de date

**Împărțire recomandată:**
* 70 – train
* 15% – validation
* 15% – test

* **Principii respectate:** Se va aplica **diviziunea temporală** (time-based split), asigurând că datele de test sunt întotdeauna **ulterioare** celor de antrenament, pentru a simula un scenariu real de predicție. Statisticiile de normalizare vor fi calculate **DOAR** pe setul de antrenament și aplicate seturilor de validare și test (pentru a evita *data leakage*).

### 4.4 Salvarea rezultatelor preprocesării

* Date preprocesate în `data/processed/`
* Seturi train/val/test în foldere dedicate
* Parametrii de preprocesare în `config/preprocessing_config.*` (opțional)

---

##  5. Fișiere Generate în Această Etapă

* `data/raw/` – Fișiere `.csv` convertite din `rosbag`
* `data/processed/` – Setul de date curățat, normalizat și transformat în secvențe temporale (numpy arrays sau fișiere CSV structurate)
* `data/train/`, `data/validation/`, `data/test/` – Seturile finale de secvențe (Input X) și etichete (Output Y)
* `src/preprocessing/` – Scriptul Python **`preprocess_data.py`** care implementează pașii 4.1-4.3
* `data/README.md` – Descrierea detaliată a datelor (similar secțiunii 2 din acest fișier)

---

##  6. Stare Etapă (de completat de student)

- [ ] Structură repository configurată
- [ ] Dataset analizat (EDA realizată)
- [ ] Date preprocesate
- [ ] Seturi train/val/test generate
- [ ] Documentație actualizată în README + `data/README.md`

---
