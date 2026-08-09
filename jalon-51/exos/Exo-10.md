---
title: "Exercice 10 : Métrique p-adique sur les rationnels"
---

### Exercice 10 : Métrique p-adique sur les rationnels \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $p$ un nombre premier. Pour tout rationnel non nul $x = p^k \frac{a}{b}$ où $a,b$ sont des entiers non divisibles par $p$, on définit sa valeur absolue p-adique $|x|_p = p^{-k}$. On pose $|0|_p = 0$. Démontrer que $d(x, y) = |x - y|_p$ est une distance sur $\mathbb{Q}$, et vérifier qu'elle est ultramétrique.

**Correction Détaillée :**
1. **Séparation :** Si $d(x, y) = 0$, alors $|x - y|_p = 0$. Par définition, cela n'arrive que si $x - y = 0$, donc $x = y$.
2. **Symétrie :** $d(y, x) = |y - x|_p = |-1 \cdot (x - y)|_p$. L'entier $-1$ n'est pas divisible par $p$, sa valuation est $0$, donc son module est $1$. $|y - x|_p = |x - y|_p$.
3. **Ultramétrie (et donc Inégalité triangulaire) :** Il suffit de montrer que $|u + v|_p \le \max(|u|_p, |v|_p)$ pour tous $u, v \in \mathbb{Q}$.
Soient $u = p^{k_u} \frac{a}{b}$ et $v = p^{k_v} \frac{c}{d}$. Supposons $k_u \le k_v$.
Alors $u + v = p^{k_u} (\frac{a}{b} + p^{k_v - k_u} \frac{c}{d}) = p^{k_u} \frac{ad + p^{k_v - k_u} bc}{bd}$.
La puissance de $p$ factorisant le numérateur est au moins $0$. Donc la valuation de $u+v$ est $\ge k_u$.
Ainsi $|u+v|_p \le p^{-k_u} = \max(|u|_p, |v|_p)$.
En appliquant avec $u = x-y$ et $v = y-z$, $x-z = u+v$, ce qui donne $d(x, z) \le \max(d(x, y), d(y, z))$.
Cette métrique étrange (où $1024$ est extrêmement 'proche' de $0$ pour $p=2$ car $2^{10}$ a un module $2^{-10} = 1/1024$) est le fondement de l'analyse p-adique.
