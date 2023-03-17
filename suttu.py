# Esimerkkejä päivämäärien, tiedostojen ja JSON-tietojen käytöstä

import datetime  # Sisäänrakennettu kirjasto aikamääreille
import json  # Sisäänrakennettu kirjasto JSON-objektien käsittelyä varten

'''
# Päiväyksen muodostaminen
year = 2023
month = 3
day = 17
date = datetime.datetime(year, month, day)
print(date)

# Päivämäärän ja kellonajan selvittäminen
just_now = datetime.datetime.now()
print(just_now)

# Funktio joka laskee päivämäärien eron päivinä


def datediff(d1, d2):
    """Calculates the difference between two dates in days 

    Args:
        d1 (str): A date in ISO format YYYY-MM-DD
        d2 (str): A date in ISO format YYYY-MM-DD

    Returns:
        int: absolute diccerence in days
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days)
    return difference


ero = datediff("2023-03-17", "2023-01-20")
print(ero)

# Funktio, joka laskee kahden kellonajan välisen eron tunteina


def timediff(t1, t2):
    """Calculates the difference between two time values

    Args:
        t1 (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss

    Returns:
        float: time difference in hours
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")

    # Vain sekunnit ja mikrosekunnit on tuettu
    seconds = abs((t2 - t1).seconds)
    hours = seconds / 3600
    return hours


kesto = timediff("10:00:00", "14:30:00")
print(kesto)
'''

# Luodaan tyhjä lista pinon perustaksi
jumppari_lista = []

# Määritellään Python sanakirja
jumppari = {'nimi': 'Erkki', 'Pituus': 171, 'Paino': 75.5}
jumppari2 = {'nimi': 'Essi', 'Pituus': 165, 'Paino': 61.2}

# Lisätään jumpparit listaan
jumppari_lista.append(jumppari)
jumppari_lista.append(jumppari2)

print(jumppari_lista)

'''
# Luodaan JSON-merkkijono (objekti)
json_jumppari = json.dumps(jumppari)
print(json_jumppari)


# Luodaan tiedosto
file_to_use = open('kuntoilijat.json', 'x')
file_to_use.close()  # Suljetaan tiedosto operaation jälkeen.


# Kirjoitetaan tiedostoon JSON-objekti
file_to_use = open('kuntoilijat.json', 'w')

# Muutetaan sanakirja JSON-muotoon ja tallennetaan
json.dump(jumppari, file_to_use)
file_to_use.close() # Suljetaan AINA tiedosto


# Luetaan JSON-objekti tiedostosta
file_to_use = open('kuntoilijat.json', 'r')
data = json.load(file_to_use)
file_to_use.close()
print(data)


# Lisätään toinen JSON-objekti tiedoston loppuun
with open('kuntoilijat.json', 'a') as file_to_use:
    json.dump(jumppari2, file_to_use)
'''    

with open('kuntoilijat.json', 'w') as file_to_use:
    json.dump(jumppari_lista, file_to_use, indent=4)

with open('kuntoilijat.json', 'r') as file_to_use:
    read_data = json.load(file_to_use)
    last_data = read_data.pop()
    print(last_data)
