# This is a readme file

## Tetris
Tetris toteutettu pygame-kirjaston avulla.

Pelin tavoitteena on täyttää pelialueen rivejä eri muotoisilla palikoilla. Rivin täytyttyä se katoaa ja pelaaja saa pisteitä. Monen rivin poistaminen antaa enemmän pisteitä ja pelin jatkuessa rivin poiston antama pistemäärä kasvaa.

Peli loppuu kun uuden palikan luomiselle ei enää ole tilaa pelialueella.

Pelaajan liikutettavissa oleva palikka liikku alaspäin itsekseen. Palikan nopeus on aluksi hidas ja nousee pelin jatkuessa.

### Palikan liikuttaminen
- nuolinäppäimillä liikutetaan palikkaa vasemmalle, oikealle, ja alas
- s ja d pyörittävät palikkaa

## Dokumentaatio
Dokumentaatiossa puutteita.

[käyttöohje.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/kayttoohje.md)
 
[vaatimusmaarittely.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/tuntikirjanpito.md)

[changelog.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/changelog.md)

[arkkitehtuuri.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/arkkitehtuuri.md)

[testausdokumentti.md](https://github.com/meri573/ot-harjoitustyo/blob/main/tetris/dokumentaatio/testaus.md)

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
