**Exercice 10 (Jalon 104)**

**Titre :** Caractérisation et Démonstration d'une Base Hilbertienne pour $L^2([0,1])$.

**Énoncé :**
Soit $H = L^2([0,1], \mathbb{C})$ l'espace de Hilbert des fonctions de carré sommable sur l'intervalle $[0,1]$ à valeurs complexes, muni de son produit scalaire standard défini par $\langle f, g \rangle = \int_0^1 f(x) \overline{g(x)} dx$.

Considérons le système de fonctions $\mathcal{B} = \{e_n\}_{n \in \mathbb{N}_0}$ défini comme suit :
$e_0(x) = 1$ pour tout $x \in [0,1]$,
et pour tout $n \in \mathbb{N}^* = \{1, 2, 3, \ldots\}$, $e_n(x) = \sqrt{2}\cos(n\pi x)$ pour tout $x \in [0,1]$.

1.  Démontrer rigoureusement que le système $\mathcal{B}$ est un système orthonormal dans $H$.
2.  Démontrer rigoureusement que le système $\mathcal{B}$ est une base hilbertienne pour $H$.

**Difficulté :** $\bigstar$\bigstar$\bigstar$\bigstar$\bigstar

---

**Correction :**

Nous procédons par étapes pour établir les propriétés requises du système $\mathcal{B}$.

**Partie 1 : Démonstration que $\mathcal{B}$ est un système orthonormal.**

Un système est orthonormal si tous ses éléments sont de norme 1 et sont mutuellement orthogonaux.
Puisque les fonctions $e_n(x)$ sont toutes réelles, nous avons $\overline{e_n(x)} = e_n(x)$ pour tout $n \in \mathbb{N}_0$.

1.  **Calcul de la norme de $e_0$ :**
    $\|e_0\|^2 = \langle e_0, e_0 \rangle = \int_0^1 e_0(x) \overline{e_0(x)} dx = \int_0^1 1 \cdot 1 dx = \int_0^1 1 dx = [x]_0^1 = 1 - 0 = 1$.
    Ainsi, $\|e_0\| = 1$.

2.  **Calcul de la norme de $e_n$ pour $n \in \mathbb{N}^*$ :**
    Pour $n \in \mathbb{N}^*$, $\|e_n\|^2 = \langle e_n, e_n \rangle = \int_0^1 e_n(x) \overline{e_n(x)} dx = \int_0^1 (\sqrt{2}\cos(n\pi x))^2 dx$.
    $\|e_n\|^2 = \int_0^1 2\cos^2(n\pi x) dx$.
    Utilisant l'identité trigonométrique $\cos^2(\theta) = \frac{1+\cos(2\theta)}{2}$, nous obtenons :
    $\|e_n\|^2 = \int_0^1 2 \left(\frac{1+\cos(2n\pi x)}{2}\right) dx = \int_0^1 (1+\cos(2n\pi x)) dx$.
    $\|e_n\|^2 = \left[x + \frac{\sin(2n\pi x)}{2n\pi}\right]_0^1$.
    $\|e_n\|^2 = \left(1 + \frac{\sin(2n\pi)}{2n\pi}\right) - \left(0 + \frac{\sin(0)}{2n\pi}\right)$.
    Comme $n \in \mathbb{N}^*$, $2n\pi$ est un multiple entier de $\pi$, donc $\sin(2n\pi) = 0$.
    Par conséquent, $\|e_n\|^2 = (1+0) - (0+0) = 1$.
    Ainsi, $\|e_n\| = 1$ pour tout $n \in \mathbb{N}^*$.

3.  **Calcul du produit scalaire $\langle e_0, e_n \rangle$ pour $n \in \mathbb{N}^*$ :**
    $\langle e_0, e_n \rangle = \int_0^1 e_0(x) \overline{e_n(x)} dx = \int_0^1 1 \cdot \sqrt{2}\cos(n\pi x) dx$.
    $\langle e_0, e_n \rangle = \sqrt{2} \int_0^1 \cos(n\pi x) dx = \sqrt{2} \left[\frac{\sin(n\pi x)}{n\pi}\right]_0^1$.
    $\langle e_0, e_n \rangle = \sqrt{2} \left(\frac{\sin(n\pi)}{n\pi} - \frac{\sin(0)}{n\pi}\right)$.
    Comme $n \in \mathbb{N}^*$, $n\pi$ est un multiple entier de $\pi$, donc $\sin(n\pi) = 0$.
    Par conséquent, $\langle e_0, e_n \rangle = \sqrt{2} (0 - 0) = 0$.

