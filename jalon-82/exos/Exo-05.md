\subsection*{Exercice 5 : Distribution associée à la valeur absolue \quad $\bigstar\bigstar\bigstar\star\star$}

**Énoncé :**
Montrer que la fonction $f(x) = |x|$ définit une distribution régulière et expliciter son action.

**Correction :**
La fonction $f(x) = |x|$ est continue sur $\mathbb{R}$. Toute fonction continue est localement intégrable (car bornée sur tout compact). Elle définit donc une distribution régulière $T_{|x|}$.
Pour toute fonction $\phi \in \mathcal{D}(\mathbb{R})$ :
$$\langle T_{|x|}, \phi \rangle = \int_{-\infty}^{+\infty} |x| \phi(x) dx$$
On sépare l'intégrale en $0$ car l'expression de $|x|$ change de signe :
$$\langle T_{|x|}, \phi \rangle = \int_{-\infty}^0 (-x) \phi(x) dx + \int_0^{+\infty} (x) \phi(x) dx$$
$$\langle T_{|x|}, \phi \rangle = \int_0^{+\infty} x \phi(x) dx - \int_{-\infty}^0 x \phi(x) dx$$
