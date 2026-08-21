---
uuid: "jalon-65-exo-05"
title: "Exercice 5 : Tribu engendrée par une fonction"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 5 : Tribu engendrée par une fonction

## Énoncé

Soit $f : X \to Y$. Montrer que l'ensemble $\mathcal{A} = \{ f^{-1}(B) \mid B \in \mathcal{B} \}$ où $\mathcal{B}$ est une tribu sur $Y$, est une tribu sur $X$. On l'appelle tribu engendrée par $f$, notée $\sigma(f)$.

## Solution Détaillée

Vérifions les axiomes d'une tribu pour $\mathcal{A}$ :
1. L'espace total : $Y \in \mathcal{B}$, or $f^{-1}(Y) = X$, donc $X \in \mathcal{A}$.
2. Stabilité par complémentaire : Soit $A \in \mathcal{A}$. Il existe $B \in \mathcal{B}$ tel que $A = f^{-1}(B)$. Or $A^c = (f^{-1}(B))^c = f^{-1}(B^c)$. Puisque $\mathcal{B}$ est une tribu, $B^c \in \mathcal{B}$, donc $A^c \in \mathcal{A}$.
3. Stabilité par union dénombrable : Soit $(A_n)$ une suite dans $\mathcal{A}$. Pour chaque $n$, il existe $B_n \in \mathcal{B}$ tel que $A_n = f^{-1}(B_n)$. L'union $\cup_n A_n = \cup_n f^{-1}(B_n) = f^{-1}(\cup_n B_n)$. Puisque $\mathcal{B}$ est une tribu, $\cup_n B_n \in \mathcal{B}$, donc l'union $\cup_n A_n \in \mathcal{A}$.
$\mathcal{A}$ est donc bien une tribu. $\blacksquare$