4.  **Calcul du produit scalaire $\langle e_m, e_n \rangle$ pour $m, n \in \mathbb{N}^*$ avec $m \neq n$ :**
    $\langle e_m, e_n \rangle = \int_0^1 e_m(x) \overline{e_n(x)} dx = \int_0^1 (\sqrt{2}\cos(m\pi x)) (\sqrt{2}\cos(n\pi x)) dx$.
    $\langle e_m, e_n \rangle = 2 \int_0^1 \cos(m\pi x)\cos(n\pi x) dx$.
    Utilisant l'identité trigonométrique $2\cos A \cos B = \cos(A+B) + \cos(A-B)$, nous obtenons :
    $\langle e_m, e_n \rangle = \int_0^1 (\cos((m+n)\pi x) + \cos((m-n)\pi x)) dx$.
    Puisque $m \neq n$, $(m-n)$ est un entier non nul. $(m+n)$ est également un entier non nul.
    $\langle e_m, e_n \rangle = \left[\frac{\sin((m+n)\pi x)}{(m+n)\pi} + \frac{\sin((m-n)\pi x)}{(m-n)\pi}\right]_0^1$.
    $\langle e_m, e_n \rangle = \left(\frac{\sin((m+n)\pi)}{(m+n)\pi} + \frac{\sin((m-n)\pi)}{(m-n)\pi}\right) - \left(\frac{\sin(0)}{(m+n)\pi} + \frac{\sin(0)}{(m-n)\pi}\right)$.
    Comme $(m+n)\pi$ et $(m-n)\pi$ sont des multiples entiers non nuls de $\pi$, leurs sinus sont nuls.
    Par conséquent, $\langle e_m, e_n \rangle = (0+0) - (0+0) = 0$.

En résumé, nous avons démontré que :
*   $\|e_n\| = 1$ pour tout $n \in \mathbb{N}_0$.
*   $\langle e_m, e_n \rangle = 0$ pour tout $m \neq n$, $m, n \in \mathbb{N}_0$.
Le système $\mathcal{B} = \{e_n\}_{n \in \mathbb{N}_0}$ est donc un système orthonormal dans $H$.

---

**Partie 2 : Démonstration que $\mathcal{B}$ est une base hilbertienne.**

Pour démontrer que $\mathcal{B}$ est une base hilbertienne, nous allons montrer que son orthogonal complément est trivial. C'est-à-dire, si $f \in H$ est orthogonal à tous les éléments de $\mathcal{B}$, alors $f$ doit être la fonction nulle (presque partout).

Soit $f \in H$ une fonction telle que $\langle f, e_n \rangle = 0$ pour tout $n \in \mathbb{N}_0$.
Ces conditions d'orthogonalité se traduisent par :
1.  Pour $n=0$ : $\langle f, e_0 \rangle = \int_0^1 f(x) \overline{e_0(x)} dx = \int_0^1 f(x) \cdot 1 dx = 0$.
2.  Pour $n \in \mathbb{N}^*$ : $\langle f, e_n \rangle = \int_0^1 f(x) \overline{\sqrt{2}\cos(n\pi x)} dx = \sqrt{2} \int_0^1 f(x) \cos(n\pi x) dx = 0$.
    Cela implique $\int_0^1 f(x) \cos(n\pi x) dx = 0$ pour tout $n \in \mathbb{N}^*$.

Nous allons étendre la fonction $f$ à l'intervalle $[-1,1]$. Soit $g: [-1,1] \to \mathbb{C}$ la fonction définie par :
$g(x) = f(x)$ pour $x \in [0,1]$
$g(x) = f(-x)$ pour $x \in [-1,0]$ (extension paire de $f$).

Montrons que $g \in L^2([-1,1])$.
$\int_{-1}^1 |g(x)|^2 dx = \int_{-1}^0 |g(x)|^2 dx + \int_0^1 |g(x)|^2 dx$.
Pour la première intégrale, nous effectuons le changement de variable $y = -x$, donc $dy = -dx$. Lorsque $x=-1$, $y=1$. Lorsque $x=0$, $y=0$.
$\int_{-1}^0 |g(x)|^2 dx = \int_{-1}^0 |f(-x)|^2 dx = \int_1^0 |f(y)|^2 (-dy) = \int_0^1 |f(y)|^2 dy$.
Donc, $\int_{-1}^1 |g(x)|^2 dx = \int_0^1 |f(x)|^2 dx + \int_0^1 |f(x)|^2 dx = 2 \int_0^1 |f(x)|^2 dx = 2\|f\|^2$.
Puisque $f \in L^2([0,1])$, $\|f\|^2 < \infty$, ce qui implique $\|g\|^2 < \infty$. Donc $g \in L^2([-1,1])$.

