---
uuid: "jalon-69"
title: "Théorème de convergence dominée (TCD)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
next: "[[Jalon 70 (Espaces mesurés produits).md]]"
---

# Jalon 69 : Théorème de convergence dominée (TCD)

## 1. Genèse et Intuition Physique

Le théorème de convergence dominée (TCD) de Lebesgue est sans doute le résultat le plus emblématique et le plus utilisé de toute la théorie de la mesure. Il offre une réponse définitive et élégante au problème de l'interversion de la limite et de l'intégrale.
La théorie de Riemann exigeait une convergence uniforme, une condition souvent trop rigide, notamment en mécanique quantique ou en théorie des probabilités où des singularités isolées apparaissent. Lebesgue a démontré que si toute l'agitation des fonctions $f_n$ est contenue, en valeur absolue, sous une enveloppe mesurable et intégrable $g$, alors l'interversion est valide, indépendamment des variations microscopiques locales.

## 2. Définitions, Théorèmes et Exemples

### Théorème de Lebesgue (TCD)

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables à valeurs réelles ou complexes.
Supposons que :
1. La suite $(f_n)$ converge presque partout vers une fonction $f$.
2. Il existe une fonction $g : X \to [0, +\infty]$ **intégrable** (i.e. $\int g d\mu < +\infty$) telle que :
   $$\forall n \in \mathbb{N}, \quad |f_n| \le g \quad \text{presque partout.}$$

Alors :
- $f$ est intégrable sur $X$.
- $\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$.
- $\lim_{n \to \infty} \int_X |f_n - f| d\mu = 0$ (Convergence dans $L^1$).

### Exemples Concrets et Immédiats

