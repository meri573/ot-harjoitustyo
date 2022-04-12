## Luokkakaavio?
```mermaid
classDiagram
  GameLoop "1" -- "1" Playfield
  
  Playfield "1" -- "*" Palikka
  
```
Playfield huolehtii pelialueesta ja pelialueella sijaitsevista palikoista.
