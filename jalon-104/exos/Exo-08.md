**EXERCICE 8 (Jalon 104)**

**Difficulté :** $\bigstar$\bigstar$\bigstar$\bigstar\star$

**Problème : Étude d'une Base Hilbertienne de l'Espace des Fonctions de Carré Sommable sur $[0, \pi]$**

Soit $H = L^2([0, \pi], \mathbb{C})$ l'espace de Hilbert des fonctions de carré sommable sur l'intervalle $[0, \pi]$ à valeurs complexes, muni de son produit scalaire canonique défini par $\langle f, g \rangle = \int_0^\pi f(x) \overline{g(x)} dx$ pour $f, g \in H$.

Nous allons étudier la famille de fonctions $\mathcal{F} = \{f_n\}_{n \in \mathbb{N}_0}$ où $f_n(x) = \cos(nx)$ pour tout $x \in [0, \pi]$ et $\mathbb{N}_0 = \{0, 1, 2, \ldots\}$.

**Partie I : Orthogonalisation et Normalisation de la Famille de Fonctions**

1.  Démontrer rigoureusement que la famille $\mathcal{F}$ est une famille orthogonale dans $H$.
    *   Vous devrez considérer séparément les cas $n=m=0$, $n=0, m \ne 0$ (et vice-versa), et $n \ne m$, $n,m \ne 0$.

2.  Calculer la norme $\lVert f_n \rVert$ de chaque fonction $f_n \in \mathcal{F}$ pour tout $n \in \mathbb{N}_0$.

3.  Déduire des questions précédentes une famille $\mathcal{B} = \{e_n\}_{n \in \mathbb{N}_0}$ qui est orthonormée dans $H$. Expliciter la forme de $e_n(x)$.

**Partie II : Complétude de la Base Hilbertienne**

Afin de démontrer que la famille orthonormée $\mathcal{B}$ est une base hilbertienne de $H$, il est nécessaire de prouver sa complétude. C'est-à-dire, si une fonction $g \in H$ est orthogonale à tous les éléments de $\mathcal{B}$, alors $g$ doit être la fonction nulle presque partout.

4.  Soit $g \in H$ une fonction telle que $\langle g, e_n \rangle = 0$ pour tout $n \in \mathbb{N}_0$.
    Démontrer que $g(x) = 0$ presque partout sur $[0, \pi]$.
    *   Indication : Vous pourrez considérer une extension paire de $g$ sur l'intervalle $[-\pi, \pi]$ et utiliser la complétude de la base de Fourier dans $L^2([-\pi, \pi])$.

---

**CORRECTION DE L'EXERCICE 8**

**Partie I : Orthogonalisation et Normalisation de la Famille de Fonctions**

