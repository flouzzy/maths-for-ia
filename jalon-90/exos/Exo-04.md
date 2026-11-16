# Exercice 4 : Convergence en probabilité sans convergence p.s.

Niveau : $\bigstar\bigstar\bigstar\star\star$

Sur $\Omega = [0, 1]$ muni de la mesure de Lebesgue et de la tribu borélienne, on définit une suite $(X_n)$ d'indicatrices d'intervalles $A_n$ de longueurs $\frac{1}{n}$. On pose $X_n = \mathbb{1}_{A_n}$ où la suite $(A_n)$ ne tend pas vers l'ensemble vide mais passe indéfiniment sur tout $[0, 1]$.
Concrètement, soit $A_1 = [0, 1]$, $A_2 = [0, \frac{1}{2}]$, $A_3 = [\frac{1}{2}, 1]$, $A_4 = [0, \frac{1}{3}], \dots$
Montrer que $X_n \xrightarrow{\mathbb{P}} 0$ mais que $X_n$ ne converge presque sûrement pour aucun point de $[0, 1]$.

## Correction

**1. Convergence en probabilité :**
Soit $\varepsilon \in ]0, 1[$. On a $\mathbb{P}(|X_n - 0| > \varepsilon) = \mathbb{P}(X_n = 1) = \mathbb{P}(A_n)$.
Par construction, pour un entier $n$ appartenant au "bloc" de division en $k$ parties, la longueur de l'intervalle $A_n$ est $\frac{1}{k}$.
Plus précisément, si $n$ est grand, $k$ est grand, donc $\mathbb{P}(A_n) \to 0$ lorsque $n \to +\infty$.
Ainsi, $\lim_{n \to +\infty} \mathbb{P}(|X_n - 0| > \varepsilon) = 0$, d'où $X_n \xrightarrow{\mathbb{P}} 0$.

**2. Non-convergence presque sûre :**
Soit $\omega \in [0, 1]$. Par construction, la suite $(A_n)$ balaie indéfiniment l'intervalle $[0, 1]$.
Par conséquent, $\omega$ appartient à une infinité d'intervalles $A_n$. Pour cette sous-suite d'indices, $X_n(\omega) = 1$.
D'autre part, $\omega$ n'appartient pas à une infinité d'autres intervalles $A_n$ (car la longueur tend vers 0). Pour cette autre sous-suite, $X_n(\omega) = 0$.
La suite $(X_n(\omega))$ alterne donc une infinité de fois entre 0 et 1.
Elle ne converge donc vers aucune limite pour *aucun* $\omega \in [0, 1]$.
Ainsi, l'ensemble des $\omega$ où $X_n(\omega)$ converge est l'ensemble vide, dont la probabilité est 0, et non 1.
Ceci démontre que la convergence en probabilité n'implique pas la convergence presque sûre en général.
