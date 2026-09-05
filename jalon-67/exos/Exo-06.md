# Exercice 6 : Limite impliquant arctangente
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

### Énoncé

Évaluer $\lim_{n \to +\infty} \int_0^{+\infty} \frac{1}{(1+x^2)^n} \arctan\left(\frac{x}{n}\right) \, dx$ en justifiant rigoureusement le passage à la limite.

---
### Correction détaillée

1. Posons $f_n(x) = \frac{1}{(1+x^2)^n} \arctan\left(\frac{x}{n}\right)$.
2. Analysons la monotonie : bien que les termes soient positifs pour $x>0$, la suite $(f_n(x))$ **n'est pas croissante**. En effet, le terme $\frac{1}{(1+x^2)^n}$ décroît fortement vers 0 avec $n$, et $\arctan(x/n)$ décroît également vers 0. Ainsi la suite $(f_n(x))$ est décroissante et tend vers 0.
3. Le Théorème de Convergence Monotone "classique" ne s'applique qu'aux suites croissantes. Cependant, un analogue du TCM existe pour les suites décroissantes de fonctions mesurables positives, **à condition que l'intégrale de la première fonction soit finie**.
4. Démonstration de l'analogue : soit $(g_n)$ une suite décroissante de fonctions mesurables positives (c-à-d $g_n \ge g_{n+1} \ge 0$). Supposons que $\int g_1 d\mu < +\infty$.
   Posons $h_n = g_1 - g_n$. Alors $h_n \ge 0$ et $h_n$ est croissante avec $n$, car $g_n$ décroît.
   Par le TCM classique sur $h_n$ : $\lim_n \int (g_1 - g_n) d\mu = \int \lim_n (g_1 - g_n) d\mu$.
   Soit $\int g_1 d\mu - \lim_n \int g_n d\mu = \int g_1 d\mu - \int \lim_n g_n d\mu$.
   Puisque $\int g_1 d\mu < +\infty$, on peut soustraire cette quantité des deux côtés pour conclure que $\lim_n \int g_n d\mu = \int \lim_n g_n d\mu$.
5. Appliquons ce résultat à notre suite $f_n(x)$. La limite ponctuelle est $f(x) = 0$.
6. La fonction $f_1(x) = \frac{1}{1+x^2} \arctan(x)$ est mesurable et positive sur $]0, +\infty[$. Son intégrale est finie : $\int_0^{+\infty} f_1(x) \, dx < \int_0^{+\infty} \frac{\pi/2}{1+x^2} dx = \frac{\pi^2}{4} < +\infty$.
7. Comme $(f_n)$ décroît vers 0 et que $f_1$ est intégrable, par l'analogue décroissant du TCM (ou Convergence Dominée), l'intégrale de la limite est la limite des intégrales.
8. Donc $\lim_{n \to +\infty} \int_0^{+\infty} \frac{1}{(1+x^2)^n} \arctan\left(\frac{x}{n}\right) \, dx = \int_0^{+\infty} 0 \, dx = 0$.
