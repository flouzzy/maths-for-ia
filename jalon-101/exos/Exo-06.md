# Exercice 06: Caractérisation d'un Isomorphisme Topologique entre Espaces de Séquences Pondérées

Ce problème approfondit la structure des espaces de Banach de suites et culmine par l'application rigoureuse du Théorème de l'Isomorphisme de Banach pour établir la continuité de l'opérateur inverse, sans calcul direct de sa norme. Il exige une parfaite maîtrise des définitions de complétude, de continuité des opérateurs, et de la nature des bijections linéaires entre espaces normés.

Difficulté : $\bigstar\bigstar\bigstar\star\star$

---

## Énoncé

Soit $\mathbb{N}_0 = \{0, 1, 2, \dots\}$ l'ensemble des entiers naturels incluant zéro. Nous définissons deux espaces de séquences réelles :

1.  Soit $X$ l'espace des séquences réelles $x = (x_n)_{n \in \mathbb{N}_0}$ telles que la série $\sum_{n=0}^\infty |x_n|$ converge. Nous munissons $X$ de la norme $\|x\|_X = \sum_{n=0}^\infty |x_n|$.
2.  Soit $Y$ l'espace des séquences réelles $y = (y_n)_{n \in \mathbb{N}_0}$ telles que la série $\sum_{n=0}^\infty (n+1)|y_n|$ converge. Nous munissons $Y$ de la norme $\|y\|_Y = \sum_{n=0}^\infty (n+1)|y_n|$.

**Questions:**

1.  Démontrer que $(X, \|\cdot\|_X)$ est un espace de Banach.
2.  Démontrer que $(Y, \|\cdot\|_Y)$ est un espace de Banach.
3.  Considérons l'opérateur linéaire $T: X \to Y$ défini par $(Tx)_n = \frac{x_n}{n+1}$ pour tout $n \in \mathbb{N}_0$.
    a.  Vérifier que l'opérateur $T$ est bien défini, c'est-à-dire que pour tout $x \in X$, la séquence $Tx$ appartient à $Y$.
    b.  Démontrer que $T$ est un opérateur linéaire continu de $(X, \|\cdot\|_X)$ vers $(Y, \|\cdot\|_Y)$.
    c.  Démontrer que $T$ est un opérateur bijectif. Déterminer explicitement son inverse $T^{-1}$.
    d.  En utilisant les résultats précédents, et sans calculer explicitement $\|T^{-1}\|$, déduire que $T$ est un isomorphisme topologique.

---

## Correction

### Question 1 : Démontrer que $(X, \|\cdot\|_X)$ est un espace de Banach.

Pour montrer que $(X, \|\cdot\|_X)$ est un espace de Banach, nous devons prouver qu'il s'agit d'un espace vectoriel normé complet.

**Étape 1 : Vérifier que $X$ est un espace vectoriel.**
Soient $x = (x_n)_{n \in \mathbb{N}_0}$ et $z = (z_n)_{n \in \mathbb{N}_0}$ deux séquences dans $X$, et soit $\alpha \in \mathbb{R}$.
1.  **Addition :** $x+z = (x_n+z_n)_{n \in \mathbb{N}_0}$. Nous devons vérifier que $\sum_{n=0}^\infty |x_n+z_n|$ converge. Par l'inégalité triangulaire, $|x_n+z_n| \le |x_n|+|z_n|$. Ainsi, $\sum_{n=0}^\infty |x_n+z_n| \le \sum_{n=0}^\infty (|x_n|+|z_n|) = \sum_{n=0}^\infty |x_n| + \sum_{n=0}^\infty |z_n|$. Puisque $\sum_{n=0}^\infty |x_n|$ et $\sum_{n=0}^\infty |z_n|$ convergent (car $x, z \in X$), leur somme est finie, et donc $\sum_{n=0}^\infty |x_n+z_n|$ converge. Donc $x+z \in X$.
2.  **Multiplication par un scalaire :** $\alpha x = (\alpha x_n)_{n \in \mathbb{N}_0}$. Nous devons vérifier que $\sum_{n=0}^\infty |\alpha x_n|$ converge. Nous avons $\sum_{n=0}^\infty |\alpha x_n| = \sum_{n=0}^\infty |\alpha||x_n| = |\alpha| \sum_{n=0}^\infty |x_n|$. Puisque $\sum_{n=0}^\infty |x_n|$ converge, $|\alpha| \sum_{n=0}^\infty |x_n|$ converge également. Donc $\alpha x \in X$.
3.  L'élément nul est la suite $0 = (0)_{n \in \mathbb{N}_0}$, et $\sum_{n=0}^\infty |0| = 0$, donc $0 \in X$.
Ces propriétés montrent que $X$ est un espace vectoriel.

