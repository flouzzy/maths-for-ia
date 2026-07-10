# Exercice 2 : Série avec factorielle

**Énoncé :**
Déterminer le rayon de convergence de la série entière $\sum_{n=0}^{+\infty} \frac{n!}{2^n} z^n$.

**Démonstration à blanc :**
Posons $a_n = \frac{n!}{2^n}$ pour tout $n \in \mathbb{N}$.
Pour tout $n$, $a_n \neq 0$. Appliquons la règle de d'Alembert :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{\frac{(n+1)!}{2^{n+1}}}{\frac{n!}{2^n}} = \frac{(n+1)! \cdot 2^n}{n! \cdot 2^{n+1}} $$
En simplifiant les factorielles et les puissances de 2 :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{n! (n+1) 2^n}{n! 2^n \cdot 2} = \frac{n+1}{2} $$
Lorsque $n \to +\infty$, cette quantité tend vers $+\infty$.
Ainsi $L = +\infty$.
Par la règle de d'Alembert, le rayon de convergence est $R = \frac{1}{L} = 0$.
La série ne converge qu'en $z = 0$.
