# Exercice 5 : Valeur principale de Cauchy
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé
La fonction $x \mapsto 1/x$ n'est pas localement intégrable en 0. On définit la Valeur Principale (vp) de $1/x$ par son action sur $\varphi \in \mathcal{D}(\mathbb{R})$ : $\langle \text{vp}(1/x), \varphi \rangle = \lim_{\epsilon \to 0^+} \int_{|x| > \epsilon} \frac{\varphi(x)}{x} \,dx$. Montrer que la limite existe toujours pour $\varphi \in \mathcal{D}(\mathbb{R})$.

## Correction Détaillée
1. Puisque $\varphi \in \mathcal{D}(\mathbb{R})$, son support est contenu dans un compact $[-R, R]$. L'intégrale s'écrit donc, pour $0 < \epsilon < R$ :
   $$ I_\epsilon = \int_{[-R, -\epsilon] \cup [\epsilon, R]} \frac{\varphi(x)}{x} \,dx $$
2. Séparons l'intégrale en deux parties : sur $[-R, -\epsilon]$ et sur $[\epsilon, R]$.
   $$ I_\epsilon = \int_{-R}^{-\epsilon} \frac{\varphi(x)}{x} \,dx + \int_{\epsilon}^{R} \frac{\varphi(x)}{x} \,dx $$
3. Dans la première intégrale, faisons le changement de variable $u = -x$. Alors $dx = -du$, les bornes deviennent $R$ et $\epsilon$.
   $$ \int_{-R}^{-\epsilon} \frac{\varphi(x)}{x} \,dx = \int_{R}^{\epsilon} \frac{\varphi(-u)}{-u} (-du) = \int_{R}^{\epsilon} \frac{\varphi(-u)}{u} \,du = - \int_{\epsilon}^{R} \frac{\varphi(-u)}{u} \,du $$
4. En regroupant les deux intégrales sur le même intervalle $[\epsilon, R]$ avec la variable $x$ :
   $$ I_\epsilon = \int_{\epsilon}^{R} \frac{\varphi(x)}{x} \,dx - \int_{\epsilon}^{R} \frac{\varphi(-x)}{x} \,dx = \int_{\epsilon}^{R} \frac{\varphi(x) - \varphi(-x)}{x} \,dx $$
5. Maintenant, étudions le comportement de l'intégrand lorsque $x \to 0$. Puisque $\varphi \in C^\infty$, elle admet un développement de Taylor-Lagrange à l'ordre 1 autour de 0.
   $$ \varphi(x) = \varphi(0) + x\varphi'(0) + \frac{x^2}{2}\varphi''(c_1) $$
   $$ \varphi(-x) = \varphi(0) - x\varphi'(0) + \frac{x^2}{2}\varphi''(c_2) $$
6. Formons la différence :
   $$ \varphi(x) - \varphi(-x) = 2x\varphi'(0) + \frac{x^2}{2}(\varphi''(c_1) - \varphi''(c_2)) $$
7. Divisons par $x$ :
   $$ \frac{\varphi(x) - \varphi(-x)}{x} = 2\varphi'(0) + \frac{x}{2}(\varphi''(c_1) - \varphi''(c_2)) $$
8. Lorsque $x \to 0$, cette expression admet une limite finie qui vaut $2\varphi'(0)$. La fonction $x \mapsto \frac{\varphi(x) - \varphi(-x)}{x}$ est donc prolongeable par continuité en 0.
9. Sur l'intervalle d'intégration compact $[0, R]$, cette fonction prolongée est continue. Par conséquent, elle y est Riemann-intégrable.
10. La limite de l'intégrale $I_\epsilon$ lorsque $\epsilon \to 0^+$ est exactement l'intégrale de cette fonction continue sur $[0, R]$. L'intégrale (et donc la limite) est finie. La Valeur Principale est bien définie.
