# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on tetristä muistuttava palikoiden kasaamispeli.

## Perusversion tarjoama toiminnallisuus
- Käyttäjä voi pelata pelin tetristä
  - pelialue on 10 neliötä leveä ja 20 neliötä korkea
  
  - pelialueen ylärajaan ilmestyy neljän neliön kokoisia palikoita joita pelaaja voi liikuttaa
    - pelaaja voi liikuttaa kerralla yhtä palikkaa
    - palikan neliöt ovat kiinni toistensa sivuihin
    
   - palikat liikkuvat kohti pelialueen pohjaa
     - kun pelialueen pohja tai toinen palikka estää palikan liikettä alas palikka lukkiutuu paikalleen ja uusi palikka ilmestyy
      - palikan pysähdyttyä laskuri nousee yhdellä ja laskurin täytyttyä se resetoi ja palikoiden nopeus alaspäin kasvaa
      
   - pelaaja voi liikuttaa palikoita vasemmalle, oikealle ja alas
      - pelaaja voi myös pyörittää palikoita kumpaankin suuntaan 90 astetta kerralla
      
   - pelaajan annetaan nähdä etukäteen minkä muotoinen seuraava ilmestyvä palikka on
   
   - kun palikat ovat täyttäneet rivin jokaisen neliön rivi katoaa ja pelaaja saa pisteitä
   
    - mitä enemmän rivejä katoaa kerralla sitä enemmän pisteitä pelaaja saa
   
   
  - Pelin jälkeen käyttäjä voi tallentaa saavutetun pistemäärän ja pelin keston omalla nimimerkillään
- Käyttäjä pystyy tarkastelemaan huipputuloksia

## Jatkokehitysideoita
Muutama esimerkki mahdollisista lisäyksistä/parannuksista perusversioon ajan salliessa:
- key bindingien muutosten salliminen
- annetaan pelaajalle kyky pelin sääntöjen muuttamiseen
  - esim. palikoiden generaatioalgoritmin muutos, kuinka nopeasti palikat lukkiutuvat pysähdyttyään, palikoiden putoamisen aloitusnopeus
- erilaisten pelimuotojen lisääminen
