import os
import json
import re
import mimetypes
import chardet

# =============================
# 📂 CONFIGURAZIONE PERCORSI
# =============================
PERCORSO_INPUT = os.getenv('CHATGPT_INPUT_PATH', './conversations.json')
PERCORSO_OUTPUT = os.getenv('CHATGPT_OUTPUT_PATH', './Archivio_Chat')

# Crea cartella di output se non esiste
os.makedirs(PERCORSO_OUTPUT, exist_ok=True)


# =============================
# 🛡️ UTILITÀ
# =============================
def sanitizza_titolo(titolo):
    """Rimuove caratteri non validi dai nomi dei file."""
    return re.sub(r'[\\/*?:"<>|]', '_', titolo)


def salva_file(titolo, contenuto, formato='txt'):
    """Salva il contenuto in formato specificato (txt o json)."""
    titolo_sanitizzato = sanitizza_titolo(titolo)
    percorso_file = os.path.join(PERCORSO_OUTPUT, f"{titolo_sanitizzato}.{formato}")
    os.makedirs(os.path.dirname(percorso_file), exist_ok=True)

    with open(percorso_file, 'w', encoding='utf-8') as file:
        if formato == 'json':
            json.dump(contenuto, file, ensure_ascii=False, indent=4)
        else:
            for messaggio in contenuto:
                file.write(f"{messaggio.get('role', 'unknown').upper()}: {messaggio.get('content', '')}\n\n")
    print(f"[✅] Salvato {formato.upper()}: {percorso_file}")


# =============================
# 💬 ELABORAZIONE CHAT
# =============================
def elabora_dati_chat(contenuto_json):
    """Elabora i dati JSON delle conversazioni."""
    if not isinstance(contenuto_json, list):
        print("[❌] Formato JSON non supportato. Atteso: lista di conversazioni.")
        return

    for indice, conversazione in enumerate(contenuto_json):
        titolo = conversazione.get('title', f"conversazione_{indice+1}").replace(' ', '_')
        messaggi = []

        for key, value in conversazione.get('mapping', {}).items():
            if 'message' in value and value['message'] is not None:
                messaggio = value['message']
                contenuto = messaggio.get('content', {}).get('parts', [messaggio.get('content', '')])[0]
                messaggi.append({
                    'role': messaggio['author']['role'],
                    'content': contenuto
                })

        salva_file(titolo, messaggi, formato='json')
        salva_file(titolo, messaggi, formato='txt')


# =============================
# 📝 ANALISI FILE
# =============================
def analizza_file(percorso_file):
    """Analizza il file e gestisce la codifica e il parsing JSON."""
    if not os.path.isfile(percorso_file):
        print(f"[❌] Il file '{percorso_file}' non esiste.")
        return

    tipo_mime, _ = mimetypes.guess_type(percorso_file)
    tipo_mime = tipo_mime or "Tipo MIME sconosciuto"
    dimensione_file = os.path.getsize(percorso_file)

    with open(percorso_file, 'rb') as file:
        raw_data = file.read(10000)
        codifica = chardet.detect(raw_data)['encoding']

    try:
        with open(percorso_file, 'r', encoding=codifica) as file:
            contenuto = file.read()
    except Exception as e:
        print(f"[❌] Errore durante la lettura del file: {e}")
        return

    print(f"[ℹ️] Resoconto del file '{percorso_file}':")
    print(f" - Tipo MIME: {tipo_mime}")
    print(f" - Dimensione: {dimensione_file / (1024 * 1024):.2f} MB")
    print(f" - Codifica: {codifica}")
    print(f" - Contenuto (primi 500 caratteri):\n{contenuto[:500]}")

    if tipo_mime == 'application/json':
        try:
            print("[DEBUG] Tentativo di deserializzazione del contenuto JSON...")
            contenuto_json = json.loads(contenuto)
            elabora_dati_chat(contenuto_json)
        except json.JSONDecodeError as e:
            print(f"[❌] Errore durante la deserializzazione del JSON: {e}")
            print("[DEBUG] Contenuto JSON non valido:\n", contenuto[:1000])


# =============================
# 🚀 ESECUZIONE PRINCIPALE
# =============================
if __name__ == '__main__':
    print("⚙️ Avvio analisi del file...")
    analizza_file(PERCORSO_INPUT)
    print("✅ Analisi completata!")