**Exemple 1 : L'enveloppe exponentielle**
Soit $f_n(x) = e^{-x} \cos(nx)$ sur $X = [0, +\infty[$.
On a $|f_n(x)| \le e^{-x} = g(x)$. La fonction $g(x) = e^{-x}$ est intégrable (intégrale valant 1).
Bien que $\cos(nx)$ n'ait pas de limite simple, cet exemple illustre la notion de domination.

```tikz
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.5,0) -- (6,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,3) node[above] {$y$};
\draw[blue, thick, domain=0:5, samples=100] plot (\x, {2*exp(-\x)});
\draw[red, dashed, domain=0:5, samples=100] plot (\x, {2*exp(-\x)*cos(5*\x r)});
\node[blue, above right] at (1, 0.7) {$g(x)$};
\node[red, below] at (2, -0.3) {$f_n(x)$};
\end{tikzpicture}
\end{center}
```

**Exemple 2 : Calcul avec domination**
La limite simple de $f_n(x) = \frac{n\sin(x/n)}{x(1+x^2)}$ est $\frac{1}{1+x^2}$.
Domination : $|f_n(x)| \le \frac{x/n \cdot n}{x(1+x^2)} = \frac{1}{1+x^2}$.
La fonction $g(x) = \frac{1}{1+x^2}$ est intégrable sur $\mathbb{R}$, son intégrale est $\pi$.

**Exemple 3 : Défaut de domination (la bosse glissante)**
Soit $f_n(x) = n \mathbf{1}_{]0, 1/n[}(x)$ sur $]0, 1[$.
Limite simple : $\forall x \in ]0, 1[, \lim f_n(x) = 0$.
Mais $\int_0^1 f_n(x) dx = n \times \frac{1}{n} = 1$. L'intégrale de la limite est 0.
Pourquoi ? Car le supremum sur $n$ est $g(x) = \sup_n f_n(x) \approx 1/x$, qui n'est pas intégrable en 0. L'hypothèse de domination n'est pas satisfaite.

**Exemple 4 : Fonctions puissances**
$f_n(x) = x^n$ sur $[0, 1[$.
Limite simple $f(x) = 0$.
Domination : $|f_n(x)| \le 1$. La constante 1 est intégrable sur le segment de longueur 1.
L'intégrale est $\lim \frac{1}{n+1} = 0 = \int 0 dx$.

**Exemple 5 : Paramètre de chaleur**
$f_n(x) = e^{-nx^2}$ sur $]0, 1[$.
Limite simple $0$. Domination : $|f_n(x)| \le e^{-x^2} \le 1$, intégrable sur $]0, 1[$.

**Exemple 6 : Oscillation amortie**
Soit $f_n(x) = \frac{\sin(nx)}{x^2+n^2}$ sur $\mathbb{R}$.
Limite simple : $0$.
Domination : $|f_n(x)| \le \frac{1}{n^2} \le \frac{1}{1}$ pour $n \ge 1$, mais ce n'est pas intégrable sur $\mathbb{R}$.
Une meilleure domination pour $n \ge 1$ : $|f_n(x)| \le \frac{1}{x^2+1}$. La fonction $g(x) = \frac{1}{x^2+1}$ est intégrable sur $\mathbb{R}$.
L'intégrale limite est 0.

**Exemple 7 : Suite de fonctions de Dirac**
Soit $f_n(x) = \frac{n}{\sqrt{\pi}} e^{-n^2x^2}$ sur $\mathbb{R}$.
La limite simple est 0 presque partout (pour $x \ne 0$).
Cependant, l'intégrale de chaque $f_n$ vaut 1.
L'intégrale de la limite vaut 0.
Il n'y a pas de fonction intégrable $g$ qui domine tous les $f_n$.

**Exemple 8 : Convergence $L^1$**
Soit $f_n(x) = \frac{1}{1+x^n}$ sur $[0, 1]$.
La limite simple est $f(x) = 1$ pour $x < 1$, et $f(1) = 1/2$.
Presque partout, $f_n \to 1$.
Domination : $|f_n(x)| \le 1 = g(x)$, intégrable sur $[0, 1]$.
Ainsi, $\int_0^1 \frac{1}{1+x^n} dx \to \int_0^1 1 dx = 1$.

## 3. Démonstrations

La démonstration s'appuie sur le lemme de Fatou, déjà étudié (Jalon 68).

1. **Intégrabilité de f :**
   Puisque $|f_n| \le g$ presque partout, en passant à la limite (la fonction valeur absolue étant continue), on obtient $|f| \le g$ presque partout. Par monotonie de l'intégrale et l'hypothèse $\int g d\mu < \infty$, on conclut que $\int |f| d\mu < \infty$. Donc $f$ est intégrable.

2. **Première application de Fatou (Minoration) :**
   Considérons la suite de fonctions $h_n = g + f_n$. Par l'hypothèse de domination, $f_n \ge -g$, donc $h_n \ge 0$.
   Appliquons le lemme de Fatou aux $(h_n)$ :
   $$\int \liminf_{n \to \infty} (g + f_n) d\mu \le \liminf_{n \to \infty} \int (g + f_n) d\mu$$
   Puisque $f_n \to f$ p.p., $\liminf (g + f_n) = g + f$.
   Ainsi, $\int (g + f) d\mu \le \int g d\mu + \liminf \int f_n d\mu$.
   Comme $g$ est intégrable, $\int g d\mu$ est un nombre fini, on peut le soustraire :
   $$\int f d\mu \le \liminf_{n \to \infty} \int f_n d\mu$$

3. **Seconde application de Fatou (Majoration) :**
   Considérons la suite $k_n = g - f_n$. Par domination, $f_n \le g$, donc $k_n \ge 0$.
   De même, avec Fatou :
   $$\int \liminf_{n \to \infty} (g - f_n) d\mu \le \liminf_{n \to \infty} \int (g - f_n) d\mu$$
   $$\int (g - f) d\mu \le \int g d\mu - \limsup_{n \to \infty} \int f_n d\mu$$
   En soustrayant à nouveau $\int g d\mu$ :
   $$-\int f d\mu \le -\limsup_{n \to \infty} \int f_n d\mu \implies \limsup_{n \to \infty} \int f_n d\mu \le \int f d\mu$$

4. **Conclusion :**
   Des étapes 2 et 3, on déduit l'encadrement :
   $$\limsup_{n \to \infty} \int f_n d\mu \le \int f d\mu \le \liminf_{n \to \infty} \int f_n d\mu$$
   Puisque l'on a toujours $\liminf \le \limsup$, toutes ces valeurs doivent être strictement égales.
   La limite des intégrales existe donc et coïncide avec l'intégrale de la limite. La convergence $L^1$ s'obtient en appliquant ce même raisonnement à la suite $|f_n - f|$ dominée par $2g$.

## 4. Applications en Physique, Logique et AI

- **Théorie des Probabilités :** Le TCD justifie le passage à la limite sous le signe d'espérance mathématique. Si une suite de variables aléatoires $X_n$ converge p.s. vers $X$, et si elles sont dominées par une variable $Y$ d'espérance finie, alors $\mathbb{E}[X_n] \to \mathbb{E}[X]$.
- **Apprentissage Automatique (Machine Learning) :**
    - **Convergence du Gradient Stochastique (SGD) :** Pour prouver que le gradient stochastique calculé sur des mini-lots converge vers le gradient réel de la fonction de perte théorique, le TCD garantit que la dérivation (qui est une limite) peut traverser l'espérance (qui est une intégrale), à condition que la variance des gradients soit dominée.
    - **Auto-encodeurs Variationnels (VAE) :** La maximisation de l'ELBO nécessite de calculer des gradients d'espérances. Le *Reparameterization Trick* déplace le gradient sous l'intégrale, une opération formellement sécurisée par le TCD.
- **Mécanique Statistique :** Le calcul des fonctions de partition implique des sommes et intégrales sur des états énergétiques. Le TCD valide les dérivations thermodynamiques (calcul d'entropie, chaleur spécifique) par rapport à la température.
