**Exercice 6 (Jalon 104) - Bases Hilbertiennes**

**Difficulté :** $\bigstar$$\bigstar$$\bigstar$$\star$$\star$

Soit $H = L^2([0, 2\pi], \mathbb{C})$ l'espace de Hilbert des fonctions de carré sommable sur l'intervalle $[0, 2\pi]$, à valeurs complexes. Le produit scalaire usuel sur $H$ est défini par :
$$ \langle f, g \rangle = \int_0^{2\pi} f(x) \overline{g(x)} dx $$
où $\overline{g(x)}$ désigne le conjugué complexe de $g(x)$.

Considérons la famille de fonctions $\mathcal{B} = \{e_n \mid n \in \mathbb{Z}\}$ définie par $e_n(x) = \frac{1}{\sqrt{2\pi}} e^{inx}$ pour tout $x \in [0, 2\pi]$.

1.  Démontrer que $\mathcal{B}$ est un système orthonormal dans $H$.
2.  Démontrer que $\mathcal{B}$ est une base hilbertienne de $H$.

---

**Correction de l'Exercice 6**

Soit $H = L^2([0, 2\pi], \mathbb{C})$ muni du produit scalaire $\langle f, g \rangle = \int_0^{2\pi} f(x) \overline{g(x)} dx$.
La famille de fonctions considérée est $\mathcal{B} = \{e_n(x) = \frac{1}{\sqrt{2\pi}} e^{inx} \mid n \in \mathbb{Z}\}$.

**1. Démonstration que $\mathcal{B}$ est un système orthonormal.**

Pour qu'une famille de fonctions soit un système orthonormal, il est nécessaire que pour tous $n, m \in \mathbb{Z}$, le produit scalaire $\langle e_n, e_m \rangle$ satisfasse $\langle e_n, e_m \rangle = \delta_{nm}$, où $\delta_{nm}$ est le symbole de Kronecker ($\delta_{nm} = 1$ si $n=m$ et $\delta_{nm} = 0$ si $n \neq m$).

Calculons le produit scalaire $\langle e_n, e_m \rangle$ :
$$ \langle e_n, e_m \rangle = \int_0^{2\pi} e_n(x) \overline{e_m(x)} dx $$
Substituons les expressions des fonctions $e_n(x)$ et $e_m(x)$ :
$$ e_n(x) = \frac{1}{\sqrt{2\pi}} e^{inx} $$
Le conjugué complexe de $e_m(x)$ est :
$$ \overline{e_m(x)} = \overline{\left(\frac{1}{\sqrt{2\pi}} e^{imx}\right)} = \frac{1}{\sqrt{2\pi}} \overline{e^{imx}} = \frac{1}{\sqrt{2\pi}} e^{-imx} $$
Le produit scalaire devient alors :
$$ \langle e_n, e_m \rangle = \int_0^{2\pi} \left(\frac{1}{\sqrt{2\pi}} e^{inx}\right) \left(\frac{1}{\sqrt{2\pi}} e^{-imx}\right) dx $$
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{inx} e^{-imx} dx $$
En utilisant la propriété des exponentielles $e^a e^b = e^{a+b}$ :
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{i(n-m)x} dx $$

Nous devons analyser cette intégrale selon deux cas : $n=m$ et $n \neq m$.

**Cas 1 : $n=m$}
Si $n=m$, alors $n-m = 0$. L'intégrale prend la forme :
$$ \langle e_n, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{i(0)x} dx $$
$$ \langle e_n, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^0 dx $$
Puisque $e^0 = 1$ :
$$ \langle e_n, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} 1 dx $$
L'intégrale de 1 sur $[0, 2\pi]$ est simplement la longueur de l'intervalle :
$$ \langle e_n, e_n \rangle = \frac{1}{2\pi} [x]_0^{2\pi} $$
$$ \langle e_n, e_n \rangle = \frac{1}{2\pi} (2\pi - 0) $$
$$ \langle e_n, e_n \rangle = \frac{2\pi}{2\pi} = 1 $$
Pour $n=m$, le produit scalaire est 1. Cela signifie que chaque fonction $e_n$ est de norme 1 (unitaire), car $\|e_n\| = \sqrt{\langle e_n, e_n \rangle} = \sqrt{1} = 1$.

