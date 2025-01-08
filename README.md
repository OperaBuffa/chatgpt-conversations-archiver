# 🚀 **ChatGPT Conversations Archiver**

## 📚 **Descrizione**

**ChatGPT Conversations Archiver** è uno strumento Python progettato per analizzare ed esportare le conversazioni di ChatGPT salvate in un file `conversations.json`. Ogni conversazione viene frammentata e archiviata separatamente nei formati **TXT** e **JSON**, facilitando così la lettura, l'analisi e la conservazione.

---

## 🛠️ **Funzionalità Principali**

1. **Esportazione Multi-Formato:**  
   - Ogni conversazione viene salvata in formato **.json** e **.txt**.

2. **Sanitizzazione dei Nomi dei File:**  
   - I titoli delle conversazioni vengono puliti per evitare errori nei nomi dei file.

3. **Configurazione Flessibile:**  
   - I percorsi di input e output possono essere configurati tramite **variabili di ambiente**:  
     - `CHATGPT_INPUT_PATH`  
     - `CHATGPT_OUTPUT_PATH`  

4. **Supporto per Grandi File JSON:**  
   - Gestisce file di grandi dimensioni con parsing ottimizzato.

---

## ⚙️ **Installazione**

### 1. **Clona il Repository**
```bash
git clone https://github.com/tuo-username/chatgpt-conversations-archiver.git
cd chatgpt-conversations-archiver
```

### 2. **Installa le Dipendenze**
Assicurati di avere Python 3 installato. Poi esegui:
```bash
pip install chardet
```

---

## 📂 **Configurazione**

Puoi configurare i percorsi tramite variabili di ambiente o lasciare che lo script utilizzi i percorsi predefiniti.

### **Configurazione con Variabili di Ambiente (Opzionale)**
```bash
export CHATGPT_INPUT_PATH=/percorso/al/tuo/conversations.json
export CHATGPT_OUTPUT_PATH=/percorso/di/output
```

Se non configurati, i percorsi predefiniti saranno:
- **Input:** `./conversations.json`
- **Output:** `./Archivio_Chat`

---

## 🚀 **Utilizzo**

Esegui lo script Python con:
```bash
python3 script.py
```

Lo script eseguirà le seguenti operazioni:
1. Analizzerà il file JSON delle conversazioni.
2. Frammenterà ogni conversazione in file separati `.json` e `.txt`.
3. Salverà i file nella cartella di output configurata.

---

## 📄 **Esempio di Output**

**Formato TXT:**
```txt
USER: Ciao, come stai?
ASSISTANT: Sto bene, grazie! Come posso aiutarti oggi?
```

**Formato JSON:**
```json
[
    {
        "role": "user",
        "content": "Ciao, come stai?"
    },
    {
        "role": "assistant",
        "content": "Sto bene, grazie! Come posso aiutarti oggi?"
    }
]
```

---

## 🐍 **Struttura del Progetto**

```
📦 chatgpt-conversations-archiver
├── script.py          # Codice principale
├── Archivio_Chat/     # Cartella con file TXT e JSON generati
└── README.md          # Questo file
```

---

## 📜 **Licenza**

Distribuito sotto la **MIT License**. Sentiti libero di utilizzare, modificare e condividere questo progetto.

---

## 🤝 **Contributi**

I contributi sono i benvenuti!  
1. Fai un **fork** del progetto.  
2. Crea un nuovo **branch** per la tua modifica.  
3. Invia una **pull request**.  

---
