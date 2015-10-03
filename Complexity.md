### Complexity

#### Time

* ***P*** stands for *polynomial time*
* ***P*** = ∪<sub>c≥1</sub> ( TIME(n<sup>c</sup>) )
* ***L*** ∈ ***P*** ↔ ∃ a TM ***M<sub>L</sub>*** and a polynomial ***p*** s.t. ***M<sub>L</sub>*** decides ***L*** in p(|x|) time

----
* ***NP*** stands for *non-determinsitic polynomial time*
* ***L*** ∈ ***NP*** ↔ ∃ a TM ***M<sub>L</sub>*** and a polynomial ***p*** s.t. 
  * ***M<sub>L</sub>(x,w)*** runs in p(|x|) time
  * ***x*** ∈ ***L*** ↔ ∃ a witness ***w*** that ***M<sub>L</sub>(x,w)=1***

----  
* ***coNP*** = {***L*** | ***<del>L</del>*** ∈ ***NP*** }, ***<del>L</del>*** = {0,1}<sup>\*</sup> \ ***L***

----
* Theorem ***P*** ⊆ ***NP*** ⊆ ∪<sub>c≥1</sub> TIME(2<sup>n<sup>c</sup></sup>)
* Claim ***NP*** = ∪<sub>c≥1</sub> TIME(n<sup>c</sup>)
* Conjecture ***P*** ≠ ***NP***
* Theorem If ***SAT*** ∈ ***P*** then ***P*** = ***NP***

#### ***NP***-Completeness
* ***L<sup>'</sup>*** is ***NP***-Hard if ∀ ***L*** ∈ ***NP***, ***L*** ≤<sub>p</sub> ***L<sup>'</sup>***
* ***L<sup>'</sup>*** is ***NP***-Complete if ***L<sup>'</sup>*** is ***NP***-hard and ***L<sup>'</sup>*** ∈ ***NP***
* ***SAT***, ***3SAT*** are ***NP***-Complete
 
#### Space
