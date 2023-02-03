# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat


# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        float: painoindeksi desimaalin tarkkuudella
    """
    pituus = pituus / 100  # Muutetaan pituuks metreiksi
    bmi = paino / pituus**2
    bmi = round(bmi, 1)
    return bmi


# Määritellään funktio aikuisen rasvaprosentin laskentaan
def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee aikuisen rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: kehon rasvaprosentti (aikuinen)
    """
    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti


# Määritellään funktio lapsen rasvaprosentin laskentaan
def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee lapsen rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> poika, 0 -> tyttö

    Returns:
        float: kehon rasvaprosentti (lapsi)
    """
    rasvaprosentti = 1.51 * bmi - 0.7 * ika - 3.6 * sukupuoli + 1.4
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti

# Suoritetaan seuraavat rivit vain, jos tämä tiedosto on pääohjelma
# Mahdollistaa funktioiden lataamisen toisiin ohjelmiin
# Kun koodi ladataan toiseen tiedostoon,
# ei __name__=="__main__":n alapuolella olevaa koodia ei suoriteta.
if __name__ == "__main__":
    
    # Kysytään käyttäjältä tiedot
    pituus_teksti = input("Kuinka pitkä olet? (cm): ")
    paino_teksti = input("Kuinka paljon painat? (kg): ")
    ika_teksti = input("Kuinka vanha olet?: ")
    sukupuoli_teksti = input(
    "Mikä on sukupuolesi? mies vastaa 1, nainen vastaa 0: ")

    # Muutetaan vastaukset liukuluvuiksi
    pituus = float(pituus_teksti)
    paino = float(paino_teksti)
    ika = float(ika_teksti)
    sukupuoli = float(sukupuoli_teksti)
    
    # Lasketaan painoindeksi funktiolla laske_bmi
    oma_bmi = laske_bmi(paino, pituus)

    # Yli 18 vuotiailla käytetään aikuisen kaavaa
    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    # Muussa tapauksessa käytetään lapsen kaavaa
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)


    print("Painoindeksisi on", oma_bmi, "ja rasvaprosenttisi on", oma_rasvaprosentti)
