Voici l'exercice. Votre formation à l'école des mathématiques rigoureuses commence maintenant.

---

### Exercice 9 sur les Bases Hilbertiennes (Jalon 104)

**Difficulté :** $\bigstar$\bigstar$\bigstar$\bigstar$\bigstar$

Soit $H = L^2([0,1], \mathbb{C})$ l'espace de Hilbert des fonctions de carré intégrable sur l'intervalle $[0,1]$ à valeurs complexes, muni du produit scalaire usuel défini par $\langle f, g \rangle = \int_0^1 f(x) \overline{g(x)} dx$.

Nous considérons le sous-espace $\mathcal{S} \subset H$ défini comme suit :
$$ \mathcal{S} = \{ f \in H : f(x) = f(1-x) \text{ pour presque tout } x \in [0,1] \} $$
Ce sous-espace $\mathcal{S}$ contient toutes les fonctions de $H$ qui sont symétriques par rapport au point $x=1/2$. Il est établi que $\mathcal{S}$ est un sous-espace fermé de $H$.

Soit le système de fonctions $\mathcal{B} = \{ \phi_n \}_{n \in \mathbb{N}_0}$ où $\mathbb{N}_0 = \{0, 1, 2, \ldots\}$, défini par :
$$ \phi_0(x) = 1 $$
$$ \phi_n(x) = \sqrt{2} \cos(2\pi n x) \quad \text{pour tout } n \in \mathbb{N}^* = \{1, 2, 3, \ldots\} $$

1.  Démontrer rigoureusement que chaque fonction $\phi_n \in \mathcal{B}$ appartient au sous-espace $\mathcal{S}$.
2.  Démontrer de manière complète que le système $\mathcal{B}$ est un système orthonormal dans $H$.
3.  Démontrer avec la plus grande précision que le système $\mathcal{B}$ est une base hilbertienne pour le sous-espace $\mathcal{S}$. Ceci exige de prouver que $\overline{\text{span}(\mathcal{B})} = \mathcal{S}$.
4.  Calculer la projection orthogonale de la fonction $g(x) = e^{2\pi i x}$ sur le sous-espace $\mathcal{S}$. Exprimez le résultat sous une forme explicite.

---

### Correction de l'Exercice 9

#### Question 1 : Démontrer que chaque fonction $\phi_n \in \mathcal{B}$ appartient au sous-espace $\mathcal{S}$.

Pour qu'une fonction $f$ appartienne à $\mathcal{S}$, elle doit satisfaire $f(x) = f(1-x)$ pour presque tout $x \in [0,1]$ et être dans $L^2([0,1], \mathbb{C})$. Les fonctions $\phi_n$ sont continues sur $[0,1]$, donc elles sont trivialement dans $L^2([0,1], \mathbb{C})$.

Considérons $\phi_0(x) = 1$:
Pour tout $x \in [0,1]$, nous avons $\phi_0(x) = 1$.
De même, $\phi_0(1-x) = 1$.
Par conséquent, $\phi_0(x) = \phi_0(1-x)$, ce qui démontre que $\phi_0 \in \mathcal{S}$.

Considérons $\phi_n(x) = \sqrt{2} \cos(2\pi n x)$ pour $n \in \mathbb{N}^*$:
Pour tout $x \in [0,1]$, calculons $\phi_n(1-x)$:
$$ \phi_n(1-x) = \sqrt{2} \cos(2\pi n (1-x)) $$
$$ \phi_n(1-x) = \sqrt{2} \cos(2\pi n - 2\pi n x) $$
En utilisant la propriété de périodicité de la fonction cosinus $\cos(\theta) = \cos(\theta - 2\pi k)$ pour tout entier $k$, nous avons $\cos(2\pi n - 2\pi n x) = \cos(-2\pi n x)$.
En utilisant la propriété de parité de la fonction cosinus $\cos(-\theta) = \cos(\theta)$, nous avons $\cos(-2\pi n x) = \cos(2\pi n x)$.
Par conséquent,
$$ \phi_n(1-x) = \sqrt{2} \cos(2\pi n x) = \phi_n(x) $$
Ceci démontre que $\phi_n \in \mathcal{S}$ pour tout $n \in \mathbb{N}^*$.
Puisque toutes les fonctions $\phi_n$ appartiennent à $\mathcal{S}$, nous avons prouvé la première partie.

#### Question 2 : Démontrer que le système $\mathcal{B}$ est un système orthonormal dans $H$.

