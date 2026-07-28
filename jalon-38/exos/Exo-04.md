---
uuid: "jalon-38-exo-04"
title: "Exercice 4 : Double intégration par parties"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 4

**Difficulté :** ★★☆☆☆

**Énoncé :**
Calculer l'intégrale $L = \int_0^1 x^2 e^x \, dx$.

**Correction détaillée :**
1. La fonction $x \mapsto x^2 e^x$ est continue sur $[0, 1]$.
2. Pour calculer cette intégrale d'un produit d'un polynôme par une exponentielle, nous devons utiliser des intégrations par parties successives pour "abaisser" le degré du polynôme.
3. **Première IPP :** Posons $u_1(x) = x^2$ et $v'_1(x) = e^x$.
4. Ces fonctions sont de classe $\mathcal{C}^1$. Leurs dérivée et primitive sont $u'_1(x) = 2x$ et $v_1(x) = e^x$.
5. Appliquons la formule :
$$ L = [x^2 e^x]_0^1 - \int_0^1 2x e^x \, dx $$
6. Évaluation du crochet : $[x^2 e^x]_0^1 = 1^2 e^1 - 0^2 e^0 = e$.
7. Donc $L = e - 2 \int_0^1 x e^x \, dx$. Notons $L_1 = \int_0^1 x e^x \, dx$.
8. **Deuxième IPP :** Pour calculer $L_1$, posons $u_2(x) = x$ et $v'_2(x) = e^x$.
9. On a $u'_2(x) = 1$ et $v_2(x) = e^x$.
10. Appliquons à nouveau la formule :
$$ L_1 = [x e^x]_0^1 - \int_0^1 1 \cdot e^x \, dx $$
11. Évaluation du crochet de $L_1$ : $[x e^x]_0^1 = 1 \cdot e^1 - 0 \cdot e^0 = e$.
12. L'intégrale restante de $L_1$ est fondamentale : $\int_0^1 e^x \, dx = [e^x]_0^1 = e^1 - e^0 = e - 1$.
13. Ainsi, $L_1 = e - (e - 1) = 1$.
14. Substituons $L_1$ dans l'expression de $L$ :
$$ L = e - 2 L_1 = e - 2(1) = e - 2 $$
$\blacksquare$
