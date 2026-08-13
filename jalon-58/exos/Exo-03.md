---
uuid: "jalon-58-exo-03"
title: "Exercice 03 : Fonctions continues sur un ensemble dense"
---

## Fonctions continues sur un ensemble dense \quad $\bigstar\bigstar\star\star\star$

Soit $X$ un espace métrique complet et $f_n : X \to \mathbb{R}$ une suite de fonctions continues. Supposons que pour tout $x \in X$, il existe $C_x > 0$ tel que $\sup_n |f_n(x)| \leq C_x$. Montrer qu'il existe un ouvert non vide $U$ et une constante $M > 0$ tels que $\sup_{x \in U} \sup_n |f_n(x)| \leq M$.

## Correction Détaillée (Zéro Ellipse)


1. Pour chaque $m \in \mathbb{N}$, définissons l'ensemble $F_m = \left\lbrace x \in X \mid \forall n, |f_n(x)| \leq m \right\rbrace$.
2. Comme les fonctions $f_n$ sont continues, $|f_n|$ l'est aussi. Ainsi, $F_m = \bigcap_n \{x \in X \mid |f_n(x)| \leq m\}$ est une intersection de fermés, donc $F_m$ est fermé.
3. L'hypothèse indique que pour chaque $x \in X$, la suite $(f_n(x))$ est bornée, disons par $C_x$. Soit $m \geq C_x$ un entier, alors $x \in F_m$. Ainsi, $X = \bigcup_{m \in \mathbb{N}} F_m$.
4. $X$ étant complet, le théorème de Baire affirme qu'au moins l'un des $F_m$ est d'intérieur non vide.
5. Soit $M \in \mathbb{N}$ tel que $\mathring{F}_M \neq \emptyset$. Prenons $U = \mathring{F}_M$.
6. L'ensemble $U$ est un ouvert non vide, et pour tout $x \in U$, par définition de $F_M$, $\sup_n |f_n(x)| \leq M$.