**Cas 2 : $n \neq m$}
Si $n \neq m$, alors $n-m \neq 0$. Soit $k = n-m$. L'intégrale devient :
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{ikx} dx $$
La primitive de $e^{ikx}$ pour $k \neq 0$ est $\frac{1}{ik} e^{ikx}$ :
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi} \left[ \frac{1}{ik} e^{ikx} \right]_0^{2\pi} $$
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi ik} (e^{ik(2\pi)} - e^{ik(0)}) $$
Puisque $k$ est un entier non nul, $e^{ik(2\pi)} = (e^{i2\pi})^k = 1^k = 1$. De même, $e^{ik(0)} = e^0 = 1$.
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi ik} (1 - 1) $$
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi ik} (0) = 0 $$
Pour $n \neq m$, le produit scalaire est 0. Cela signifie que les fonctions $e_n$ et $e_m$ sont orthogonales.

En regroupant les deux cas, nous avons démontré que $\langle e_n, e_m \rangle = \delta_{nm}$.
Par conséquent, la famille $\mathcal{B}$ est un système orthonormal dans $H$.

**2. Démonstration que $\mathcal{B}$ est une base hilbertienne de $H$.**

Un système orthonormal est une base hilbertienne si et seulement s'il est complet. Un système orthonormal $\mathcal{B} = \{e_n \mid n \in \mathbb{Z}\}$ est complet si le seul élément $f \in H$ qui est orthogonal à tous les éléments de $\mathcal{B}$ est le vecteur nul. Autrement dit, si $\langle f, e_n \rangle = 0$ pour tout $n \in \mathbb{Z}$, alors $f$ doit être la fonction nulle presque partout sur $[0, 2\pi]$.

Supposons que $f \in L^2([0, 2\pi])$ est telle que $\langle f, e_n \rangle = 0$ pour tout $n \in \mathbb{Z}$.
$$ \langle f, e_n \rangle = \int_0^{2\pi} f(x) \overline{e_n(x)} dx = 0 $$
En substituant l'expression de $\overline{e_n(x)} = \frac{1}{\sqrt{2\pi}} e^{-inx}$ :
$$ \int_0^{2\pi} f(x) \frac{1}{\sqrt{2\pi}} e^{-inx} dx = 0 $$
Puisque $\frac{1}{\sqrt{2\pi}}$ est une constante non nulle, nous pouvons la multiplier par $\sqrt{2\pi}$ (ou simplement diviser par elle) pour obtenir :
$$ \int_0^{2\pi} f(x) e^{-inx} dx = 0 \quad \text{pour tout } n \in \mathbb{Z} $$
Ces intégrales sont les coefficients de Fourier de la fonction $f$ (à un facteur constant près si la définition diffère). L'hypothèse est donc que tous les coefficients de Fourier de $f$ sont nuls. Nous devons en déduire que $f$ est la fonction nulle presque partout.

Pour cela, nous utilisons un argument de densité.
Considérons l'espace des polynômes trigonométriques, noté $T$. Un polynôme trigonométrique $P(x)$ est une fonction de la forme :
$$ P(x) = \sum_{k=-N}^N c_k e^{ikx} $$
où $N$ est un entier positif et $c_k \in \mathbb{C}$ sont des coefficients complexes.