Un système est orthonormal si $\langle \phi_n, \phi_m \rangle = \delta_{nm}$ pour tous $n, m \in \mathbb{N}_0$, où $\delta_{nm}$ est le symbole de Kronecker (1 si $n=m$, 0 si $n \ne m$).

**Cas 1 : $n=m=0$**
$$ \langle \phi_0, \phi_0 \rangle = \int_0^1 \phi_0(x) \overline{\phi_0(x)} dx = \int_0^1 1 \cdot \overline{1} dx = \int_0^1 1 dx = [x]_0^1 = 1 - 0 = 1 $$

**Cas 2 : $n=m \ge 1$**
$$ \langle \phi_n, \phi_n \rangle = \int_0^1 \phi_n(x) \overline{\phi_n(x)} dx = \int_0^1 (\sqrt{2} \cos(2\pi n x)) (\overline{\sqrt{2} \cos(2\pi n x)}) dx $$
Puisque $\cos(2\pi n x)$ est réel, $\overline{\cos(2\pi n x)} = \cos(2\pi n x)$.
$$ \langle \phi_n, \phi_n \rangle = \int_0^1 2 \cos^2(2\pi n x) dx $$
En utilisant l'identité trigonométrique $\cos^2(\theta) = \frac{1 + \cos(2\theta)}{2}$:
$$ \langle \phi_n, \phi_n \rangle = 2 \int_0^1 \frac{1 + \cos(4\pi n x)}{2} dx = \int_0^1 (1 + \cos(4\pi n x)) dx $$
$$ \langle \phi_n, \phi_n \rangle = \left[ x + \frac{\sin(4\pi n x)}{4\pi n} \right]_0^1 = \left( 1 + \frac{\sin(4\pi n)}{4\pi n} \right) - \left( 0 + \frac{\sin(0)}{4\pi n} \right) $$
Puisque $\sin(4\pi n) = 0$ pour tout entier $n \ge 1$:
$$ \langle \phi_n, \phi_n \rangle = 1 + 0 - 0 - 0 = 1 $$

**Cas 3 : $n \ne m$ (orthogonalité)**

*   **Sous-cas 3.1 : $m=0$ et $n \ge 1$**
    $$ \langle \phi_n, \phi_0 \rangle = \int_0^1 \phi_n(x) \overline{\phi_0(x)} dx = \int_0^1 \sqrt{2} \cos(2\pi n x) \cdot 1 dx $$
    $$ \langle \phi_n, \phi_0 \rangle = \sqrt{2} \left[ \frac{\sin(2\pi n x)}{2\pi n} \right]_0^1 = \sqrt{2} \left( \frac{\sin(2\pi n)}{2\pi n} - \frac{\sin(0)}{2\pi n} \right) $$
    Puisque $\sin(2\pi n) = 0$ pour tout entier $n \ge 1$:
    $$ \langle \phi_n, \phi_0 \rangle = \sqrt{2} (0 - 0) = 0 $$
    (Le cas $\langle \phi_0, \phi_n \rangle$ est le conjugué, qui est aussi 0.)

*   **Sous-cas 3.2 : $n, m \ge 1$ et $n \ne m$**
    $$ \langle \phi_n, \phi_m \rangle = \int_0^1 \phi_n(x) \overline{\phi_m(x)} dx = \int_0^1 (\sqrt{2} \cos(2\pi n x)) (\sqrt{2} \cos(2\pi m x)) dx $$
    $$ \langle \phi_n, \phi_m \rangle = 2 \int_0^1 \cos(2\pi n x) \cos(2\pi m x) dx $$
    En utilisant l'identité trigonométrique $2\cos A \cos B = \cos(A+B) + \cos(A-B)$:
    $$ \langle \phi_n, \phi_m \rangle = \int_0^1 (\cos(2\pi (n+m)x) + \cos(2\pi (n-m)x)) dx $$
    Puisque $n \ne m$, $n-m \ne 0$.
    $$ \langle \phi_n, \phi_m \rangle = \left[ \frac{\sin(2\pi (n+m)x)}{2\pi (n+m)} + \frac{\sin(2\pi (n-m)x)}{2\pi (n-m)} \right]_0^1 $$
    $$ \langle \phi_n, \phi_m \rangle = \left( \frac{\sin(2\pi (n+m))}{2\pi (n+m)} + \frac{\sin(2\pi (n-m))}{2\pi (n-m)} \right) - \left( \frac{\sin(0)}{2\pi (n+m)} + \frac{\sin(0)}{2\pi (n-m)} \right) $$
    Puisque $(n+m)$ et $(n-m)$ sont des entiers non nuls, $\sin(2\pi (n+m)) = 0$ et $\sin(2\pi (n-m)) = 0$.
    $$ \langle \phi_n, \phi_m \rangle = (0 + 0) - (0 + 0) = 0 $$