**Étape 2 : Vérifier que $\|\cdot\|_X$ est une norme sur $X$.**
Soit $x = (x_n)_{n \in \mathbb{N}_0}$ et $z = (z_n)_{n \in \mathbb{N}_0}$ des séquences dans $X$, et soit $\alpha \in \mathbb{R}$.
1.  **Positivité et non-dégénérescence :** $\|x\|_X = \sum_{n=0}^\infty |x_n|$.
    *   $\|x\|_X \ge 0$ car $|x_n| \ge 0$ pour tout $n$.
    *   Si $\|x\|_X = 0$, alors $\sum_{n=0}^\infty |x_n| = 0$. Puisque tous les termes sont positifs, cela implique que $|x_n|=0$ pour tout $n \in \mathbb{N}_0$, et donc $x_n=0$ pour tout $n$. Par conséquent, $x=0$ (la suite nulle).
    *   Réciproquement, si $x=0$, alors $\|x\|_X = \sum_{n=0}^\infty |0| = 0$.
2.  **Homogénéité :** $\|\alpha x\|_X = \sum_{n=0}^\infty |\alpha x_n| = \sum_{n=0}^\infty |\alpha||x_n| = |\alpha| \sum_{n=0}^\infty |x_n| = |\alpha| \|x\|_X$.
3.  **Inégalité triangulaire :** $\|x+z\|_X = \sum_{n=0}^\infty |x_n+z_n|$. Par l'inégalité triangulaire pour les nombres réels, $|x_n+z_n| \le |x_n|+|z_n|$. Donc, $\|x+z\|_X \le \sum_{n=0}^\infty (|x_n|+|z_n|) = \sum_{n=0}^\infty |x_n| + \sum_{n=0}^\infty |z_n| = \|x\|_X + \|z\|_X$.
Ces propriétés montrent que $\|\cdot\|_X$ est une norme sur $X$.

**Étape 3 : Prouver la complétude de $(X, \|\cdot\|_X)$.**
Soit $(x^{(k)})_{k \in \mathbb{N}}$ une suite de Cauchy dans $(X, \|\cdot\|_X)$. Chaque $x^{(k)}$ est une séquence $x^{(k)} = (x^{(k)}_n)_{n \in \mathbb{N}_0}$.
Par définition, pour tout $\varepsilon > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tout $k, l \ge N$, nous avons $\|x^{(k)} - x^{(l)}\|_X < \varepsilon$.
Cela signifie que $\sum_{n=0}^\infty |x^{(k)}_n - x^{(l)}_n| < \varepsilon$.

1.  **Convergence composante par composante :**
    Pour chaque $n_0 \in \mathbb{N}_0$ fixé, nous avons $|x^{(k)}_{n_0} - x^{(l)}_{n_0}| \le \sum_{n=0}^\infty |x^{(k)}_n - x^{(l)}_n| < \varepsilon$.
    Ceci montre que pour chaque indice $n_0$, la suite de nombres réels $(x^{(k)}_{n_0})_{k \in \mathbb{N}}$ est une suite de Cauchy dans $\mathbb{R}$. Puisque $\mathbb{R}$ est un espace complet, il existe un nombre réel $x_{n_0}$ tel que $x_{n_0} = \lim_{k \to \infty} x^{(k)}_{n_0}$.
    Définissons la suite candidate $x = (x_n)_{n \in \mathbb{N}_0}$.

