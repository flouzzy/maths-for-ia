# Exercice 10 : Série avec des coefficients entrelacés

**Énoncé :**
Déterminer le rayon de convergence de la série $\sum a_n z^n$ où $a_{2k} = 2^k$ et $a_{2k+1} = 3^k$.

**Démonstration à blanc :**
On ne peut pas appliquer d'Alembert car le rapport $|a_{n+1}/a_n|$ oscille.
Calculons la racine $n$-ième pour appliquer Cauchy-Hadamard.
Pour $n = 2k$ (pair) :
$$ \sqrt[2k]{a_{2k}} = (2^k)^{1/2k} = 2^{1/2} = \sqrt{2} $$
Pour $n = 2k+1$ (impair) :
$$ \sqrt[2k+1]{a_{2k+1}} = (3^k)^{1/(2k+1)} $$
Lorsque $k \to +\infty$, $\frac{k}{2k+1} \to \frac{1}{2}$, donc cette sous-suite tend vers $3^{1/2} = \sqrt{3}$.
Les valeurs d'adhérence de la suite $(\sqrt[n]{a_n})$ sont $\sqrt{2}$ et $\sqrt{3}$.
La limite supérieure est le plus grand de ces points d'adhérence, soit $\sqrt{3}$.
Par la formule de Cauchy-Hadamard, $\frac{1}{R} = \limsup \sqrt[n]{a_n} = \sqrt{3}$.
Donc, le rayon de convergence est $R = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$.
