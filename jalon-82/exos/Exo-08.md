\subsection*{Exercice 8 : Changement de variable scalaire dans un Dirac \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Soit $a > 0$. Pour une fonction $f$, on définit la fonction dilatée $f_a(x) = f(ax)$. Par analogie, définir la distribution $\delta(ax)$ et exprimer $\delta(ax)$ en fonction de $\delta(x)$.

**Correction :**
Commençons par examiner le changement de variable pour une distribution régulière associée à une fonction $f$.
$$\langle T_{f_a}, \phi \rangle = \int_{-\infty}^{+\infty} f(ax) \phi(x) dx$$
Posons le changement de variable $y = ax$, alors $dy = a dx$ (car $a > 0$), soit $dx = \frac{dy}{a}$.
$$\langle T_{f_a}, \phi \rangle = \int_{-\infty}^{+\infty} f(y) \phi(y/a) \frac{dy}{a} = \left\langle T_f, \frac{1}{a} \phi(\cdot / a) \right\rangle$$
On étend cette définition pour toute distribution $T$ : on pose $\langle T(ax), \phi(x) \rangle = \langle T, \frac{1}{a} \phi(x/a) \rangle$. Si $a < 0$, l'inversion des bornes donne $\frac{1}{|a|}$. Généralisons : $\langle T(ax), \phi \rangle = \langle T, \frac{1}{|a|} \phi(\cdot / a) \rangle$.
Appliquons cela au Dirac :
$$\langle \delta(ax), \phi(x) \rangle = \left\langle \delta(x), \frac{1}{|a|} \phi(x/a) \right\rangle$$
Par définition du Dirac (évaluation en 0) :
$$= \frac{1}{|a|} \phi(0/a) = \frac{1}{|a|} \phi(0) = \frac{1}{|a|} \langle \delta(x), \phi(x) \rangle$$
On en déduit donc l'égalité formelle (au sens des distributions) :
$$\delta(ax) = \frac{1}{|a|} \delta(x)$$
