## Luokkakaavio?
```mermaid
classDiagram
  GameLoop "1" -- "1" Playfield
  
  Playfield "1" -- "*" Palikka
  
```
Playfield huolehtii pelialueesta ja pelialueella sijaitsevista palikoista.


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
