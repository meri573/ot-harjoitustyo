# This is a readme file

## Tetris
Tetris toteutettu pygame-kirjaston avulla.

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
2. peli käynnistyy komennolla

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


:)
