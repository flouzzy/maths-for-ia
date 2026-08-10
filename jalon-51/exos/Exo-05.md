# Exercice 5 : Distances sur l'espace des suites
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé formel
Soit $\mathcal{B}(\mathbb{N}, \mathbb{R})$ l'ensemble des suites réelles bornées. On pose $d_\infty((u_n), (v_n)) = \sup_{n \in \mathbb{N}} |u_n - v_n|$. Vérifier les axiomes de la distance.

## Résolution pas à pas
**Étape 1 : Définition rigoureuse**

Soient $U=(u_n)$ et $V=(v_n)$ deux suites bornées. La différence $u_n - v_n$ est également une suite bornée. L'ensemble $\left\lbrace |u_n - v_n| \mid n \in \mathbb{N}\right\rbrace$ est donc une partie non vide et majorée de $\mathbb{R}$, elle admet donc une borne supérieure. L'application $d_\infty$ est bien à valeurs dans $\mathbb{R}_+$.

**Étape 2 : Axiomes de base**

- **Séparation :** Si $d_\infty(U, V) = 0$, alors $\forall n, |u_n - v_n| = 0$, donc $u_n = v_n$. Ainsi $U=V$.
- **Symétrie :** Évidente par symétrie de la valeur absolue.

**Étape 3 : Inégalité triangulaire (passage à la borne supérieure)**

Pour tout entier $n$, l'inégalité triangulaire dans $\mathbb{R}$ donne : $|u_n - w_n| \le |u_n - v_n| + |v_n - w_n|$.
Puisque $|u_n - v_n| \le d_\infty(U,V)$ et $|v_n - w_n| \le d_\infty(V,W)$, on a pour tout $n$ :
$|u_n - w_n| \le d_\infty(U,V) + d_\infty(V,W)$.
Le terme de droite est un majorant de l'ensemble $\left\lbrace |u_n - w_n|\right\rbrace$. Par définition, la borne supérieure est le plus petit des majorants. Donc :
$\sup_n |u_n - w_n| \le d_\infty(U,V) + d_\infty(V,W)$, ce qui conclut la preuve. $\blacksquare$
