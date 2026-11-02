**Exercice 4**

Soit $H = L^2([0, 1])$ l'espace de Hilbert des fonctions de carré intégrable sur l'intervalle $[0, 1]$, muni du produit scalaire $\langle f, g \rangle = \int_0^1 f(x) \overline{g(x)} dx$. Pour des fonctions à valeurs réelles, ce produit scalaire devient $\langle f, g \rangle = \int_0^1 f(x) g(x) dx$.

Nous considérons la famille de fonctions $(e_n)_{n \in \mathbb{N}^*}$ définie pour tout $n \in \mathbb{N}^*$ et tout $x \in [0, 1]$ par :
$$ e_n(x) = \sqrt{2} \sin(n\pi x) $$

**Question 1.** Démontrer rigoureusement que la famille $(e_n)_{n \in \mathbb{N}^*}$ est un système orthonormal dans $H$.

**Question 2.** Soit la fonction $f: [0, 1] \to \mathbb{R}$ définie par $f(x) = x$. Calculer explicitement le coefficient de Fourier $c_1 = \langle f, e_1 \rangle$.

---
**Difficulté :** $\star\star\star\star\star$

---

### Correction

**Question 1. Démontrer rigoureusement que la famille $(e_n)_{n \in \mathbb{N}^*}$ est un système orthonormal dans $H$.**

Pour qu'une famille de fonctions $(e_n)_{n \in \mathbb{N}^*}$ soit un système orthonormal, deux conditions doivent être satisfaites :
1.  **Normalisation :** Pour tout $n \in \mathbb{N}^*$, $\langle e_n, e_n \rangle = 1$.
2.  **Orthogonalité :** Pour tout $n, m \in \mathbb{N}^*$ avec $n \neq m$, $\langle e_n, e_m \rangle = 0$.

Nous allons démontrer ces deux points séparément.

**1. Normalisation :**
Calculons $\langle e_n, e_n \rangle$ pour un $n \in \mathbb{N}^*$ quelconque.
$$ \langle e_n, e_n \rangle = \int_0^1 e_n(x) e_n(x) dx = \int_0^1 (\sqrt{2} \sin(n\pi x))^2 dx $$
$$ \langle e_n, e_n \rangle = \int_0^1 2 \sin^2(n\pi x) dx $$
Pour simplifier l'intégrale, nous utilisons l'identité trigonométrique $\sin^2(\theta) = \frac{1 - \cos(2\theta)}{2}$.
Ici, $\theta = n\pi x$. Donc, $2\theta = 2n\pi x$.
$$ \langle e_n, e_n \rangle = \int_0^1 2 \left( \frac{1 - \cos(2n\pi x)}{2} \right) dx $$
$$ \langle e_n, e_n \rangle = \int_0^1 (1 - \cos(2n\pi x)) dx $$
Nous pouvons séparer cette intégrale en deux parties :
$$ \langle e_n, e_n \rangle = \int_0^1 1 \, dx - \int_0^1 \cos(2n\pi x) \, dx $$
Calculons la première partie :
$$ \int_0^1 1 \, dx = [x]_0^1 = 1 - 0 = 1 $$
Calculons la seconde partie. Puisque $n \in \mathbb{N}^*$, $2n\pi \neq 0$.
$$ \int_0^1 \cos(2n\pi x) \, dx = \left[ \frac{\sin(2n\pi x)}{2n\pi} \right]_0^1 $$
Évaluons cette primitive aux bornes :
$$ \left[ \frac{\sin(2n\pi x)}{2n\pi} \right]_0^1 = \frac{\sin(2n\pi \cdot 1)}{2n\pi} - \frac{\sin(2n\pi \cdot 0)}{2n\pi} $$
$$ = \frac{\sin(2n\pi)}{2n\pi} - \frac{\sin(0)}{2n\pi} $$
Puisque $n$ est un entier, $2n\pi$ est un multiple entier de $\pi$. La fonction sinus s'annule pour tous les multiples entiers de $\pi$. Donc, $\sin(2n\pi) = 0$ et $\sin(0) = 0$.
$$ \left[ \frac{\sin(2n\pi x)}{2n\pi} \right]_0^1 = \frac{0}{2n\pi} - \frac{0}{2n\pi} = 0 $$
En substituant ces résultats dans l'expression de $\langle e_n, e_n \rangle$:
$$ \langle e_n, e_n \rangle = 1 - 0 = 1 $$
Nous avons démontré que pour tout $n \in \mathbb{N}^*$, $\langle e_n, e_n \rangle = 1$. La condition de normalisation est satisfaite.

