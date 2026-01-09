# CryptoTracker

## Beskrivning
Ett Python-verktyg för att hämta realtidsdata för de 7 högsta kryptovalutorna genom att hämta från CoinGecko API

## Installation
1. Klona repot: `git clone https://github.com/Toldelol/CryptoTracker.git`
2. Navigera till mappen: `cd CryptoTracker`
3. Skapa venv: `python -m venv .venv`
4. Aktivera venv: `source .venv/bin/activate` (Linux/Mac) eller `.venv\Scripts\activate` (Windows)
5. Installera beroenden: `pip install -r requirements.txt`

## Körning
Kör huvudskriptet: `python src/main.py`

Data hämtas för att sedan processa den och skriva ut en sammanfattning (inklusive tabell om pandas är installerat). Loggar sparas i `logs/crypto_tracker.log`.

## Beroenden
Se `requirements.txt` för full lista. Kräver internetåtkomst för API-anrop.

## Noteringar
- Ingen user input, allt körs automatisk.
- För testning: Aktivera venv och kör skriptet.