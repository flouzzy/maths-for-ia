---
title: "Exercice 8 : Quotient de Rayleigh"
difficulty: "★★★★☆"
---
# Exercice 8 : Quotient de Rayleigh

## Énoncé
Soit $E$ un espace euclidien non nul et $f \in \mathcal{L}(E)$ un endomorphisme symétrique.
Pour tout $x \in E \setminus \{0\}$, on définit le quotient de Rayleigh :
$$ R_f(x) = \frac{\langle f(x), x \rangle}{\|x\|^2} $$
1. Démontrer que pour tout $x \neq 0$, $\lambda_{\min} \leq R_f(x) \leq \lambda_{\max}$, où $\lambda_{\min}$ et $\lambda_{\max}$ sont respectivement la plus petite et la plus grande valeur propre de $f$.
2. Montrer que la borne supérieure $\lambda_{\max}$ est atteinte et préciser pour quels vecteurs.

## Correction Zéro Ellipse
**1. Encadrement du quotient de Rayleigh**
Puisque $f$ est un endomorphisme symétrique sur un espace euclidien, le théorème spectral s'applique formellement :
Il existe une base orthonormée $\mathcal{B} = (e_1, e_2, \dots, e_n)$ de $E$ constituée de vecteurs propres de $f$.
Notons $(\lambda_1, \lambda_2, \dots, \lambda_n)$ les valeurs propres associées (elles sont toutes réelles).
On ordonne ces valeurs propres sans perte de généralité : $\lambda_{\min} = \lambda_1 \leq \lambda_2 \leq \dots \leq \lambda_n = \lambda_{\max}$.

Soit un vecteur quelconque $x \in E \setminus \{0\}$.
Puisque $\mathcal{B}$ est une base de $E$, $x$ se décompose de manière unique : $x = \sum_{i=1}^n x_i e_i$.
Calculons la norme au carré de $x$. La base étant orthonormée (théorème de Pythagore généralisé) :
$\|x\|^2 = \sum_{i=1}^n x_i^2$.

Évaluons le numérateur $\langle f(x), x \rangle$.
Calculons d'abord $f(x)$ :
$f(x) = f\left(\sum_{i=1}^n x_i e_i\right) = \sum_{i=1}^n x_i f(e_i) = \sum_{i=1}^n x_i \lambda_i e_i$.
Le produit scalaire devient, toujours grâce à l'orthonormalité de la base $\langle e_i, e_j \rangle = \delta_{i,j}$ :
$\langle f(x), x \rangle = \left\langle \sum_{i=1}^n x_i \lambda_i e_i, \sum_{j=1}^n x_j e_j \right\rangle = \sum_{i=1}^n \lambda_i x_i^2$.

Ainsi, le quotient de Rayleigh s'écrit explicitement :
$R_f(x) = \frac{\sum_{i=1}^n \lambda_i x_i^2}{\sum_{i=1}^n x_i^2}$.

- *Majoration :*
Pour chaque $i$, on a $\lambda_i \leq \lambda_{\max}$. Puisque $x_i^2 \geq 0$, on multiplie sans changer le sens de l'inégalité : $\lambda_i x_i^2 \leq \lambda_{\max} x_i^2$.
En sommant sur $i$ :
$\sum_{i=1}^n \lambda_i x_i^2 \leq \sum_{i=1}^n \lambda_{\max} x_i^2 = \lambda_{\max} \sum_{i=1}^n x_i^2$.
En divisant par $\|x\|^2$ (qui est strictement positif car $x \neq 0$) :
$R_f(x) \leq \frac{\lambda_{\max} \|x\|^2}{\|x\|^2} = \lambda_{\max}$.

- *Minoration :*
De manière totalement symétrique, $\lambda_i \geq \lambda_{\min}$. Donc $\lambda_i x_i^2 \geq \lambda_{\min} x_i^2$.
Par sommation : $\sum_{i=1}^n \lambda_i x_i^2 \geq \lambda_{\min} \sum_{i=1}^n x_i^2$.
En divisant par $\|x\|^2$ : $R_f(x) \geq \lambda_{\min}$.

L'encadrement $\lambda_{\min} \leq R_f(x) \leq \lambda_{\max}$ est démontré pour tout $x \in E \setminus \{0\}$.

**2. Atteinte de la borne supérieure**
La borne $\lambda_{\max}$ est la plus grande valeur propre. Il existe donc au moins un vecteur propre non nul associé à cette valeur propre.
Soit $v \in E_{\lambda_{\max}} \setminus \{0\}$.
Calculons son quotient de Rayleigh :
$R_f(v) = \frac{\langle f(v), v \rangle}{\|v\|^2}$.
Puisque $v$ est vecteur propre pour $\lambda_{\max}$, $f(v) = \lambda_{\max} v$.
Donc $R_f(v) = \frac{\langle \lambda_{\max} v, v \rangle}{\|v\|^2} = \frac{\lambda_{\max} \langle v, v \rangle}{\|v\|^2} = \frac{\lambda_{\max} \|v\|^2}{\|v\|^2} = \lambda_{\max}$.
La borne supérieure est donc bien un maximum, et elle est atteinte par tous les vecteurs propres appartenant au sous-espace propre associé à la plus grande valeur propre.