2.  **Appartenance de la limite à $X$ :**
    Nous devons montrer que $x \in X$, c'est-à-dire que $\sum_{n=0}^\infty |x_n|$ converge.
    Puisque $(x^{(k)})_{k \in \mathbb{N}}$ est une suite de Cauchy, pour tout $\varepsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tout $k, l \ge N$, $\sum_{n=0}^\infty |x^{(k)}_n - x^{(l)}_n| < \varepsilon$.
    Fixons un $k \ge N$. Pour tout $M \in \mathbb{N}$, nous avons $\sum_{n=0}^M |x^{(k)}_n - x^{(l)}_n| < \varepsilon$.
    Lorsque $l \to \infty$, pour un $k$ fixé, $x^{(l)}_n \to x_n$. Par la continuité de la fonction valeur absolue et de la somme finie, nous obtenons :
    $\sum_{n=0}^M |x^{(k)}_n - x_n| \le \varepsilon$.
    Cette inégalité est valable pour tout $M \in \mathbb{N}$. En faisant tendre $M \to \infty$, la série $\sum_{n=0}^\infty |x^{(k)}_n - x_n|$ converge et sa somme est inférieure ou égale à $\varepsilon$.
    Donc, $x^{(k)} - x \in X$ pour $k \ge N$.
    Puisque $x^{(k)} = x + (x^{(k)} - x)$, et $x^{(k)} \in X$, et $x^{(k)} - x \in X$, alors $x \in X$ car $X$ est un espace vectoriel (déjà montré).
    Plus précisément, $\|x\|_X = \|x^{(k)} - (x^{(k)} - x)\|_X \le \|x^{(k)}\|_X + \|x^{(k)} - x\|_X$. Puisque $\|x^{(k)}\|_X$ est fini et $\|x^{(k)} - x\|_X$ est fini (au plus $\varepsilon$), alors $\|x\|_X$ est fini.

3.  **Convergence de la suite vers sa limite dans $X$ :**
    Nous devons montrer que $\|x^{(k)} - x\|_X \to 0$ lorsque $k \to \infty$.
    De l'étape précédente, nous avons établi que pour tout $\varepsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tout $k \ge N$, $\sum_{n=0}^\infty |x^{(k)}_n - x_n| \le \varepsilon$.
    Cette inégalité n'est rien d'autre que $\|x^{(k)} - x\|_X \le \varepsilon$.
    Donc, $\lim_{k \to \infty} \|x^{(k)} - x\|_X = 0$.

Par conséquent, $(X, \|\cdot\|_X)$ est un espace de Banach.

### Question 2 : Démontrer que $(Y, \|\cdot\|_Y)$ est un espace de Banach.

La démonstration est analogue à celle de la Question 1, en tenant compte du poids $(n+1)$ dans la norme.

**Étape 1 : Vérifier que $Y$ est un espace vectoriel.**
Soient $y = (y_n)_{n \in \mathbb{N}_0}$ et $w = (w_n)_{n \in \mathbb{N}_0}$ deux séquences dans $Y$, et soit $\alpha \in \mathbb{R}$.
1.  **Addition :** $y+w = (y_n+w_n)_{n \in \mathbb{N}_0}$. Nous devons vérifier que $\sum_{n=0}^\infty (n+1)|y_n+w_n|$ converge.
    Par l'inégalité triangulaire, $(n+1)|y_n+w_n| \le (n+1)(|y_n|+|w_n|) = (n+1)|y_n|+(n+1)|w_n|$.
    Ainsi, $\sum_{n=0}^\infty (n+1)|y_n+w_n| \le \sum_{n=0}^\infty ((n+1)|y_n|+(n+1)|w_n|) = \sum_{n=0}^\infty (n+1)|y_n| + \sum_{n=0}^\infty (n+1)|w_n|$.
    Puisque $y, w \in Y$, les deux sommes à droite convergent, leur somme est finie, et donc $\sum_{n=0}^\infty (n+1)|y_n+w_n|$ converge. Donc $y+w \in Y$.
