# Changelog

## Viikko 3
- pelialueen luomistoiminnallisuus lisätty
- testattu, että pelialue luodaan oikein

## viikko 4
- pelin alkaessa pelialueelle luodann yksi pelaajan liikuteltavissa oleva palikka 
  - palikkaa liikutetaan näppäimistön nuolinäppäimillä
- palikan generaatiota testattu
## viikko 5
- palikka lukkiutuu puolen sekunnin jälkeen jos se ei pysty liikkumaan alaspäin
  - lukkiutumisen jälkeen uusi palikka generoidaan
- kaikki tetriksen palikat voivat nyt generoitua
- painovoima toimii
  - tällä hetkellä painovoima ei muutu
- täydet rivit katoavat oikein
- pelaaja voi pyörittää liikutettavaa palikkaa
- palikoiden painovoima muuttuu tietyillä level laskurin arvoilla 
  - level laskuri kasvaa aina kun uusi palikka luodaan tai linja poistetaan
    - kun level % 100 == 99 vain rivin poisto kasvattaa level laskuria
  - level laskuri ei ole tällä hetkellä näkyvissä pelaajalle
- pelaaja voi kerätä pisteitä poistamalla linjoja
- peli sulkeutuu jos uusi palikka on luomisen jälkeen lukitun palikan sisällä
  - peli kirjaa komentolinjalle pelaajan saavuttaman level laskimen arvon ja pistemäärän
- liikkumisnapin pohjassa pito saa pienen viiveen jälkeen palikan liikumaan jatkuvasti siihen suuntaan
- piste ja level laskurit lisätty näkyviin pelissä
- seuraavaksi esiintyvä palikka näytetään pelaajalle
