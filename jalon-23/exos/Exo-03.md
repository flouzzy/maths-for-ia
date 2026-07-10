# Exercice 3 : Critère de d'Alembert modifié

**Énoncé :**
Déterminer le rayon de convergence de $\sum_{n=1}^{+\infty} \frac{2^n}{n} z^{2n}$.

**Démonstration à blanc :**
Cette série ne possède que des puissances paires de $z$. Les coefficients $a_m$ devant $z^m$ sont nuls pour $m$ impair. On ne peut pas appliquer directement la règle de d'Alembert aux $a_m$.
Posons $Z = z^2$. La série devient $\sum_{n=1}^{+\infty} \frac{2^n}{n} Z^n$.
Posons $b_n = \frac{2^n}{n}$. Appliquons d'Alembert à la série en $Z$ :
$$ \left| \frac{b_{n+1}}{b_n} \right| = \frac{\frac{2^{n+1}}{n+1}}{\frac{2^n}{n}} = \frac{2^{n+1} \cdot n}{2^n \cdot (n+1)} = 2 \frac{n}{n+1} $$
Lorsque $n \to +\infty$, $\frac{n}{n+1} \to 1$, donc la limite est $L_Z = 2$.
Le rayon de convergence pour la variable $Z$ est $R_Z = \frac{1}{2}$.
Ainsi, la série converge absolument si $|Z| < \frac{1}{2}$ et diverge si $|Z| > \frac{1}{2}$.
En revenant à $z$, on a $|z^2| < \frac{1}{2} \iff |z| < \frac{1}{\sqrt{2}}$.
Le rayon de convergence de la série initiale en $z$ est donc $R = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$.