2.  **Multiplication par un scalaire :** $\alpha y = (\alpha y_n)_{n \in \mathbb{N}_0}$.
    $\sum_{n=0}^\infty (n+1)|\alpha y_n| = \sum_{n=0}^\infty (n+1)|\alpha||y_n| = |\alpha| \sum_{n=0}^\infty (n+1)|y_n|$.
    Puisque $y \in Y$, la somme à droite converge, donc $\alpha y \in Y$.
3.  L'élément nul est la suite $0 = (0)_{n \in \mathbb{N}_0}$, et $\sum_{n=0}^\infty (n+1)|0| = 0$, donc $0 \in Y$.
$Y$ est un espace vectoriel.

**Étape 2 : Vérifier que $\|\cdot\|_Y$ est une norme sur $Y$.**
Soit $y = (y_n)_{n \in \mathbb{N}_0}$ et $w = (w_n)_{n \in \mathbb{N}_0}$ des séquences dans $Y$, et soit $\alpha \in \mathbb{R}$.
1.  **Positivité et non-dégénérescence :** $\|y\|_Y = \sum_{n=0}^\infty (n+1)|y_n|$.
    *   $\|y\|_Y \ge 0$ car $(n+1)|y_n| \ge 0$ pour tout $n$.
    *   Si $\|y\|_Y = 0$, alors $\sum_{n=0}^\infty (n+1)|y_n| = 0$. Puisque tous les termes sont positifs, $(n+1)|y_n|=0$ pour tout $n \in \mathbb{N}_0$. Pour $n \ge 0$, $n+1 \ge 1$, donc cela implique $|y_n|=0$ pour tout $n$, et $y=0$.
2.  **Homogénéité :** $\|\alpha y\|_Y = \sum_{n=0}^\infty (n+1)|\alpha y_n| = |\alpha| \sum_{n=0}^\infty (n+1)|y_n| = |\alpha| \|y\|_Y$.
3.  **Inégalité triangulaire :** $\|y+w\|_Y = \sum_{n=0}^\infty (n+1)|y_n+w_n|$. Par l'inégalité triangulaire pour les nombres réels, $|y_n+w_n| \le |y_n|+|w_n|$.
    Donc, $\|y+w\|_Y \le \sum_{n=0}^\infty (n+1)(|y_n|+|w_n|) = \sum_{n=0}^\infty (n+1)|y_n| + \sum_{n=0}^\infty (n+1)|w_n| = \|y\|_Y + \|w\|_Y$.
Ces propriétés montrent que $\|\cdot\|_Y$ est une norme sur $Y$.

**Étape 3 : Prouver la complétude de $(Y, \|\cdot\|_Y)$.**
Soit $(y^{(k)})_{k \in \mathbb{N}}$ une suite de Cauchy dans $(Y, \|\cdot\|_Y)$. Chaque $y^{(k)}$ est une séquence $y^{(k)} = (y^{(k)}_n)_{n \in \mathbb{N}_0}$.
Par définition, pour tout $\varepsilon > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tout $k, l \ge N$, nous avons $\|y^{(k)} - y^{(l)}\|_Y < \varepsilon$.
Cela signifie que $\sum_{n=0}^\infty (n+1)|y^{(k)}_n - y^{(l)}_n| < \varepsilon$.

