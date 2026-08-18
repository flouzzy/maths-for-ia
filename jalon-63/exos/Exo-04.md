---
uuid: "exo-jalon-63-04"
title: "Exercice 4 : Mesure image"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Mesure image

## Énoncé

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré, et $(Y, \mathcal{B})$ un espace mesurable. Soit $f : X \to Y$ une application mesurable (i.e. $\forall B \in \mathcal{B}, f^{-1}(B) \in \mathcal{A}$). On définit l'application $\mu_f : \mathcal{B} \to [0, +\infty]$ par $\mu_f(B) = \mu(f^{-1}(B))$. Démontrer que $\mu_f$ est une mesure sur $(Y, \mathcal{B})$.

## Correction Détaillée

Vérifions les deux axiomes définissant une mesure pour $\mu_f$ :

1. **Valeur sur l'ensemble vide :**
$f^{-1}(\emptyset) = \{x \in X \mid f(x) \in \emptyset\} = \emptyset$.
Donc $\mu_f(\emptyset) = \mu(f^{-1}(\emptyset)) = \mu(\emptyset) = 0$.

2. **$\sigma$-additivité :**
Soit $(B_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\mathcal{B}$ deux à deux disjoints.
Considérons leurs images réciproques $A_n = f^{-1}(B_n)$.
Les $(A_n)$ sont des éléments de $\mathcal{A}$ car $f$ est mesurable.
De plus, ils sont deux à deux disjoints : en effet, si $x \in A_i \cap A_j$ pour $i \neq j$, alors $f(x) \in B_i$ et $f(x) \in B_j$, ce qui implique $B_i \cap B_j \neq \emptyset$, ce qui contredit l'hypothèse de disjonction des $B_n$.
Enfin, l'image réciproque d'une union est l'union des images réciproques : $f^{-1}\left( \bigcup_{n=0}^{+\infty} B_n \right) = \bigcup_{n=0}^{+\infty} f^{-1}(B_n) = \bigcup_{n=0}^{+\infty} A_n$.

Nous appliquons la $\sigma$-additivité de $\mu$ sur la suite disjointe $(A_n)$ :
$$ \mu_f\left( \bigcup_{n=0}^{+\infty} B_n \right) = \mu\left( f^{-1}\left( \bigcup_{n=0}^{+\infty} B_n \right) \right) = \mu\left( \bigcup_{n=0}^{+\infty} A_n \right) $$
$$ = \sum_{n=0}^{+\infty} \mu(A_n) = \sum_{n=0}^{+\infty} \mu(f^{-1}(B_n)) = \sum_{n=0}^{+\infty} \mu_f(B_n) $$
L'application $\mu_f$ satisfait tous les axiomes : c'est bien une mesure sur l'espace d'arrivée $Y$. $\blacksquare$
