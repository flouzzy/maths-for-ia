---
title: "Exercice 4 : Densité des fonctions en escalier"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 4 : Densité des fonctions en escalier

## Énoncé

Montrez que si un réseau de neurones peut reproduire arbitrairement bien la fonction indicatrice d'un intervalle $\mathbb{1}_{[a, b]}$, alors il est capable d'approximer uniformément n'importe quelle fonction continue $f$ sur un segment $[c, d]$.

## Correction Rigoureuse

**Étape 1 : Approximation par des fonctions en escalier**
Soit $f \in \mathcal{C}([c, d], \mathbb{R})$. Puisque $[c, d]$ est compact, le théorème de Heine nous assure que $f$ est uniformément continue.
Pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que pour tout $x, y \in [c, d]$ vérifiant $|x - y| < \delta$, on ait $|f(x) - f(y)| < \epsilon / 2$.

**Étape 2 : Subdivisions du domaine**
Subdivisons $[c, d]$ en $N$ sous-intervalles $I_k = [x_k, x_{k+1}[$ (avec le dernier fermé) de longueur constante $h = (d-c)/N < \delta$.
Définissons la fonction en escalier :
$S(x) = \sum_{k=1}^N f(x_k) \mathbb{1}_{I_k}(x)$
Par construction, pour tout $x \in I_k$, on a $|x - x_k| < \delta$, donc $|f(x) - S(x)| = |f(x) - f(x_k)| < \epsilon / 2$.
Ainsi, $\|f - S\|_\infty \leq \epsilon / 2$.

**Étape 3 : Utilisation du réseau de neurones**
Par hypothèse, le réseau peut approcher chaque fonction indicatrice $\mathbb{1}_{I_k}$. Soit $G_k(x)$ une approximation neuronale telle que $\|\mathbb{1}_{I_k} - G_k\|_\infty < \frac{\epsilon}{2N \max |f|}$.
Définissons $G(x) = \sum_{k=1}^N f(x_k) G_k(x)$.
Par inégalité triangulaire :
$\|S - G\|_\infty \leq \sum_{k=1}^N |f(x_k)| \|\mathbb{1}_{I_k} - G_k\|_\infty \leq N \max|f| \frac{\epsilon}{2N \max |f|} = \epsilon / 2$

**Étape 4 : Conclusion (Inégalité triangulaire finale)**
$\|f - G\|_\infty \leq \|f - S\|_\infty + \|S - G\|_\infty \leq \epsilon / 2 + \epsilon / 2 = \epsilon$.
Le réseau de neurones est donc bien un approximateur universel. $\blacksquare$
