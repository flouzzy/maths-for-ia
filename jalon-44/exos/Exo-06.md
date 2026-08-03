---
title: "Exercice 6 : Ensemble compact dans $R^n$"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 6 : Ensemble compact dans $\mathbb{R}^n$

## Énoncé

Considérons l'ensemble $K = \{ (x, y) \in \mathbb{R}^2 \mid x^4 + y^4 = 1 \}$.
Montrer que $K$ est un compact de $\mathbb{R}^2$.

## Solution détaillée

1. **Rappel du théorème fondamental (Heine-Borel)** :
   Dans un espace vectoriel normé de dimension finie (comme $\mathbb{R}^2$), un sous-ensemble est compact si et seulement s'il est **fermé** et **borné**. Il suffit donc de prouver ces deux propriétés pour $K$.

2. **Démonstration de la fermeture de $K$** :
   Définissons l'application continue $f : \mathbb{R}^2 \to \mathbb{R}$ par $f(x, y) = x^4 + y^4$.
   L'ensemble $K$ peut s'écrire comme l'image réciproque du singleton $\{1\}$ :
   $$ K = f^{-1}(\{1\}) $$
   Le singleton $\{1\}$ est un ensemble fermé dans $\mathbb{R}$.
   Puisque $f$ est une fonction continue (car polynomiale), et que l'image réciproque d'un fermé par une fonction continue est un fermé, on conclut que **$K$ est fermé**.

3. **Démonstration de la bornitude de $K$** :
   Un sous-ensemble est borné s'il peut être inclus dans une boule de rayon fini, ce qui revient à montrer qu'il existe une constante $M > 0$ telle que pour tout $(x, y) \in K$, on a $\|(x,y)\| \leq M$.

   Pour tout $(x, y) \in K$, nous avons par définition :
   $$ x^4 + y^4 = 1 $$

   Puisque $x^4 \geq 0$ et $y^4 \geq 0$, cette équation implique nécessairement que :
   $$ x^4 \leq 1 \implies x^2 \leq 1 \implies |x| \leq 1 $$
   $$ y^4 \leq 1 \implies y^2 \leq 1 \implies |y| \leq 1 $$

   Calculons la norme euclidienne au carré pour un point arbitraire de $K$ :
   $$ \|(x,y)\|^2 = x^2 + y^2 $$
   Puisque $x^2 \leq 1$ et $y^2 \leq 1$, on a :
   $$ \|(x,y)\|^2 \leq 1 + 1 = 2 $$
   Donc pour tout $(x, y) \in K$, $\|(x,y)\| \leq \sqrt{2}$.
   L'ensemble $K$ est contenu dans la boule fermée de centre $(0,0)$ et de rayon $\sqrt{2}$. **$K$ est donc borné**.

4. **Conclusion** :
   L'ensemble $K$ étant à la fois fermé et borné dans l'espace de dimension finie $\mathbb{R}^2$, il est, d'après le théorème de Borel-Lebesgue, **compact**.
