# Exercice 9 : Construction de mesures (Lien avec probabilités)
$\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $\Omega$ un ensemble. On note $B(\Omega)$ l'espace des fonctions bornées sur $\Omega$ avec la norme supremum.
En utilisant Hahn-Banach, montrer qu'il existe une mesure "finiment additive" de probabilité $\mu$ sur $\mathcal{P}(\Omega)$ (même si $\Omega$ n'est pas dénombrable).

## Correction Détaillée
1. Sur $B(\Omega)$, on définit $p(f) = \sup_{\omega \in \Omega} f(\omega)$. C'est une fonctionnelle sous-linéaire.
2. Soit $M = \mathbb{R}\mathbf{1}$ (où $\mathbf{1}$ est la fonction constante égale à 1).
3. On définit $L_0(c\mathbf{1}) = c$ sur $M$.
4. On a $L_0(c\mathbf{1}) = c \le p(c\mathbf{1}) = c$ (si $c \ge 0$) ou $\le -c$ (si $c < 0$), dans tous les cas $L_0 \le p$.
5. Par Hahn-Banach, il existe un prolongement $L$ à $B(\Omega)$ tel que $L(f) \le \sup f$.
6. Si $f \ge 0$, $\sup(-f) \le 0$, donc $L(-f) \le 0 \implies L(f) \ge 0$. $L$ est positive.
7. Pour tout $A \subset \Omega$, posons $\mu(A) = L(\mathbf{1}_A)$.
8. $\mu(\Omega) = L(\mathbf{1}_\Omega) = L(\mathbf{1}) = 1$.
9. $\mu(A \cup B) = L(\mathbf{1}_{A \cup B}) = L(\mathbf{1}_A + \mathbf{1}_B) = \mu(A) + \mu(B)$ si $A$ et $B$ sont disjoints.
$\mu$ est une mesure finiment additive de probabilité universelle. $\blacksquare$
