# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
# -----------------------------------------------------------------

# LIBRARIES AND MODULES

import kuntoilija




# Enter information about an athlete
nimi = input("Nimi: ")

# Use ask_user funktion to get height and convert it into float
answer = ask_user("Pituus (cm): ")

# Read the 1st element of the tuple containing height value
pituus = answer[0]

answer = ask_user("Paino (kg): ")
paino = answer[0]

answer = ask_user("Ikä: ")
ika = answer[0]

answer = ask_user("Sukupuoli, 1 mies, 0 nainen: ")
sukupuoli = answer[0]


'''
# Loop until user gives a correctly formatted value

while True:
    pituus_txt = input("Pituus (cm): ")

# Let's try convert input to numeric
    try:
        pituus = float(pituus_txt)
        break

    # If an error occurs tell the user to check    
    except Exception as e:
        print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)

# Loop until user gives a correctly formatted value
while True:
    paino_txt = input("Paino (kg): ")

# Let's try convert input to numeric
    try:
        paino = float(paino_txt)
        break

    # If an error occurs tell the user to check    
    except Exception as e:
        print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)

# Loop until user gives a correctly formatted value
while True:
    ika_txt = input("Ikä: ")

# Let's try convert input to numeric
    try:
        ika = float(ika_txt)
        break

    # If an error occurs tell the user to check    
    except Exception as e:
        print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)

# Loop until user gives a correctly formatted value
while True:
    sukupuoli_txt = input("Sukupuoli, mies 1, nainen 0: : ")

# Let's try convert input to numeric
    try:
        sukupuoli = float(sukupuoli_txt)
        break

    # If an error occurs tell the user to check    
    except Exception as e:
        print("Virhe syötetyssä arvossa, älä käytä yksiköitä", e)

'''

kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)

print(kuntoilija1.nimi, "painoindeksisi on ", kuntoilija1.bmi)

print("Viimeisen kysymyksen virheilmoitus",
      answer[1], "koodi", answer[2], "engl. ilmoitus", answer[3])
