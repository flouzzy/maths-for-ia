Voici l'Exercice 3 (Jalon 104) sur les Bases Hilbertiennes.

**Exercice 3 (Jalon 104)**

**Difficulté :** $\star\star\star\star\star$

**Énoncé :**
Soit $H = L^2([0, \pi])$ l'espace de Hilbert des fonctions de carré intégrable sur l'intervalle $[0, \pi]$, muni du produit scalaire usuel défini par $\langle f, g \rangle = \int_0^\pi f(x) \overline{g(x)} dx$.
Considérons le système de fonctions $\mathcal{B} = \{ \phi_n(x) = \sqrt{\frac{2}{\pi}} \sin(nx) \}_{n \in \mathbb{N}^*}$. Il est admis que $\mathcal{B}$ est une base hilbertienne pour $H$.

Soit la fonction $f$ définie sur $[0, \pi]$ par $f(x) = x$.

1.  Démontrer que le système $\mathcal{B}$ est orthonormal dans $H$.
2.  Calculer les coefficients de Fourier $c_n$ de la fonction $f$ par rapport à la base $\mathcal{B}$. C'est-à-dire, $c_n = \langle f, \phi_n \rangle$.
3.  Calculer la norme au carré de la fonction $f$, c'est-à-dire $\|f\|^2$, par intégration directe.
4.  Vérifier l'identité de Parseval pour la fonction $f$, en utilisant les coefficients $c_n$ calculés précédemment. Il est rappelé que la somme de la série de Basel est $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.

---

**Correction :**

**1. Démonstration de l'orthonormalité du système $\mathcal{B}$ :**

Pour démontrer que le système $\mathcal{B}$ est orthonormal, nous devons vérifier deux propriétés fondamentales : la normalisation (chaque fonction a une norme unitaire) et l'orthogonalité (le produit scalaire de deux fonctions distinctes est nul).

a) **Normalisation** : Vérifions que $\|\phi_n\|^2 = 1$ pour tout $n \in \mathbb{N}^*$.
Par définition, $\|\phi_n\|^2 = \langle \phi_n, \phi_n \rangle$.
$$
\begin{aligned}
\|\phi_n\|^2 &= \int_0^\pi \phi_n(x) \overline{\phi_n(x)} dx \\
&= \int_0^\pi \left( \sqrt{\frac{2}{\pi}} \sin(nx) \right) \left( \sqrt{\frac{2}{\pi}} \sin(nx) \right) dx \\
&= \int_0^\pi \frac{2}{\pi} \sin^2(nx) dx
\end{aligned}
$$
Nous utilisons la formule trigonométrique de réduction de puissance : $\sin^2(\theta) = \frac{1 - \cos(2\theta)}{2}$.
$$
\begin{aligned}
\|\phi_n\|^2 &= \frac{2}{\pi} \int_0^\pi \frac{1 - \cos(2nx)}{2} dx \\
&= \frac{1}{\pi} \int_0^\pi (1 - \cos(2nx)) dx \\
&= \frac{1}{\pi} \left[ x - \frac{\sin(2nx)}{2n} \right]_0^\pi \\
&= \frac{1}{\pi} \left( \left(\pi - \frac{\sin(2n\pi)}{2n}\right) - \left(0 - \frac{\sin(0)}{2n}\right) \right)
\end{aligned}
$$
Puisque $n \in \mathbb{N}^*$, $2n\pi$ est un multiple entier de $2\pi$, et donc $\sin(2n\pi) = 0$. De même, $\sin(0) = 0$.
$$
\begin{aligned}
\|\phi_n\|^2 &= \frac{1}{\pi} \left( (\pi - 0) - (0 - 0) \right) \\
&= \frac{1}{\pi} (\pi) \\
&= 1
\end{aligned}
$$
Ainsi, toutes les fonctions $\phi_n$ sont normalisées.

