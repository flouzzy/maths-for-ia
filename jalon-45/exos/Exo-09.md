---
title: "Exercice 9 : Différentiabilité et Gradient"
difficulty: "★★★★★"
---

# Exercice 9 : Gradient du déterminant

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit l'application déterminant $\det : M_n(\mathbb{R}) \to \mathbb{R}$. Démontrer que $\det$ est différentiable sur $M_n(\mathbb{R})$. Trouver sa différentielle en la matrice identité $I_n$. En déduire la différentielle pour toute matrice $A \in GL_n(\mathbb{R})$ à l'aide de la formule de Jacobi : $d(\det)_A(H) = \det(A) \text{Tr}(A^{-1}H)$.

---
## Correction Détaillée

Le déterminant est un polynôme par rapport aux $n^2$ coefficients de la matrice, il est donc infiniment différentiable sur $M_n(\mathbb{R})$.

**1. Différentielle en l'identité $I_n$ :**
Soit $H = (h_{ij}) \in M_n(\mathbb{R})$. Nous cherchons le coefficient de degré 1 en $H$ dans le développement de $\det(I_n + H)$.
Le polynôme caractéristique de $-H$ est $P_{-H}(\lambda) = \det(-H - \lambda I_n) = (-1)^n \det(H + \lambda I_n)$.
On a donc $\det(I_n + H) = (-1)^n P_{-H}(-1)$.
Nous savons que $P_M(\lambda) = \lambda^n - \text{Tr}(M)\lambda^{n-1} + \dots + (-1)^n \det(M)$.
En utilisant la définition combinatoire du déterminant ou le développement du polynôme, les termes de degré 1 par rapport aux coefficients $h_{ij}$ proviennent uniquement du produit diagonal $\prod_{i=1}^n (1 + h_{ii})$.
$$ \prod_{i=1}^n (1 + h_{ii}) = 1 + \sum_{i=1}^n h_{ii} + O(\|H\|^2) = 1 + \text{Tr}(H) + O(\|H\|^2) $$
Les termes hors de la diagonale donnent des contributions d'ordre 2 au minimum (à cause des transpositions dans le groupe symétrique $\mathfrak{S}_n$).
Ainsi, le développement limité à l'ordre 1 est :
$$ \det(I_n + H) = 1 + \text{Tr}(H) + o(\|H\|) = \det(I_n) + \text{Tr}(H) + o(\|H\|) $$
Par identification formelle de la partie linéaire : $d(\det)_{I_n}(H) = \text{Tr}(H)$.

**2. Différentielle en $A \in GL_n(\mathbb{R})$ :**
Soit un accroissement matriciel $H$. On peut écrire :
$$ \det(A + H) = \det(A(I_n + A^{-1}H)) = \det(A) \det(I_n + A^{-1}H) $$
On utilise le développement limité obtenu précédemment avec l'accroissement $K = A^{-1}H$ :
$$ \det(A + H) = \det(A) \left[ \det(I_n) + d(\det)_{I_n}(A^{-1}H) + o(\|A^{-1}H\|) \right] $$
$$ \det(A + H) = \det(A) [1 + \text{Tr}(A^{-1}H)] + o(\|H\|) $$
$$ \det(A + H) = \det(A) + \det(A)\text{Tr}(A^{-1}H) + o(\|H\|) $$
L'application $H \mapsto \det(A)\text{Tr}(A^{-1}H)$ étant linéaire, on conclut rigoureusement :
$$ d(\det)_A(H) = \det(A) \text{Tr}(A^{-1}H) $$
Cette relation est connue sous le nom de formule de Jacobi. Si on introduit la matrice de la comatrice (matrice adjointe), sachant que $A^{-1} = \frac{1}{\det A} (\text{Com} A)^T$, l'expression se généralise même pour les matrices non inversibles sous la forme $d(\det)_A(H) = \text{Tr}((\text{Com} A)^T H)$.
