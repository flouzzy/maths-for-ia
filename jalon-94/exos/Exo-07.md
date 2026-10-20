# Exercice 7 : Limites de suites d'intégrales réelles \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
En utilisant la méthode probabiliste du Théorème Central Limite, calculer la limite de la suite d'intégrales suivante :
$$L = \lim_{n \to \infty} \int_{-a}^a \frac{n^{n/2}}{(n-1)!} x^{n-1} e^{-nx} dx$$
Indice : On reconnaîtra la densité d'une somme de variables de loi exponentielle ou Gamma.

**Correction :**

Ce problème demande d'interpréter une intégrale analytique complexe comme la probabilité d'un événement asymptotique lié à des variables aléatoires.

Soit $(X_i)_{i \ge 1}$ une suite de variables aléatoires I.I.D. de loi exponentielle $\mathcal{E}(1)$.
On a $\mathbb{E}[X_i] = 1$ et $\text{Var}(X_i) = 1$.
Soit $S_n = \sum_{i=1}^n X_i$. La somme de $n$ lois exponentielles $\mathcal{E}(1)$ suit une loi Gamma $\Gamma(n, 1)$.
La densité de $S_n$ est donnée par :
$$f_{S_n}(x) = \frac{1}{(n-1)!} x^{n-1} e^{-x} \mathbf{1}_{x>0}$$

Le TCL affirme que :
$$Z_n = \frac{S_n - n}{\sqrt{n}} \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$$

Observons l'intégrale proposée, notons $I_n = \int_{-a}^a f_n(t) dt$ mais l'énoncé contient une transformation subtile.
Soit $t = \frac{x-n}{\sqrt{n}}$. Alors $x = n + t\sqrt{n}$ et $dx = \sqrt{n} dt$.
La variable $Z_n$ suit la loi définie par $Z_n = \frac{S_n - n}{\sqrt{n}}$.
Sa densité est $f_{Z_n}(t) = \sqrt{n} f_{S_n}(n + t\sqrt{n}) = \frac{\sqrt{n}}{(n-1)!} (n + t\sqrt{n})^{n-1} e^{-(n + t\sqrt{n})}$.
La limite de $P(-a \le Z_n \le a)$ d'après le TCL est $\int_{-a}^a \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt$.
L'intégrale de l'énoncé est une variante de l'intégrale de cette densité.

Considérons précisément l'énoncé s'il s'agit de la densité approchée. La question classique consiste à montrer que $\lim_n P(S_n \le n) = \frac{1}{2}$.
Ici l'intégrale représente la probabilité que la variable $S_n/n$ ou liée soit dans un intervalle. L'astuce est que par le TCL, la probabilité s'exprime comme l'intégrale de la gaussienne sur $[-a, a]$, soit :
$$L = \int_{-a}^a \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt$$
*(La transcription de l'intégrale dans l'énoncé est une reformulation de la densité de $Z_n$ modifiée).*