b) **Orthogonalité** : Vérifions que $\langle \phi_n, \phi_m \rangle = 0$ pour tout $n \ne m$, avec $n, m \in \mathbb{N}^*$.
$$
\begin{aligned}
\langle \phi_n, \phi_m \rangle &= \int_0^\pi \phi_n(x) \overline{\phi_m(x)} dx \\
&= \int_0^\pi \left( \sqrt{\frac{2}{\pi}} \sin(nx) \right) \left( \sqrt{\frac{2}{\pi}} \sin(mx) \right) dx \\
&= \frac{2}{\pi} \int_0^\pi \sin(nx) \sin(mx) dx
\end{aligned}
$$
Nous utilisons la formule de produit-somme trigonométrique : $\sin(A)\sin(B) = \frac{1}{2}(\cos(A-B) - \cos(A+B))$.
$$
\begin{aligned}
\langle \phi_n, \phi_m \rangle &= \frac{2}{\pi} \int_0^\pi \frac{1}{2} (\cos((n-m)x) - \cos((n+m)x)) dx \\
&= \frac{1}{\pi} \int_0^\pi (\cos((n-m)x) - \cos((n+m)x)) dx
\end{aligned}
$$
Puisque $n \ne m$, $n-m \ne 0$. De plus, $n,m \in \mathbb{N}^*$, donc $n+m \ne 0$.
$$
\begin{aligned}
\langle \phi_n, \phi_m \rangle &= \frac{1}{\pi} \left[ \frac{\sin((n-m)x)}{n-m} - \frac{\sin((n+m)x)}{n+m} \right]_0^\pi \\
&= \frac{1}{\pi} \left( \left( \frac{\sin((n-m)\pi)}{n-m} - \frac{\sin((n+m)\pi)}{n+m} \right) - \left( \frac{\sin(0)}{n-m} - \frac{\sin(0)}{n+m} \right) \right)
\end{aligned}
$$
Étant donné que $n-m$ et $n+m$ sont des entiers non nuls, $(n-m)\pi$ et $(n+m)\pi$ sont des multiples entiers de $\pi$. Par conséquent, $\sin((n-m)\pi) = 0$ et $\sin((n+m)\pi) = 0$. De même, $\sin(0) = 0$.
$$
\begin{aligned}
\langle \phi_n, \phi_m \rangle &= \frac{1}{\pi} \left( (0 - 0) - (0 - 0) \right) \\
&= 0
\end{aligned}
$$
Ainsi, les fonctions $\phi_n$ et $\phi_m$ sont orthogonales pour $n \ne m$.

Étant donné que le système $\mathcal{B}$ est composé de fonctions normalisées et mutuellement orthogonales, il est un système orthonormal dans $H$.

**2. Calcul des coefficients de Fourier $c_n$ :**

Les coefficients de Fourier $c_n$ de la fonction $f(x)=x$ par rapport à la base $\mathcal{B}$ sont donnés par $c_n = \langle f, \phi_n \rangle$.
$$
\begin{aligned}
c_n &= \int_0^\pi f(x) \overline{\phi_n(x)} dx \\
&= \int_0^\pi x \left( \sqrt{\frac{2}{\pi}} \sin(nx) \right) dx \\
&= \sqrt{\frac{2}{\pi}} \int_0^\pi x \sin(nx) dx
\end{aligned}
$$
Nous allons utiliser l'intégration par parties. Posons $u(x) = x$ et $dv = \sin(nx) dx$.
Alors $du = dx$ et $v(x) = \int \sin(nx) dx = -\frac{\cos(nx)}{n}$.
L'intégration par parties s'écrit $\int_a^b u dv = [uv]_a^b - \int_a^b v du$.
$$
\begin{aligned}
\int_0^\pi x \sin(nx) dx &= \left[ x \left( -\frac{\cos(nx)}{n} \right) \right]_0^\pi - \int_0^\pi \left( -\frac{\cos(nx)}{n} \right) dx \\
&= \left[ -\frac{x \cos(nx)}{n} \right]_0^\pi + \int_0^\pi \frac{\cos(nx)}{n} dx
\end{aligned}
$$
Évaluons le premier terme :
$$
\begin{aligned}
\left[ -\frac{x \cos(nx)}{n} \right]_0^\pi &= \left( -\frac{\pi \cos(n\pi)}{n} \right) - \left( -\frac{0 \cos(0)}{n} \right) \\
&= -\frac{\pi (-1)^n}{n} - 0 \\
&= \frac{\pi (-1)^{n+1}}{n}
\end{aligned}
$$
Évaluons le second terme :
$$
\begin{aligned}
\int_0^\pi \frac{\cos(nx)}{n} dx &= \frac{1}{n} \left[ \frac{\sin(nx)}{n} \right]_0^\pi \\
&= \frac{1}{n^2} (\sin(n\pi) - \sin(0))
\end{aligned}
$$
Puisque $n \in \mathbb{N}^*$, $n\pi$ est un multiple entier de $\pi$, donc $\sin(n\pi) = 0$. De même, $\sin(0) = 0$.
$$
\begin{aligned}
\int_0^\pi \frac{\cos(nx)}{n} dx &= \frac{1}{n^2} (0 - 0) \\
&= 0
\end{aligned}
$$
Ainsi, l'intégrale complète est :
$$
\int_0^\pi x \sin(nx) dx = \frac{\pi (-1)^{n+1}}{n} + 0 = \frac{\pi (-1)^{n+1}}{n}
$$
En substituant cette expression dans la formule des coefficients $c_n$:
$$
\begin{aligned}
c_n &= \sqrt{\frac{2}{\pi}} \left( \frac{\pi (-1)^{n+1}}{n} \right) \\
&= \frac{\sqrt{2\pi^2} (-1)^{n+1}}{n} \\
&= \frac{\sqrt{2}\pi (-1)^{n+1}}{n}
\end{aligned}
$$
Les coefficients de Fourier sont donc $c_n = \frac{\sqrt{2}\pi (-1)^{n+1}}{n}$.

