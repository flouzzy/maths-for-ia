# Exercice 8 : Convergence du noyau de Fejér
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
En analyse de Fourier, le noyau de Fejér est donné par $F_n(x) = \frac{1}{2\pi n} \left( \frac{\sin(nx/2)}{\sin(x/2)} \right)^2$. Montrer que, vu comme suite de distributions sur $]-\pi, \pi[$, $F_n$ converge vers $\delta_0$. (On rappelle que $\int_{-\pi}^{\pi} F_n(x) dx = 1$ et que pour tout $\delta > 0$, $\lim_{n \to \infty} \int_{\delta < |x| < \pi} F_n(x) dx = 0$).

## Correction Détaillée
1. Soit $\varphi \in \mathcal{D}(]-\pi, \pi[)$ une fonction test. Nous devons évaluer la limite de $I_n = \langle T_{F_n}, \varphi \rangle = \int_{-\pi}^{\pi} F_n(x)\varphi(x) \,dx$.
2. Écrivons $I_n$ sous la forme :
   $$ I_n = \int_{-\pi}^{\pi} F_n(x) [\varphi(x) - \varphi(0)] \,dx + \int_{-\pi}^{\pi} F_n(x)\varphi(0) \,dx $$
3. Puisque $\int_{-\pi}^{\pi} F_n(x) dx = 1$, la deuxième intégrale vaut exactement $\varphi(0)$. Il reste à montrer que le premier terme tend vers 0.
4. Notons $J_n = \int_{-\pi}^{\pi} F_n(x) |\varphi(x) - \varphi(0)| \,dx$.
5. La fonction test $\varphi$ est continue. Par définition de la continuité en 0, pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que pour tout $|x| \le \delta$, $|\varphi(x) - \varphi(0)| < \epsilon/2$.
6. On décompose l'intégrale $J_n$ en deux parties : la région "centrale" $|x| \le \delta$ et la région "extérieure" $\delta < |x| < \pi$.
   $$ J_n = \int_{|x| \le \delta} F_n(x) |\varphi(x) - \varphi(0)| \,dx + \int_{\delta < |x| < \pi} F_n(x) |\varphi(x) - \varphi(0)| \,dx $$
7. Majorons la partie centrale. Sur $|x| \le \delta$, on a $|\varphi(x) - \varphi(0)| < \epsilon/2$. De plus, $F_n(x) \ge 0$. Donc :
   $$ \int_{|x| \le \delta} F_n(x) |\varphi(x) - \varphi(0)| \,dx \le \frac{\epsilon}{2} \int_{|x| \le \delta} F_n(x) \,dx \le \frac{\epsilon}{2} \int_{-\pi}^{\pi} F_n(x) \,dx = \frac{\epsilon}{2} \times 1 = \frac{\epsilon}{2} $$
8. Majorons la partie extérieure. $\varphi$ est continue sur un compact, elle est donc bornée. Soit $M = \sup |\varphi(x)|$. On a $|\varphi(x) - \varphi(0)| \le 2M$.
   $$ \int_{\delta < |x| < \pi} F_n(x) |\varphi(x) - \varphi(0)| \,dx \le 2M \int_{\delta < |x| < \pi} F_n(x) \,dx $$
9. Par hypothèse (propriété de concentration du noyau de Fejér), cette dernière intégrale tend vers 0 quand $n \to \infty$. Il existe donc un rang $N$ tel que pour tout $n > N$, $2M \int_{\delta < |x| < \pi} F_n(x) \,dx < \epsilon/2$.
10. Finalement, pour $n > N$, $J_n < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$. Ceci prouve que $\lim_{n \to \infty} J_n = 0$.
11. On conclut que $\lim_{n \to \infty} I_n = \varphi(0) + 0 = \langle \delta_0, \varphi \rangle$. La suite $(F_n)$ converge bien vers $\delta_0$ au sens des distributions.
