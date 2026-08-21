---
uuid: "jalon-65-exo-07"
title: "Exercice 7 : Continuité et mesurabilité"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Continuité et mesurabilité

## Énoncé

Montrer que toute fonction continue $f : \mathbb{R} \to \mathbb{R}$ est borélienne. Est-ce vrai pour les fonctions dérivables ?

## Solution Détaillée

Soit $\mathcal{C}$ la famille des ouverts de $\mathbb{R}$. La tribu borélienne $\mathcal{B}(\mathbb{R})$ est générée par $\mathcal{C}$. Par le théorème sur les systèmes générateurs, il suffit de vérifier que l'image réciproque de tout ouvert par $f$ est un ensemble mesurable. Or, par définition topologique de la continuité, l'image réciproque de tout ouvert par une fonction continue est un ouvert. Comme tout ouvert est un borélien (puisque les ouverts génèrent la tribu borélienne), $f^{-1}(U) \in \mathcal{B}(\mathbb{R})$ pour tout ouvert $U$. Donc $f$ est borélienne. Toute fonction dérivable est continue, donc toute fonction dérivable est borélienne. $\blacksquare$
