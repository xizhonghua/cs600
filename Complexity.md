### Complexity

#### Time

* ***P*** stands for *polynomial time*
* ***P*** = Union( TIME(n<sup>c</sup>) ), c ≧ 1
* ***L*** ∈ ***P*** ↔ ∃ a TM ***M<sub>L</sub>*** and a polynomial ***p*** s.t. ***M<sub>L</sub>*** decides ***L*** in p(|x|) time

----

* ***NP*** stands for *non-determinsitic polynomial time*
* ***L*** ∈ ***NP*** ↔ ∃ a TM ***M<sub>L</sub>*** and a polynomial ***p*** s.t. 
  * ***M<sub>L</sub>(x,w)*** runs in p(|x|) time
  * ***x*** ∈ ***L*** ↔ ∃ a witness ***w*** that ***M<sub>L</sub>(x,w)=1***

#### Space
