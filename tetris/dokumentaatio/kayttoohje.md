# Käyttöohje

## Pelin käynnistäminen
Komennot eivät välttämättä toimi oikein jos niitä ei suoriteta tetris kansiossa.

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

## Pelin pelaaminen
Ohjelma aukeaa suoraan pelinäkymään.

### Palikan liikuttaminen
Pelaaja voi liikuttaa palikkaa vasemmalle, oikealle tai alas nuolinäppäimillä ja palikan pyörittäminen onnistuu s- ja d-näppäimillä

### Pelin tavoite
Pelin tavoitteena on täyttää pelialueen rivejä eri muotoisilla palikoilla. Rivin täytyttyä se katoaa ja pelaaja saa pisteitä. Monen rivin poistaminen antaa enemmän pisteitä ja pelin jatkuessa rivin poiston antama pistemäärä kasvaa.

Peli loppuu kun uuden palikan luomiselle ei enää ole tilaa pelialueella.

Pelaajan liikutettavissa oleva palikka liikku alaspäin itsekseen. Palikan nopeus on aluksi hidas ja nousee pelin jatkuessa.

## Pisteiden tallentaminen
Pelin loputtua pelaaja voi tallentaa saamansa pisteet syöttämällä haluamansa nimimerkin.

## Pisteiden katsominen
Pelin loputtua parhaat tulokset esitetään pelaajalle.

