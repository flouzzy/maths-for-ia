---
uuid: "jalon-38-exo-05"
title: "Exercice 5 : Changement de variable trigonométrique"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 5

**Difficulté :** ★★★☆☆

**Énoncé :**
Calculer l'intégrale $M = \int_0^1 \sqrt{1 - x^2} \, dx$ géométriquement, puis formellement par un changement de variable.

**Correction détaillée :**
1. **Méthode 1 : Interprétation géométrique.** La courbe d'équation $y = \sqrt{1 - x^2}$ pour $x \in [0, 1]$ représente le quart du cercle de centre $(0,0)$ et de rayon $1$ situé dans le premier quadrant (car $y \ge 0$ et $x \ge 0$).
2. L'aire totale d'un cercle de rayon $R$ est $\pi R^2$. Ici, pour le quart de cercle de rayon $1$, l'aire est $\frac{\pi \cdot 1^2}{4} = \frac{\pi}{4}$. Donc $M = \frac{\pi}{4}$.
3. **Méthode 2 : Changement de variable.** Nous allons formaliser rigoureusement ce calcul.
4. Posons $x = \sin(t)$. L'intervalle de $x$ est $[0, 1]$. La fonction $t \mapsto \sin(t)$ est une bijection de classe $\mathcal{C}^1$ de $[0, \pi/2]$ vers $[0, 1]$. Ce changement de variable est valide.
5. On a $dx = \cos(t) dt$.
6. Déterminons les nouvelles bornes : si $x = 0$, $t = \arcsin(0) = 0$. Si $x = 1$, $t = \arcsin(1) = \frac{\pi}{2}$.
7. L'intégrale devient :
$$ M = \int_0^{\pi/2} \sqrt{1 - \sin^2(t)} \cos(t) \, dt $$
8. Par l'identité fondamentale de la trigonométrie, $1 - \sin^2(t) = \cos^2(t)$. Donc $\sqrt{1 - \sin^2(t)} = \sqrt{\cos^2(t)} = |\cos(t)|$.
9. Sur l'intervalle $[0, \pi/2]$, la fonction cosinus est positive, donc $|\cos(t)| = \cos(t)$.
10. Substituons dans l'intégrale :
$$ M = \int_0^{\pi/2} \cos(t) \cdot \cos(t) \, dt = \int_0^{\pi/2} \cos^2(t) \, dt $$
11. Pour intégrer $\cos^2(t)$, nous utilisons la formule de linéarisation : $\cos^2(t) = \frac{1 + \cos(2t)}{2}$.
12. L'intégrale se scinde en deux :
$$ M = \int_0^{\pi/2} \frac{1}{2} dt + \int_0^{\pi/2} \frac{\cos(2t)}{2} dt $$
13. Calculons la première : $[\frac{t}{2}]_0^{\pi/2} = \frac{\pi}{4}$.
14. Calculons la seconde : une primitive de $\frac{\cos(2t)}{2}$ est $\frac{\sin(2t)}{4}$.
$$ \left[ \frac{\sin(2t)}{4} \right]_0^{\pi/2} = \frac{\sin(\pi)}{4} - \frac{\sin(0)}{4} = 0 - 0 = 0 $$
15. La somme donne bien : $M = \frac{\pi}{4} + 0 = \frac{\pi}{4}$.
$\blacksquare$
