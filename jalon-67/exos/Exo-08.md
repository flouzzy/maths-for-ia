---
title: "Exercice 8 : Fatou vs Beppo Levi"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 8 : Fatou vs Beppo Levi

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $(f_n)$ une suite de fonctions mesurables positives convergeant simplement vers $f$. On suppose que $\lim \int f_n d\mu$ existe. A-t-on toujours $\int f d\mu \le \lim \int f_n d\mu$ ? Le montrer si oui, donner un contre-exemple si non. Que donne Beppo Levi si la suite est croissante ?

## Correction Détaillée

1. A-t-on toujours $\int f d\mu \le \lim \int f_n d\mu$ pour des fonctions positives ?
   **OUI**. C'est exactement l'énoncé du Lemme de Fatou, qui s'applique à toute suite de fonctions mesurables positives (sans condition de monotonie ou de domination).
   Lemme de Fatou : $\int (\liminf f_n) d\mu \le \liminf (\int f_n d\mu)$.
   Ici, comme la suite converge simplement, $\liminf f_n = f$, et comme la limite des intégrales existe, $\liminf \int f_n = \lim \int f_n$. Donc on a bien $\int f d\mu \le \lim \int f_n d\mu$.
2. Si la suite est croissante, le théorème de Beppo Levi nous dit que nous n'avons pas seulement une inégalité, mais une **égalité** stricte :
   $\int f d\mu = \lim \int f_n d\mu$.
3. Le lemme de Fatou fournit une minoration de la limite des intégrales (la masse peut "fuir" à l'infini, donc l'intégrale de la limite est plus petite).
   Considérons le contre-exemple classique : $f_n = n \mathbf{1}_{]0, 1/n]}$.
   Ici, $f = \lim f_n = 0$.
   On a $\int f = 0$ et $\lim \int f_n = 1$.
   L'inégalité de Fatou donne $0 \le 1$, ce qui est vrai. La masse a fui vers 0. Le fait que la suite ne soit pas croissante a empêché l'égalité de se produire.
