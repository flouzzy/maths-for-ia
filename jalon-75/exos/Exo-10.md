\subsection*{Exercice 10 : Convergence faible dans l'espace de Hilbert $L^2$ \quad $\bigstar\bigstar\star$}
**Énoncé :**
Sur $L^2([0,2\pi])$, on considère la suite de fonctions $f_n(x) = \sin(nx)$.
1. Montrer que pour toute fonction $g \in L^2$, $\langle f_n, g \rangle = \int_0^{2\pi} f_n(x)g(x) \, dx \to 0$. On dit que $f_n$ converge faiblement vers $0$.
2. Montrer que $(f_n)$ ne converge pas fortement (en norme $L^2$) vers $0$.

**Correction détaillée :**
1. Par le théorème de Fourier (ou le lemme de Riemann-Lebesgue), toute fonction $g \in L^2$ a des coefficients de Fourier $\int_0^{2\pi} g(x)\sin(nx)\,dx$ qui tendent vers 0 lorsque $n \to \infty$ (car la série des carrés des coefficients converge, ils doivent donc tendre vers 0). Par conséquent, $\langle f_n, g \rangle \to 0$. $f_n$ converge faiblement vers $0$.
2. Calculons la norme $L^2$ de $f_n$ :
   $\|f_n\|_2^2 = \int_0^{2\pi} \sin^2(nx) \, dx = \int_0^{2\pi} \frac{1 - \cos(2nx)}{2} \, dx = \left[ \frac{x}{2} - \frac{\sin(2nx)}{4n} \right]_0^{2\pi} = \pi$.
   Ainsi, $\|f_n\|_2 = \sqrt{\pi} \neq 0$. La norme ne tend pas vers 0, la suite ne converge pas fortement dans $L^2$.
C'est un phénomène typique de dimension infinie : une suite de vecteurs peut tendre vers 0 "directionnellement" pour chaque coordonnée sans que sa norme (sa taille) ne diminue. \qed
