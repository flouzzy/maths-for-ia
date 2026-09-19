### Exercice 10 : Inégalité de Clarkson $\bigstar\bigstar\star\star\star$

**Énoncé :** Pour $p \ge 2$, on pose $q = \frac{p}{p-1}$. Soient $f, g \in L^p(\mu)$. Démontrer l'inégalité de Clarkson :
$\|\frac{f+g}{2}\|_p^p + \|\frac{f-g}{2}\|_p^p \le \frac{1}{2}(\|f\|_p^p + \|g\|_p^p)$.

**Correction Détaillée :**
*Analyse :* Cette inégalité quantifie l'uniforme convexité de $L^p$. Elle se déduit de l'inégalité ponctuelle $\left|\frac{a+b}{2}\right|^p + \left|\frac{a-b}{2}\right|^p \le \frac{1}{2}(|a|^p + |b|^p)$.
*Résolution pas-à-pas :*
1. On fixe $a, b \in \mathbb{R}$. Il faut d'abord prouver l'inégalité pour ces réels :
   $$\left|\frac{a+b}{2}\right|^p + \left|\frac{a-b}{2}\right|^p \le \frac{1}{2}(|a|^p + |b|^p)$$
2. La fonction $\phi(x) = |x|^p$ est convexe. De plus, sa dérivée seconde est $\phi''(x) = p(p-1)|x|^{p-2}$, qui est croissante sur $\mathbb{R}_+$.
3. Une méthode élégante consiste à utiliser l'identité $|x+y|^p + |x-y|^p$ et développer. Plus simplement, pour $p \ge 2$, la fonction $h(t) = \frac{(1+t)^p + (1-t)^p}{2} - (1+t^p)$ est positive sur $[0,1]$ par étude de fonction.
4. En posant $a = x+y, b = x-y$, on obtient $|x|^p + |y|^p \le \frac{1}{2}(|x+y|^p + |x-y|^p)$ pour $x, y$. En réinversant les rôles $x=(a+b)/2, y=(a-b)/2$, on obtient exactement l'inégalité ponctuelle cherchée.
5. On applique cette inégalité ponctuellement pour presque tout $x \in X$ aux fonctions $f(x)$ et $g(x)$ :
   $$\left|\frac{f(x)+g(x)}{2}\right|^p + \left|\frac{f(x)-g(x)}{2}\right|^p \le \frac{1}{2}(|f(x)|^p + |g(x)|^p)$$
6. Les fonctions étant mesurables et positives, on peut intégrer cette inégalité par rapport à la mesure $\mu$ :
   $$\int_X \left|\frac{f+g}{2}\right|^p d\mu + \int_X \left|\frac{f-g}{2}\right|^p d\mu \le \frac{1}{2} \left(\int_X |f|^p d\mu + \int_X |g|^p d\mu \right)$$
7. Ce qui est exactement la définition avec les normes :
   $$\|\frac{f+g}{2}\|_p^p + \|\frac{f-g}{2}\|_p^p \le \frac{1}{2}(\|f\|_p^p + \|g\|_p^p)$$
