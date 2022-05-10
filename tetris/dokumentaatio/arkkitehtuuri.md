# Arkkitehtuurikuvaus
## Rakenne 
![](/dokumentaatio/kuvat/pakkausrakenne.png)

_ui_ sisältää käyttöliittymästä, _game_logic_ sovelluslogiikasta ja _score_database_ tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus _sprites_ sisältää luokkia, jotka kuvastavat sovelluksen käyttämiä spritejä.

## Käyttöliittymä



## Luokkakaavio?
```mermaid
classDiagram
  GameLoop "1" -- "1" Playfield
  
  Playfield "1" -- "*" Palikka
  
```
Playfield huolehtii pelialueesta ja pelialueella sijaitsevista palikoista.

## Tietojen pysyväistallennus
Pakkauksen _score_database_ luokka `ScoreRepository` huolehtii tietojen tallettamisesta

Pelaajan tulokset tallennetaan SQLite-tietokannan `scores` tauluun.

scores tauluun tallennetaan pelaajan saavuttama pistemäärä ja syöttämä nimimerkki.

## Päätoiminnallisuudet
Joitain ohjelman päätoiminnallisuuden sekvenssiokaavioita

### palikan liikuttaminen
```mermaid
sequenceDiagram
  actor User
  participant Renderer
  participant GameLoop
  participant PlayField
  User->>GameLoop: Keydown event or pressed key
  GameLoop->>GameLoop: _event_handling()
  GameLoop->>PlayField: move_group(active_block, delta_x, delta_y)
  PlayField-->>GameLoop: None
  GameLoop->>Renderer: render()
  
```

### tuloksen tallennus

```mermaid
sequenceDiagram
  actor User
  participant GameLoop
  participant ScoreRepository
  User->>GameLoop: Press "Enter"
  GameLoop->>GameLoop: _event_handling()
  GameLoop->>ScoreRepository: save_score(username, score)
  ScoreRepository-->>GameLoop: None
  
```