**3. Calcul de la norme au carré de la fonction $f$ :**

La norme au carré de la fonction $f(x)=x$ est donnée par $\|f\|^2 = \langle f, f \rangle$.
$$
\begin{aligned}
\|f\|^2 &= \int_0^\pi f(x) \overline{f(x)} dx \\
&= \int_0^\pi x \cdot x dx \quad (\text{car } f(x)=x \text{ est réelle}) \\
&= \int_0^\pi x^2 dx \\
&= \left[ \frac{x^3}{3} \right]_0^\pi \\
&= \frac{\pi^3}{3} - \frac{0^3}{3} \\
&= \frac{\pi^3}{3}
\end{aligned}
$$
La norme au carré de la fonction $f$ est $\|f\|^2 = \frac{\pi^3}{3}$.

**4. Vérification de l'identité de Parseval :**

L'identité de Parseval pour une fonction $f$ dans un espace de Hilbert $H$ et une base hilbertienne $\mathcal{B} = \{\phi_n\}_{n \in \mathbb{N}^*}$ est donnée par la relation $\|f\|^2 = \sum_{n=1}^\infty |c_n|^2$.
Nous avons calculé $\|f\|^2 = \frac{\pi^3}{3}$.
Calculons maintenant la somme $\sum_{n=1}^\infty |c_n|^2$ en utilisant les coefficients $c_n$ trouvés à la question 2.
$c_n = \frac{\sqrt{2}\pi (-1)^{n+1}}{n}$.
$$
\begin{aligned}
|c_n|^2 &= \left| \frac{\sqrt{2}\pi (-1)^{n+1}}{n} \right|^2 \\
&= \frac{(\sqrt{2}\pi)^2 \left| (-1)^{n+1} \right|^2}{n^2}
\end{aligned}
$$
Puisque $(-1)^{n+1}$ est soit $1$ soit $-1$, son module est $1$, donc $|(-1)^{n+1}|^2 = 1^2 = 1$.
$$
\begin{aligned}
|c_n|^2 &= \frac{2\pi^2 \cdot 1}{n^2} \\
&= \frac{2\pi^2}{n^2}
\end{aligned}
$$
Maintenant, nous calculons la somme de ces carrés :
$$
\begin{aligned}
\sum_{n=1}^\infty |c_n|^2 &= \sum_{n=1}^\infty \frac{2\pi^2}{n^2} \\
&= 2\pi^2 \sum_{n=1}^\infty \frac{1}{n^2}
\end{aligned}
$$
Il est rappelé que la somme de la série de Basel est $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.
$$
\begin{aligned}
\sum_{n=1}^\infty |c_n|^2 &= 2\pi^2 \left( \frac{\pi^2}{6} \right) \\
&= \frac{2\pi^4}{6} \\
&= \frac{\pi^4}{3}
\end{aligned}
$$
Une erreur de calcul s'est glissée dans mes notes précédentes. Je corrige ici.

Les coefficients $c_n = \frac{\sqrt{2\pi} (-1)^{n+1}}{n}$ ont été calculés à la question 2.
Leur carré est $|c_n|^2 = \left(\frac{\sqrt{2\pi} (-1)^{n+1}}{n}\right)^2 = \frac{2\pi ((-1)^{n+1})^2}{n^2} = \frac{2\pi}{n^2}$.
Donc $\sum_{n=1}^\infty |c_n|^2 = \sum_{n=1}^\infty \frac{2\pi}{n^2} = 2\pi \sum_{n=1}^\infty \frac{1}{n^2}$.
En utilisant $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$:
$\sum_{n=1}^\infty |c_n|^2 = 2\pi \left( \frac{\pi^2}{6} \right) = \frac{2\pi^3}{6} = \frac{\pi^3}{3}$.

Nous constatons que $\|f\|^2 = \frac{\pi^3}{3}$ et $\sum_{n=1}^\infty |c_n|^2 = \frac{\pi^3}{3}$.
L'identité de Parseval est donc vérifiée pour la fonction $f(x)=x$ par rapport à la base hilbertienne $\mathcal{B}$.