1.  **Démonstration de l'orthogonalité de la famille $\mathcal{F} = \{\cos(nx)\}_{n \in \mathbb{N}_0}$ :**
    Nous devons montrer que pour tout $n, m \in \mathbb{N}_0$ tels que $n \neq m$, nous avons $\langle f_n, f_m \rangle = 0$.
    Le produit scalaire est défini par $\langle f_n, f_m \rangle = \int_0^\pi f_n(x) \overline{f_m(x)} dx$. Puisque les fonctions $f_n(x) = \cos(nx)$ sont à valeurs réelles, $\overline{f_m(x)} = f_m(x) = \cos(mx)$.
    Ainsi, $\langle f_n, f_m \rangle = \int_0^\pi \cos(nx) \cos(mx) dx$.

    Nous utilisons la formule de trigonométrie pour le produit de cosinus :
    $2 \cos A \cos B = \cos(A+B) + \cos(A-B)$.
    Par conséquent, $\cos(nx) \cos(mx) = \frac{1}{2} [\cos((n+m)x) + \cos((n-m)x)]$.

    Nous allons examiner les différents cas pour $n \neq m$ :

    *   **Cas 1 : $n=0$ et $m \in \mathbb{N}, m \neq 0$.**
        La fonction $f_0(x) = \cos(0x) = 1$.
        $\langle f_0, f_m \rangle = \int_0^\pi 1 \cdot \cos(mx) dx$.
        $\langle f_0, f_m \rangle = \left[ \frac{\sin(mx)}{m} \right]_0^\pi$.
        $\langle f_0, f_m \rangle = \frac{\sin(m\pi)}{m} - \frac{\sin(0)}{m}$.
        Puisque $m$ est un entier non nul, $m\pi$ est un multiple entier de $\pi$, ce qui implique $\sin(m\pi) = 0$. De plus, $\sin(0) = 0$.
        Donc, $\langle f_0, f_m \rangle = 0 - 0 = 0$.

    *   **Cas 2 : $n \in \mathbb{N}, n \neq 0$ et $m=0$.**
        Par la propriété de symétrie du produit scalaire réel, $\langle f_n, f_0 \rangle = \langle f_0, f_n \rangle$.
        D'après le Cas 1, $\langle f_n, f_0 \rangle = 0$.

    *   **Cas 3 : $n, m \in \mathbb{N}, n \neq 0, m \neq 0$ et $n \neq m$.**
        $\langle f_n, f_m \rangle = \int_0^\pi \frac{1}{2} [\cos((n+m)x) + \cos((n-m)x)] dx$.
        $\langle f_n, f_m \rangle = \frac{1}{2} \left[ \frac{\sin((n+m)x)}{n+m} + \frac{\sin((n-m)x)}{n-m} \right]_0^\pi$.
        Nous savons que $n \neq m$, donc $n-m \neq 0$. De même $n+m \neq 0$.
        L'évaluation aux bornes donne :
        $\langle f_n, f_m \rangle = \frac{1}{2} \left( \left[ \frac{\sin((n+m)\pi)}{n+m} + \frac{\sin((n-m)\pi)}{n-m} \right] - \left[ \frac{\sin(0)}{n+m} + \frac{\sin(0)}{n-m} \right] \right)$.
        Puisque $(n+m)$ et $(n-m)$ sont des entiers non nuls, $\sin((n+m)\pi) = 0$ et $\sin((n-m)\pi) = 0$. De plus, $\sin(0) = 0$.
        Donc, $\langle f_n, f_m \rangle = \frac{1}{2} ( (0+0) - (0+0) ) = 0$.

    Dans tous les cas où $n \neq m$, nous avons démontré que $\langle f_n, f_m \rangle = 0$.
    Par conséquent, la famille $\mathcal{F} = \{\cos(nx)\}_{n \in \mathbb{N}_0}$ est une famille orthogonale dans $H$.

2.  **Calcul de la norme $\lVert f_n \rVert$ pour chaque $n \in \mathbb{N}_0$ :**
    La norme $\lVert f_n \rVert$ est définie par $\lVert f_n \rVert = \sqrt{\langle f_n, f_n \rangle}$.
    Nous devons calculer $\lVert f_n \rVert^2 = \int_0^\pi \cos^2(nx) dx$.

    *   **Cas 1 : $n=0$.**
        $f_0(x) = \cos(0x) = 1$.
        $\lVert f_0 \rVert^2 = \int_0^\pi 1^2 dx = \int_0^\pi 1 dx = [x]_0^\pi = \pi - 0 = \pi$.
        Par conséquent, $\lVert f_0 \rVert = \sqrt{\pi}$.

    *   **Cas 2 : $n \in \mathbb{N}, n \neq 0$.**
        Nous utilisons la formule de trigonométrie : $\cos^2 A = \frac{1 + \cos(2A)}{2}$.
        Donc, $\cos^2(nx) = \frac{1 + \cos(2nx)}{2}$.
        $\lVert f_n \rVert^2 = \int_0^\pi \frac{1 + \cos(2nx)}{2} dx$.
        $\lVert f_n \rVert^2 = \frac{1}{2} \int_0^\pi (1 + \cos(2nx)) dx$.
        $\lVert f_n \rVert^2 = \frac{1}{2} \left[ x + \frac{\sin(2nx)}{2n} \right]_0^\pi$.
        L'évaluation aux bornes donne :
        $\lVert f_n \rVert^2 = \frac{1}{2} \left( \left[ \pi + \frac{\sin(2n\pi)}{2n} \right] - \left[ 0 + \frac{\sin(0)}{2n} \right] \right)$.
        Puisque $n$ est un entier non nul, $2n\pi$ est un multiple entier de $\pi$, donc $\sin(2n\pi) = 0$. De plus, $\sin(0) = 0$.
        Donc, $\lVert f_n \rVert^2 = \frac{1}{2} (\pi + 0 - 0 - 0) = \frac{\pi}{2}$.
        Par conséquent, $\lVert f_n \rVert = \sqrt{\frac{\pi}{2}}$ pour $n \in \mathbb{N}, n \neq 0$.

    En résumé, les normes sont :
    $\lVert f_0 \rVert = \sqrt{\pi}$.
    $\lVert f_n \rVert = \sqrt{\frac{\pi}{2}}$ pour $n \in \mathbb{N}, n \neq 0$.