1.  **Convergence composante par composante :**
    Pour chaque $n_0 \in \mathbb{N}_0$ fixé, nous avons $(n_0+1)|y^{(k)}_{n_0} - y^{(l)}_{n_0}| \le \sum_{n=0}^\infty (n+1)|y^{(k)}_n - y^{(l)}_n| < \varepsilon$.
    Puisque $n_0+1 \ge 1$, il en résulte que $|y^{(k)}_{n_0} - y^{(l)}_{n_0}| \le \frac{\varepsilon}{n_0+1} \le \varepsilon$.
    Ceci montre que pour chaque indice $n_0$, la suite de nombres réels $(y^{(k)}_{n_0})_{k \in \mathbb{N}}$ est une suite de Cauchy dans $\mathbb{R}$. Puisque $\mathbb{R}$ est complet, il existe un nombre réel $y_{n_0}$ tel que $y_{n_0} = \lim_{k \to \infty} y^{(k)}_{n_0}$.
    Définissons la suite candidate $y = (y_n)_{n \in \mathbb{N}_0}$.

2.  **Appartenance de la limite à $Y$ :**
    Nous devons montrer que $y \in Y$, c'est-à-dire que $\sum_{n=0}^\infty (n+1)|y_n|$ converge.
    Puisque $(y^{(k)})_{k \in \mathbb{N}}$ est une suite de Cauchy, pour tout $\varepsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tout $k, l \ge N$, $\sum_{n=0}^\infty (n+1)|y^{(k)}_n - y^{(l)}_n| < \varepsilon$.
    Fixons un $k \ge N$. Pour tout $M \in \mathbb{N}$, nous avons $\sum_{n=0}^M (n+1)|y^{(k)}_n - y^{(l)}_n| < \varepsilon$.
    Lorsque $l \to \infty$, pour un $k$ fixé, $y^{(l)}_n \to y_n$. Par la continuité de la fonction valeur absolue et de la somme finie, nous obtenons :
    $\sum_{n=0}^M (n+1)|y^{(k)}_n - y_n| \le \varepsilon$.
    Cette inégalité est valable pour tout $M \in \mathbb{N}$. En faisant tendre $M \to \infty$, la série $\sum_{n=0}^\infty (n+1)|y^{(k)}_n - y_n|$ converge et sa somme est inférieure ou égale à $\varepsilon$.
    Donc, $y^{(k)} - y \in Y$ pour $k \ge N$.
    Puisque $y^{(k)} = y + (y^{(k)} - y)$, et $y^{(k)} \in Y$, et $y^{(k)} - y \in Y$, alors $y \in Y$ car $Y$ est un espace vectoriel.
    Plus précisément, $\|y\|_Y = \|y^{(k)} - (y^{(k)} - y)\|_Y \le \|y^{(k)}\|_Y + \|y^{(k)} - y\|_Y$. Puisque $\|y^{(k)}\|_Y$ est fini et $\|y^{(k)} - y\|_Y$ est fini (au plus $\varepsilon$), alors $\|y\|_Y$ est fini.

3.  **Convergence de la suite vers sa limite dans $Y$ :**
    Nous devons montrer que $\|y^{(k)} - y\|_Y \to 0$ lorsque $k \to \infty$.
    De l'étape précédente, nous avons établi que pour tout $\varepsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tout $k \ge N$, $\sum_{n=0}^\infty (n+1)|y^{(k)}_n - y_n| \le \varepsilon$.
    Cette inégalité n'est rien d'autre que $\|y^{(k)} - y\|_Y \le \varepsilon$.
    Donc, $\lim_{k \to \infty} \|y^{(k)} - y\|_Y = 0$.

Par conséquent, $(Y, \|\cdot\|_Y)$ est un espace de Banach.

### Question 3 : L'opérateur linéaire $T: X \to Y$

#### Question 3.a : Vérifier que $T$ est bien défini.