En combinant tous les cas, nous avons démontré que $\langle \phi_n, \phi_m \rangle = \delta_{nm}$ pour tous $n, m \in \mathbb{N}_0$. Le système $\mathcal{B}$ est donc un système orthonormal.

#### Question 3 : Démontrer que le système $\mathcal{B}$ est une base hilbertienne pour le sous-espace $\mathcal{S}$.

Pour démontrer que $\mathcal{B}$ est une base hilbertienne pour $\mathcal{S}$, nous devons prouver que $\mathcal{B}$ est un système orthonormal total dans $\mathcal{S}$. La partie orthonormale a été établie à la Question 2. Il reste à prouver la totalité.

Un système orthonormal est total dans un espace de Hilbert $X$ si, pour tout $f \in X$, l'identité de Parseval est satisfaite, ou de manière équivalente, si la seule fonction $f \in X$ orthogonale à tous les éléments du système est la fonction nulle.
Soit $f \in \mathcal{S}$ tel que $\langle f, \phi_n \rangle = 0$ pour tout $n \in \mathbb{N}_0$. Nous devons montrer que $f=0$.

Rappelons que $H = L^2([0,1], \mathbb{C})$ a pour base hilbertienne canonique le système de Fourier $\mathcal{E} = \{e_k(x) = e^{2\pi i k x}\}_{k \in \mathbb{Z}}$.
Toute fonction $f \in H$ peut être représentée par sa série de Fourier :
$$ f(x) = \sum_{k \in \mathbb{Z}} c_k e^{2\pi i k x} $$
où les coefficients de Fourier sont donnés par $c_k = \langle f, e_k \rangle = \int_0^1 f(x) e^{-2\pi i k x} dx$.

Si $f \in \mathcal{S}$, nous savons que $f(x) = f(1-x)$. Calculons $c_{-k}$:
$$ c_{-k} = \int_0^1 f(x) e^{-2\pi i (-k) x} dx = \int_0^1 f(x) e^{2\pi i k x} dx $$
En utilisant la propriété $f(x) = f(1-x)$, nous pouvons substituer $f(x)$ par $f(1-x)$:
$$ c_{-k} = \int_0^1 f(1-x) e^{2\pi i k x} dx $$
Effectuons le changement de variable $y = 1-x$, de sorte que $x = 1-y$ et $dx = -dy$. Les bornes d'intégration deviennent $x=0 \to y=1$ et $x=1 \to y=0$.
$$ c_{-k} = \int_1^0 f(y) e^{2\pi i k (1-y)} (-dy) = \int_0^1 f(y) e^{2\pi i k} e^{-2\pi i k y} dy $$
Puisque $e^{2\pi i k} = (\cos(2\pi k) + i \sin(2\pi k)) = 1$ pour tout entier $k$:
$$ c_{-k} = \int_0^1 f(y) e^{-2\pi i k y} dy = c_k $$
Ainsi, pour toute fonction $f \in \mathcal{S}$, ses coefficients de Fourier satisfont la propriété $c_k = c_{-k}$ pour tout $k \in \mathbb{Z}$.

Maintenant, examinons les conditions d'orthogonalité de $f \in \mathcal{S}$ avec les fonctions de $\mathcal{B}$:

1.  Orthogonalité à $\phi_0$:
    $$ \langle f, \phi_0 \rangle = \int_0^1 f(x) \overline{1} dx = \int_0^1 f(x) e^{-2\pi i (0) x} dx = c_0 $$
    Si $\langle f, \phi_0 \rangle = 0$, alors $c_0 = 0$.

