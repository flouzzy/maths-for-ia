# Exercice 2 : Cross-Entropy avec un modèle uniforme

$\bigstar\bigstar\star\star\star$


On reprend la source $P$ de l'exercice précédent. Un modèle d'apprentissage initialisé aléatoirement prédit une distribution uniforme $Q$ sur les 4 symboles.

**1.** Calculer la cross-entropy $H(P, Q)$.
**2.** En déduire la divergence de Kullback-Leibler $D_{KL}(P \| Q)$.

**Correction :**

**1.** Le modèle uniforme attribue $q(x) = \frac{1}{4} = 0,25$ pour tout $x$.
La cross-entropy en base 2 est :
$$H(P, Q) = - \sum_{x} p(x) \log_2 q(x)$$
Puisque $q(x)$ est constant, nous avons :
$$H(P, Q) = - \sum_{x} p(x) \log_2(0,25) = - \log_2(0,25) \sum_{x} p(x)$$
Puisque $\sum_x p(x) = 1$, la cross-entropy est :
$$H(P, Q) = - \log_2(2^{-2}) = 2 \text{ bits}.$$

**2.** Nous savons par le théorème fondamental de ce cours que :
$$H(P, Q) = H(P) + D_{KL}(P \| Q)$$
D'après l'exercice précédent, $H(P) = 1,75$ bits. Par conséquent :
$$D_{KL}(P \| Q) = H(P, Q) - H(P) = 2 - 1,75 = 0,25 \text{ bits}.$$
Ce résultat quantifie exactement l'inefficacité du modèle uniforme par rapport à la vraie distribution.
