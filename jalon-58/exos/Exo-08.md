---
uuid: "jalon-58-exo-08"
title: "Exercice 08 : Sous-espaces de dimension infinie"
---

## Sous-espaces de dimension infinie \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Montrer qu'un espace de Banach (espace normé complet) de dimension infinie ne peut pas admettre de base dénombrable (base de Hamel).

## Correction Détaillée (Zéro Ellipse)


1. Soit $E$ un espace de Banach de dimension infinie, et supposons par l'absurde qu'il admette une base de Hamel dénombrable $(e_n)_{n \in \mathbb{N}}$.
2. Définissons $F_n = \text{Vect}(e_0, \dots, e_n)$.
3. Pour tout $n$, $F_n$ est un sous-espace de dimension finie, donc il est fermé dans $E$.
4. De plus, comme $\dim E = \infty$, $F_n \neq E$. Or un sous-espace fermé propre est toujours d'intérieur vide (car il ne peut contenir de boule ouverte de $E$).
5. L'hypothèse selon laquelle $(e_n)$ est une base signifie que tout vecteur s'écrit comme une combinaison linéaire finie de $e_i$. Ainsi, $E = \bigcup_{n \in \mathbb{N}} F_n$.
6. $E$ est donc une union dénombrable de fermés d'intérieur vide.
7. Ceci contredit le Théorème de Baire, puisque $E$ est complet. Donc aucune base de Hamel de $E$ n'est dénombrable.
