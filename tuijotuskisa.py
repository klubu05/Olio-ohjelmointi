import random
import time

class Olento:
    def __init__(self, nimi, rohkeus, katseen_voima):
        """Konstruktori."""
        self.nimi = nimi
        self.rohkeus = rohkeus
        self.katseen_voima = katseen_voima

class Peikko(Olento):
    """Luokka, joka kuvaa Peikon.

    :ivar nimi: peikon nimi, arvotaan
    :type nimi: str
    :ivar rohkeus: peikon rohkeus, arvotaan
    :type rohkeus: int
    :ivar katseen_voima: peikon katseen voimakkuus, arvotaan
    :type katseen_voima: int

    Julkiset metodit
        arvo_hurraus()
    """

    NIMITAVUT = ("Ur", "Gar", "Grah", "Gur", "Kan", "Kazah", "Bar", "Bazh", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brar", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")

    def __init__(self, nimi="", rohkeus=4, katseen_voima=4):
        """Konstruktori."""
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        rohkeus = random.randint(4, 8)
        katseen_voima = random.randint(2, 4)

        super().__init__(nimi, rohkeus, katseen_voima)

    def _arvo_sanat(self, tavut, n, erotin, p=0.5):
        """Muodostaa satunnaisen tekstin annetuista tavuista.

        :param tavut: ne tavut, joita palautettava teksti voi sisältää
        :type tavut: Union[list[str], tuple[str]]
        :param n: mukaan poimittavien tavujen maksimimäärä
        :type n: int
        :param erotin: tavujen väliin satunnaisesti laitettava merkki
        :type erotin: str
        :param p: todennäköisyys lisätä erotin tavujen väliin (oletus 0.5)
        :type p: float
        :return: satunnainen teksti
        :rtype: str
        """
        osat = random.choices(tavut, k=random.randint(2, n))
        sanat = osat[0]
        for osa in osat[1:]:
            if random.random() < p:
                sanat += erotin + osa
            else:
                sanat += osa.lower()
        return sanat

    def arvo_hurraus(self):
        """Palauttaa satunnaisen hurraushuudahduksen.

        :return: hurraava huudahdus
        :rtype: str
        """
        return self._arvo_sanat(self.RIEMUTAVUT, 8, " ", 0.7)

    #tätä muokkasin
class Sankari(Olento):
    __HURRAUKSET = ("Jee", "jihppii", "MMMMMH", "RAWRRRR", "GÖRRRR", "MURINAA")
    def __init__(self, nimi):
        rohkeus = random.randint(5, 9)
        katseen_voima = random.randint(5, 9)

        super().__init__(nimi, rohkeus, katseen_voima)
    def arvo_hurraus(self):
        return random.choice(self.__HURRAUKSET)



