# Exercice 8 : Application aux probabilités de grands écarts

$\bigstar\bigstar\bigstar\bigstar\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables I.I.D. d'espérance $\mu = 0$ et de moment d'ordre 4 fini ($\mathbb{E}[X_1^4] = K$).
On pose $S_n = \sum_{i=1}^n X_i$.
Dans la preuve de la LFGN, on a montré que $\mathbb{E}[S_n^4] \leq 3K n^2$.
Utiliser cette majoration pour borner la probabilité $P_n = \mathbb{P}\left(\max_{1 \le k \le n} \left|\frac{S_k}{k}\right| \ge \epsilon\right)$.
*Indice : On pourra se contenter de borner $\mathbb{P}\left(\left|\frac{S_n}{n}\right| \ge \epsilon\right)$ et discuter de l'union.*

**Correction détaillée :**

1. Fixons $\epsilon > 0$. Par l'inégalité de Markov appliquée à la puissance 4 :
   $$ \mathbb{P}\left(\left|\frac{S_n}{n}\right| \geq \epsilon\right) = \mathbb{P}\left(\frac{S_n^4}{n^4} \geq \epsilon^4\right) \leq \frac{\mathbb{E}[S_n^4]}{n^4 \epsilon^4} $$
2. En injectant la borne supérieure $\mathbb{E}[S_n^4] \leq 3K n^2$ :
   $$ \mathbb{P}\left(\left|\frac{S_n}{n}\right| \geq \epsilon\right) \leq \frac{3K n^2}{n^4 \epsilon^4} = \frac{3K}{\epsilon^4 n^2} $$
3. Cette inégalité nous donne une borne de décroissance polynomiale en $O(1/n^2)$ pour l'écart de la moyenne empirique à sa cible, pour un $n$ fixé.
   C'est la sommabilité de cette borne ($\sum \frac{1}{n^2} < \infty$) qui permet d'utiliser le lemme de Borel-Cantelli.
   C'est une borne typique de probabilité de grands écarts (large deviations), bien que des outils plus puissants comme le lemme de Chernoff fourniraient une borne exponentielle en $e^{-cn}$ si on supposait l'existence d'une fonction génératrice des moments.
