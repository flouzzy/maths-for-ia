---
title: "Exercice 10 : Théorème de Courant-Fischer (Min-Max)"
difficulty: "★★★★★"
---
# Exercice 10 : Théorème de Courant-Fischer (Min-Max)

## Énoncé
Soit $E$ un espace euclidien de dimension $n$, et $f \in \mathcal{L}(E)$ un endomorphisme symétrique.
Soient $\lambda_1 \leq \lambda_2 \leq \dots \leq \lambda_n$ les valeurs propres de $f$ triées par ordre croissant, et $(e_1, \dots, e_n)$ la base orthonormée associée.
Démontrer le théorème min-max de Courant-Fischer, qui caractérise la $k$-ième valeur propre $\lambda_k$ ($1 \leq k \leq n$) de manière purement géométrique :
$$ \lambda_k = \min_{V, \dim(V)=k} \left( \max_{x \in V, x \neq 0} \frac{\langle f(x), x \rangle}{\|x\|^2} \right) $$
où le minimum est pris sur tous les sous-espaces vectoriels $V$ de $E$ de dimension exacte $k$.

## Correction Zéro Ellipse
Ce théorème vertigineux donne une construction topologique des valeurs propres sans avoir besoin de calculer le polynôme caractéristique.

**Étape 1 : Borner supérieurement le max interne pour un sous-espace très spécifique.**
Considérons un sous-espace particulier : l'espace engendré par les $k$ premiers vecteurs propres.
Soit $W_k = \text{Vect}(e_1, e_2, \dots, e_k)$.
La dimension de $W_k$ est exactement $k$ car la famille est une base orthonormée.
Pour tout vecteur $x \in W_k \setminus \{0\}$, $x$ se décompose en $x = \sum_{i=1}^k x_i e_i$.
Calculons le quotient de Rayleigh sur cet espace :
$$ R_f(x) = \frac{\langle f(x), x \rangle}{\|x\|^2} = \frac{\sum_{i=1}^k \lambda_i x_i^2}{\sum_{i=1}^k x_i^2} $$
Puisque les valeurs propres sont ordonnées $\lambda_1 \leq \dots \leq \lambda_k \leq \dots \leq \lambda_n$, pour tout $i \leq k$, on a $\lambda_i \leq \lambda_k$.
On peut donc majorer brutalement :
$$ \sum_{i=1}^k \lambda_i x_i^2 \leq \sum_{i=1}^k \lambda_k x_i^2 = \lambda_k \sum_{i=1}^k x_i^2 $$
En divisant par $\|x\|^2 = \sum_{i=1}^k x_i^2 > 0$, on obtient :
$$ \forall x \in W_k \setminus \{0\}, \quad R_f(x) \leq \lambda_k $$
Or, si on prend le vecteur spécifique $x = e_k \in W_k$, on obtient $R_f(e_k) = \frac{\langle \lambda_k e_k, e_k \rangle}{\|e_k\|^2} = \lambda_k$.
Le maximum du quotient sur ce sous-espace particulier est donc *exactement* atteint et vaut $\lambda_k$ :
$$ \max_{x \in W_k, x \neq 0} R_f(x) = \lambda_k $$
Puisque le minimum sur TOUS les sous-espaces de dimension $k$ doit être inférieur ou égal à la valeur obtenue pour un sous-espace particulier ($W_k$), on en déduit formellement que :
$$ \min_{\dim(V)=k} \left( \max_{x \in V, x \neq 0} R_f(x) \right) \leq \lambda_k $$

**Étape 2 : Borner inférieurement pour n'importe quel sous-espace.**
Il s'agit maintenant de montrer que pour n'importe quel sous-espace arbitraire $V$ de dimension $k$, le maximum de $R_f(x)$ sur ce $V$ est nécessairement supérieur ou égal à $\lambda_k$.
Soit $V$ un sous-espace vectoriel quelconque de $E$ de dimension $\dim(V) = k$.
Considérons un autre sous-espace construit à partir des "grandes" valeurs propres :
$U_{n-k+1} = \text{Vect}(e_k, e_{k+1}, \dots, e_n)$.
La dimension de cet espace est $(n) - (k) + 1 = n - k + 1$.
Nous avons deux sous-espaces de $E$ : $V$ et $U_{n-k+1}$.
Utilisons la formule de Grassmann pour la dimension de l'intersection :
$\dim(V \cap U_{n-k+1}) = \dim(V) + \dim(U_{n-k+1}) - \dim(V + U_{n-k+1})$.
Remplaçons les dimensions connues :
$\dim(V \cap U_{n-k+1}) = k + (n - k + 1) - \dim(V + U_{n-k+1}) = n + 1 - \dim(V + U_{n-k+1})$.
Puisque $V + U_{n-k+1}$ est un sous-espace de $E$ (qui est de dimension $n$), sa dimension maximale est $n$.
Donc $\dim(V + U_{n-k+1}) \leq n$.
On en déduit que $\dim(V \cap U_{n-k+1}) \geq n + 1 - n = 1$.
Il y a donc obligatoirement une intersection non triviale ! Il existe un vecteur $v \in V \cap U_{n-k+1}$ tel que $v \neq 0$.
Puisque ce vecteur $v$ appartient à $U_{n-k+1}$, il s'écrit uniquement à l'aide des vecteurs de base de $e_k$ à $e_n$ :
$v = \sum_{i=k}^n v_i e_i$.
Calculons le quotient de Rayleigh pour ce vecteur d'intersection :
$$ R_f(v) = \frac{\sum_{i=k}^n \lambda_i v_i^2}{\sum_{i=k}^n v_i^2} $$
Puisque l'indice de sommation commence à $k$, pour tous les termes on a $i \geq k \implies \lambda_i \geq \lambda_k$.
On peut donc minorer brutalement :
$$ \sum_{i=k}^n \lambda_i v_i^2 \geq \sum_{i=k}^n \lambda_k v_i^2 = \lambda_k \sum_{i=k}^n v_i^2 $$
En divisant par $\|v\|^2$, on obtient $R_f(v) \geq \lambda_k$.
Nous avons donc trouvé au moins UN vecteur non nul $v \in V$ dont le quotient de Rayleigh est $\geq \lambda_k$.
Le MAXIMUM sur tout l'espace $V$ doit donc être au moins aussi grand que cette valeur ponctuelle :
$$ \max_{x \in V, x \neq 0} R_f(x) \geq R_f(v) \geq \lambda_k $$
Ce résultat est vrai pour N'IMPORTE QUEL sous-espace $V$ de dimension $k$.
Le minimum de toutes ces valeurs maximales (le min-max) doit donc aussi être au moins $\lambda_k$ :
$$ \min_{\dim(V)=k} \left( \max_{x \in V, x \neq 0} R_f(x) \right) \geq \lambda_k $$

**Étape 3 : Conclusion par double inégalité**
Nous avons formellement prouvé :
1. $\text{Min-Max} \leq \lambda_k$
2. $\text{Min-Max} \geq \lambda_k$
Par antisymétrie de l'ordre sur $\mathbb{R}$, on conclut à l'égalité parfaite :
$$ \min_{\dim(V)=k} \max_{x \in V, x \neq 0} R_f(x) = \lambda_k $$
Ce résultat magistral clôt la démonstration rigoureuse sans la moindre ellipse.
