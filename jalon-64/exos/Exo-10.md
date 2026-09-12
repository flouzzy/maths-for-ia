---
title: "Exercice 10 : Mesure d'un ensemble de nombres ne contenant pas le chiffre 7"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

## Énoncé

Considérons le segment $I = [0, 1]$. Soit $E$ l'ensemble des réels de $I$ dont le développement décimal peut s'écrire sans jamais utiliser le chiffre 7. (S'il existe un développement propre et un développement impropre, on autorise qu'au moins l'un des deux respecte cette condition).
En vous inspirant de la construction fractale de l'ensemble de Cantor, démontrer rigoureusement par découpage que la mesure de Lebesgue de l'ensemble $E$ est nulle : $\lambda(E) = 0$.

## Correction Détaillée

La résolution nécessite une modélisation par itération spatiale du processus d'élimination, similaire à la poussière de Cantor mais basé sur la base 10 (système décimal) au lieu de la base 3.

**Étape 1 : Construction itérative des exclusions.**
Un nombre $x \in [0, 1]$ s'écrit en développement décimal $x = 0,d_1 d_2 d_3 \dots$ où chaque $d_i \in \{0, 1, \dots, 9\}$.
Interprétons l'exclusion du chiffre "7" à la première décimale ($d_1 \neq 7$).
Le segment $[0, 1]$ se découpe en 10 sous-intervalles de longueur $1/10$ de la forme $[\frac{k}{10}, \frac{k+1}{10}]$.
Ceux ayant $d_1 = 7$ constituent l'intervalle ouvert $]0.7, 0.8[$ (aux bornes près, qui sont dénombrables et donc de mesure nulle).
Ainsi, à la 1ère étape d'exclusion, nous retirons 1 intervalle sur 10.
Soit $E_1$ l'ensemble des nombres n'ayant pas $7$ à la première position. Il est constitué de la réunion disjointe de 9 intervalles de longueur $1/10$.
$$\lambda(E_1) = 9 \times \frac{1}{10} = \frac{9}{10}$$

Procédons par récurrence algébrique.
Soit $E_n$ l'ensemble des réels dont le développement décimal n'utilise pas le chiffre 7 jusqu'à la $n$-ième position.
L'ensemble $E_n$ est géométriquement constitué de $9^n$ petits intervalles disjoints (aux extrémités près), chacun de longueur exactement $1/10^n$.
La mesure de Lebesgue de l'ensemble à l'itération $n$ s'évalue par somme des longueurs, car il s'agit d'une union finie :
$$\lambda(E_n) = 9^n \times \frac{1}{10^n} = \left(\frac{9}{10}\right)^n$$

**Étape 2 : L'itération $n+1$.**
Vérifions le passage au rang $n+1$. Chaque petit intervalle fermé composant $E_n$ (de longueur $1/10^n$) est découpé en 10 micro-intervalles pour examiner la $(n+1)$-ième décimale.
Sur ces 10 micro-intervalles, nous excluons systématiquement celui correspondant au chiffre 7.
On conserve donc 9 micro-intervalles sur 10.
Le nombre total d'intervalles conservés est multiplié par 9 ($9^{n} \times 9 = 9^{n+1}$), et la taille de chaque micro-intervalle est divisée par 10 (longueur $1/10^{n+1}$).
La formule $\lambda(E_n) = (9/10)^n$ est parfaitement confirmée.

**Étape 3 : Passage asymptotique à la limite spatiale.**
L'ensemble final ciblé, $E$, est précisément l'intersection infinie de toutes ces contraintes de raffinement :
$$E = \bigcap_{n=1}^{+\infty} E_n$$
La suite $(E_n)_{n \in \mathbb{N}^*}$ est strictement décroissante au sens de l'inclusion topologique usuelle ($E_{n+1} \subset E_n$), car si on exige une restriction supplémentaire, le nouvel ensemble est nécessairement un sous-ensemble du précédent.
L'espace initial ayant une mesure finie ($\lambda([0,1]) = 1 < +\infty$), nous sommes légalement autorisés à utiliser le théorème de continuité décroissante pour les intersections dénombrables d'ensembles mesurables :
$$\lambda(E) = \lambda\left(\bigcap_{n=1}^{+\infty} E_n\right) = \lim_{n \to +\infty} \lambda(E_n)$$

La suite réelle correspondante, $u_n = \left(\frac{9}{10}\right)^n$, est une suite géométrique canonique de raison $|q| < 1$.
Par le théorème des suites géométriques asymptotiques, cette suite converge fatalement vers $0$ :
$$\lim_{n \to +\infty} \left(\frac{9}{10}\right)^n = 0$$

**Conclusion finale :**
L'évaluation limite conduit à :
$$\lambda(E) = 0$$
Ce résultat d'apparence contre-intuitive démontre que dans un système de représentation décimale continue, l'omission d'un seul des 10 chiffres pour composer un nombre infini "épuise" la quasi-totalité de l'espace probabiliste. En tirant un nombre réel au hasard uniforme entre 0 et 1 (mesure de Lebesgue de probabilité), la chance qu'il ne contienne *aucun* 7 dans son expansion décimale infinie est absolue et mathématiquement égale à 0.
