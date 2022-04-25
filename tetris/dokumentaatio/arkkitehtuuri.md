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
  User->>GameLoop: K_left
  GameLoop->>GameLoop: _event_handling()
  GameLoop->>PlayField: move_group(active_block, -1 * cell_size, 0)
  PlayField-->>GameLoop: None
  GameLoop->>Renderer: render()
  
```
