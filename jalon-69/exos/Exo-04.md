## Exercice 4 : Intégrabilité et continuité de la transformée de Fourier \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in \mathcal{L}^1(\mathbb{R})$. On définit sa transformée de Fourier par $\hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-i \xi x} dx$.
Montrer à l'aide du TCD que $\hat{f}$ est une fonction continue sur $\mathbb{R}$.

**Correction :**
Soit $\xi_0 \in \mathbb{R}$ et $(\xi_n)$ une suite convergeant vers $\xi_0$.
Considérons les fonctions $g_n(x) = f(x) e^{-i \xi_n x}$.
1. **Convergence simple :** Comme l'exponentielle complexe est continue, pour tout $x \in \mathbb{R}$, on a :
   $\lim_{n \to \infty} g_n(x) = f(x) e^{-i \xi_0 x}$.
2. **Domination :** On a $|g_n(x)| = |f(x)| |e^{-i \xi_n x}| = |f(x)| \times 1 = |f(x)|$.
   Comme $f \in \mathcal{L}^1(\mathbb{R})$, la fonction $|f|$ est intégrable sur $\mathbb{R}$ et indépendante de $n$. Elle constitue une fonction dominatrice parfaite.
3. **Conclusion :** D'après le TCD, on peut intervertir limite et intégrale :
   $\lim_{n \to \infty} \hat{f}(\xi_n) = \lim_{n \to \infty} \int_{\mathbb{R}} g_n(x) dx = \int_{\mathbb{R}} \lim_{n \to \infty} g_n(x) dx = \int_{\mathbb{R}} f(x) e^{-i \xi_0 x} dx = \hat{f}(\xi_0)$.
   Ceci prouve que $\hat{f}$ est séquentiellement continue en tout point, et donc continue.