Considérons la base hilbertienne standard de $L^2([-1,1])$ donnée par les fonctions exponentielles complexes $\{\phi_k(x) = \frac{1}{\sqrt{2}}e^{i k \pi x}\}_{k \in \mathbb{Z}}$. Pour montrer que $g=0$ (presque partout), il suffit de montrer que $g$ est orthogonal à tous les éléments de cette base, c'est-à-dire $\langle g, \phi_k \rangle = 0$ pour tout $k \in \mathbb{Z}$.

Calculons $\langle g, \phi_k \rangle = \int_{-1}^1 g(x) \overline{\phi_k(x)} dx = \int_{-1}^1 g(x) \frac{1}{\sqrt{2}}e^{-i k \pi x} dx$.
Nous séparons l'intégrale :
$\int_{-1}^1 g(x) e^{-i k \pi x} dx = \int_{-1}^0 g(x) e^{-i k \pi x} dx + \int_0^1 g(x) e^{-i k \pi x} dx$.

Pour la première partie, effectuons le changement de variable $y = -x$ (donc $dx = -dy$) :
$\int_{-1}^0 g(x) e^{-i k \pi x} dx = \int_{1}^0 g(-y) e^{i k \pi y} (-dy) = \int_0^1 f(y) e^{i k \pi y} dy$.
Pour la deuxième partie, rappelons $g(x) = f(x)$ sur $[0,1]$ :
$\int_0^1 g(x) e^{-i k \pi x} dx = \int_0^1 f(x) e^{-i k \pi x} dx$.

En additionnant les deux parties, nous obtenons :
$\int_{-1}^1 g(x) e^{-i k \pi x} dx = \int_0^1 f(x) e^{i k \pi x} dx + \int_0^1 f(x) e^{-i k \pi x} dx$.
Utilisons l'identité d'Euler $e^{i\theta} + e^{-i\theta} = 2\cos\theta$ :
$\int_{-1}^1 g(x) e^{-i k \pi x} dx = \int_0^1 f(x) (e^{i k \pi x} + e^{-i k \pi x}) dx = \int_0^1 f(x) (2\cos(k\pi x)) dx = 2 \int_0^1 f(x) \cos(k\pi x) dx$.

Nous examinons maintenant ce résultat pour différentes valeurs de $k$:

*   **Cas $k=0$ :**
    $\langle g, \phi_0 \rangle = \frac{1}{\sqrt{2}} \int_{-1}^1 g(x) dx = \frac{1}{\sqrt{2}} \cdot 2 \int_0^1 f(x) \cos(0\pi x) dx = \frac{2}{\sqrt{2}} \int_0^1 f(x) \cdot 1 dx$.
    D'après notre condition d'orthogonalité sur $f$ avec $e_0$, nous savons que $\int_0^1 f(x) dx = 0$.
    Donc, $\langle g, \phi_0 \rangle = 0$.

*   **Cas $k \in \mathbb{Z}^*$ (donc $k \neq 0$) :**
    $\langle g, \phi_k \rangle = \frac{1}{\sqrt{2}} \cdot 2 \int_0^1 f(x) \cos(k\pi x) dx$.
    D'après notre condition d'orthogonalité sur $f$ avec $e_{|k|}$ (si $k \in \mathbb{N}^*$) ou $e_{|-k|}$ (si $k \in \mathbb{Z}^-$), nous savons que $\int_0^1 f(x) \cos(n\pi x) dx = 0$ pour tout $n \in \mathbb{N}^*$.
    Puisque $|k| \in \mathbb{N}^*$ pour $k \in \mathbb{Z}^*$, il s'ensuit que $\int_0^1 f(x) \cos(k\pi x) dx = 0$.
    Donc, $\langle g, \phi_k \rangle = 0$ pour tout $k \in \mathbb{Z}^*$.

Nous avons démontré que $\langle g, \phi_k \rangle = 0$ pour tout $k \in \mathbb{Z}$. Puisque $\{\phi_k\}_{k \in \mathbb{Z}}$ est une base hilbertienne pour $L^2([-1,1])$, et que $g$ est orthogonale à tous ses éléments, nous concluons que $g(x) = 0$ presque partout sur $[-1,1]$.

Étant donné que $f(x) = g(x)$ pour tout $x \in [0,1]$, il s'ensuit que $f(x) = 0$ presque partout sur $[0,1]$.
Par conséquent, le seul vecteur de $H$ orthogonal à tous les éléments du système $\mathcal{B}$ est le vecteur nul. C'est la condition équivalente à la densité de l'enveloppe linéaire fermée de $\mathcal{B}$ dans $H$.
Ceci démontre que le système $\mathcal{B} = \{e_n\}_{n \in \mathbb{N}_0}$ est une base hilbertienne pour $H = L^2([0,1], \mathbb{C})$.