```mermaid
classDiagram
  Pelaaja "1" -- "1" Nappula
  
  
  Pelilauta "1" -- "*" Ruutu
  
  Ruutu "1" -- "*" Nappula
  
  
  Pelaaja "*" -- "1" Nopat
  
  
  class Nappula

  
  class Ruutu{
     SeuraavaRuutu
  }

```
