---
uuid: "jalon-26-exo-01"
title: "Produit scalaire usuel et Cauchy-Schwarz"
difficulty: 1
---

# Exercice 1 : Produit scalaire usuel et Cauchy-Schwarz (Difficulté ★☆☆☆☆)

Soit $E = \mathbb{R}^n$ muni du produit scalaire canonique $\langle x, y \rangle = \sum_{i=1}^n x_i y_i$.
1. Redémontrer l'inégalité de Cauchy-Schwarz dans ce cas particulier en étudiant le polynôme $P(t) = \sum_{i=1}^n (x_i + t y_i)^2$.
2. En déduire que pour tout $x \in \mathbb{R}^n$, $\sum_{i=1}^n |x_i| \le \sqrt{n} \sqrt{\sum_{i=1}^n x_i^2}$.
3. Pour quels vecteurs $x$ l'égalité est-elle vérifiée ?

## Démonstration Rigoureuse à Blanc

1. Considérons le polynôme $P(t) = \sum_{i=1}^n (x_i + t y_i)^2$.
   - Ce polynôme est une somme de carrés de réels, il est donc toujours positif ou nul : $\forall t \in \mathbb{R}, P(t) \ge 0$.
   - Développons $P(t)$ :
     $$ P(t) = \sum_{i=1}^n (x_i^2 + 2t x_i y_i + t^2 y_i^2) = (\sum_{i=1}^n y_i^2)t^2 + 2(\sum_{i=1}^n x_i y_i)t + (\sum_{i=1}^n x_i^2) $$
   - Il s'agit d'un trinôme du second degré en $t$, de la forme $at^2 + bt + c$.
   - S'il est toujours positif ou nul, c'est qu'il ne s'annule au plus qu'une fois, donc son discriminant (réduit) est négatif ou nul : $\Delta' = (\frac{b}{2})^2 - ac \le 0$.
   - Calculons $\Delta'$ :
     $$ (\sum_{i=1}^n x_i y_i)^2 - (\sum_{i=1}^n y_i^2)(\sum_{i=1}^n x_i^2) \le 0 $$
     $$ (\sum_{i=1}^n x_i y_i)^2 \le (\sum_{i=1}^n x_i^2)(\sum_{i=1}^n y_i^2) $$
   - En prenant la racine carrée (croissante sur $\mathbb{R}^+$), on obtient :
     $$ |\sum_{i=1}^n x_i y_i| \le \sqrt{\sum_{i=1}^n x_i^2} \sqrt{\sum_{i=1}^n y_i^2} $$
     C'est l'inégalité de Cauchy-Schwarz.

2. Soit $x \in \mathbb{R}^n$. Définissons le vecteur $y = (y_1, \ldots, y_n)$ tel que $y_i = \text{sign}(x_i)$.
   - Si $x_i \neq 0$, $y_i = \frac{|x_i|}{x_i}$, et si $x_i = 0, y_i = 1$ (par convention pour cette démonstration).
   - Ainsi, $\sum_{i=1}^n x_i y_i = \sum_{i=1}^n x_i \text{sign}(x_i) = \sum_{i=1}^n |x_i|$.
   - D'autre part, $y_i^2 = (\pm 1)^2 = 1$. Donc $\sum_{i=1}^n y_i^2 = \sum_{i=1}^n 1 = n$.
   - Appliquons Cauchy-Schwarz :
     $$ |\sum_{i=1}^n x_i y_i| \le \sqrt{\sum_{i=1}^n x_i^2} \sqrt{\sum_{i=1}^n y_i^2} $$
     $$ \sum_{i=1}^n |x_i| \le \sqrt{\sum_{i=1}^n x_i^2} \sqrt{n} $$

3. L'égalité dans Cauchy-Schwarz est vérifiée si et seulement si les vecteurs $x$ et $y$ sont colinéaires.
   - Ici $y_i \in \{-1, 1\}$. Pour que $x$ et $y$ soient colinéaires, il doit exister une constante $\lambda$ telle que $x_i = \lambda y_i$ pour tout $i$.
   - Cela implique que tous les $|x_i|$ doivent être égaux, car $|x_i| = |\lambda| |y_i| = |\lambda|$.
   - Donc, l'égalité est vérifiée si et seulement si $|x_1| = |x_2| = \ldots = |x_n| = |\lambda|$.
   $\blacksquare$
