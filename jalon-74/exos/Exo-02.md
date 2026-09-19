### Exercice 2 : Hölder discrète $\bigstar\bigstar$

**Énoncé :** Soient $x_1, \dots, x_n$ et $y_1, \dots, y_n$ des réels positifs. Soient $p, q > 1$ conjugués. Montrer que $\sum_{i=1}^n x_i y_i \le \left(\sum_{i=1}^n x_i^p\right)^{1/p} \left(\sum_{i=1}^n y_i^q\right)^{1/q}$.

**Correction Détaillée :**
*Analyse :* C'est l'inégalité de Hölder pour la mesure de comptage sur un ensemble fini.
*Résolution pas-à-pas :*
1. Posons $X = (\sum_{i=1}^n x_i^p)^{1/p}$ et $Y = (\sum_{i=1}^n y_i^q)^{1/q}$. Si $X=0$ ou $Y=0$, tous les $x_i$ ou $y_i$ sont nuls et l'inégalité est $0 \le 0$. On suppose $X > 0, Y > 0$.
2. On définit des variables normalisées $u_i = \frac{x_i}{X}$ et $v_i = \frac{y_i}{Y}$. On a $\sum u_i^p = 1$ et $\sum v_i^q = 1$.
3. On applique l'inégalité de Young pour chaque $i$ :
   $$u_i v_i \le \frac{u_i^p}{p} + \frac{v_i^q}{q}$$
4. On somme sur $i = 1 \dots n$ :
   $$\sum_{i=1}^n u_i v_i \le \frac{1}{p} \sum_{i=1}^n u_i^p + \frac{1}{q} \sum_{i=1}^n v_i^q = \frac{1}{p} + \frac{1}{q} = 1$$
5. En remplaçant $u_i$ et $v_i$ :
   $$\sum_{i=1}^n \frac{x_i y_i}{X Y} \le 1 \implies \sum_{i=1}^n x_i y_i \le X Y$$
