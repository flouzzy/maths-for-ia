---
title: "Exercice 4 : Différentiabilité et Gradient"
difficulty: "★★★☆☆"
---

# Exercice 4 : Différentielle d'une forme bilinéaire

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $B : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ une forme bilinéaire continue. Démontrer rigoureusement que $B$ est différentiable en tout point $(x, y) \in \mathbb{R}^n \times \mathbb{R}^n$ et déterminer sa différentielle $dB_{(x,y)}$.

---
## Correction Détaillée

L'espace vectoriel d'étude est $E = \mathbb{R}^n \times \mathbb{R}^n$. Un point de $E$ est un couple $(x, y)$. Un vecteur d'accroissement est de la forme $h = (h_1, h_2) \in E$.

**1. Écriture de l'accroissement :**
Calculons $B(x + h_1, y + h_2)$ en utilisant la bilinéarité de $B$ :
$$ B(x + h_1, y + h_2) = B(x, y + h_2) + B(h_1, y + h_2) $$
$$ B(x + h_1, y + h_2) = B(x, y) + B(x, h_2) + B(h_1, y) + B(h_1, h_2) $$

**2. Identification des termes :**
Nous avons une décomposition exacte :
$$ B(x + h_1, y + h_2) = B(x, y) + L_{(x,y)}(h_1, h_2) + R(h_1, h_2) $$
Avec :
- $L_{(x,y)}(h_1, h_2) = B(x, h_2) + B(h_1, y)$. L'application $(h_1, h_2) \mapsto B(x, h_2) + B(h_1, y)$ est clairement linéaire par rapport au couple $(h_1, h_2)$ (somme d'applications linéaires par bilinéarité de $B$).
- $R(h_1, h_2) = B(h_1, h_2)$ est le terme de reste.

**3. Étude du reste :**
L'espace $\mathbb{R}^n$ étant de dimension finie, toute forme bilinéaire est continue. Il existe donc une constante $M > 0$ telle que pour tout $(u, v) \in \mathbb{R}^n \times \mathbb{R}^n$, $|B(u, v)| \le M \|u\| \|v\|$.
Munissons l'espace produit $E$ de la norme $\| (h_1, h_2) \|_E = \max(\|h_1\|, \|h_2\|)$.
Alors $\|h_1\| \le \|h\|_E$ et $\|h_2\| \le \|h\|_E$.
Majorons le reste :
$$ |R(h_1, h_2)| = |B(h_1, h_2)| \le M \|h_1\| \|h_2\| \le M \|h\|_E^2 $$
Ainsi, on a :
$$ \frac{|R(h)|}{\|h\|_E} \le M \|h\|_E $$
Ce qui tend vers $0$ lorsque $\|h\|_E \to 0$.

**Conclusion :**
La fonction $B$ est différentiable en tout point $(x, y)$, et sa différentielle est donnée par :
$$ dB_{(x,y)}(h_1, h_2) = B(x, h_2) + B(h_1, y) $$
