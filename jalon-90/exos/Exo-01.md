# Exercice 1 : Convergence certaine vs convergence presque sûre
$\bigstar\star\star\star\star$


On considère l'espace de probabilité continu $(\Omega, \mathcal{F}, \mathbb{P})$ où $\Omega = [0, 1]$ muni de la mesure de Lebesgue et de sa tribu des boréliens. On définit une suite de variables aléatoires par $X_n(\omega) = \frac{\omega}{n}$.
1. Étudiez la convergence de la suite $(X_n(\omega))_{n\in\mathbb{N}}$ pour un $\omega \in [0, 1]$ fixé.
2. Montrez que $X_n$ converge uniformément sur $\Omega$.
3. Conclure quant à la convergence presque sûre et la convergence en probabilité de cette suite.

**Correction :**
1. Soit $\omega \in [0, 1]$ fixé. La suite numérique réelle $\left(\frac{\omega}{n}\right)_{n\in\mathbb{N}}$ tend vers $0$ lorsque $n$ tend vers l'infini, car $\lim_{n\to\infty}\frac{1}{n}=0$ et $\omega$ est une constante.
2. La convergence est uniforme. En effet, $\sup_{\omega\in[0,1]}|X_n(\omega) - 0| = \sup_{\omega\in[0,1]}\frac{\omega}{n} = \frac{1}{n}$. Puisque $\lim_{n\to\infty}\frac{1}{n} = 0$, la suite converge uniformément vers la variable aléatoire nulle.
3. La convergence certaine (pour tout $\omega$) implique la convergence presque sûre, qui implique à son tour la convergence en probabilité. Ainsi, $X_n \xrightarrow{\text{p.s.}} 0$ et $X_n \xrightarrow{\mathbb{P}} 0$.
