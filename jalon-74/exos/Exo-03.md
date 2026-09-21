---
title: "Exercice 3 : Application des Inégalités"
difficulty: "★★★☆☆"
---

# Exercice 3 : Application des Inégalités

**Niveau :** ★★★☆☆

**Énoncé :**
En utilisant l'inégalité de Jensen, prouver l'inégalité arithmético-géométrique : pour tous réels strictement positifs $x_1, \dots, x_n$, $\sqrt[n]{x_1 x_2 \dots x_n} \le \frac{x_1 + \dots + x_n}{n}$.

**Correction Détaillée :**
La fonction $t \mapsto -\ln(t)$ est strictement convexe sur $\mathbb{R}_{>0}$ (sa dérivée seconde est $1/t^2 > 0$).<br>Considérons l'espace fini $\{1, 2, \dots, n\}$ avec la mesure de probabilité uniforme $\mu(\{i\}) = 1/n$.<br>Définissons la variable aléatoire (ou fonction) $X(i) = x_i$.<br>L'espérance de $X$ est $\mathbb{E}[X] = \frac{1}{n} \sum_{i=1}^n x_i$.<br>L'inégalité de Jensen énonce que $\phi(\mathbb{E}[X]) \le \mathbb{E}[\phi(X)]$.<br>$-\ln\left( \frac{1}{n} \sum_{i=1}^n x_i \right) \le \frac{1}{n} \sum_{i=1}^n -\ln(x_i)$.<br>$-\ln\left( \frac{x_1 + \dots + x_n}{n} \right) \le -\frac{1}{n} \ln(x_1 x_2 \dots x_n) = -\ln\left( (x_1 \dots x_n)^{1/n} \right)$.<br>En multipliant par $-1$ (l'inégalité change de sens) : $\ln\left( \frac{x_1 + \dots + x_n}{n} \right) \ge \ln\left( \sqrt[n]{x_1 \dots x_n} \right)$.<br>La fonction exponentielle étant strictement croissante, on déduit le résultat voulu.
