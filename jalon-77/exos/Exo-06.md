# Exercice 6 : Lemme de Riemann-Lebesgue (version $L^1$)

**Niveau :** \bigstar\bigstar\bigstar\bigstar\star

**Énoncé :**
Soit $f \in L^1(\mathbb{R})$. Montrer par un argument de densité que :
$\lim_{n \to +\infty} \int_{\mathbb{R}} f(x) \sin(nx) dx = 0$.

**Correction Détaillée :**
1. **Cas d'une indicatrice d'intervalle :**
   Soit $f = \mathbf{1}_{[a, b]}$.
   L'intégrale vaut $\int_a^b \sin(nx) dx = \left[ -\frac{\cos(nx)}{n} \right]_a^b = \frac{\cos(na) - \cos(nb)}{n}$.
   Comme le numérateur est borné par $2$, la limite quand $n \to +\infty$ est $0$.

2. **Cas d'une fonction étagée :**
   Toute fonction étagée intégrable (qui peut s'écrire comme somme d'indicatrices d'intervalles disjoints par approximation mesurable) vérifie la propriété par linéarité.
   Soit $s = \sum_{k=1}^m \alpha_k \mathbf{1}_{I_k}$.
   $\int s(x) \sin(nx) dx = \sum \alpha_k \int_{I_k} \sin(nx) dx \to 0$.

3. **Cas général par densité :**
   Soit $f \in L^1(\mathbb{R})$ et $\varepsilon > 0$.
   Il existe une fonction en escalier $s \in L^1(\mathbb{R})$ telle que $\|f - s\|_1 \le \frac{\varepsilon}{2}$.
   Majorons la différence des intégrales :
   $\left| \int f(x)\sin(nx) dx - \int s(x)\sin(nx) dx \right| \le \int |f(x) - s(x)| |\sin(nx)| dx$.
   Comme $|\sin(nx)| \le 1$, cette erreur est bornée par $\|f - s\|_1 \le \frac{\varepsilon}{2}$.
   Par ailleurs, il existe $N \in \mathbb{N}$ tel que pour $n \ge N$, $\left| \int s(x)\sin(nx) dx \right| \le \frac{\varepsilon}{2}$.
   Alors pour $n \ge N$, $\left| \int f(x)\sin(nx) dx \right| \le \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$.
   La propriété (Théorème de Riemann-Lebesgue) est prouvée.
