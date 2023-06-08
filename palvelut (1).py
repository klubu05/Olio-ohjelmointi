import random

class Asiakas:
    def __init__(self, nimi, ika):
        self._nimi = nimi
        self._ika = ika
        self._asiakasnumero = self._luo_nro()  # Generoidaan uniikki asiakasnumero jokaiselle asiakkaalle

    def get_nimi(self):
        return self._nimi

    def set_nimi(self, nimi):
        if not nimi:
            raise ValueError("Uusi nimi on annettava.")
        self._nimi = nimi

    def get_ika(self):
        return self._ika

    def set_ika(self, ika):
        if not ika:
            raise ValueError("Uusi ikä on annettava.")
        self._ika = ika

    def get_asiakasnumero(self):
        # Muotoillaan asiakasnumero muotoon XX-XXX-XXX
        return f"{self._asiakasnumero[0]:02}-{self._asiakasnumero[1]:03}-{self._asiakasnumero[2]:03}"

    def _luo_nro(self):
        # Generoidaan satunnainen asiakasnumero muodossa [XX, XXX, XXX]
        return [random.randint(10, 99), random.randint(100, 999), random.randint(100, 999)]


class Palvelu:
    def __init__(self, tuotenimi):
        self._tuotenimi = tuotenimi
        self._asiakkaat = []  # Lista, johon tallennetaan asiakasoliot

    def lisaa_asiakas(self, asiakas):
        if not asiakas:
            raise ValueError("Asiakas on annettava.")
        self._asiakkaat.append(asiakas)  # Lisätään asiakasolio listaan

    def poista_asiakas(self, asiakas):
        try:
            self._asiakkaat.remove(asiakas)  # Poistetaan asiakasolio listalta
        except ValueError:
            pass

    def tulosta_asiakkaat(self):
        print(f"Tuotteen {self._tuotenimi} asiakkaat ovat:")
        for asiakas in self._asiakkaat:
            print(self._luo_asiakasrivi(asiakas))  # Tulostetaan tietoja jokaisesta asiakkaasta
        print()

    def _luo_asiakasrivi(self, asiakas):
        # Luodaan muotoiltu merkkijono asiakkaan tiedoilla
        return f'{asiakas.get_nimi()} ({asiakas.get_asiakasnumero()}) on {asiakas.get_ika()}-vuotias.'


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self._edut = []  # Lista, johon tallennetaan lisäedut

    def lisaa_etu(self, etu):
        self._edut.append(etu)  # Lisätään etu listaan

    def poista_etu(self, etu):
        try:
            self._edut.remove(etu)  # Poistetaan etu listalta
        except ValueError:
            pass

    def tulosta_edut(self):
        print(f"Tuotteen {self._tuotenimi} edut ovat:")
        for etu in self._edut:
            print(etu)  # Tulostetaan jokainen etu
        print()
