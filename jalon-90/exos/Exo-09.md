# Exercice 9 : Convergence en loi d'une somme de variables uniformes vers une Gaussienne
$\bigstar\bigstar\bigstar\bigstar\bigstar$


Considérons une suite $(U_n)$ de variables indépendantes et identiquement distribuées, suivant une loi uniforme sur $[-1, 1]$.
Posons $S_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n U_i$.
1. Calculez la variance de $U_1$.
2. En anticipant sur le Théorème Central Limite, donnez de manière rigoureuse la loi limite de la suite $Z_n = \sqrt{3} S_n$. Comment s'écrit formellement cette convergence ?

**Correction :**
1. La variable $U_1$ suit une distribution uniforme sur l'intervalle $[a, b] = [-1, 1]$.
Son espérance est $\mathbb{E}[U_1] = \frac{a+b}{2} = 0$.
Sa variance s'obtient par la formule générale $\mathbb{V}(U_1) = \frac{(b-a)^2}{12} = \frac{2^2}{12} = \frac{4}{12} = \frac{1}{3}$.
Une preuve intégrale donne : $\mathbb{E}[U_1^2] = \int_{-1}^{1} x^2 \frac{1}{2} dx = \frac{1}{2} \left[\frac{x^3}{3}\right]_{-1}^1 = \frac{1}{2} \left(\frac{1}{3} - \frac{-1}{3}\right) = \frac{1}{3}$.
2. Soit $\mu = \mathbb{E}[U_1] = 0$ et $\sigma^2 = \mathbb{V}(U_1) = 1/3$.
Le Théorème Central Limite (TCL) stipule que pour une somme de i.i.d., la variable centrée réduite converge en loi vers une loi normale standard $\mathcal{N}(0, 1)$.
La variable somme centrée réduite classique est $T_n = \frac{\sum_{i=1}^n U_i - n\mu}{\sqrt{n \sigma^2}}$.
Ici, $\mu = 0$ et $\sigma^2 = 1/3$, donc $T_n = \frac{\sum_{i=1}^n U_i}{\sqrt{n / 3}} = \frac{\sqrt{3}}{\sqrt{n}} \sum_{i=1}^n U_i = \sqrt{3} S_n = Z_n$.
Le TCL nous affirme donc directement que :
$$ Z_n \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1) $$
Formellement, cela s'écrit sur les fonctions de répartition : si $F_n(x) = \mathbb{P}(Z_n \leq x)$, et $\Phi(x)$ est la fonction de répartition de la loi normale, on a $\forall x \in \mathbb{R}, \lim_{n \to \infty} F_n(x) = \Phi(x)$.