# tämä on itsetehty
class Vuorenpeikko(Peikko):
    NIMITAVUT = ("Uh", "Gah", "Ghah", "Guh", "Kah", "Katah", "Bah", "Bath", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brah", "Dza", "Gra", "Gur", "Rah", "Urgh", "Ra")

    def __init__(self):
        """Konstruktori."""
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        rohkeus = random.randint(4, 8)
        katseen_voima = random.randint(2, 4)

        super().__init__(nimi, rohkeus, katseen_voima)

# tämä on itse tehty
class Luolapeikko(Peikko):
    NIMITAVUT = ("Uk", "Gak", "Ghak", "Guk", "Kau", "Katak", "Bak", "Batk", "Ragh", "Rudz")
    RIEMUTAVUT = ("Agh", "Ugh", "Ourgh", "Drar", "Brak", "Dza", "Grak", "Gurk", "Raku", "Urgh", "Ra")

    def __init__(self):
        """Konstruktori."""
        nimi = self._arvo_sanat(self.NIMITAVUT, 3, "-")
        rohkeus = random.randint(4, 8)
        katseen_voima = random.randint(2, 4)

        super().__init__(nimi, rohkeus, katseen_voima)

#tätä on muokattu
def hurraa(olio):
    """Tulostaa satunnaisen hurrauksen annetulle oliolle.

    :param olio: hurraava olio
    """
    print('%s: "%s!"' % (olio.nimi, olio.arvo_hurraus()))


def tulosta_rapaytys(rapayttaja):
    """Tulostaa sopivan tekstin räpäyttävälle oliolle.

    :param rapayttaja: silmiään räpäyttävä olio
    """
    if rapayttaja:
        if rapayttaja.rohkeus > 0:
            print("ja %s räpäyttää!" % rapayttaja.nimi)
        else:
            print("ja %s karkaa!" % rapayttaja.nimi)
    else:
        print("eikä kummankaan silmä rävähdä!")


def tuijota(olio1, olio2):
    """Asettaa annetut oliot taistelemaan keskenään yhden kierroksen.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: hävinnyt olio
    :rtype: Union[Sankari, Peikko]
    """
    print("He tuijottavat toisiaan...", end='')
    time.sleep(1)
    # Arvotaan kummankin olion tämän kierroksen vahvuus.
    katse1 = random.randint(0, olio1.katseen_voima)
    katse2 = random.randint(0, olio2.katseen_voima)
    rapayttaja = None

    # heikomman vahvuuden saanut olio menettää rohkeutta
    if katse1 > katse2:
        rapayttaja = olio2
        rapayttaja.rohkeus -= katse1
    elif katse1 < katse2:
        rapayttaja = olio1
        rapayttaja.rohkeus -= katse2
    return rapayttaja


def taistele(vasen, oikea):
    """Asettaa annetut oliot taistelemaan keskenään, kunnes toinen voittaa.

    :param vasen: ensimmäinen taisteleva olio
    :type vasen: Union[Sankari, Peikko]
    :param oikea: toinen taisteleva olio
    :type oikea: Union[Sankari, Peikko]
    :return: voittanut olio
    :rtype: Union[Sankari, Peikko]
    """
    while vasen.rohkeus > 0 and oikea.rohkeus > 0:
        haviaja = tuijota(vasen, oikea)
        tulosta_rapaytys(haviaja)
        time.sleep(0.5)
    if vasen.rohkeus > 0:
        return vasen
    else:
        return oikea


sankari = Sankari(input("Mikä on sankarimme nimi? "))
pelastetut = 0
# Käydään tuijotuskisoja peikkoja vastaan, kunnes sankari karkaa
while sankari.rohkeus > 0:
    # Tulostetaan kierroksen alkutiedot.
    sankarin_tiedot = sankari.nimi + " [" + str(sankari.rohkeus) + "]"
    print("Sankarimme %s kävelee kohti seikkailua." % sankarin_tiedot)
    time.sleep(0.7)

    # Tulostetaan vastaan tulevan peikon tiedot.
    peikko = random.choice([Vuorenpeikko, Peikko, Luolapeikko])()
    peikon_tiedot = peikko.nimi + " [" + str(peikko.rohkeus) + "]"
    print("Vastaan tulee hurja %s!" % peikon_tiedot)
    time.sleep(1)

    # Käydään tuijotuskisa peikkoa vastaan.
    voittaja = taistele(peikko, sankari)
    hurraa(voittaja)
    print()
    time.sleep(1.5)

time.sleep(1.5)
print("%s herää sängystään hikisenä - onneksi se oli vain unta!" % sankari.nimi)

# Luokka Olento määrittelee yleisen olentojen luokan, jossa on attribuutit nimi, rohkeus ja katseen_voima. Tämä luokka on periytetty muille olentoluokille.
#Luokka Peikko perii luokan Olento ja lisää sille ominaisuuksia. Luokassa määritellään myös kaksi luokka-attribuuttia NIMITAVUT ja RIEMUTAVUT, jotka sisältävät satunnaisesti valittavia nimi- ja hurraustavuja peikolle.
#Luokassa Peikko on metodi _arvo_sanat, joka luo satunnaisen tekstin annetuista tavuista ja erotinmerkistä.
#Luokassa Peikko on metodi arvo_hurraus, joka palauttaa satunnaisen hurraushuudahduksen käyttäen luokan RIEMUTAVUT-attribuuttia.
#Luokka Sankari perii luokan Olento ja määrittelee sille omat ominaisuudet. Luokalla on myös metodi arvo_hurraus, joka palauttaa satunnaisen hurraushuudahduksen käyttäen luokan __HURRAUKSET-attribuuttia.
#Luokka Vuorenpeikko perii luokan Peikko ja lisää sille oman luokka-attribuutin NIMITAVUT, joka sisältää satunnaisesti valittavia nimitavuja vuorenpeikolle.
#Luokka Luolapeikko perii luokan Peikko ja lisää sille oman luokka-attribuutin NIMITAVUT, joka sisältää satunnaisesti valittavia nimitavuja luolapeikolle.
#Funktio hurraa tulostaa satunnaisen hurrauksen annetulle oliolle käyttäen olion arvo_hurraus-metodia.
#Funktio tulosta_rapaytys tulostaa sopivan tekstin silmiään räpäyttävälle oliolle.
#Funktio tuijota asettaa kaksi annettua oliota tuijottamaan toisiaan yhden kierroksen ajan. Tuijotuksen tuloksena arvotaan kummankin olion vahvuudet ja heikompi menettää rohkeutta riippuen vahvuuksista.
#Funktio taistele asettaa kaksi annettua oliota taistelemaan keskenään kunnes toinen voittaa. Taistelu tapahtuu toistamalla tuijotuskierroksia, kunnes toisen olion rohkeus menee alle nollan.
#Koodissa luodaan Sankari-olio nimellä, jonka käyttäjä syöttää.
#Koodissa suoritetaan toistolause, joka jatkuu niin kauan kuin sankarin rohkeus on suurempi kuin nolla.
#Joka kierroksella arvotaan vastaan tuleva peikko (joko Vuorenpeikko, Peikko tai Luolapeikko).
#Kutsutaan taistele-funktiota peikon ja sankarin välillä.
#Tulostetaan voittajan hurraushuuto.
#Lopuksi tulostetaan viesti sankarin heräämisestä unesta.
#Yleisesti ottaen koodi luo olioluokkia (Olento, Peikko, Sankari, Vuorenpeikko, Luolapeikko) ja käyttää niitä simuloimaan tuijotusta ja taistelua peikkojen ja sankarin välillä. Olioluokissa määritellään ominaisuuksia ja metodeja, joita käytetään toiminnan toteuttamiseen.
