# Exercice 6 : Non-implication P implique p.s. : un cas subtil
$\bigstar\bigstar\bigstar\star\star$


Soit l'espace $\Omega = [0, 1]$ avec la mesure de Lebesgue. On définit les intervalles $I_{n,k} = [\frac{k-1}{n}, \frac{k}{n}]$ pour $n \in \mathbb{N}^*$ et $1 \leq k \leq n$. On énumère ces intervalles dans l'ordre : $I_1 = I_{1,1}$, $I_2 = I_{2,1}, I_3 = I_{2,2}$, etc.
Soit la variable aléatoire $X_m(\omega) = \mathbf{1}_{I_m}(\omega)$.
1. Montrez que $X_m$ converge en probabilité vers $0$.
2. Montrez de façon rigoureuse que la limite $\lim_{m\to\infty} X_m(\omega)$ n'existe pour aucun $\omega \in [0,1]$.
3. Quelle implication théorique des modes de convergence cet exemple illustre-t-il ?

**Correction :**
1. Soit $\epsilon \in ]0, 1[$. La probabilité $\mathbb{P}(|X_m - 0| > \epsilon)$ équivaut à la mesure de l'intervalle $I_m$. Si $m$ correspond à un certain rang $n$, sa longueur est $\frac{1}{n}$. Comme $n \to \infty$ quand $m \to \infty$, la mesure tend vers $0$. Donc $X_m \xrightarrow{\mathbb{P}} 0$.
2. Fixons un $\omega \in [0, 1]$. Pour chaque cycle de longueur $n$, la collection des intervalles $(I_{n,k})_{1\le k\le n}$ recouvre intégralement $[0, 1]$. Ainsi, pour chaque $n$, il existe au moins un entier $k$ tel que $\omega \in I_{n,k}$, ce qui donne $X_m(\omega) = 1$. Mais pour d'autres intervalles du même cycle (si $n > 1$), $\omega$ n'y est pas, donc $X_{m'}(\omega) = 0$. La suite $(X_m(\omega))_{m\in\mathbb{N}}$ ne fait qu'alterner entre $0$ et $1$ indéfiniment. Elle ne peut converger.
3. Cet exemple prouve définitivement que la réciproque de "$X_n \xrightarrow{\text{p.s.}} X \implies X_n \xrightarrow{\mathbb{P}} X$" est fausse. La convergence en probabilité n'exige aucune monotonie trajectorielle, contrairement à la convergence presque sûre.
