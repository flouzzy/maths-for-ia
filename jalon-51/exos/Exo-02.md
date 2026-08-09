---
title: "Exo-02 : Norme et distance associée"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exo-02 : Norme et distance associée


## 1. Énoncé

Soit $(E, \|\cdot\|)$ un espace vectoriel normé. On définit l'application $d : E \times E \to \mathbb{R}_+$ par $d(x, y) = \|x - y\|$.

1. Montrer que $d$ est une distance sur $E$.
2. Montrer que cette distance est invariante par translation : $d(x+a, y+a) = d(x, y)$ pour tout $a \in E$.
3. Montrer l'homogénéité : $d(\lambda x, \lambda y) = |\lambda| d(x, y)$ pour tout scalaire $\lambda$.

## 2. Correction détaillée

**Question 1 :**
Vérifions les axiomes de distance en utilisant les axiomes de la norme.
- **Séparation :** $d(x, y) = 0 \iff \|x - y\| = 0 \iff x - y = 0_E \iff x = y$.
- **Symétrie :** $d(x, y) = \|x - y\| = \|-(y - x)\| = |-1|\|y - x\| = \|y - x\| = d(y, x)$.
- **Inégalité triangulaire :** Pour $x, y, z \in E$,
  $d(x, z) = \|x - z\| = \|(x - y) + (y - z)\|$
  Par l'inégalité triangulaire de la norme :
  $\|(x - y) + (y - z)\| \le \|x - y\| + \|y - z\| = d(x, y) + d(y, z)$.
Ainsi, $d$ est bien une distance.

**Question 2 :**
Soit $a \in E$. Calculons $d(x+a, y+a)$ :
$d(x+a, y+a) = \|(x+a) - (y+a)\| = \|x + a - y - a\| = \|x - y\| = d(x, y)$.
L'invariance par translation est fondamentale dans les espaces vectoriels normés.

**Question 3 :**
Soit $\lambda$ un scalaire. Calculons $d(\lambda x, \lambda y)$ :
$d(\lambda x, \lambda y) = \|\lambda x - \lambda y\| = \|\lambda(x - y)\|$.
Par l'axiome d'homogénéité de la norme :
$\|\lambda(x - y)\| = |\lambda| \|x - y\| = |\lambda| d(x, y)$.
