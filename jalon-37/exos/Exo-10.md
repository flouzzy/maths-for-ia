---
uuid: "jalon-37-exo-10"
title: "Exercice 10 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 10

**Difficulté :** ★★★★★

**Énoncé :**
Soient $f, g : [0, 1] \to \mathbb{R}$ deux fonctions continues. Calculer :
$$ \lim_{n \to \infty} \int_0^1 f(x^n) g(x) \, dx $$

**Correction détaillée :**
1. Fixons $\epsilon > 0$. Comme $g$ est continue sur $[0,1]$, elle y est bornée par un réel $M > 0$.
2. Considérons un réel $c \in ]0, 1[$. Nous allons découper l'intégrale en deux parties sur $[0, c]$ et sur $[c, 1]$.
3. $\int_0^1 f(x^n) g(x) \, dx = \int_0^c f(x^n) g(x) \, dx + \int_c^1 f(x^n) g(x) \, dx$.
4. Sur $[0, c]$, lorsque $n \to \infty$, $x^n \to 0$ uniformément. $f(x^n) \to f(0)$.
5. La première intégrale vérifie :
$$ \left| \int_0^c f(x^n) g(x) \, dx - \int_0^c f(0) g(x) \, dx \right| \le \int_0^c |f(x^n) - f(0)| |g(x)| \, dx $$
6. $f$ est continue en $0$, donc pour $\epsilon$ donné, il existe $N$ tel que pour $n \ge N$ et $x \in [0,c]$, $x^n \le c^n$, qui peut être rendu aussi petit que voulu. La différence converge vers $0$.
7. Pour la seconde intégrale sur $[c, 1]$, on majore grossièrement. $f$ est bornée par $K$.
$$ \left| \int_c^1 f(x^n) g(x) \, dx \right| \le K \cdot M \cdot (1 - c) $$
8. On peut choisir $c$ arbitrairement proche de $1$ de sorte que $K \cdot M \cdot (1 - c) < \frac{\epsilon}{2}$.
9. En rendant $n$ suffisamment grand, le terme de la première intégrale s'approche de $\int_0^1 f(0) g(x) \, dx$ à $\frac{\epsilon}{2}$ près.
10. Rigoureusement, on a convergé vers $\int_0^1 f(0) g(x) \, dx$.
11. La limite est donc $f(0) \int_0^1 g(x) \, dx$. $\blacksquare$
