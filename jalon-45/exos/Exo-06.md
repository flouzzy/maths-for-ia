---
title: "Exercice 6 : Différentiabilité et Gradient"
difficulty: "★★★★☆"
---

# Exercice 6 : Gradient de la fonction quadratique de coût (Machine Learning)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Dans un problème de régression, on cherche à minimiser la fonction de coût $J : \mathbb{R}^p \to \mathbb{R}$ définie par $J(\theta) = \frac{1}{2} \|X\theta - y\|^2$, où $X \in M_{n,p}(\mathbb{R})$ est la matrice des caractéristiques, $y \in \mathbb{R}^n$ le vecteur des cibles, et $\theta \in \mathbb{R}^p$ le vecteur des paramètres. Démontrer rigoureusement que le gradient de $J$ est $\nabla J(\theta) = X^T(X\theta - y)$.

---
## Correction Détaillée

La norme utilisée est la norme euclidienne, issue du produit scalaire canonique sur $\mathbb{R}^n$ : $\|u\|^2 = \langle u, u \rangle = u^T u$.

**1. Développement de l'accroissement :**
Soit $h \in \mathbb{R}^p$. Calculons $J(\theta + h)$ :
$$ J(\theta + h) = \frac{1}{2} \langle X(\theta + h) - y, X(\theta + h) - y \rangle $$
$$ J(\theta + h) = \frac{1}{2} \langle (X\theta - y) + Xh, (X\theta - y) + Xh \rangle $$
Par bilinéarité et symétrie du produit scalaire :
$$ J(\theta + h) = \frac{1}{2} \left[ \langle X\theta - y, X\theta - y \rangle + 2 \langle X\theta - y, Xh \rangle + \langle Xh, Xh \rangle \right] $$
$$ J(\theta + h) = J(\theta) + \langle X\theta - y, Xh \rangle + \frac{1}{2} \|Xh\|^2 $$

**2. Identification de l'application linéaire et de l'adjoint :**
Par définition de l'opérateur adjoint (transposé pour les matrices réelles), $\langle u, Xv \rangle_{\mathbb{R}^n} = \langle X^T u, v \rangle_{\mathbb{R}^p}$.
On peut donc réécrire le terme linéaire :
$$ L(h) = \langle X\theta - y, Xh \rangle_{\mathbb{R}^n} = \langle X^T(X\theta - y), h \rangle_{\mathbb{R}^p} $$
L'application $h \mapsto \langle X^T(X\theta - y), h \rangle$ est clairement une forme linéaire sur $\mathbb{R}^p$.

**3. Étude du reste :**
Le reste est $R(h) = \frac{1}{2} \|Xh\|^2$. L'opérateur $X$ étant linéaire en dimension finie, il est continu, et il existe une norme subordonnée $\|X\|$ telle que $\|Xh\| \le \|X\| \|h\|$.
D'où $0 \le R(h) \le \frac{1}{2} \|X\|^2 \|h\|^2$.
Ainsi $\frac{R(h)}{\|h\|} \le \frac{1}{2} \|X\|^2 \|h\|$, ce qui tend vers $0$ quand $\|h\| \to 0$.

**Conclusion :**
La fonction $J$ est différentiable en $\theta$ et sa différentielle est $dJ_\theta(h) = \langle X^T(X\theta - y), h \rangle$.
Par définition du gradient $dJ_\theta(h) = \langle \nabla J(\theta), h \rangle$, on identifie l'unique vecteur gradient :
$$ \nabla J(\theta) = X^T(X\theta - y) $$
