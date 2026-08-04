---
title: "Exercice 7 : Différentiabilité et Gradient"
difficulty: "★★★★☆"
---

# Exercice 7 : Différentiabilité de l'inverse d'une matrice

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $GL_n(\mathbb{R})$ l'ensemble des matrices inversibles, qui est un ouvert de $M_n(\mathbb{R})$. Soit la fonction d'inversion $f : GL_n(\mathbb{R}) \to M_n(\mathbb{R})$ définie par $f(X) = X^{-1}$. Montrer que $f$ est différentiable en tout $X \in GL_n(\mathbb{R})$ et que sa différentielle est donnée par $df_X(H) = -X^{-1}HX^{-1}$.

---
## Correction Détaillée

Soit $X \in GL_n(\mathbb{R})$. Considérons un accroissement matriciel $H \in M_n(\mathbb{R})$ tel que $X+H$ reste dans l'ouvert $GL_n(\mathbb{R})$.

**1. Écriture de l'inverse perturbé :**
On peut factoriser $X+H = X(I + X^{-1}H)$.
Ainsi, $(X+H)^{-1} = (I + X^{-1}H)^{-1} X^{-1}$.

**2. Développement limité de Neumann :**
Pour $\|H\|$ suffisamment petit, la norme $\|X^{-1}H\|$ est strictement inférieure à 1. Dans ce régime, la série de Neumann est convergente :
$$ (I + K)^{-1} = I - K + K^2 - K^3 + \dots $$
Ici, avec $K = X^{-1}H$, on obtient pour $\|H\|$ petit :
$$ (I + X^{-1}H)^{-1} = I - X^{-1}H + (X^{-1}H)^2 - (X^{-1}H)^3 + \dots $$
$$ (I + X^{-1}H)^{-1} = I - X^{-1}H + R_0(H) $$
où $R_0(H) = \sum_{k=2}^\infty (-1)^k (X^{-1}H)^k$.

En multipliant à droite par $X^{-1}$ :
$$ (X+H)^{-1} = (I - X^{-1}H + R_0(H)) X^{-1} = X^{-1} - X^{-1}HX^{-1} + R_0(H)X^{-1} $$

**3. Identification de la différentielle et du reste :**
L'équation s'écrit $f(X+H) = f(X) + L(H) + R(H)$, avec :
- $L(H) = -X^{-1}HX^{-1}$, qui est clairement une application linéaire de $H$.
- $R(H) = R_0(H)X^{-1} = (X^{-1}H)^2 (I + X^{-1}H)^{-1} X^{-1}$.

Il reste à borner $\|R(H)\|$ pour une norme matricielle sous-multiplicative :
$$ \|R(H)\| \le \|X^{-1}\|^2 \|H\|^2 \|(I + X^{-1}H)^{-1}\| \|X^{-1}\| $$
Pour $\|H\|$ suffisamment petit, $\|(I + X^{-1}H)^{-1}\|$ est majoré par une constante (par exemple 2). On a alors $\|R(H)\| \le C \|H\|^2$.
Ainsi $\frac{\|R(H)\|}{\|H\|} \le C\|H\| \to 0$ lorsque $H \to 0$.

**Conclusion :**
L'application $f(X) = X^{-1}$ est différentiable sur $GL_n(\mathbb{R})$ et $df_X(H) = -X^{-1}HX^{-1}$.
