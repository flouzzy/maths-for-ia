### Exercice 7 : Interpolation des espaces $L^p$ $\bigstar\bigstar\bigstar$

**Énoncé :** Soit $1 \le p \le r \le q \le +\infty$. Montrer que si $f \in L^p \cap L^q$, alors $f \in L^r$, et il existe $\theta \in [0, 1]$ tel que $\|f\|_r \le \|f\|_p^\theta \|f\|_q^{1-\theta}$. Expliciter $\theta$.

**Correction Détaillée :**
*Analyse :* On cherche à écrire $r$ comme une combinaison de $p$ et $q$. On utilise Hölder.
*Résolution pas-à-pas :*
1. Si $p=r=q$, c'est trivial avec $\theta = 1$. Supposons $p < r < q$.
2. On cherche $\theta \in ]0, 1[$ tel que $\frac{1}{r} = \frac{\theta}{p} + \frac{1-\theta}{q}$. On trouve $\theta = \frac{1/r - 1/q}{1/p - 1/q}$.
3. On écrit l'intégrale de $|f|^r$ en séparant l'exposant : $|f|^r = |f|^{\theta r} |f|^{(1-\theta)r}$.
4. On applique Hölder à ce produit. Il faut choisir des exposants conjugués $u, v$. On prend $u = \frac{p}{\theta r}$ et $v = \frac{q}{(1-\theta)r}$.
5. Vérifions que $u, v$ sont conjugués : $\frac{1}{u} + \frac{1}{v} = \frac{\theta r}{p} + \frac{(1-\theta)r}{q} = r(\frac{\theta}{p} + \frac{1-\theta}{q}) = r(\frac{1}{r}) = 1$.
6. L'inégalité de Hölder donne :
   $$\int |f|^r = \int |f|^{\theta r} |f|^{(1-\theta)r} \le \left( \int (|f|^{\theta r})^u \right)^{1/u} \left( \int (|f|^{(1-\theta)r})^v \right)^{1/v}$$
7. On remplace $u$ et $v$ :
   $$\int |f|^r \le \left( \int |f|^p \right)^{\frac{\theta r}{p}} \left( \int |f|^q \right)^{\frac{(1-\theta)r}{q}}$$
8. On élève à la puissance $1/r$ :
   $$\|f\|_r \le \left( \int |f|^p \right)^{\frac{\theta}{p}} \left( \int |f|^q \right)^{\frac{1-\theta}{q}} = \|f\|_p^\theta \|f\|_q^{1-\theta}$$
