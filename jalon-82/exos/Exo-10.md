# Exercice 10 : Indépendance de la base et convergence singulière

\subsection*{Exercice 10 : Indépendance de la base et convergence singulière \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Soit $T_n(x) = e^{inx}$. Montrer que $T_n$ converge vers 0 au sens des distributions.

**Démonstration pas à pas :**
1. **Action d'une exponentielle oscillante :** Pour $\phi \in \mathcal{D}(\mathbb{R})$ :
   $$ \langle T_n, \phi \rangle = \int_{-\infty}^{+\infty} e^{inx} \phi(x) dx $$
2. **Lemme de Riemann-Lebesgue :** La fonction test $\phi$ est de classe $C^\infty$ et à support compact, donc elle appartient à $L^1(\mathbb{R})$.
   L'intégrale $\int e^{inx} \phi(x) dx$ est exactement la transformée de Fourier de $\phi$ évaluée en $-n$.
   D'après le lemme de Riemann-Lebesgue, pour toute fonction $L^1$, sa transformée de Fourier tend vers 0 à l'infini.
   Ainsi, $\lim_{n \to \pm \infty} \int e^{inx} \phi(x) dx = 0$.
3. **Intégration par parties alternative :** On peut aussi intégrer par parties. $e^{inx} = \frac{1}{in} \frac{d}{dx} (e^{inx})$.
   $$ \int e^{inx} \phi(x) dx = \left[ \frac{1}{in} e^{inx} \phi(x) \right]_{-\infty}^{+\infty} - \frac{1}{in} \int e^{inx} \phi'(x) dx $$
   Le terme de bord est nul car $\phi$ est à support compact. L'intégrale est majorée par $\frac{1}{n} \int |\phi'(x)| dx$, qui tend clairement vers 0.
   La convergence dans $\mathcal{D}'(\mathbb{R})$ est démontrée. $\blacksquare$
