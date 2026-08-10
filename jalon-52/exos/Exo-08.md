---
title: "Homéomorphisme local vs global (Revetements)"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---

# Exercice 08 : Homéomorphisme local vs global (Revetements)
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Une application $f : X \to Y$ est un **homéomorphisme local** si tout point $x \in X$ possède un ouvert $U$ contenant $x$ tel que $f(U)$ est ouvert dans $Y$ et la restriction $f_{|U} : U \to f(U)$ est un homéomorphisme.
L'application complexe exponentielle $f : \mathbb{C} \to \mathbb{C}^*$ définie par $f(z) = e^z$ est-elle un homéomorphisme global ? Est-elle un homéomorphisme local ?

**Correction Détaillée :**
1. **Global ?**
L'application n'est pas un homéomorphisme global, car elle n'est pas injective. En effet, $f(z + 2i\pi) = e^{z}e^{2i\pi} = e^z = f(z)$. $f$ n'est pas une bijection de $\mathbb{C}$ vers $\mathbb{C}^*$.

2. **Local ?**
Soit $z_0 = x_0 + iy_0 \in \mathbb{C}$. Considérons la bande horizontale ouverte :
$U = \{ z = x+iy \in \mathbb{C} \mid x \in \mathbb{R}, y \in ]y_0 - \pi, y_0 + \pi[ \}$.
Sur ce domaine, l'application est strictement injective (car la différence de partie imaginaire entre deux points distincts est strictement inférieure à $2\pi$).
L'image de $U$ par $f$ est $f(U) = \mathbb{C} \setminus D$, où $D$ est la demi-droite paramétrée par $re^{i(y_0+\pi)}$ pour $r \ge 0$.
$f(U)$ est bien un ouvert de $\mathbb{C}^*$.
La restriction $f_{|U}$ admet une réciproque (une détermination du logarithme complexe) qui est holomorphe, et donc analytique et continue.
Par conséquent, $f_{|U} : U \to f(U)$ est bien un homéomorphisme. $f$ est donc un homéomorphisme local.
