---
uuid: "jalon-65-exo-10"
title: "Exercice 10 : Lemme de factorisation de Doob"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Lemme de factorisation de Doob

## Énoncé

Soient $X, Y : \Omega \to \mathbb{R}$ deux variables aléatoires. Démontrer que $Y$ est $\sigma(X)$-mesurable si et seulement s'il existe une fonction borélienne $f : \mathbb{R} \to \mathbb{R}$ telle que $Y = f(X)$. (Preuve sur les indicatrices puis étagées).

## Solution Détaillée

Si $Y = f(X)$ avec $f$ borélienne, alors $Y$ est la composée d'une fonction borélienne et d'une fonction mesurable, donc $Y$ est $\sigma(X)$-mesurable. Réciproquement, soit $Y$ une variable $\sigma(X)$-mesurable.
1) Si $Y = \mathbb{1}_A$ avec $A \in \sigma(X)$. Par définition de la tribu engendrée, il existe un borélien $B$ tel que $A = X^{-1}(B)$. Alors $\mathbb{1}_A(\omega) = \mathbb{1}_B(X(\omega))$, donc $f = \mathbb{1}_B$ convient.
2) Par linéarité, si $Y$ est étagée positive, il existe $f$ étagée telle que $Y = f(X)$.
3) Si $Y$ est mesurable positive, il existe une suite de fonctions étagées $Y_n \uparrow Y$. Par (2), $Y_n = f_n(X)$. Posons $f(x) = \limsup f_n(x)$. $f$ est borélienne et pour tout $\omega$, $Y(\omega) = \limsup Y_n(\omega) = \limsup f_n(X(\omega)) = f(X(\omega))$.
4) Pour $Y$ quelconque, on décompose $Y = Y^+ - Y^-$, on trouve $f^+$ et $f^-$ et $f = f^+ - f^-$. $\blacksquare$
