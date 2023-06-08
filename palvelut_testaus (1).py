import random
import palvelut

# Tuodaan tarvittavat moduulit ja luokat

# Asiakkaat
a = palvelut.Asiakas('Jompainen', random.randint(20, 30))
b = palvelut.Asiakas('Suvantolainen', random.randint(70, 90))
c = palvelut.Asiakas('Louheatar', random.randint(40, 60))

# Luodaan kolme asiakasta nimineen ja satunnaisilla iällä

# Palvelu
p = palvelut.Palvelu('Sammas')

# Luodaan Palvelu-olio nimellä 'Sammas'

p.lisaa_asiakas(a)
p.lisaa_asiakas(b)

# Lisätään asiakkaat palveluun p

p.tulosta_asiakkaat()

# Tulostetaan palvelun p asiakkaat

# ParempiPalvelu
pp = palvelut.ParempiPalvelu('Kirjokansi')

# Luodaan ParempiPalvelu-olio nimellä 'Kirjokansi'

pp.lisaa_asiakas(c)

# Lisätään asiakas c ParempiPalveluun pp

pp.tulosta_asiakkaat()

# Tulostetaan ParempiPalvelun pp asiakkaat

pp.lisaa_etu('Jauhaa rahaa.')
pp.lisaa_etu('Jauhaa viljaa.')
pp.lisaa_etu('Jauhaa suolaa.')

# Lisätään ParempiPalvelulle pp etuja

pp.tulosta_edut()

# Tulostetaan ParempiPalvelun pp edut

# Poikkeustapauksien käsittely
print()

# Tyhjä rivi tulostuksen erottamiseksi

pp.poista_etu('Jauhaa kultaa.')

# Yritetään poistaa etu 'Jauhaa kultaa.' ParempiPalvelusta pp

try:
    pp.lisaa_asiakas(None)
except ValueError as e:
    print(e)

# Yritetään lisätä None-asiakas ParempiPalveluun pp ja tulostetaan virheviesti, jos ValueError esiintyy

try:
    a.set_nimi('')
except ValueError as e:
    print(e)

# Yritetään asettaa asiakkaan a nimeksi tyhjä merkkijono ja tulostetaan virheviesti, jos ValueError esiintyy
