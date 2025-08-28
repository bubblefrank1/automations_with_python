import requests
import pandas as pd
import time

def geocode_address(address, api_key, retry=False):
    """
    Funzione per ottenere le coordinate di un indirizzo.
    Se il primo tentativo fallisce, può essere ritentata una seconda volta.
    """
    url = f"https://geocode.maps.co/search?q={address}&api_key={api_key}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                lat = data[0].get("lat")
                lon = data[0].get("lon")
                return lat, lon
        else:
            print(f"Errore HTTP per l'indirizzo '{address}': {response.status_code}")
    except Exception as e:
        print(f"Eccezione per l'indirizzo '{address}': {e}")

    if not retry:
        print(f"🔁 Ritento per '{address}'...")
        time.sleep(2)
        return geocode_address(address, api_key, retry=True)

    return None, None

# Percorso del file .txt
file_input = '/Users/paolo/Desktop/WhatsApp Addresses.txt'
addresses = []

# Legge gli indirizzi dal file
with open(file_input, "r", encoding="latin-1") as file:
    for line in file:
        addr = line.strip()
        if addr:
            addresses.append(addr)

# Chiave API
api_key = "67f7de3bf337f600450800mdhb4bb8b"

# Lista risultati
results = []

# Geocodifica ogni indirizzo
for i, addr in enumerate(addresses):
    print(f"\n📍 Geocodifica {i+1}/{len(addresses)}: {addr}")
    lat, lon = geocode_address(addr, api_key)
    results.append({
        "Indirizzo": addr,
        "Latitudine": lat,
        "Longitudine": lon
    })
    time.sleep(3)  # attesa tra una richiesta e l'altra

# Crea DataFrame e salva in CSV
df_results = pd.DataFrame(results)
output_file = "/Users/paolo/Desktop/addresses_geocodificato.csv"
df_results.to_csv(output_file, index=False, encoding="latin-1")

print(f"\n✅ File salvato: {output_file}")
