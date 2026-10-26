# Exercice 2 : La fuite de masse vers l'infini
$\bigstar\star\star\star\star$


Soit $(\Omega, \mathcal{F}, \mathbb{P})$ l'espace de probabilité mesuré avec $\Omega = \mathbb{R}$ et une loi telle que la densité d'une variable soit étudiée de la manière suivante. On considère la suite de variables $X_n$ telle que $\mathbb{P}(X_n = n) = \frac{1}{n}$ et $\mathbb{P}(X_n = 0) = 1 - \frac{1}{n}$.
1. Étudiez la convergence en probabilité de la suite $(X_n)$.
2. Étudiez la convergence dans $L^1$ de la suite $(X_n)$. La limite est-elle identique ? Pourquoi ?

**Correction :**
1. Fixons un $\epsilon > 0$. On a $\mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P}(X_n = n) = \frac{1}{n}$ car, pour $n$ assez grand, $n > \epsilon$. Comme $\lim_{n\to\infty}\frac{1}{n} = 0$, alors la suite $X_n$ converge en probabilité vers la constante $0$.
2. Pour la convergence $L^1$, on calcule l'espérance de l'écart :
$$ \mathbb{E}[|X_n - 0|] = n \cdot \mathbb{P}(X_n = n) + 0 \cdot \mathbb{P}(X_n = 0) = n \cdot \frac{1}{n} + 0 = 1 $$
La suite de ces espérances vaut constamment $1$, sa limite est donc $1 \neq 0$. La suite ne converge donc pas vers $0$ dans l'espace $L^1$. Cela montre qu'il y a une fuite de masse : les valeurs extrêmes deviennent si importantes qu'elles empêchent la convergence en moyenne.