Soit $x = (x_n)_{n \in \mathbb{N}_0}$ une séquence dans $X$. Nous devons montrer que la séquence $Tx = ((Tx)_n)_{n \in \mathbb{N}_0}$, où $(Tx)_n = \frac{x_n}{n+1}$, appartient à $Y$.
Pour cela, nous devons vérifier que la série $\sum_{n=0}^\infty (n+1)|(Tx)_n|$ converge.
Calculons cette somme :
$\sum_{n=0}^\infty (n+1)|(Tx)_n| = \sum_{n=0}^\infty (n+1)\left|\frac{x_n}{n+1}\right|$.
Puisque $n+1 \ge 1$ pour tout $n \in \mathbb{N}_0$, nous pouvons simplifier l'expression :
$\sum_{n=0}^\infty (n+1)\left|\frac{x_n}{n+1}\right| = \sum_{n=0}^\infty (n+1)\frac{|x_n|}{n+1} = \sum_{n=0}^\infty |x_n|$.
Par définition, $x \in X$ signifie que $\sum_{n=0}^\infty |x_n|$ converge et est égale à $\|x\|_X$.
Donc, $\sum_{n=0}^\infty (n+1)|(Tx)_n| = \|x\|_X$.
Puisque $x \in X$, $\|x\|_X$ est fini. Par conséquent, la série $\sum_{n=0}^\infty (n+1)|(Tx)_n|$ converge, ce qui implique que $Tx \in Y$.
L'opérateur $T$ est donc bien défini.

#### Question 3.b : Démontrer que $T$ est un opérateur linéaire continu de $(X, \|\cdot\|_X)$ vers $(Y, \|\cdot\|_Y)$.

**Étape 1 : Linéarité.**
Soient $x, z \in X$ et $\alpha \in \mathbb{R}$.
1.  **Additivité :** $(T(x+z))_n = \frac{(x+z)_n}{n+1} = \frac{x_n+z_n}{n+1} = \frac{x_n}{n+1} + \frac{z_n}{n+1} = (Tx)_n + (Tz)_n = (Tx+Tz)_n$.
    Donc, $T(x+z) = Tx+Tz$.
2.  **Homogénéité :** $(T(\alpha x))_n = \frac{(\alpha x)_n}{n+1} = \frac{\alpha x_n}{n+1} = \alpha \left(\frac{x_n}{n+1}\right) = \alpha (Tx)_n = (\alpha Tx)_n$.
    Donc, $T(\alpha x) = \alpha Tx$.
$T$ est un opérateur linéaire.

**Étape 2 : Continuité.**
Un opérateur linéaire $T$ est continu si et seulement s'il est borné, c'est-à-dire s'il existe une constante $C > 0$ telle que $\|Tx\|_Y \le C \|x\|_X$ pour tout $x \in X$.
D'après la question 3.a, nous avons déjà calculé $\|Tx\|_Y$:
$\|Tx\|_Y = \sum_{n=0}^\infty (n+1)|(Tx)_n| = \sum_{n=0}^\infty (n+1)\left|\frac{x_n}{n+1}\right| = \sum_{n=0}^\infty |x_n| = \|x\|_X$.
Nous avons donc $\|Tx\|_Y = 1 \cdot \|x\|_X$.
Ceci montre que $T$ est borné avec une constante $C=1$.
Par conséquent, $T$ est un opérateur linéaire continu. Sa norme d'opérateur est $\|T\| = \sup_{x \ne 0} \frac{\|Tx\|_Y}{\|x\|_X} = 1$.

#### Question 3.c : Démontrer que $T$ est un opérateur bijectif. Déterminer explicitement son inverse $T^{-1}$.

Pour montrer que $T$ est bijectif, nous devons prouver qu'il est injectif et surjectif.

**Étape 1 : Injectivité.**
Soit $x \in X$ tel que $Tx = 0$.
Par définition de $T$, $(Tx)_n = \frac{x_n}{n+1}$.
Si $Tx = 0$ (la suite nulle dans $Y$), alors $(Tx)_n = 0$ pour tout $n \in \mathbb{N}_0$.
Ceci implique $\frac{x_n}{n+1} = 0$ pour tout $n \in \mathbb{N}_0$.
Puisque $n+1 \ne 0$ pour tout $n \in \mathbb{N}_0$, nous devons avoir $x_n = 0$ pour tout $n \in \mathbb{N}_0$.
Donc, $x = 0$ (la suite nulle dans $X$).
Par conséquent, le noyau de $T$ est trivial, $Ker(T) = \{0\}$, ce qui signifie que $T$ est injectif.

