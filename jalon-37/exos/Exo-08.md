---
uuid: "jalon-37-exo-8"
title: "Exercice 8 : Calculs et Propriétés de l'Intégrale de Riemann"
tags:
  - math/analyse
  - ia/calcul-integral
---

# Exercice 8

**Difficulté :** ★★★★☆

**Énoncé :**
Lemme de Riemann-Lebesgue.
Soit $f : [a, b] \to \mathbb{R}$ de classe $C^1$. Montrer par intégration par parties que :
$$ \lim_{\lambda \to +\infty} \int_a^b f(t) \sin(\lambda t) \, dt = 0 $$

**Correction détaillée :**
1. Soit $\lambda > 0$. Les fonctions $f$ et $t \mapsto \sin(\lambda t)$ sont de classe $C^1$ sur $[a, b]$, ce qui justifie l'utilisation de l'intégration par parties.
2. Posons $u(t) = f(t)$ et $v'(t) = \sin(\lambda t)$.
3. Leurs dérivées/primitives sont : $u'(t) = f'(t)$ et $v(t) = -\frac{\cos(\lambda t)}{\lambda}$.
4. Appliquons la formule d'intégration par parties :
$$ \int_a^b f(t) \sin(\lambda t) \, dt = \left[ -f(t)\frac{\cos(\lambda t)}{\lambda} \right]_a^b - \int_a^b f'(t) \left( -\frac{\cos(\lambda t)}{\lambda} \right) \, dt $$
5. Évaluons le terme tout intégré :
$$ \left[ -f(t)\frac{\cos(\lambda t)}{\lambda} \right]_a^b = -\frac{f(b)\cos(\lambda b) - f(a)\cos(\lambda a)}{\lambda} $$
6. Majorons ce terme en utilisant l'inégalité triangulaire et le fait que $|\cos(x)| \le 1$ :
$$ \left| -\frac{f(b)\cos(\lambda b) - f(a)\cos(\lambda a)}{\lambda} \right| \le \frac{|f(b)| + |f(a)|}{\lambda} $$
7. Majorons l'intégrale restante :
$$ \left| \int_a^b f'(t) \frac{\cos(\lambda t)}{\lambda} \, dt \right| \le \int_a^b \frac{|f'(t)| \cdot |\cos(\lambda t)|}{\lambda} \, dt \le \frac{1}{\lambda} \int_a^b |f'(t)| \, dt $$
8. La fonction $f'$ étant continue sur le segment $[a, b]$, la quantité $\int_a^b |f'(t)| \, dt$ est une constante finie $M$.
9. En combinant les majorations :
$$ \left| \int_a^b f(t) \sin(\lambda t) \, dt \right| \le \frac{|f(b)| + |f(a)| + M}{\lambda} $$
10. Lorsque $\lambda \to +\infty$, la quantité $\frac{|f(b)| + |f(a)| + M}{\lambda}$ tend vers $0$.
11. Par le théorème des gendarmes, $\lim_{\lambda \to +\infty} \int_a^b f(t) \sin(\lambda t) \, dt = 0$. $\blacksquare$
