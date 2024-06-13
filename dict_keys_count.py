import json



def count_keys_in_json(file_path):
    # Leggi il file JSON
    with open(file_path, 'r') as file:
        # Carica il contenuto del file come un array di dizionari
        data = json.load(file)

    # Assicurati che il contenuto sia una lista di dizionari
    if isinstance(data, list):
        # Conta il numero di chiavi in ciascun dizionario
        key_counts = [len(d.keys()) for d in data]
        return key_counts
    else:
        raise ValueError("Il file JSON deve contenere un array di dizionari")

# Specifica il percorso del file JSON
file_path = "prova.json"

# Chiama la funzione e stampa i risultati
try:
    key_counts = count_keys_in_json(file_path)
    for i, count in enumerate(key_counts):
        print(f"Dizionario {i+1} ha {count} chiavi.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")

