---
uuid: exo-10
title: Exercice 10 - Inégalité de Cheeger
---

# Exercice 10 : Inégalité de Cheeger et conductivité

**Énoncé :**
Cet exercice aborde un théorème profond reliant le trou spectral (la deuxième plus petite valeur propre de $L$) à la coupe d'un graphe.
Soit $G = (V, E)$ un graphe régulier de degré $d$. On note $0 = \lambda_1 \leq \lambda_2 \leq \dots \leq \lambda_n$ les valeurs propres de son laplacien $L$.
On définit le quotient de Rayleigh pour un vecteur $x$ orthogonal au vecteur $\mathbf{1}$ (vecteur composé uniquement de $1$) comme :
$$R(x) = \frac{x^T L x}{x^T x}$$
Démontrer que :
$$\lambda_2 = \min_{x \perp \mathbf{1}, x \neq 0} \frac{\sum_{\{i,j\} \in E} (x_i - x_j)^2}{\sum_{i \in V} x_i^2}$$

**Correction Détaillée :**

*   *Analyse de l'énoncé :* La matrice $L$ est symétrique réelle. Le théorème spectral s'applique. Il s'agit d'utiliser la caractérisation variationnelle des valeurs propres (Principe du Min-Max de Courant-Fischer).

*   *Résolution pas-à-pas :*
1. **Théorème Spectral :**
   Puisque $L$ est une matrice symétrique réelle de dimension $n \times n$, le théorème spectral garantit qu'il existe une base orthonormée de $\mathbb{R}^n$ formée de vecteurs propres de $L$.
   Notons $v_1, v_2, \dots, v_n$ ces vecteurs propres associés respectivement aux valeurs propres $\lambda_1 \leq \lambda_2 \leq \dots \leq \lambda_n$.
   On a donc $L v_k = \lambda_k v_k$ pour $k = 1, \dots, n$, et $v_i^T v_j = \delta_{ij}$.

2. **Propriétés de la plus petite valeur propre :**
   Nous savons que $\lambda_1 = 0$ et qu'un vecteur propre associé est le vecteur constant $\mathbf{1} = (1, 1, \dots, 1)^T$ car $L \mathbf{1} = \mathbf{0}$.
   Pour que la base soit orthonormée, le vecteur $v_1$ est simplement $\mathbf{1}$ normalisé : $v_1 = \frac{1}{\sqrt{n}} \mathbf{1}$.

3. **Décomposition d'un vecteur $x$ :**
   Soit $x \in \mathbb{R}^n$ un vecteur non nul tel que $x \perp \mathbf{1}$. Cela implique que $x \perp v_1$, c'est-à-dire $x^T v_1 = 0$.
   Puisque $\{v_1, v_2, \dots, v_n\}$ est une base de $\mathbb{R}^n$, on peut exprimer $x$ comme une combinaison linéaire :
   $x = \sum_{k=1}^n \alpha_k v_k$
   Comme $x \perp v_1$, la coordonnée $\alpha_1 = x^T v_1$ est nulle. Ainsi :
   $x = \sum_{k=2}^n \alpha_k v_k$

4. **Évaluation du dénominateur $x^T x$ :**
   $x^T x = \left(\sum_{j=2}^n \alpha_j v_j\right)^T \left(\sum_{k=2}^n \alpha_k v_k\right) = \sum_{j=2}^n \sum_{k=2}^n \alpha_j \alpha_k v_j^T v_k$
   Grâce à l'orthonormalité ($v_j^T v_k = \delta_{jk}$), tous les termes croisés s'annulent et il reste :
   $x^T x = \sum_{k=2}^n \alpha_k^2$

5. **Évaluation du numérateur $x^T L x$ :**
   Tout d'abord, calculons $Lx$ :
   $Lx = L \left( \sum_{k=2}^n \alpha_k v_k \right) = \sum_{k=2}^n \alpha_k L v_k = \sum_{k=2}^n \alpha_k \lambda_k v_k$
   Maintenant, évaluons $x^T L x$ :
   $x^T L x = \left(\sum_{j=2}^n \alpha_j v_j\right)^T \left(\sum_{k=2}^n \alpha_k \lambda_k v_k\right) = \sum_{j=2}^n \sum_{k=2}^n \alpha_j \alpha_k \lambda_k v_j^T v_k$
   À nouveau, en utilisant l'orthonormalité, cela se simplifie en :
   $x^T L x = \sum_{k=2}^n \lambda_k \alpha_k^2$

6. **Minimisation du quotient de Rayleigh :**
   Le quotient de Rayleigh s'écrit donc, pour $x \perp \mathbf{1}$ :
   $$R(x) = \frac{\sum_{k=2}^n \lambda_k \alpha_k^2}{\sum_{k=2}^n \alpha_k^2}$$
   Puisque les valeurs propres sont ordonnées $\lambda_2 \leq \lambda_3 \leq \dots \leq \lambda_n$, on peut minorer la somme au numérateur :
   $\sum_{k=2}^n \lambda_k \alpha_k^2 \geq \sum_{k=2}^n \lambda_2 \alpha_k^2 = \lambda_2 \sum_{k=2}^n \alpha_k^2$
   On en déduit que pour tout vecteur $x \perp \mathbf{1}, x \neq 0$ :
   $R(x) = \frac{x^T L x}{x^T x} \geq \frac{\lambda_2 \sum_{k=2}^n \alpha_k^2}{\sum_{k=2}^n \alpha_k^2} = \lambda_2$

7. **Atteinte du minimum :**
   Pour montrer que ce minorant est bien le minimum, il suffit de trouver un vecteur $x$ pour lequel l'égalité est vérifiée.
   Prenons $x = v_2$ (le vecteur propre associé à $\lambda_2$).
   On a bien $v_2 \perp v_1$, donc $v_2 \perp \mathbf{1}$.
   Le quotient de Rayleigh pour $v_2$ est :
   $R(v_2) = \frac{v_2^T L v_2}{v_2^T v_2} = \frac{v_2^T (\lambda_2 v_2)}{1} = \lambda_2 v_2^T v_2 = \lambda_2$
   Ainsi, le minimum est atteint.

8. **Conclusion Finale :**
   En se rappelant de la forme quadratique fondamentale $x^T L x = \sum_{\{i,j\} \in E} (x_i - x_j)^2$,
   nous pouvons substituer cette expression dans le quotient de Rayleigh. On a $x^T x = \sum_{i=1}^n x_i^2$.
   Par conséquent, la deuxième valeur propre est donnée par :
   $$\lambda_2 = \min_{x \perp \mathbf{1}, x \neq 0} \frac{\sum_{\{i,j\} \in E} (x_i - x_j)^2}{\sum_{i \in V} x_i^2}$$
   Ceci termine la démonstration. Cette valeur $\lambda_2$, appelée trou spectral ou connectivité algébrique (valeur de Fiedler), est intimement liée à la difficulté de couper le graphe en deux morceaux déconnectés, ce qui est le cœur de l'inégalité de Cheeger.
