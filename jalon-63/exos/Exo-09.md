---
uuid: "exo-jalon-63-09"
title: "Exercice 9 : Limites d'ensembles symétriques"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Limites d'ensembles symétriques

## Énoncé

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré avec $\mu(X) < +\infty$. Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'ensembles mesurables telle que $\mu(A_n \Delta A) \to 0$ lorsque $n \to \infty$, où $\Delta$ désigne la différence symétrique $A_n \Delta A = (A_n \setminus A) \cup (A \setminus A_n)$. Démontrer rigoureusement que $\lim_{n \to \infty} \mu(A_n) = \mu(A)$.

## Correction Détaillée

Rappelons la définition de l'union : $A_n \cup A = A \cup (A_n \setminus A)$. C'est une union disjointe.
Par additivité disjointe :
$\mu(A_n \cup A) = \mu(A) + \mu(A_n \setminus A)$.  (Équation 1)
De la même manière, on peut écrire $A_n \cup A = A_n \cup (A \setminus A_n)$ :
$\mu(A_n \cup A) = \mu(A_n) + \mu(A \setminus A_n)$. (Équation 2)

En soustrayant (Équation 2) de (Équation 1) (ce qui est légitime car la mesure est totale finie) :
$\mu(A) + \mu(A_n \setminus A) - \mu(A_n) - \mu(A \setminus A_n) = 0$
$\mu(A_n) - \mu(A) = \mu(A_n \setminus A) - \mu(A \setminus A_n)$

Prenons la valeur absolue de cette différence :
$|\mu(A_n) - \mu(A)| = |\mu(A_n \setminus A) - \mu(A \setminus A_n)| \leq \mu(A_n \setminus A) + \mu(A \setminus A_n)$
Or, par additivité disjointe, $\mu(A_n \setminus A) + \mu(A \setminus A_n) = \mu((A_n \setminus A) \cup (A \setminus A_n)) = \mu(A_n \Delta A)$.

Nous avons donc établi la majoration fondamentale :
$|\mu(A_n) - \mu(A)| \leq \mu(A_n \Delta A)$.

Par hypothèse du problème, $\lim_{n \to \infty} \mu(A_n \Delta A) = 0$.
Par le théorème des gendarmes, on conclut immédiatement que $\lim_{n \to \infty} |\mu(A_n) - \mu(A)| = 0$, ce qui signifie que $\lim_{n \to \infty} \mu(A_n) = \mu(A)$. $\blacksquare$
