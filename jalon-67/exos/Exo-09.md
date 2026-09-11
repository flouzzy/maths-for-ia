---
title: "Exercice 9 : TCM"
difficulty: "★★★★★"
---
# Exercice 9 : Convergence Monotone de l'entropie

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $p_n(x)$ une suite de densités de probabilité approchant la distribution uniforme sur $[0,1]$ par paliers ($p_n$ constant sur des intervalles de taille $1/2^n$). Prouver via le TCM l'égalité des limites des entropies différentielles.

**Correction détaillée :**
1. Posons $H(p_n) = -\int_0^1 p_n(x) \ln p_n(x) dx$.
2. On sait que $x \ln x$ n'est pas monotone. Le TCM ne s'applique pas brutalement.
3. Mais on sait que $p_n$ est étagée, positive. En étudiant $-x \ln x$, on peut la borner par $1/e$ sur $[0,1]$.
4. On pose alors $g_n(x) = 1/e + p_n(x) \ln p_n(x) \ge 0$. Cette suite de fonctions n'est toujours pas garantie croissante.
5. En réalité, le passage à la limite de l'entropie repose sur un argument de type Lemme de Fatou (Jalon 68) ou Convergence Dominée, montrant que les hypothèses du TCM (monotonie p.p.) sont ici trop rigides. Cet exercice met en lumière les *limites* d'applicabilité du TCM lorsqu'on perd la monotonie !
