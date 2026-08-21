---
uuid: "jalon-65-exo-08"
title: "Exercice 8 : Mesurabilité de fonctions monotones"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 8 : Mesurabilité de fonctions monotones

## Énoncé

Montrer que toute fonction monotone $f : \mathbb{R} \to \mathbb{R}$ est borélienne.

## Solution Détaillée

Supposons $f$ croissante. Pour montrer que $f$ est mesurable, utilisons le système générateur $\mathcal{C} = \{ ]a, +\infty[ \mid a \in \mathbb{R} \}$. Soit $a \in \mathbb{R}$, considérons $E_a = \{ x \in \mathbb{R} \mid f(x) > a \}$. Puisque $f$ est croissante, si $x_0 \in E_a$ et $x \ge x_0$, alors $f(x) \ge f(x_0) > a$, donc $x \in E_a$. Ainsi, $E_a$ est nécessairement un intervalle (soit $]c, +\infty[$, soit $[c, +\infty[$, soit $\emptyset$, soit $\mathbb{R}$). Tous ces intervalles sont des boréliens. L'image réciproque de chaque élément du système générateur est mesurable, donc $f$ est mesurable. La démonstration est analogue pour $f$ décroissante. $\blacksquare$
