---
uuid: "jalon-58-exo-02"
title: "Exercice 02 : Théorème de l'application ouverte (cas particulier)"
---

## Théorème de l'application ouverte (cas particulier) \quad $\bigstar\bigstar\star\star\star$

Montrer que si $f: \mathbb{R} \to \mathbb{R}$ est continue, et si $\mathbb{R}$ s'écrit comme l'union dénombrable de fermés $F_n$, alors l'un au moins de ces fermés contient un intervalle non vide.

## Correction Détaillée (Zéro Ellipse)


1. On nous donne $\mathbb{R} = \bigcup_{n \in \mathbb{N}} F_n$.
2. L'espace $\mathbb{R}$ muni de sa métrique usuelle est un espace métrique complet.
3. D'après le Théorème de Baire, un espace complet ne peut pas être une union dénombrable de fermés d'intérieur vide.
4. Par conséquent, il existe au moins un entier $n \in \mathbb{N}$ tel que l'intérieur de $F_n$ est non vide, soit $\mathring{F}_n \neq \emptyset$.
5. Par définition de l'intérieur dans $\mathbb{R}$, $\mathring{F}_n$ contient une boule ouverte $B(x, r)$ pour un certain $x \in \mathbb{R}$ et $r > 0$.
6. Toute boule ouverte $B(x, r)$ dans $\mathbb{R}$ est exactement l'intervalle ouvert $]x-r, x+r[$.
7. Donc $F_n$ contient un intervalle non vide.