2.  Orthogonalité à $\phi_n$ pour $n \in \mathbb{N}^*$:
    $$ \langle f, \phi_n \rangle = \int_0^1 f(x) \overline{\sqrt{2} \cos(2\pi n x)} dx $$
    $$ \langle f, \phi_n \rangle = \sqrt{2} \int_0^1 f(x) \cos(2\pi n x) dx $$
    Utilisons la formule d'Euler pour le cosinus : $\cos(\theta) = \frac{e^{i\theta} + e^{-i\theta}}{2}$.
    $$ \langle f, \phi_n \rangle = \sqrt{2} \int_0^1 f(x) \frac{e^{2\pi i n x} + e^{-2\pi i n x}}{2} dx $$
    $$ \langle f, \phi_n \rangle = \frac{\sqrt{2}}{2} \left( \int_0^1 f(x) e^{-2\pi i (-n) x} dx + \int_0^1 f(x) e^{-2\pi i n x} dx \right) $$
    $$ \langle f, \phi_n \rangle = \frac{\sqrt{2}}{2} (c_{-n} + c_n) $$
    Puisque $f \in \mathcal{S}$, nous savons que $c_{-n} = c_n$. Donc :
    $$ \langle f, \phi_n \rangle = \frac{\sqrt{2}}{2} (c_n + c_n) = \frac{\sqrt{2}}{2} (2c_n) = \sqrt{2} c_n $$
    Si $\langle f, \phi_n \rangle = 0$ pour tout $n \in \mathbb{N}^*$, alors $\sqrt{2} c_n = 0$, ce qui implique $c_n = 0$ pour tout $n \in \mathbb{N}^*$.

En résumé, si $f \in \mathcal{S}$ est orthogonal à toutes les fonctions de $\mathcal{B}$, alors :
*   $c_0 = 0$.
*   $c_n = 0$ pour tout $n \in \mathbb{N}^*$.
*   Puisque $f \in \mathcal{S}$, nous avons $c_{-n} = c_n$. Donc $c_{-n} = 0$ pour tout $n \in \mathbb{N}^*$.

Par conséquent, tous les coefficients de Fourier $c_k$ de $f$ sont nuls pour tout $k \in \mathbb{Z}$. Puisque $\mathcal{E}$ est une base hilbertienne pour $H$, l'égalité $f(x) = \sum_{k \in \mathbb{Z}} c_k e^{2\pi i k x}$ implique que $f(x)$ est la fonction nulle (dans $L^2([0,1], \mathbb{C})$).
Ceci démontre que le système $\mathcal{B}$ est total dans $\mathcal{S}$.
Ayant prouvé que $\mathcal{B}$ est un système orthonormal et total dans $\mathcal{S}$, nous avons conclu qu'il s'agit d'une base hilbertienne pour $\mathcal{S}$.

#### Question 4 : Calculer la projection orthogonale d'une fonction $g(x) = e^{2\pi i x}$ sur le sous-espace $\mathcal{S}$.

La projection orthogonale $P_\mathcal{S}(g)$ d'une fonction $g \in H$ sur le sous-espace $\mathcal{S}$ est donnée par la formule :
$$ P_\mathcal{S}(g) = \sum_{n=0}^\infty \langle g, \phi_n \rangle \phi_n $$
Nous devons calculer les coefficients $\langle g, \phi_n \rangle$.

**Cas 1 : $n=0$**
$$ \langle g, \phi_0 \rangle = \int_0^1 e^{2\pi i x} \overline{1} dx = \int_0^1 e^{2\pi i x} dx $$
$$ \langle g, \phi_0 \rangle = \left[ \frac{e^{2\pi i x}}{2\pi i} \right]_0^1 = \frac{e^{2\pi i (1)} - e^{2\pi i (0)}}{2\pi i} $$
Puisque $e^{2\pi i} = 1$ et $e^0 = 1$:
$$ \langle g, \phi_0 \rangle = \frac{1 - 1}{2\pi i} = 0 $$

**Cas 2 : $n \ge 1$**
$$ \langle g, \phi_n \rangle = \int_0^1 e^{2\pi i x} \overline{\sqrt{2} \cos(2\pi n x)} dx = \sqrt{2} \int_0^1 e^{2\pi i x} \cos(2\pi n x) dx $$
Utilisons la formule d'Euler $\cos(\theta) = \frac{e^{i\theta} + e^{-i\theta}}{2}$:
$$ \langle g, \phi_n \rangle = \sqrt{2} \int_0^1 e^{2\pi i x} \frac{e^{2\pi i n x} + e^{-2\pi i n x}}{2} dx $$
$$ \langle g, \phi_n \rangle = \frac{\sqrt{2}}{2} \int_0^1 (e^{2\pi i (1+n)x} + e^{2\pi i (1-n)x}) dx $$

