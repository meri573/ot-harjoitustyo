# Testausdokumentti


### Testauskattavuus

ui:ta lukuunottamatta testikattavuus on 71%

![](/tetris/dokumentaatio/kuvat/testikattavuus.png)

Testaamatta jäi suurin osa _game_loop.py_-tiedostosta ja muutama muu asia.

## Järjestelmätestaus
Manuaalisesti testattu.

### Asennus 
Testattu Linux-ympäristössä [käyttöohjetta](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/kayttoohje.md) seuraten.

### Toiminallisuus
[Määrittelydokumentin](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/vaatimusmaarittely.md) listaamat toiminnallisuudet ovat testattu toimivan.

## Sovellukseen jääneitä laatuongelmia
- täysien linjojen poistossa on hyvin harvinainen bugi jolloin jäljelle jääneet rivit eivät liiku alas oikealla tavalla.
- Jos SQLite tietokantaa ei ole alustettu ohjelma ei anna järkevää virheilmoitusta.
