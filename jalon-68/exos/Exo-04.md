## Exercice 4 : Fonction intégrable mais non bornée \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit l'espace mesuré $]0, 1]$ muni de la mesure de Lebesgue $\lambda$.
Considérons la fonction $f(x) = \frac{1}{\sqrt{x}}$.
1. Montrer que $f$ n'est pas bornée sur $]0, 1]$.
2. Montrer que $f$ est intégrable sur cet espace et calculer son intégrale.

**Correction :**
1. $\lim_{x \to 0^+} \frac{1}{\sqrt{x}} = +\infty$. La fonction prend des valeurs arbitrairement grandes près de 0, elle n'est donc pas bornée sur $]0, 1]$.
2. Pour montrer que $f$ est intégrable, il faut montrer que $\int_{]0,1]} |f| d\lambda < \infty$.
   Comme $f$ est positive, $|f| = f$. Pour calculer l'intégrale de Lebesgue, on peut utiliser l'intégrale de Riemann généralisée, car la fonction est continue sur $]0,1]$.
   $\int_{]0, 1]} \frac{1}{\sqrt{x}} d\lambda = \lim_{\epsilon \to 0^+} \int_{\epsilon}^{1} x^{-1/2} dx = \lim_{\epsilon \to 0^+} [2x^{1/2}]_{\epsilon}^{1} = \lim_{\epsilon \to 0^+} (2 - 2\sqrt{\epsilon}) = 2$.
   L'intégrale est finie, donc $f \in \mathcal{L}^1(\lambda)$.
