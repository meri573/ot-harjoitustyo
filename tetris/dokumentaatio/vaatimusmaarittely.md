# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on tetristä muistuttava palikoiden kasaamispeli.

## Perusversion tarjoama toiminnallisuus
- [ ] Käyttäjä voi pelata pelin tetristä
  - [x] pelialue on 10 neliötä leveä ja 20 neliötä korkea
  
  - [x] pelialueen ylärajaan ilmestyy neljän neliön kokoisia palikoita joita pelaaja voi liikuttaa
    - [x] pelaaja voi liikuttaa kerralla yhtä palikkaa
    - [x] palikan neliöt ovat kiinni toistensa sivuihin
    
   - [x] palikat liikkuvat kohti pelialueen pohjaa
     - [x] kun pelialueen pohja tai toinen palikka estää palikan liikettä alas palikka lukkiutuu paikalleen ja uusi palikka ilmestyy
      - [x] palikan pysähdyttyä laskuri nousee yhdellä ja laskurin täytyttyä se resetoi ja palikoiden nopeus alaspäin kasvaa
      
   - [x] pelaaja voi liikuttaa palikoita vasemmalle, oikealle ja alas
      - [x] pelaaja voi myös pyörittää palikoita kumpaankin suuntaan 90 astetta kerralla
      
   - [x] pelaajan annetaan nähdä etukäteen minkä muotoinen seuraava ilmestyvä palikka on
   
   - [x] kun palikat ovat täyttäneet rivin jokaisen neliön rivi katoaa
      - [x] pelaaja ansaitsee näin pisteitä
        - [x] mitä enemmän rivejä katoaa kerralla sitä enemmän pisteitä pelaaja saa
   
   
  - [ ] Pelin jälkeen käyttäjä voi tallentaa saavutetun pistemäärän ja pelin keston omalla nimimerkillään
- [ ] Käyttäjä pystyy tarkastelemaan huipputuloksia

## Jatkokehitysideoita
Muutama esimerkki mahdollisista lisäyksistä/parannuksista perusversioon ajan salliessa:
- key bindingien muutosten salliminen
- annetaan pelaajalle kyky pelin sääntöjen muuttamiseen
  - esim. palikoiden generaatioalgoritmin muutos, kuinka nopeasti palikat lukkiutuvat pysähdyttyään, palikoiden putoamisen aloitusnopeus
- erilaisten pelimuotojen lisääminen
