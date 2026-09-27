## Exercice 3 : Phénomène de Gibbs et Série trigonométrique \quad \bigstar\bigstar\bigstar\star\star

Montrer que la série $\sum_{n=1}^\infty \frac{\sin(nx)}{n}$ converge ponctuellement mais non uniformément sur $[0, \pi]$.

**Correction :**
Ponctuellement, la série converge par le critère de Dirichlet pour les séries numériques (sommes de $\sin(nx)$ bornées et $1/n$ décroît vers 0). La limite est la fonction en dent de scie $(\pi-x)/2$ sur $]0, 2\pi[$.
Si la convergence était uniforme sur $[0,\pi]$, la fonction limite serait continue en $0$.
Or $\lim_{x \to 0^+} \frac{\pi-x}{2} = \pi/2$, mais la valeur de la série en $x=0$ est $0$. Il y a discontinuité, donc la convergence n'est pas uniforme (Phénomène de Gibbs).