*   **Sous-cas 2.1 : $n=1$**
    $$ \langle g, \phi_1 \rangle = \frac{\sqrt{2}}{2} \int_0^1 (e^{2\pi i (1+1)x} + e^{2\pi i (1-1)x}) dx $$
    $$ \langle g, \phi_1 \rangle = \frac{\sqrt{2}}{2} \int_0^1 (e^{4\pi i x} + e^{0}) dx = \frac{\sqrt{2}}{2} \int_0^1 (e^{4\pi i x} + 1) dx $$
    $$ \langle g, \phi_1 \rangle = \frac{\sqrt{2}}{2} \left[ \frac{e^{4\pi i x}}{4\pi i} + x \right]_0^1 $$
    $$ \langle g, \phi_1 \rangle = \frac{\sqrt{2}}{2} \left( \left( \frac{e^{4\pi i}}{4\pi i} + 1 \right) - \left( \frac{e^0}{4\pi i} + 0 \right) \right) $$
    Puisque $e^{4\pi i} = 1$ et $e^0 = 1$:
    $$ \langle g, \phi_1 \rangle = \frac{\sqrt{2}}{2} \left( \frac{1}{4\pi i} + 1 - \frac{1}{4\pi i} \right) = \frac{\sqrt{2}}{2} (1) = \frac{\sqrt{2}}{2} $$

*   **Sous-cas 2.2 : $n \ne 1$ (pour $n \ge 1$)**
    Dans ce cas, $1+n \ne 0$ et $1-n \ne 0$.
    $$ \langle g, \phi_n \rangle = \frac{\sqrt{2}}{2} \left[ \frac{e^{2\pi i (1+n)x}}{2\pi i (1+n)} + \frac{e^{2\pi i (1-n)x}}{2\pi i (1-n)} \right]_0^1 $$
    $$ \langle g, \phi_n \rangle = \frac{\sqrt{2}}{2} \left( \left( \frac{e^{2\pi i (1+n)}}{2\pi i (1+n)} - \frac{e^{0}}{2\pi i (1+n)} \right) + \left( \frac{e^{2\pi i (1-n)}}{2\pi i (1-n)} - \frac{e^{0}}{2\pi i (1-n)} \right) \right) $$
    Puisque $1+n$ et $1-n$ sont des entiers non nuls, $e^{2\pi i (1+n)} = 1$ et $e^{2\pi i (1-n)} = 1$. De plus $e^0=1$.
    $$ \langle g, \phi_n \rangle = \frac{\sqrt{2}}{2} \left( \left( \frac{1}{2\pi i (1+n)} - \frac{1}{2\pi i (1+n)} \right) + \left( \frac{1}{2\pi i (1-n)} - \frac{1}{2\pi i (1-n)} \right) \right) $$
    $$ \langle g, \phi_n \rangle = \frac{\sqrt{2}}{2} (0 + 0) = 0 $$

Seul le coefficient pour $n=1$ est non nul.
La projection orthogonale $P_\mathcal{S}(g)$ est donc :
$$ P_\mathcal{S}(g) = \langle g, \phi_1 \rangle \phi_1 $$
$$ P_\mathcal{S}(g) = \frac{\sqrt{2}}{2} \cdot (\sqrt{2} \cos(2\pi (1) x)) $$
$$ P_\mathcal{S}(g) = \frac{2}{2} \cos(2\pi x) $$
$$ P_\mathcal{S}(g) = \cos(2\pi x) $$

Pour vérification, la fonction $g(x) = e^{2\pi i x}$ peut s'écrire $g(x) = \cos(2\pi x) + i \sin(2\pi x)$.
Nous avons montré que $\cos(2\pi x)$ est une fonction de $\mathcal{S}$ (c'est $\frac{1}{\sqrt{2}}\phi_1(x)$).
La fonction $h(x) = i \sin(2\pi x)$ est-elle dans $\mathcal{S}$?
$h(1-x) = i \sin(2\pi(1-x)) = i \sin(2\pi - 2\pi x) = i \sin(-2\pi x) = -i \sin(2\pi x) = -h(x)$.
Puisque $h(1-x) = -h(x)$, la fonction $h(x)$ est anti-symétrique et n'appartient pas à $\mathcal{S}$ (à moins qu'elle ne soit nulle).
En fait, $\mathcal{S}$ et le sous-espace des fonctions anti-symétriques sont des compléments orthogonaux l'un de l'autre dans $L^2([0,1])$. La projection de $g$ sur $\mathcal{S}$ doit être la partie symétrique de $g$, ce qui est bien $\cos(2\pi x)$.

La projection orthogonale de $g(x) = e^{2\pi i x}$ sur le sous-espace $\mathcal{S}$ est $P_\mathcal{S}(g)(x) = \cos(2\pi x)$.

---