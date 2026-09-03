# Exercice 5 : Mesure de comptage et sommes doubles
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Démontrer formellement que pour toute suite double de réels positifs $(a_{i,j})_{(i,j) \in \mathbb{N}^2}$, on a $\sum_{i=0}^{+\infty} \sum_{j=0}^{+\infty} a_{i,j} = \sum_{j=0}^{+\infty} \sum_{i=0}^{+\infty} a_{i,j}$.

## Correction Détaillée

Considérons l'espace mesuré $(\mathbb{N}, \mathcal{P}(\mathbb{N}), \mu)$ où $\mu$ est la mesure de comptage.
L'intégrale d'une fonction $g: \mathbb{N} \to \overline{\mathbb{R}}_+$ par rapport à $\mu$ est exactement sa somme : $\int_\mathbb{N} g \, d\mu = \sum_{i=0}^{+\infty} g(i)$.
Posons $f_n(i) = \sum_{j=0}^n a_{i,j}$.
Puisque $a_{i,j} \geq 0$, pour tout $i$, la suite $n \mapsto f_n(i)$ est une suite croissante de réels positifs :
$f_{n+1}(i) - f_n(i) = a_{i,n+1} \geq 0$.
La limite de $f_n$ est la fonction $f(i) = \sum_{j=0}^{+\infty} a_{i,j}$.
Le Théorème de Convergence Monotone s'applique :
$$\int_\mathbb{N} \left( \lim_{n \to +\infty} f_n(i) \right) d\mu(i) = \lim_{n \to +\infty} \int_\mathbb{N} f_n(i) d\mu(i)$$
Traduit en sommes de séries, le membre de gauche est :
$$\int_\mathbb{N} f(i) d\mu(i) = \sum_{i=0}^{+\infty} \left( \sum_{j=0}^{+\infty} a_{i,j} \right)$$
Le membre de droite est :
$$\lim_{n \to +\infty} \sum_{i=0}^{+\infty} f_n(i) = \lim_{n \to +\infty} \sum_{i=0}^{+\infty} \sum_{j=0}^n a_{i,j} = \lim_{n \to +\infty} \sum_{j=0}^n \sum_{i=0}^{+\infty} a_{i,j} = \sum_{j=0}^{+\infty} \sum_{i=0}^{+\infty} a_{i,j}$$
L'interversion de sommes finies et infinies est autorisée à l'étape intermédiaire, et Beppo-Levi garantit le passage final à la limite, validant le théorème de Fubini pour la mesure de comptage.
