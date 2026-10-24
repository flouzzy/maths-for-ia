# Exercice 9 : $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Formuler le théorème de séparation pour le problème des SVM (Séparateurs à Vaste Marge). Montrer que si l'enveloppe convexe des points positifs $C_+$ et l'enveloppe convexe des points négatifs $C_-$ dans $\mathbb{R}^n$ sont disjointes, alors les classes sont linéairement séparables avec une marge.

## Correction

**Étape 1 : Propriétés des ensembles**
Soient $X_+ = \{x_1, \dots, x_p\}$ et $X_- = \{y_1, \dots, y_q\}$ deux ensembles finis disjoints dans $\mathbb{R}^n$.
$C_+ = \text{Conv}(X_+)$ et $C_- = \text{Conv}(X_-)$.
L'enveloppe convexe d'un ensemble fini en dimension finie est un polytope fermé et borné, donc compact.

**Étape 2 : Application du théorème**
$C_+$ et $C_-$ sont des convexes compacts.
Si $C_+ \cap C_- = \emptyset$, on peut appliquer le théorème de Hahn-Banach (forme stricte).
Il existe un vecteur $w \in \mathbb{R}^n$ et une constante $b \in \mathbb{R}$ tels que pour un certain $\epsilon > 0$ :
$\forall x \in C_-, \langle w, x \rangle \le b - \epsilon < b < b + \epsilon \le \langle w, y \rangle, \forall y \in C_+$.

**Étape 3 : Marge SVM**
Quitte à diviser par $||w||$, on peut normaliser l'équation. C'est l'essence du SVM à marge dure : maximiser la distance géométrique $\gamma = \frac{\epsilon}{||w||}$ entre les deux enveloppes. L'existence de l'hyperplan optimal est garantie par Hahn-Banach et un théorème de projection sur les convexes fermés. $\blacksquare$
