---
title: "Exercice 1 : Application des Inégalités"
difficulty: "★☆☆☆☆"
---

# Exercice 1 : Application des Inégalités

**Niveau :** ★☆☆☆☆

**Énoncé :**
Montrer, en utilisant l'inégalité de Cauchy-Schwarz ($L^2$ sur un espace discret fini), que pour tous réels $a,b,c$, on a $(a+b+c)^2 \le 3(a^2+b^2+c^2)$.

**Correction Détaillée :**
L'inégalité de Cauchy-Schwarz sur $\mathbb{R}^3$ s'écrit $|\sum_{i=1}^3 u_i v_i| \le \sqrt{\sum u_i^2} \sqrt{\sum v_i^2}$.<br>Posons le vecteur $u = (a, b, c)$ et le vecteur $v = (1, 1, 1)$.<br>Le produit scalaire est $u \cdot v = a(1) + b(1) + c(1) = a+b+c$.<br>Les normes euclidiennes au carré sont $\|u\|^2 = a^2+b^2+c^2$ et $\|v\|^2 = 1^2+1^2+1^2 = 3$.<br>En élevant Cauchy-Schwarz au carré : $(u \cdot v)^2 \le \|u\|^2 \|v\|^2$.<br>Soit $(a+b+c)^2 \le 3(a^2+b^2+c^2)$. La preuve est complète.