**Étape 2 : Surjectivité.**
Soit $y = (y_n)_{n \in \mathbb{N}_0}$ une séquence arbitraire dans $Y$. Nous devons trouver une séquence $x = (x_n)_{n \in \mathbb{N}_0}$ dans $X$ telle que $Tx = y$.
L'équation $Tx = y$ se traduit par $(Tx)_n = y_n$ pour tout $n \in \mathbb{N}_0$.
En utilisant la définition de $T$, nous avons $\frac{x_n}{n+1} = y_n$.
Nous pouvons résoudre pour $x_n$: $x_n = (n+1)y_n$.
Définissons la séquence candidate $x = ((n+1)y_n)_{n \in \mathbb{N}_0}$.
Nous devons maintenant vérifier que cette séquence $x$ appartient bien à $X$. Pour cela, nous devons calculer $\|x\|_X$:
$\|x\|_X = \sum_{n=0}^\infty |x_n| = \sum_{n=0}^\infty |(n+1)y_n| = \sum_{n=0}^\infty (n+1)|y_n|$.
Par définition, $y \in Y$ signifie que $\sum_{n=0}^\infty (n+1)|y_n|$ converge et est égale à $\|y\|_Y$.
Donc, $\|x\|_X = \|y\|_Y$.
Puisque $y \in Y$, $\|y\|_Y$ est fini, ce qui implique que $\|x\|_X$ est fini. Par conséquent, la séquence $x$ construite appartient à $X$.
Pour tout $y \in Y$, nous avons trouvé un $x \in X$ tel que $Tx=y$. Ceci démontre que $T$ est surjectif.

**Étape 3 : Inverse $T^{-1}$.**
Puisque $T$ est injectif et surjectif, il est bijectif. Son inverse $T^{-1}: Y \to X$ est bien défini.
L'opérateur inverse $T^{-1}$ prend une séquence $y = (y_n)_{n \in \mathbb{N}_0} \in Y$ et lui associe la séquence $x = (x_n)_{n \in \mathbb{N}_0} \in X$ telle que $x_n = (n+1)y_n$.
Donc, $T^{-1}y = ((n+1)y_n)_{n \in \mathbb{N}_0}$.

#### Question 3.d : Déduire que $T$ est un isomorphisme topologique.

Un opérateur linéaire $T: X \to Y$ est un isomorphisme topologique si $T$ est bijectif, continu, et son inverse $T^{-1}$ est également continu.

Récapitulons les propriétés établies pour $T$:
1.  $(X, \|\cdot\|_X)$ est un espace de Banach (démontré en Question 1).
2.  $(Y, \|\cdot\|_Y)$ est un espace de Banach (démontré en Question 2).
3.  $T$ est un opérateur linéaire (démontré en Question 3.b).
4.  $T$ est continu (démontré en Question 3.b).
5.  $T$ est bijectif (démontré en Question 3.c).

Puisque $X$ et $Y$ sont des espaces de Banach, et $T: X \to Y$ est un opérateur linéaire continu et bijectif, nous pouvons appliquer le Théorème de l'Isomorphisme de Banach (aussi connu sous le nom de Théorème de l'Application Ouverte pour les opérateurs bijectifs).

Le Théorème de l'Isomorphisme de Banach stipule que si $X$ et $Y$ sont des espaces de Banach, et si $T: X \to Y$ est un opérateur linéaire continu et bijectif, alors son inverse $T^{-1}: Y \to X$ est également continu.

Toutes les conditions du Théorème de l'Isomorphisme de Banach sont remplies.
Par conséquent, $T^{-1}$ est continu.
Puisque $T$ est un opérateur linéaire bijectif, continu, et dont l'inverse est continu, $T$ est un isomorphisme topologique.