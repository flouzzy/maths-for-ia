---
uuid: "exo-7-10"
title: "Exo 10 - Jalon 7"
---

# Exercice 10 : Lemme de l'échange de Steinitz (Preuve abstraite)

## Énoncé
Soit $E$ un espace vectoriel engendré par une famille finie $G = (g_1, \dots, g_n)$. Soit $L = (v_1, \dots, v_p)$ une famille libre de $E$.
Montrer que $p \le n$. (Théorème fondamental de la dimension).

## Correction
Nous allons procéder par récurrence sur $p$, le cardinal de la famille libre.

**Initialisation ($p=1$) :**
Si $L = (v_1)$ est libre, alors $v_1 \neq 0$. Puisque $G$ engendre $E$, on ne peut pas avoir $n=0$ (sinon $E=\{0\}$ et $v_1=0$). Donc $n \ge 1 = p$. L'initialisation est vérifiée.

**Hérédité :**
Supposons le théorème vrai pour toute famille libre de $p-1$ éléments.
Considérons une famille libre $L = (v_1, \dots, v_p)$.
La sous-famille $(v_1, \dots, v_{p-1})$ est libre. Par hypothèse de récurrence, $p-1 \le n$.
De plus, par le lemme d'échange (ou par le fait qu'une base peut être formée en complétant $v_1, \dots, v_{p-1}$ avec des éléments de $G$), il existe des éléments de $G$ qui, ajoutés à $(v_1, \dots, v_{p-1})$, forment une famille génératrice de même cardinal $n$.
Quitte à réindexer $G$, on peut supposer que $(v_1, \dots, v_{p-1}, g_p, \dots, g_n)$ engendre $E$.
Maintenant, on exprime $v_p$ dans ce système générateur :
$v_p = \lambda_1 v_1 + \dots + \lambda_{p-1} v_{p-1} + \mu_p g_p + \dots + \mu_n g_n$.
Si on avait $p > n$, alors la liste des $g_i$ (de $p$ à $n$) serait vide.
On aurait alors $v_p = \lambda_1 v_1 + \dots + \lambda_{p-1} v_{p-1}$.
Cela s'écrit $\lambda_1 v_1 + \dots + \lambda_{p-1} v_{p-1} - v_p = 0$.
Ceci est une combinaison linéaire nulle avec au moins un coefficient non nul (celui de $v_p$ qui vaut $-1$). Cela contredit la liberté de la famille $L$.
Donc la liste des $g_i$ restants ne peut pas être vide, ce qui signifie qu'il reste au moins un élément d'indice $\ge p$. Donc $n \ge p$.

**Conclusion :**
Le théorème est vrai pour tout $p$. Une famille libre ne peut pas comporter plus d'éléments qu'une famille génératrice.
