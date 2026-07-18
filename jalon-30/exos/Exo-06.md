# Exercice 6 : Commutant de la décomposition de Dunford (★★★)

Soit $f \in \mathcal{L}(E)$ tel que son polynôme caractéristique soit scindé, et soit $f = d + n$ sa décomposition de Dunford.
Soit $g \in \mathcal{L}(E)$. Montrer que $f \circ g = g \circ f \iff d \circ g = g \circ d \text{ et } n \circ g = g \circ n$.

### Solution :

**Sens réciproque ($\impliedby$) :**
Supposons que $d \circ g = g \circ d$ et $n \circ g = g \circ n$.
Calculons $(f \circ g)$ :
$$ f \circ g = (d + n) \circ g = d \circ g + n \circ g $$
En utilisant les hypothèses de commutation :
$$ f \circ g = g \circ d + g \circ n = g \circ (d + n) = g \circ f $$
Le sens réciproque est donc immédiat en exploitant la linéarité.

**Sens direct ($\implies$) :**
Supposons que $f \circ g = g \circ f$.
Le point crucial réside dans le théorème de Dunford étendu, qui stipule que **la composante diagonalisable $d$ et la composante nilpotente $n$ sont des polynômes en $f$**.
Il existe des polynômes $P, Q \in \mathbb{K}[X]$ tels que $d = P(f)$ et $n = Q(f)$.
Puisque $g$ commute avec $f$, une propriété fondamentale de l'algèbre des endomorphismes affirme que $g$ commute avec tout polynôme en $f$.
Démontrons-le rigoureusement. Soit $P(X) = \sum_{k=0}^m a_k X^k$.
$$ P(f) \circ g = \left( \sum_{k=0}^m a_k f^k \right) \circ g = \sum_{k=0}^m a_k (f^k \circ g) $$
Or, par une récurrence immédiate, si $g \circ f = f \circ g$, alors pour tout $k \in \mathbb{N}$, $g \circ f^k = f^k \circ g$.
Ainsi :
$$ \sum_{k=0}^m a_k (f^k \circ g) = \sum_{k=0}^m a_k (g \circ f^k) = g \circ \left( \sum_{k=0}^m a_k f^k \right) = g \circ P(f) $$
Par conséquent, $g$ commute avec $P(f) = d$, c'est-à-dire $d \circ g = g \circ d$.
De même, $g$ commute avec $Q(f) = n$, c'est-à-dire $n \circ g = g \circ n$.

Cet exercice prouve que le commutant de $f$, noté $\mathcal{C}(f)$, est exactement l'intersection des commutants de $d$ et de $n$ : $\mathcal{C}(f) = \mathcal{C}(d) \cap \mathcal{C}(n)$.
