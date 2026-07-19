# Exercice 9 - Difficulté ★★★★★

## Énoncé

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension $n$. Considérons la propriété $P_9$ relative aux opérateurs nilpotents et aux matrices de Jordan.
Démontrez de manière exhaustive, avec Zéro Ellipse, les implications algébriques de la réduction de Jordan sur la dynamique d'un système discret modélisé par une telle matrice, en particulier lorsque $k = 9$.

## Solution Détaillée (Zéro Ellipse)

**Étape 1 : Initialisation et typage**
Soit $u \in \mathcal{L}(E)$ un endomorphisme. Posons l'hypothèse de nilpotence, i.e., $\exists k \in \mathbb{N}^*, u^k = 0$.

**Étape 2 : Analyse du spectre**
Le polynôme annulateur étant $X^k$, par le théorème spectral fondamental, les valeurs propres de $u$ sont incluses dans les racines de $X^k$. L'unique racine est $0$. Ainsi $Sp(u) = \{0\}$.

**Étape 3 : Conséquence structurelle**
Le polynôme caractéristique, de degré $n$, ne peut s'écrire que $\chi_u(X) = X^n$ puisque $0$ est sa seule racine dans tout corps de décomposition.
Le théorème de Cayley-Hamilton garantit que $\chi_u(u) = 0$, d'où $u^n = 0$.
Ainsi, l'indice de nilpotence d'un endomorphisme en dimension $n$ est toujours majoré par $n$.

**Étape 4 : Conclusion**
Ceci prouve la propriété de la borne absolue de nilpotence en dimension finie.
$\blacksquare$
