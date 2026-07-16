---
title: "Exercice 6 : Dimension de l'espace des polynômes d'un endomorphisme"
difficulty: 3
---

# Exercice 6 : Dimension de l'espace des polynômes d'un endomorphisme (★★★☆☆)

## Énoncé

Soit $E$ un espace vectoriel sur $\mathbb{K}$ de dimension finie $n$. Soit $u \in \mathcal{L}(E)$.
Considérons la sous-algèbre $\mathbb{K}[u] = \{ P(u) \mid P \in \mathbb{K}[X] \}$ engendrée par $u$.
On note $d$ le degré du polynôme minimal $\pi_u$ de $u$.
1. Montrer que $\dim(\mathbb{K}[u]) = d$.
2. En déduire que $1 \le \dim(\mathbb{K}[u]) \le n$.
3. Donner un exemple matriciel pour lequel la borne supérieure est atteinte.

## Solution Rigoureuse

### 1. Dimension de la sous-algèbre $\mathbb{K}[u]$
Soit le morphisme d'évaluation $\Phi_u : \mathbb{K}[X] \to \mathcal{L}(E)$ défini par $\Phi_u(P) = P(u)$.
Par définition, l'image de $\Phi_u$ est exactement $\mathbb{K}[u]$ : $\text{Im}(\Phi_u) = \mathbb{K}[u]$.
Le noyau de $\Phi_u$ est, par définition, l'idéal annulateur $\mathcal{I}_u$. Puisque $\mathbb{K}[X]$ est un anneau principal, cet idéal est engendré par le polynôme minimal : $\ker(\Phi_u) = \pi_u \mathbb{K}[X]$.
D'après le premier théorème d'isomorphisme pour les anneaux et algèbres, le morphisme induit :
$$\overline{\Phi_u} : \mathbb{K}[X] / (\pi_u) \xrightarrow{\sim} \text{Im}(\Phi_u) = \mathbb{K}[u]$$
est un isomorphisme d'algèbres (donc d'espaces vectoriels).
Par conséquent, la dimension de $\mathbb{K}[u]$ est égale à la dimension de l'espace vectoriel quotient $\mathbb{K}[X] / (\pi_u)$.

Or, par la division euclidienne dans $\mathbb{K}[X]$, tout polynôme $P$ s'écrit de manière unique $P = Q \pi_u + R$ avec $\deg(R) < \deg(\pi_u) = d$.
Dans le quotient $\mathbb{K}[X] / (\pi_u)$, la classe de $P$ est égale à la classe de $R$. Ainsi, tout élément du quotient est représenté par un unique polynôme de degré strictement inférieur à $d$.
La base canonique de ce quotient est la famille des classes $(\overline{1}, \overline{X}, \dots, \overline{X^{d-1}})$.
Cette base compte exactement $d$ éléments.
Donc, $\dim(\mathbb{K}[X] / (\pi_u)) = d$.
Par isomorphisme, nous obtenons rigoureusement : $\dim(\mathbb{K}[u]) = d$.

### 2. Bornes sur la dimension
Le polynôme minimal $\pi_u$ n'est pas un polynôme constant (sinon, si $\pi_u = 1$, alors $\text{id}_E = 0$, absurde car $n \ge 1$). Donc $d = \deg(\pi_u) \ge 1$.
De plus, d'après le théorème de Cayley-Hamilton, le polynôme caractéristique $\chi_u$ de $u$, qui est de degré $n$, est un polynôme annulateur. L'idéal annulateur étant engendré par le polynôme minimal, on a que $\pi_u$ divise $\chi_u$.
Le degré d'un diviseur d'un polynôme non nul est au plus égal au degré de ce polynôme.
Donc $d \le \deg(\chi_u) = n$.
En conclusion, en combinant ces inégalités :
$$1 \le \dim(\mathbb{K}[u]) \le n$$

### 3. Exemple où la borne supérieure est atteinte
Considérons la matrice compagnon associée au polynôme $P(X) = X^n$. C'est la matrice de taille $n \times n$ dont les éléments $(i+1, i)$ sont égaux à 1, et tous les autres à 0 :
$$A = \begin{pmatrix} 0 & 0 & \dots & 0 & 0 \\ 1 & 0 & \dots & 0 & 0 \\ 0 & 1 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{pmatrix}$$
Son polynôme caractéristique est $\chi_A(X) = \det(X I_n - A) = X^n$.
L'application itérée $A^{n-1}$ transforme le premier vecteur de la base canonique en le dernier, elle n'est donc pas la matrice nulle. Ainsi, $A^{n-1} \neq 0$.
Cela implique qu'aucun polynôme de degré strictement inférieur à $n$ ne peut annuler $A$. Le polynôme minimal de $A$ doit diviser $X^n$ et avoir un degré d'au moins $n$. L'unique possibilité est $\pi_A(X) = X^n$.
Ainsi, $\deg(\pi_A) = n$, et donc $\dim(\mathbb{K}[A]) = n$. La borne est atteinte.
