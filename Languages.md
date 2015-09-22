## Languages

### Definitions
* *L<sub>halt</sub>* / *A<sub>TM</sub>* = {*(\<M\>,x)* | *M(x)* halts with output 1}
* *L<sub>A/R</sub>* / *Halt<sub>TM</sub>* = {*(\<M\>,x)* | *M(x)* halts with output 0 or 1}
* *L<sub>EQ</sub>* / *EQ<sub>TM</sub>* = {*(\<M<sub>1</sub>\>,\<M<sub>2</sub>\>)* | *L(M<sub>1</sub>)* = *L(M<sub>2</sub>)*}
* *L<sub>∅</sub>* / *E<sub>TM</sub>* = {*(\<M\>* | *L(M)* = ∅}

### Decidability
| Language                            | D    | R    | Language                         | D    | R    |
| ------------------------------------|:----:|:----:|----------------------------------|:----:|:----:|
| *L<sub>halt</sub>*                  | NO   | YES  | *(L<sub>halt</sub>)<sup>c</sup>* | NO   | YES  |
| *L<sub>∅</sub>*                     | NO   | NO   | *(L<sub>∅</sub>)<sup>c</sup>*    | NO   | YES  |
| *L<sub>EQ</sub>*                    | NO   | NO   | *(L<sub>EQ</sub>)<sup>c</sup>*   | NO   | NO   |