Si $\int_0^{2\pi} f(x) e^{-inx} dx = 0$ pour tout $n \in \mathbb{Z}$, alors $f$ est orthogonal à chaque fonction $e^{-inx}$.
Calculons le produit scalaire de $f$ avec un polynôme trigonométrique $P(x)$ arbitraire :
$$ \langle f, P \rangle = \int_0^{2\pi} f(x) \overline{P(x)} dx $$
Substituons l'expression de $P(x)$ et son conjugué :
$$ \overline{P(x)} = \overline{\left(\sum_{k=-N}^N c_k e^{ikx}\right)} = \sum_{k=-N}^N \overline{c_k} \overline{e^{ikx}} = \sum_{k=-N}^N \overline{c_k} e^{-ikx} $$
Le produit scalaire devient :
$$ \langle f, P \rangle = \int_0^{2\pi} f(x) \left(\sum_{k=-N}^N \overline{c_k} e^{-ikx}\right) dx $$
Par linéarité de l'intégrale (la somme est finie, donc l'échange est valide) :
$$ \langle f, P \rangle = \sum_{k=-N}^N \overline{c_k} \int_0^{2\pi} f(x) e^{-ikx} dx $$
Puisque nous avons établi que $\int_0^{2\pi} f(x) e^{-ikx} dx = 0$ pour tout $k \in \mathbb{Z}$ :
$$ \langle f, P \rangle = \sum_{k=-N}^N \overline{c_k} \cdot 0 = 0 $$
Ainsi, $f$ est orthogonal à tout polynôme trigonométrique $P(x)$.

Le théorème de Stone-Weierstrass, sous sa forme trigonométrique, stipule que l'ensemble des polynômes trigonométriques $T$ est dense dans l'espace $C([0, 2\pi])$ des fonctions continues sur $[0, 2\pi]$ (avec $f(0)=f(2\pi)$ pour garantir la périodicité nécessaire à la convergence des séries de Fourier) pour la norme uniforme.
De plus, l'espace $C([0, 2\pi])$ est dense dans $L^2([0, 2\pi])$ pour la norme $L^2$.
Par conséquent, l'ensemble des polynômes trigonométriques $T$ est dense dans $L^2([0, 2\pi])$. Cela signifie que pour toute fonction $g \in L^2([0, 2\pi])$, il existe une suite $(P_j)_{j \in \mathbb{N}}$ de polynômes trigonométriques telle que $P_j$ converge vers $g$ dans la norme $L^2$, c'est-à-dire $\|P_j - g\|_{L^2} \to 0$ lorsque $j \to \infty$.

Nous avons montré que $f$ est orthogonal à tout $P_j$, donc $\langle f, P_j \rangle = 0$ pour tout $j \in \mathbb{N}$.
Considérons le produit scalaire de $f$ avec une fonction $g \in L^2([0, 2\pi])$ quelconque. En raison de la continuité du produit scalaire dans un espace de Hilbert :
$$ \langle f, g \rangle = \langle f, \lim_{j \to \infty} P_j \rangle $$
$$ \langle f, g \rangle = \lim_{j \to \infty} \langle f, P_j \rangle $$
Puisque $\langle f, P_j \rangle = 0$ pour tous les $j$ :
$$ \langle f, g \rangle = \lim_{j \to \infty} 0 = 0 $$
Donc, $f$ est orthogonale à toute fonction $g \in L^2([0, 2\pi])$.
En particulier, en choisissant $g=f$, nous obtenons :
$$ \langle f, f \rangle = 0 $$
Par définition du produit scalaire, $\langle f, f \rangle = \|f\|^2$. Donc $\|f\|^2 = 0$.
Dans un espace normé, $\|f\|^2 = 0$ implique que $f$ est le vecteur nul. Dans $L^2([0, 2\pi])$, cela signifie que $f(x) = 0$ pour presque tout $x \in [0, 2\pi]$.

Puisque la seule fonction $f \in L^2([0, 2\pi])$ orthogonale à tous les éléments du système $\mathcal{B}$ est la fonction nulle, le système orthonormal $\mathcal{B}$ est complet.
Par définition, un système orthonormal complet est une base hilbertienne.

Donc, $\mathcal{B} = \{e_n(x) = \frac{1}{\sqrt{2\pi}} e^{inx} \mid n \in \mathbb{Z}\}$ est une base hilbertienne de $L^2([0, 2\pi], \mathbb{C})$.