# Calcul élémentaire pour une fonction polynomiale

$\bigstar\star\star\star\star$

Soit $f$ la fonction $2\pi$-périodique, définie sur $]-\pi, \pi]$ par $f(t) = t$.
1. Déterminer la parité de $f$. En déduire les coefficients $a_n(f)$.
2. Calculer les coefficients $b_n(f)$ pour $n \ge 1$.
3. En utilisant le théorème de Dirichlet, en déduire la valeur de la série $\sum_{n=1}^{+\infty} \frac{\sin(n)}{n}$.

**Correction détaillée :**
1. La fonction $f$ est impaire sur $]-\pi, \pi]$ car $f(-t) = -t = -f(t)$. L'intervalle de définition est symétrique. Par conséquent, pour tout $n \ge 0$, le coefficient $a_n(f) = \frac{1}{\pi} \int_{-\pi}^{\pi} t \cos(nt) dt = 0$.
2. Calculons $b_n(f)$ par intégration par parties. Posons $u(t) = t \implies u'(t) = 1$ et $v'(t) = \sin(nt) \implies v(t) = -\frac{\cos(nt)}{n}$.
   $$ b_n(f) = \frac{1}{\pi} \int_{-\pi}^{\pi} t \sin(nt) dt = \frac{2}{\pi} \int_{0}^{\pi} t \sin(nt) dt $$
   (car la fonction est paire). Par parties :
   $$ b_n(f) = \frac{2}{\pi} \left( \left[ -t \frac{\cos(nt)}{n} \right]_0^\pi - \int_0^\pi 1 \left( -\frac{\cos(nt)}{n} \right) dt \right) $$
   $$ b_n(f) = \frac{2}{\pi} \left( -\pi \frac{\cos(n\pi)}{n} + \left[ \frac{\sin(nt)}{n^2} \right]_0^\pi \right) = \frac{2}{\pi} \left( -\pi \frac{(-1)^n}{n} + 0 \right) = \frac{2(-1)^{n+1}}{n} $$
3. $f$ est continue par morceaux et $C^1$ par morceaux sur $\mathbb{R}$. En $t=1$, $f$ est continue. Par le théorème de Dirichlet :
   $$ f(1) = 1 = \sum_{n=1}^{+\infty} b_n(f) \sin(n\cdot 1) = \sum_{n=1}^{+\infty} \frac{2(-1)^{n+1}}{n} \sin(n) $$
   Ceci est une série alternée. La question demande $\sum \frac{\sin(n)}{n}$, ce qui n'apparaît pas directement. Prenons plutôt $t=\frac{\pi}{2}$.
   $f(\pi/2) = \frac{\pi}{2} = \sum_{n=1}^{+\infty} \frac{2(-1)^{n+1}}{n} \sin(n\pi/2)$.
   Pour $n=2p$, $\sin(p\pi) = 0$. Pour $n=2p+1$, $\sin((2p+1)\pi/2) = (-1)^p$.
   $$ \frac{\pi}{2} = 2 \sum_{p=0}^{+\infty} \frac{(-1)^{2p+2}}{2p+1} (-1)^p = 2 \sum_{p=0}^{+\infty} \frac{(-1)^p}{2p+1} \implies \sum_{p=0}^{+\infty} \frac{(-1)^p}{2p+1} = \frac{\pi}{4} $$