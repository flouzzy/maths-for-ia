---
title: "Le cube et la boule fermée (Topologie d'homéomorphisme abstrait)"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---

# Exercice 10 : Le cube et la boule fermée (Topologie d'homéomorphisme abstrait)
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Dans l'espace $\mathbb{R}^3$ usuel, soient $B = \{ (x,y,z) \mid x^2+y^2+z^2 \le 1 \}$ la boule unité fermée pour la norme euclidienne, et $C = [-1, 1]^3$ le cube fermé, correspondant à la boule unité pour la norme infinie $\Vert \cdot \Vert_\infty$.
Démontrer que l'application $f : B \to C$ définie par $f(0)=0$ et $f(v) = \frac{\Vert v \Vert_2}{\Vert v \Vert_\infty} v$ pour $v \neq 0$ est un homéomorphisme.

**Correction Détaillée :**
1. **Continuité :** La norme euclidienne $\Vert \cdot \Vert_2$ et la norme infinie $\Vert \cdot \Vert_\infty$ sont des fonctions continues sur $\mathbb{R}^3$. Puisque le dénominateur $\Vert v \Vert_\infty$ ne s'annule qu'en $v=0$, $f$ est trivialement continue sur $B \setminus \{0\}$.
Pour la continuité en $0$, on observe que :
$$ \Vert f(v) \Vert_\infty = \frac{\Vert v \Vert_2}{\Vert v \Vert_\infty} \Vert v \Vert_\infty = \Vert v \Vert_2 $$
Ainsi, lorsque $v \to 0$ (pour n'importe quelle norme en dimension finie), $\Vert f(v) \Vert \to 0$, ce qui prouve la continuité de $f$ en l'origine.

2. **Bijectivité :** Calculons la réciproque. Soit $w \in C$. Si $w = 0$, $v=0$. Si $w \neq 0$, on cherche $v$ tel que $w = c \cdot v$ (les deux vecteurs sont colinéaires).
Posons $g(w) = \frac{\Vert w \Vert_\infty}{\Vert w \Vert_2} w$.
Vérifions : $f(g(w)) = f( \lambda w )$ avec $\lambda = \frac{\Vert w \Vert_\infty}{\Vert w \Vert_2}$.
$$ f(\lambda w) = \frac{\Vert \lambda w \Vert_2}{\Vert \lambda w \Vert_\infty} \lambda w = \frac{\lambda \Vert w \Vert_2}{\lambda \Vert w \Vert_\infty} \lambda w = \frac{\Vert w \Vert_2}{\Vert w \Vert_\infty} \frac{\Vert w \Vert_\infty}{\Vert w \Vert_2} w = w $$
L'inverse est donc explicitement $g$, qui est globalement bien définie sur $C$. $f$ est une bijection.

3. **Continuité de l'inverse :** L'expression de l'inverse $g$ a la même forme rationnelle à composantes continues que $f$. Par la même preuve d'équivalence de normes pour la limite en 0, $g$ est continue sur $C$.
Le cube fermé et la boule fermée de $\mathbb{R}^3$ sont donc homéomorphes.
