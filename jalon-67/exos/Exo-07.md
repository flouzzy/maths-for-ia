---
title: "Exercice 7 : TCM"
difficulty: "★★★★☆"
---
# Exercice 7 : Intégrale de Gauss fractionnaire

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
En utilisant un développement en série, calculer $\int_0^1 x^a (1-x)^b dx$ pour $a, b > -1$ se ramenant à des suites infinies (Fonction Bêta).

**Correction détaillée :**
1. Supposons $b \in \mathbb{N}$ pour simplifier, disons $b=k$. $(1-x)^k = \sum_{j=0}^k \binom{k}{j} (-1)^j x^j$. C'est une somme finie, pas besoin de TCM.
2. Pour $b$ réel, $(1-x)^b = \sum_{j=0}^{+\infty} \frac{(-1)^j \Gamma(b+1)}{j! \Gamma(b-j+1)} x^j$.
3. Les termes ne sont pas tous de même signe, donc le TCM (qui exige la positivité) ne s'applique pas directement à la série.
4. Cependant, on peut scinder la série en parties positive et négative, ou utiliser Beppo-Levi sur la somme absolue (ce qui justifie l'interversion si la somme des intégrales des modules converge, un résultat appelé théorème de Tonelli ou TCM généralisé pour Fubini). L'intégrale donne alors $\frac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+2)}$.
