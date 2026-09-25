# Exercice 10 : Convergence d'une régularisation par convolution (Mollifier)

**Niveau :** \bigstar\bigstar\bigstar\bigstar\bigstar

**Énoncé :**
Soit $\rho \in \mathcal{C}_c^\infty(\mathbb{R})$ une fonction positive telle que $\int \rho(x) dx = 1$. On pose $\rho_n(x) = n \rho(nx)$.
Soit $f \in L^p(\mathbb{R})$ ($1 \le p < +\infty$). Montrer par densité que $f * \rho_n$ converge vers $f$ dans $L^p(\mathbb{R})$.

**Correction Détaillée :**
1. **Écriture de l'erreur :**
   Puisque $\int \rho_n(y) dy = 1$, on a $f(x) = \int f(x) \rho_n(y) dy$.
   L'erreur est : $(f * \rho_n)(x) - f(x) = \int [f(x-y) - f(x)] \rho_n(y) dy$.
   En posant $z = ny$, on a $(f * \rho_n)(x) - f(x) = \int [f(x-z/n) - f(x)] \rho(z) dz$.

2. **Inégalité de Minkowski pour les intégrales :**
   On a $\|f * \rho_n - f\|_p \le \int \|f(\cdot - z/n) - f(\cdot)\|_p \rho(z) dz$.

3. **Utilisation de la continuité des translations (Exo 5) :**
   Soit $\varepsilon > 0$. Par l'exercice 5, la fonction $h \mapsto \|\tau_h f - f\|_p$ est continue en $0$ et s'y annule.
   De plus, le support de $\rho$ est compact, donc $\rho$ s'annule en dehors d'un intervalle $[-A, A]$.
   Pour $z \in [-A, A]$, le paramètre de translation $h = -z/n$ tend uniformément vers $0$ lorsque $n \to +\infty$.
   Il existe $N$ tel que pour $n \ge N$ et $z \in [-A, A]$, on a $\|f(\cdot - z/n) - f(\cdot)\|_p \le \varepsilon$.

4. **Conclusion :**
   Pour $n \ge N$,
   $\|f * \rho_n - f\|_p \le \int_{-A}^A \varepsilon \rho(z) dz = \varepsilon \int \rho(z) dz = \varepsilon$.
   Donc $\|f * \rho_n - f\|_p \to 0$. C'est le théorème d'approximation par l'unité, garantissant la densité des fonctions $\mathcal{C}^\infty$ dans $L^p$.
