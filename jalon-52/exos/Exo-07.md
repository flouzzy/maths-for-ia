---
title: "Adhérence et continuité"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 07 : Adhérence et continuité
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f : X \to Y$ une application entre espaces topologiques.
Montrer que $f$ est continue si et seulement si pour tout sous-ensemble $A \subset X$, $f(\overline{A}) \subset \overline{f(A)}$, où $\overline{E}$ désigne l'adhérence topologique de $E$.

**Correction Détaillée :**
1. **Supposons $f$ continue :**
Soit $A \subset X$. Le sous-ensemble $\overline{f(A)}$ est un fermé de $Y$ (par définition de l'adhérence).
Puisque $f$ est continue, l'image réciproque d'un fermé est un fermé. Ainsi, $f^{-1}(\overline{f(A)})$ est un fermé de $X$.
Or, on a clairement $A \subset f^{-1}(f(A))$, et comme $f(A) \subset \overline{f(A)}$, on en déduit $A \subset f^{-1}(\overline{f(A)})$.
L'adhérence de $A$ étant le plus petit fermé contenant $A$, il vient $\overline{A} \subset f^{-1}(\overline{f(A)})$.
En appliquant $f$, on obtient $f(\overline{A}) \subset \overline{f(A)}$.

2. **Supposons $f(\overline{A}) \subset \overline{f(A)}$ pour tout $A$ :**
Soit $F$ un fermé de $Y$. Posons $A = f^{-1}(F)$. Nous voulons montrer que $A$ est fermé, c'est-à-dire que $\overline{A} = A$.
Par l'hypothèse, $f(\overline{A}) \subset \overline{f(A)} = \overline{f(f^{-1}(F))}$.
Comme $f(f^{-1}(F)) \subset F$ et que $F$ est fermé, $\overline{f(f^{-1}(F))} \subset \overline{F} = F$.
Donc $f(\overline{A}) \subset F$.
Ceci implique que $\overline{A} \subset f^{-1}(F) = A$.
Or l'inclusion inverse $A \subset \overline{A}$ est toujours vraie. Donc $A = \overline{A}$, $A$ est fermé. L'application $f$ est continue.