3.  **Déduction de la famille orthonormée $\mathcal{B} = \{e_n\}_{n \in \mathbb{N}_0}$ :**
    Pour obtenir une famille orthonormée à partir d'une famille orthogonale dont aucun élément n'est nul (ce qui est le cas ici puisque toutes les normes sont non nulles), il suffit de diviser chaque vecteur par sa norme.
    $e_n(x) = \frac{f_n(x)}{\lVert f_n \rVert}$.

    *   Pour $n=0$ :
        $e_0(x) = \frac{\cos(0x)}{\sqrt{\pi}} = \frac{1}{\sqrt{\pi}}$.

    *   Pour $n \in \mathbb{N}, n \neq 0$ :
        $e_n(x) = \frac{\cos(nx)}{\sqrt{\frac{\pi}{2}}} = \sqrt{\frac{2}{\pi}} \cos(nx)$.

    La famille orthonormée $\mathcal{B}$ est donc :
    $\mathcal{B} = \left\{ \frac{1}{\sqrt{\pi}} \right\} \cup \left\{ \sqrt{\frac{2}{\pi}} \cos(nx) \right\}_{n \in \mathbb{N}, n \neq 0}$.

**Partie II : Complétude de la Base Hilbertienne**

4.  **Démonstration de la complétude de $\mathcal{B}$ :**
    Nous devons démontrer que si $g \in H$ est une fonction telle que $\langle g, e_n \rangle = 0$ pour tout $n \in \mathbb{N}_0$, alors $g(x) = 0$ presque partout sur $[0, \pi]$.

    L'hypothèse $\langle g, e_n \rangle = 0$ pour tout $n \in \mathbb{N}_0$ se traduit par :
    *   $\langle g, e_0 \rangle = \int_0^\pi g(x) \overline{\left(\frac{1}{\sqrt{\pi}}\right)} dx = \frac{1}{\sqrt{\pi}} \int_0^\pi g(x) dx = 0$.
        Ceci implique $\int_0^\pi g(x) dx = 0$.
    *   Pour $n \in \mathbb{N}, n \neq 0$, $\langle g, e_n \rangle = \int_0^\pi g(x) \overline{\left(\sqrt{\frac{2}{\pi}} \cos(nx)\right)} dx = \sqrt{\frac{2}{\pi}} \int_0^\pi g(x) \cos(nx) dx = 0$.
        Ceci implique $\int_0^\pi g(x) \cos(nx) dx = 0$ pour tout $n \in \mathbb{N}, n \neq 0$.

    En résumé, nous avons $\int_0^\pi g(x) \cos(nx) dx = 0$ pour tout $n \in \mathbb{N}_0$.

    Considérons la fonction $\tilde{g}: [-\pi, \pi] \to \mathbb{C}$ définie comme l'extension paire de $g$ sur l'intervalle $[-\pi, \pi]$ :
    $\tilde{g}(x) = \begin{cases} g(x) & \text{si } x \in [0, \pi] \\ g(-x) & \text{si } x \in [-\pi, 0) \end{cases}$.

    Nous devons d'abord vérifier que $\tilde{g} \in L^2([-\pi, \pi])$.
    $\int_{-\pi}^\pi |\tilde{g}(x)|^2 dx = \int_{-\pi}^0 |\tilde{g}(x)|^2 dx + \int_0^\pi |\tilde{g}(x)|^2 dx$.
    Par la définition de $\tilde{g}$, cela devient :
    $\int_{-\pi}^\pi |\tilde{g}(x)|^2 dx = \int_{-\pi}^0 |g(-x)|^2 dx + \int_0^\pi |g(x)|^2 dx$.
    Dans la première intégrale, nous effectuons un changement de variable : $u = -x$. Alors $du = -dx$.
    Lorsque $x = -\pi$, $u = \pi$. Lorsque $x = 0$, $u = 0$.
    Donc, $\int_{-\pi}^0 |g(-x)|^2 dx = \int_{\pi}^0 |g(u)|^2 (-du) = \int_0^\pi |g(u)|^2 du$.
    Ainsi, $\int_{-\pi}^\pi |\tilde{g}(x)|^2 dx = \int_0^\pi |g(x)|^2 dx + \int_0^\pi |g(x)|^2 dx = 2 \int_0^\pi |g(x)|^2 dx = 2 \lVert g \rVert_H^2$.
    Puisque $g \in H = L^2([0, \pi])$, $\lVert g \rVert_H^2 < \infty$. Par conséquent, $\int_{-\pi}^\pi |\tilde{g}(x)|^2 dx < \infty$, ce qui signifie que $\tilde{g} \in L^2([-\pi, \pi])$.

    Maintenant, nous allons calculer les coefficients de Fourier complexes de $\tilde{g}$ par rapport à la base trigonométrique classique de $L^2([-\pi, \pi])$. Les coefficients $c_k$ sont définis pour $k \in \mathbb{Z}$ par :
    $c_k = \frac{1}{2\pi} \int_{-\pi}^\pi \tilde{g}(x) e^{-ikx} dx$.

    Nous décomposons l'intégrale sur $[-\pi, \pi]$ :
    $c_k = \frac{1}{2\pi} \left( \int_{-\pi}^0 \tilde{g}(x) e^{-ikx} dx + \int_0^\pi \tilde{g}(x) e^{-ikx} dx \right)$.
    En substituant la définition de $\tilde{g}(x)$ :
    $c_k = \frac{1}{2\pi} \left( \int_{-\pi}^0 g(-x) e^{-ikx} dx + \int_0^\pi g(x) e^{-ikx} dx \right)$.

    Dans la première intégrale, nous effectuons le changement de variable $u=-x$:
    $\int_{-\pi}^0 g(-x) e^{-ikx} dx = \int_{\pi}^0 g(u) e^{iku} (-du) = \int_0^\pi g(u) e^{iku} du$.
    En substituant cela dans l'expression de $c_k$ et en remplaçant $u$ par $x$ (variable muette) :
    $c_k = \frac{1}{2\pi} \left( \int_0^\pi g(x) e^{ikx} dx + \int_0^\pi g(x) e^{-ikx} dx \right)$.
    Nous pouvons factoriser $g(x)$ :
    $c_k = \frac{1}{2\pi} \int_0^\pi g(x) (e^{ikx} + e^{-ikx}) dx$.
    Nous utilisons la formule d'Euler $e^{i\theta} + e^{-i\theta} = 2 \cos(\theta)$ :
    $c_k = \frac{1}{2\pi} \int_0^\pi g(x) (2 \cos(kx)) dx$.
    $c_k = \frac{1}{\pi} \int_0^\pi g(x) \cos(kx) dx$.

    D'après notre hypothèse initiale, nous savons que $\int_0^\pi g(x) \cos(nx) dx = 0$ pour tout $n \in \mathbb{N}_0$.
    Par conséquent :
    *   Si $k=0$, $c_0 = \frac{1}{\pi} \int_0^\pi g(x) \cos(0x) dx = \frac{1}{\pi} \int_0^\pi g(x) dx = 0$.
    *   Si $k \in \mathbb{N}, k \neq 0$, $c_k = \frac{1}{\pi} \int_0^\pi g(x) \cos(kx) dx = 0$.
    *   Si $k \in \mathbb{Z}, k < 0$, posons $j = -k$. Alors $j \in \mathbb{N}, j \neq 0$.
        $c_k = \frac{1}{\pi} \int_0^\pi g(x) \cos(-jx) dx = \frac{1}{\pi} \int_0^\pi g(x) \cos(jx) dx$.
        D'après notre hypothèse, $\int_0^\pi g(x) \cos(jx) dx = 0$, donc $c_k = 0$.

    Ainsi, nous avons démontré que tous les coefficients de Fourier $c_k$ de $\tilde{g}$ sont nuls pour tout $k \in \mathbb{Z}$.

    Il est un résultat fondamental de l'analyse fonctionnelle que la famille trigonométrique $\{e^{ikx}\}_{k \in \mathbb{Z}}$ forme une base hilbertienne complète de l'espace $L^2([-\pi, \pi], \mathbb{C})$. La complétude signifie que si tous les coefficients de Fourier d'une fonction dans $L^2([-\pi, \pi])$ sont nuls, alors cette fonction doit être la fonction nulle presque partout sur cet intervalle.
    Par conséquent, puisque tous ses coefficients de Fourier sont nuls, $\tilde{g}(x) = 0$ presque partout sur $[-\pi, \pi]$.

    Par définition de $\tilde{g}$, pour tout $x \in [0, \pi]$, nous avons $\tilde{g}(x) = g(x)$.
    La nullité presque partout de $\tilde{g}$ sur $[-\pi, \pi]$ implique directement que $g(x) = 0$ presque partout sur $[0, \pi]$.

    Ceci démontre la complétude de la famille orthonormée $\mathcal{B}$.
    Par conséquent, la famille $\mathcal{B} = \left\{ \frac{1}{\sqrt{\pi}} \right\} \cup \left\{ \sqrt{\frac{2}{\pi}} \cos(nx) \right\}_{n \in \mathbb{N}, n \neq 0}$ est une base hilbertienne de $L^2([0, \pi], \mathbb{C})$.