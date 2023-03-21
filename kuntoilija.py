# KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
# =====================================

# KIRJASTOT JA MODUULIT (LIBRARES AND MODULES)
# --------------------------------------------

import fitness

# LUOKKAMÄÄRITYKSET (CLASS DEFINITIONS)
# -------------------------------------

# Kuntoilija-luokka Yliluokka JunioriKuntoilijalle (super class)

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    # Oliomuodostin eli kontruktori, self -> tuleva olio
    def __init__(self, nimi, pituus, paino, ika, sukupuoli, paiva):

        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)
        self.punnitus_paiva =paiva

    # Metodi rasvaprosentin laskemiseen (yleinen / aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti
    
    # Metodit rasvaprosenttien laskemiseen USA:n armeijan metodeilla
    def usa_rasvaprosentti_mies(self, pituus, vyotaron_ymparys, kaulan_ymparys):
        """Laskee miehen rasvaprosentin USA:n armeijan kaavalla
        Args:
            pituus (float): pituus (cm)
            vyotaron_ymparys (float): vyötärön ympärysmitta (cm)
            kaulan_ymparys (float): kaulan ympärys (cm)
        Returns:
            float: rasvaprosentti
        """
        usa_rasvaprosentti = fitness.usarasvaprosentti_mies(pituus, vyotaron_ymparys,kaulan_ymparys)
        return usa_rasvaprosentti

    def usa_rasvaprosentti_nainen(self, pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys):
        """Laskee kehon rasvaprosentin USA:n armeijan kaavalla
        Args:
            pituus (float): pituus (cm)
            vyotaron_ymparys (float): vyötärön ympärysmitta (cm)
            lantion_ymparys (float): lantion ympärysmitta (cm)
            kaulan_ymparys (float): kaulan ympärysmitta (cm)
        Returns:
            float: rasvaprosentti
        """
        usa_rasvaprosentti = fitness.usarasvaprosentti_nainen(
            pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys)
        return usa_rasvaprosentti
    
# JunioriKuntoilija-luokka Kuntoilija-luokan aliluokka (sub class) 
 
class JunioriKuntoilija(Kuntoilija):
    """Luokka nuoren kuntoilijan tiedoille."""
    
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään periytyminen, mitä ominaisuuksia perii
        super().__init__(nimi, pituus, paino, ika, sukupuoli)

    # Metodi rasvaprosentin laskemiseen (ylikirjoitettu lapsen metodilla)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti
    


if __name__ == "__main__":

    # Luodaan olio luokasta Kuntoilija
    kuntoilija = Kuntoilija("Kalle Kuntoilija", 171, 65, 40, 1)
    print(kuntoilija.nimi, "painaa", kuntoilija.paino, "kg")
   #print("Painoindeksi on ", .painoindeksi())
    print("Rasvaprosentti on", kuntoilija.rasvaprosentti())

    # Toinen olio luokasta Kuntoilija 
    kuntoilija1 = Kuntoilija("Jutta Jumppaaja", 156, 60, 33, 0)
    print(kuntoilija1.nimi, "painaa", kuntoilija1.paino, "kg")
    #print("Painoindeksi on ", kuntoilija1.painoindeksi())
    print("Rasvaprosentti on", kuntoilija1.rasvaprosentti())

    # Luodaan olio luokasta Juniorikuntoilija
    juniorikuntoilija = JunioriKuntoilija("Aku", 171, 65, 16, 1)
    print(juniorikuntoilija.nimi, "painaa", juniorikuntoilija.paino, "kg")
    #("Painoindeksi on ", juniorikuntoilija.painoindeksi())
    print("Rasvaprosentti on", juniorikuntoilija.rasvaprosentti())

    # Toinen olio luokasta Juniorikuntoilija
    juniorikuntoilija1 = JunioriKuntoilija("Anni", 156, 60, 16, 0)
    print(juniorikuntoilija1.nimi, "painaa", juniorikuntoilija1.paino, "kg")
    #("Painoindeksi on ", juniorikuntoilija1.painoindeksi())
    print("Rasvaprosentti on", juniorikuntoilija1.rasvaprosentti())