**2. Orthogonalité :**
Calculons $\langle e_n, e_m \rangle$ pour $n, m \in \mathbb{N}^*$ avec $n \neq m$.
$$ \langle e_n, e_m \rangle = \int_0^1 e_n(x) e_m(x) dx = \int_0^1 (\sqrt{2} \sin(n\pi x)) (\sqrt{2} \sin(m\pi x)) dx $$
$$ \langle e_n, e_m \rangle = \int_0^1 2 \sin(n\pi x) \sin(m\pi x) dx $$
Nous utilisons l'identité trigonométrique de produit-somme : $2 \sin A \sin B = \cos(A-B) - \cos(A+B)$.
Ici, $A = n\pi x$ et $B = m\pi x$.
$$ \langle e_n, e_m \rangle = \int_0^1 (\cos((n-m)\pi x) - \cos((n+m)\pi x)) dx $$
Nous pouvons séparer cette intégrale en deux parties :
$$ \langle e_n, e_m \rangle = \int_0^1 \cos((n-m)\pi x) dx - \int_0^1 \cos((n+m)\pi x) dx $$
Calculons la première partie. Puisque $n \neq m$, $n-m \neq 0$.
$$ \int_0^1 \cos((n-m)\pi x) dx = \left[ \frac{\sin((n-m)\pi x)}{(n-m)\pi} \right]_0^1 $$
Évaluons cette primitive aux bornes :
$$ = \frac{\sin((n-m)\pi \cdot 1)}{(n-m)\pi} - \frac{\sin((n-m)\pi \cdot 0)}{(n-m)\pi} $$
$$ = \frac{\sin((n-m)\pi)}{(n-m)\pi} - \frac{\sin(0)}{(n-m)\pi} $$
Puisque $n$ et $m$ sont des entiers, $n-m$ est un entier. Donc $(n-m)\pi$ est un multiple entier de $\pi$. Par conséquent, $\sin((n-m)\pi) = 0$ et $\sin(0)=0$.
$$ \int_0^1 \cos((n-m)\pi x) dx = \frac{0}{(n-m)\pi} - \frac{0}{(n-m)\pi} = 0 $$
Calculons la seconde partie. Puisque $n, m \in \mathbb{N}^*$, $n+m \ge 2$, donc $n+m \neq 0$.
$$ \int_0^1 \cos((n+m)\pi x) dx = \left[ \frac{\sin((n+m)\pi x)}{(n+m)\pi} \right]_0^1 $$
Évaluons cette primitive aux bornes :
$$ = \frac{\sin((n+m)\pi \cdot 1)}{(n+m)\pi} - \frac{\sin((n+m)\pi \cdot 0)}{(n+m)\pi} $$
$$ = \frac{\sin((n+m)\pi)}{(n+m)\pi} - \frac{\sin(0)}{(n+m)\pi} $$
Puisque $n$ et $m$ sont des entiers, $n+m$ est un entier. Donc $(n+m)\pi$ est un multiple entier de $\pi$. Par conséquent, $\sin((n+m)\pi) = 0$ et $\sin(0)=0$.
$$ \int_0^1 \cos((n+m)\pi x) dx = \frac{0}{(n+m)\pi} - \frac{0}{(n+m)\pi} = 0 $$
En substituant ces résultats dans l'expression de $\langle e_n, e_m \rangle$:
$$ \langle e_n, e_m \rangle = 0 - 0 = 0 $$
Nous avons démontré que pour tout $n, m \in \mathbb{N}^*$ avec $n \neq m$, $\langle e_n, e_m \rangle = 0$. La condition d'orthogonalité est satisfaite.

