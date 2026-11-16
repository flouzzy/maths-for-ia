# Exercice 1 : Convergence presque sûre vs en probabilité (Cas déterministe)

Niveau : $\bigstar\star\star\star\star$

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé. Considérons une suite de variables aléatoires $(X_n)_{n \in \mathbb{N}}$ constantes, telles que pour tout $n \in \mathbb{N}$ et tout $\omega \in \Omega$, $X_n(\omega) = \frac{1}{n+1}$.
Montrer que $X_n \xrightarrow{\text{p.s.}} 0$ et $X_n \xrightarrow{\mathbb{P}} 0$.

## Correction

**1. Convergence presque sûre :**
Soit $\omega \in \Omega$. On a $X_n(\omega) = \frac{1}{n+1}$.
Puisque $\lim_{n \to +\infty} \frac{1}{n+1} = 0$, la suite $(X_n(\omega))$ converge vers $0$ pour tout $\omega \in \Omega$.
Ainsi, l'ensemble de convergence $\{ \omega \in \Omega \mid \lim_{n \to +\infty} X_n(\omega) = 0 \}$ est exactement $\Omega$.
Or $\mathbb{P}(\Omega) = 1$, donc $X_n \xrightarrow{\text{p.s.}} 0$.

**2. Convergence en probabilité :**
Soit $\varepsilon > 0$. On cherche à évaluer $\mathbb{P}(|X_n - 0| > \varepsilon) = \mathbb{P}\left(\frac{1}{n+1} > \varepsilon\right)$.
Puisque $\varepsilon > 0$ est fixé, il existe un rang $N \in \mathbb{N}$ tel que pour tout $n \ge N$, on a $\frac{1}{n+1} \le \varepsilon$.
Par conséquent, pour tout $n \ge N$, l'événement $\left\{ \frac{1}{n+1} > \varepsilon \right\}$ est l'ensemble vide $\emptyset$.
Donc pour tout $n \ge N$, $\mathbb{P}(|X_n - 0| > \varepsilon) = \mathbb{P}(\emptyset) = 0$.
Ainsi, $\lim_{n \to +\infty} \mathbb{P}(|X_n - 0| > \varepsilon) = 0$, ce qui prouve que $X_n \xrightarrow{\mathbb{P}} 0$.
(On retrouve d'ailleurs le théorème général : la convergence presque sûre implique la convergence en probabilité).
