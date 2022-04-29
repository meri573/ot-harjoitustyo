# This is a readme file

## Tetris
Tetris toteutettu pygame-kirjaston avulla.

Pelin tavoitteena on muodostaa pelialueen ylärajaan esiintyvistä palikoista täysiä rivejä. Rivin täytyttyä se katoaa ja pelaajalle kertyy pisteitä.

Palikat liikkuvat automaattisesti kohti pelialueen pohjaa ja mitä pidempään peli jatkuu sitä nopeampaa tämä liike on.
  - level laskurin kasvaessa palikoiden putoamisnopeus kasvaa
     - level laskuri kasvaa aina kun uusi palikka luodaan tai linja poistetaan
       - kun level % 100 == 99 vain rivin poisto kasvattaa level laskuria
### Palikan liikuttaminen
- nuolinäppäimillä liikutetaan palikkaa vasemmalle, oikealle, ja alas
- s ja d pyörittävät palikkaa

## Dokumentaatio
 
[vaatimusmaarittely.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/tuntikirjanpito.md)

[changelog.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. riippuvuudet saa asennettua komennolla

```bash
poetry install
```
2. tietokannan saa alustettua komennolla 

```bash
poetry run invoke build
```

3. peli käynnistyy komennolla

```bash
poetry run invoke start
```

## Komentorivikomennot
pelin käynnistys
```bash
poetry run invoke start
```
testien suoritus
```bash
poetry run invoke test
```
testikattavuusreportin generointi
```bash
poetry run invoke coverage-report
```
pylint kooditarkastus
```bash
poetry run invoke pylint
```
koodin automaattinen formatointi
```bash
poetry run invoke format
```

## release 1
[linkki](https://github.com/meri573/ot-harjoitustyo/releases/tag/viikko5)

:)
