# Exercice 4 : La valeur principale de Cauchy

\subsection*{Exercice 4 : La valeur principale de Cauchy \quad $\bigstar\bigstar\bigstar\bigstar\star$}

**Énoncé :**
On définit l'action de la valeur principale de $1/x$, notée $vp(1/x)$, par : $\langle vp(1/x), \phi \rangle = \lim_{\epsilon \to 0} \int_{|x| > \epsilon} \frac{\phi(x)}{x} dx$. Montrer que cette limite existe pour tout $\phi \in \mathcal{D}(\mathbb{R})$.

**Démonstration pas à pas :**
1. **Analyse du problème :** La fonction $1/x$ n'est pas dans $L^1_{loc}$ autour de 0, donc l'intégrale classique diverge.
2. **Astuce de symétrie :** L'intégrale sur $|x| > \epsilon$ se décompose en $\int_{-R}^{-\epsilon} \frac{\phi(x)}{x} dx + \int_{\epsilon}^{R} \frac{\phi(x)}{x} dx$ (où $[-R, R]$ contient le support de $\phi$).
   Par le changement de variable $x \mapsto -x$ dans la première intégrale, on obtient :
   $$ \int_{\epsilon}^{R} \frac{\phi(x) - \phi(-x)}{x} dx $$
3. **Limites :** Par le théorème des accroissements finis ou un développement de Taylor, $\phi(x) - \phi(-x) = 2x \phi'(0) + o(x)$.
   Donc $\frac{\phi(x) - \phi(-x)}{x}$ est continue en 0 (et prolongeable par la valeur $2\phi'(0)$).
   La fonction à intégrer est donc continue sur le compact $[0, R]$, l'intégrale a donc une limite finie quand $\epsilon \to 0$.
   L'existence est démontrée. $\blacksquare$
