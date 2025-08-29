# 🗺️ Address Geocoder Script

Questo script Python permette di **geocodificare indirizzi** (cioè ottenere latitudine e longitudine) a partire da un file di testo contenente una lista di indirizzi.  
I risultati vengono salvati in un file CSV.

## 📦 Requisiti

Assicurati di avere installato i seguenti pacchetti Python:

```bash
pip install requests pandas
```

## ⚙️ Funzionamento

1. Lo script legge un file `.txt` contenente una lista di indirizzi (uno per riga).
2. Per ogni indirizzo effettua una richiesta all’API di [geocode.maps.co](https://geocode.maps.co/).
3. Recupera **latitudine** e **longitudine**.
4. Salva i risultati in un file `.csv`.

## 📂 Struttura

- `coderV3.py` → script principale
- `WhatsApp Addresses.txt` → file di input con gli indirizzi
- `addresses_geocodificato.csv` → file di output con risultati

## 📝 Esempio di input (`WhatsApp Addresses.txt`)

```
Via Roma 1, Milano
Piazza Duomo, Firenze
Corso Vittorio Emanuele II, Torino
```

## 📝 Esempio di output (`addresses_geocodificato.csv`)

| Indirizzo                        | Latitudine  | Longitudine |
|----------------------------------|-------------|-------------|
| Via Roma 1, Milano               | 45.4642     | 9.19        |
| Piazza Duomo, Firenze            | 43.7731     | 11.256      |
| Corso Vittorio Emanuele II, Torino | 45.0703   | 7.6869      |

## 🚀 Utilizzo

Esegui lo script da terminale:

```bash
python coderV3.py
```

Assicurati di modificare nel codice i percorsi dei file:

```python
file_input = "/percorso/del/file/WhatsApp Addresses.txt"
output_file = "/percorso/dove/salvare/addresses_geocodificato.csv"
```

## 🔑 API Key

Lo script utilizza un’API key di [geocode.maps.co](https://geocode.maps.co/).  
Puoi generarne una gratuita sul sito e sostituirla qui:

```python
api_key = "LA_TUA_API_KEY"
```

## ⚠️ Note

- Lo script include un **ritardo di 3 secondi** tra una richiesta e l’altra per evitare limitazioni dell’API.
- Se una richiesta fallisce, viene automaticamente ritentata una seconda volta.
