---
uuid: "jalon-53-exo-10"
title: "Compacité et séparation"
---

## Exercice 10 : Compacité et séparation \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$


**Énoncé :**
Montrer que toute application continue et bijective d'un espace topologique compact $X$ vers un espace topologique Hausdorff $Y$ est un homéomorphisme.

**Correction Détaillée :**
Soit $f : X \to Y$ continue et bijective. Il faut montrer que $f^{-1} : Y \to X$ est continue, ce qui équivaut à montrer que pour tout fermé $F$ de $X$, $(f^{-1})^{-1}(F) = f(F)$ est fermé dans $Y$.
Soit $F$ un fermé de $X$. Comme $X$ est compact et que tout fermé d'un compact est compact, $F$ est compact.
L'image continue d'un compact est compacte. Donc $f(F)$ est compact dans $Y$.
Puisque $Y$ est un espace Hausdorff, et que tout sous-espace compact d'un espace Hausdorff est fermé, on conclut que $f(F)$ est fermé.
Ainsi, $f$ est une application fermée, et bijective. Donc $f^{-1}$ est continue. $f$ est un homéomorphisme.
C'est un théorème central liant compacité et séparation.
