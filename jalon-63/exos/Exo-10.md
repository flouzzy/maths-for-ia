---
uuid: "exo-jalon-63-10"
title: "Exercice 10 : Théorème de l'Atome (Non-atomicité)"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Théorème de l'Atome (Non-atomicité)

## Énoncé

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré fini. Un atome de la mesure $\mu$ est un ensemble mesurable $A$ tel que $\mu(A) > 0$, et pour tout sous-ensemble $B \subset A$ mesurable, on a soit $\mu(B) = 0$, soit $\mu(B) = \mu(A)$. Montrer que si $\mu$ est une mesure *sans atome* (non-atomique) et $\mu(X) = 1$, alors pour tout $c \in [0, 1]$, il existe un sous-ensemble $E \in \mathcal{A}$ tel que $\mu(E) = c$. (Ébauche de preuve par épuisement).

## Correction Détaillée

Ce théorème puissant affirme que toute mesure finie sans atome prend un continuum de valeurs. La démonstration complète requiert l'axiome du choix ou le lemme de Zorn, nous en présentons l'ossature rigoureuse.

Soit $c \in [0, 1]$. Si $c=0$, $E=\emptyset$ convient. Si $c=1$, $E=X$ convient. Supposons $0 < c < 1$.
Considérons l'ensemble $\mathcal{S} = \{ A \in \mathcal{A} \mid \mu(A) \leq c \}$. Cet ensemble est non vide (il contient $\emptyset$) et partiellement ordonné par l'inclusion ensembliste usuelle $\subset$.

L'idée centrale de la méthode d'épuisement consiste à montrer que toute chaîne croissante (pour l'inclusion) dans $\mathcal{S}$ possède un majorant dans $\mathcal{S}$.
Soit $(A_i)_{i \in I}$ une chaîne de $\mathcal{S}$. On pose $A^\star = \bigcup A_i$. Par continuité croissante (la chaîne équivaut topologiquement à une suite croissante de limite $A^\star$), on obtient $\mu(A^\star) = \sup \mu(A_i) \leq c$. Donc $A^\star \in \mathcal{S}$.
D'après le Lemme de Zorn, $\mathcal{S}$ possède donc un élément maximal $M$.
On a par définition $\mu(M) \leq c$.

Raisonnement par l'absurde : Supposons que $\mu(M) < c$.
L'ensemble résiduel $X \setminus M$ a pour mesure $\mu(X \setminus M) = 1 - \mu(M) > 1 - c > 0$.
Puisque la mesure est supposée sans atome, $X \setminus M$ ne peut pas être un atome. Il existe donc un sous-ensemble mesurable $B \subset X \setminus M$ tel que $0 < \mu(B) < \mu(X \setminus M)$.
Puisque $\mu$ est continue (par l'absence d'atome), on peut en fait extraire des portions de plus en plus petites. Il existerait nécessairement un $B^\star \subset X \setminus M$ suffisamment "petit" tel que $0 < \mu(B^\star) \leq c - \mu(M)$.

Considérons l'ensemble $M' = M \cup B^\star$.
Puisque l'union est disjointe, $\mu(M') = \mu(M) + \mu(B^\star) \leq \mu(M) + (c - \mu(M)) = c$.
Ainsi $M' \in \mathcal{S}$.
Mais $M$ est strictement inclus dans $M'$, ce qui contredit formellement la maximalité de $M$ garantie par le Lemme de Zorn.

L'hypothèse $\mu(M) < c$ est donc fausse. On a inévitablement $\mu(M) = c$. L'ensemble maximal $M$ est l'ensemble recherché $E$. $\blacksquare$
