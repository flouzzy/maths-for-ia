# Exercice 2 : Série entière avec des factorielles

**Énoncé :**
Calculer le rayon de convergence $R$ de la série entière $\sum_{n \geq 0} \frac{n!}{(2n)!} z^n$.

**Correction détaillée :**
Identifions le coefficient général : $a_n = \frac{n!}{(2n)!}$.
Ces coefficients sont manifestement non nuls pour tout $n \in \mathbb{N}$. Appliquons le critère de d'Alembert.
Formons le quotient et examinons son comportement asymptotique :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{\frac{(n+1)!}{(2(n+1))!}}{\frac{n!}{(2n)!}} = \frac{(n+1)!}{(2n+2)!} \cdot \frac{(2n)!}{n!} $$
Procédons au réarrangement et aux simplifications des factorielles.
Pour le numérateur : $(n+1)! = (n+1) \cdot n!$.
Pour le dénominateur : $(2n+2)! = (2n+2)(2n+1) \cdot (2n)!$.
L'expression devient alors :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{(n+1) \cdot n!}{(2n+2)(2n+1) \cdot (2n)!} \cdot \frac{(2n)!}{n!} $$
Les factorielles $n!$ et $(2n)!$ s'annihilent, laissant place à la fraction rationnelle simplifiée :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{n+1}{(2n+2)(2n+1)} $$
Notons que $2n+2 = 2(n+1)$, nous pouvons procéder à une simplification supplémentaire :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{n+1}{2(n+1)(2n+1)} = \frac{1}{2(2n+1)} = \frac{1}{4n+2} $$
Passons à la limite lorsque $n \to +\infty$ :
$$ L = \lim_{n \to +\infty} \frac{1}{4n+2} = 0 $$
D'après la règle de d'Alembert stipulant que $R = 1/L$, la limite étant nulle, on déduit que :
$$ R = +\infty $$
La série converge donc sur l'ensemble du plan complexe tout entier.