Les deux conditions de normalisation et d'orthogonalité étant remplies, nous concluons que la famille $(e_n)_{n \in \mathbb{N}^*}$ est bien un système orthonormal dans $H$.

---

**Question 2. Soit la fonction $f: [0, 1] \to \mathbb{R}$ définie par $f(x) = x$. Calculer explicitement le coefficient de Fourier $c_1 = \langle f, e_1 \rangle$.**

Le coefficient de Fourier $c_1$ est défini par $c_1 = \langle f, e_1 \rangle$.
En utilisant la définition du produit scalaire et de $e_1(x)$:
$$ e_1(x) = \sqrt{2} \sin(1\pi x) = \sqrt{2} \sin(\pi x) $$
Alors :
$$ c_1 = \int_0^1 f(x) e_1(x) dx = \int_0^1 x (\sqrt{2} \sin(\pi x)) dx $$
$$ c_1 = \sqrt{2} \int_0^1 x \sin(\pi x) dx $$
Nous allons calculer cette intégrale par parties. Rappelons la formule d'intégration par parties : $\int_a^b u(x) v'(x) dx = [u(x)v(x)]_a^b - \int_a^b u'(x)v(x) dx$.

Choisissons $u(x) = x$ et $v'(x) = \sin(\pi x)$.
Alors $u'(x) = 1$.
Pour trouver $v(x)$, nous intégrons $v'(x)$:
$$ v(x) = \int \sin(\pi x) dx = -\frac{1}{\pi} \cos(\pi x) $$
Appliquons la formule d'intégration par parties :
$$ \int_0^1 x \sin(\pi x) dx = \left[ x \left( -\frac{1}{\pi} \cos(\pi x) \right) \right]_0^1 - \int_0^1 1 \cdot \left( -\frac{1}{\pi} \cos(\pi x) \right) dx $$
$$ = \left[ -\frac{x}{\pi} \cos(\pi x) \right]_0^1 + \frac{1}{\pi} \int_0^1 \cos(\pi x) dx $$
Évaluons le premier terme aux bornes :
$$ \left[ -\frac{x}{\pi} \cos(\pi x) \right]_0^1 = \left( -\frac{1}{\pi} \cos(\pi \cdot 1) \right) - \left( -\frac{0}{\pi} \cos(\pi \cdot 0) \right) $$
$$ = \left( -\frac{1}{\pi} \cos(\pi) \right) - \left( 0 \right) $$
Puisque $\cos(\pi) = -1$:
$$ = -\frac{1}{\pi} (-1) = \frac{1}{\pi} $$
Évaluons le second terme (l'intégrale restante) :
$$ \frac{1}{\pi} \int_0^1 \cos(\pi x) dx = \frac{1}{\pi} \left[ \frac{\sin(\pi x)}{\pi} \right]_0^1 $$
Évaluons cette primitive aux bornes :
$$ = \frac{1}{\pi} \left( \frac{\sin(\pi \cdot 1)}{\pi} - \frac{\sin(\pi \cdot 0)}{\pi} \right) $$
$$ = \frac{1}{\pi} \left( \frac{\sin(\pi)}{\pi} - \frac{\sin(0)}{\pi} \right) $$
Puisque $\sin(\pi) = 0$ et $\sin(0) = 0$:
$$ = \frac{1}{\pi} \left( \frac{0}{\pi} - \frac{0}{\pi} \right) = \frac{1}{\pi} (0) = 0 $$
Maintenant, combinons les résultats des deux parties de l'intégration par parties :
$$ \int_0^1 x \sin(\pi x) dx = \frac{1}{\pi} + 0 = \frac{1}{\pi} $$
Enfin, substituons ce résultat dans l'expression de $c_1$:
$$ c_1 = \sqrt{2} \left( \frac{1}{\pi} \right) = \frac{\sqrt{2}}{\pi} $$
Ainsi, le coefficient de Fourier $c_1$ pour la fonction $f(x)=x$ est $\frac{\sqrt{2}}{\pi}$.
