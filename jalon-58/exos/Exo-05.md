---
uuid: "jalon-58-exo-05"
title: "Exercice 05 : Existence de fonctions nulles part monotones"
---

## Existence de fonctions nulles part monotones \quad $\bigstar\bigstar\bigstar\star\star$

En utilisant le théorème de Baire dans l'espace $\mathcal{C}([0,1], \mathbb{R})$, prouver l'existence de fonctions continues qui ne sont monotones sur aucun sous-intervalle ouvert.

## Correction Détaillée (Zéro Ellipse)


1. Soit $E = \mathcal{C}([0,1], \mathbb{R})$ muni de la norme $\|f\|_\infty = \sup_{x} |f(x)|$. C'est un espace de Banach.
2. Soit $F_{n, +}$ l'ensemble des fonctions $f \in E$ qui sont croissantes sur au moins un intervalle $[a, b]$ de longueur $\geq 1/n$.
3. On montre que $F_{n, +}$ est fermé. Si $f_k \to f$ et $f_k$ croissante sur $[a_k, b_k]$, quitte à extraire une sous-suite, on peut supposer $a_k \to a$ et $b_k \to b$ avec $b-a \geq 1/n$. On montre alors que $f$ est croissante sur $[a, b]$.
4. On montre que $F_{n, +}$ est d'intérieur vide. Pour toute fonction $f \in F_{n, +}$ et tout $\epsilon > 0$, on peut ajouter à $f$ une fonction oscillante $g$ très rapide d'amplitude $\epsilon/2$ de sorte que $f+g$ ne soit pas croissante sur des intervalles de longueur $\geq 1/n$, tout en restant dans la boule $B(f, \epsilon)$.
5. De même pour l'ensemble $F_{n, -}$ des fonctions localement décroissantes.
6. L'ensemble des fonctions monotones sur un certain intervalle est l'union dénombrable $M = \bigcup_{n} (F_{n, +} \cup F_{n, -})$.
7. Par le théorème de Baire, $M$ est d'intérieur vide et maigre, donc son complémentaire est dense. Il existe donc des (et même "presque toutes" les) fonctions continues nulle part monotones.
