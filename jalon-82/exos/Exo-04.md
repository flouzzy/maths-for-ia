# Exercice 4 : Limite d'une suite de fonctions vers la masse de Dirac
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit $f_n(x) = \frac{n}{\pi (1 + n^2 x^2)}$ pour tout entier $n \ge 1$. Montrer que la suite de distributions régulières $T_{f_n}$ converge vers $\delta_0$ dans $\mathcal{D}'(\mathbb{R})$.

## Correction Détaillée
1. Dire que $T_{f_n} \to \delta_0$ dans $\mathcal{D}'(\mathbb{R})$ signifie que pour toute fonction test $\varphi \in \mathcal{D}(\mathbb{R})$, la suite complexe $\langle T_{f_n}, \varphi \rangle$ converge vers $\langle \delta_0, \varphi \rangle = \varphi(0)$.
2. Écrivons l'intégrale :
   $$ \langle T_{f_n}, \varphi \rangle = \int_{\mathbb{R}} \frac{n}{\pi (1 + n^2 x^2)} \varphi(x) \,dx $$
3. Effectuons le changement de variable $u = nx$. Alors $dx = \frac{du}{n}$, et les bornes restent inchangées.
4. L'intégrale devient :
   $$ \int_{\mathbb{R}} \frac{n}{\pi (1 + u^2)} \varphi\left(\frac{u}{n}\right) \frac{du}{n} = \int_{\mathbb{R}} \frac{1}{\pi (1 + u^2)} \varphi\left(\frac{u}{n}\right) \,du $$
5. Étudions la limite de la fonction à l'intérieur de l'intégrale. Pour tout $u \in \mathbb{R}$ fixé, quand $n \to +\infty$, $\frac{u}{n} \to 0$. Par continuité de $\varphi$, on a $\varphi\left(\frac{u}{n}\right) \to \varphi(0)$.
6. L'intégrand complet tend simplement vers $g(u) = \frac{1}{\pi (1 + u^2)} \varphi(0)$.
7. Pour intervertir limite et intégrale, utilisons le théorème de la convergence dominée. La fonction test $\varphi$ est bornée sur $\mathbb{R}$ car elle est continue à support compact. Il existe $M > 0$ tel que $|\varphi(x)| \le M$ pour tout $x$.
8. On a donc la majoration :
   $$ \left| \frac{1}{\pi (1 + u^2)} \varphi\left(\frac{u}{n}\right) \right| \le \frac{M}{\pi (1 + u^2)} $$
9. La fonction dominante $h(u) = \frac{M}{\pi (1 + u^2)}$ est intégrable sur $\mathbb{R}$ (son intégrale vaut $M$).
10. Par le théorème de la convergence dominée, on peut passer à la limite sous le signe intégrale :
    $$ \lim_{n \to \infty} \langle T_{f_n}, \varphi \rangle = \int_{\mathbb{R}} \lim_{n \to \infty} \left( \frac{1}{\pi (1 + u^2)} \varphi\left(\frac{u}{n}\right) \right) \,du = \int_{\mathbb{R}} \frac{1}{\pi (1 + u^2)} \varphi(0) \,du $$
11. On sort la constante $\varphi(0)$ de l'intégrale :
    $$ \varphi(0) \int_{\mathbb{R}} \frac{1}{\pi (1 + u^2)} \,du = \varphi(0) \left[ \frac{1}{\pi} \arctan(u) \right]_{-\infty}^{+\infty} $$
12. Calculons la valeur du crochet :
    $$ \frac{1}{\pi} \left( \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) \right) = \frac{1}{\pi} \times \pi = 1 $$
13. Finalement, la limite vaut $\varphi(0) \times 1 = \varphi(0) = \langle \delta_0, \varphi \rangle$. La suite $T_{f_n}$ converge bien vers $\delta_0$.
