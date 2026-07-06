# Exercice 9 - Exploration approfondie de la continuité des fonctions d'une variable réelle

Cet exercice est conçu pour évaluer votre maîtrise des concepts fondamentaux et avancés de la continuité des fonctions d'une variable réelle. Une rigueur absolue est attendue dans toutes les démonstrations.

---

## Énoncé de l'Exercice

Soit $f: D \to \mathbb{R}$ une fonction d'une variable réelle.

**Partie A : Définition formelle de la continuité en un point.**
Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = x^2 + 5x - 3$.
Démontrez, en utilisant la définition formelle $(\epsilon, \delta)$ de la continuité, que $f$ est continue au point $x_0 = 2$.

**Partie B : Continuité des fonctions définies par morceaux.**
Considérons la fonction $g: \mathbb{R} \to \mathbb{R}$ définie par :
$$
g(x) = \begin{cases}
    \frac{\sin(ax)}{x} & \text{si } x < 0 \\
    b & \text{si } x = 0 \\
    \frac{e^{2x}-1}{x} & \text{si } x > 0
\end{cases}
$$
Déterminez les valeurs des constantes réelles $a$ et $b$ pour lesquelles la fonction $g$ est continue en $x=0$.

**Partie C : Application du Théorème des Valeurs Intermédiaires.**
Soit $h: [0,1] \to [0,1]$ une fonction continue.
Démontrez qu'il existe au moins un point $c \in [0,1]$ tel que $h(c) = c$. (Un tel point est appelé point fixe de $h$).

**Partie D : Équation fonctionnelle de Cauchy et continuité.**
Soit $k: \mathbb{R} \to \mathbb{R}$ une fonction satisfaisant l'équation fonctionnelle de Cauchy :
$$
k(x+y) = k(x) + k(y) \quad \text{pour tout } x, y \in \mathbb{R}
$$
1.  Démontrez que $k(0) = 0$.
2.  Démontrez que $k(nx) = nk(x)$ pour tout $n \in \mathbb{Z}$ et tout $x \in \mathbb{R}$.
3.  Démontrez que $k(qx) = qk(x)$ pour tout $q \in \mathbb{Q}$ et tout $x \in \mathbb{R}$.
4.  Démontrez que si $k$ est continue en un point $x_0 \in \mathbb{R}$, alors $k$ est continue sur tout $\mathbb{R}$.
5.  Démontrez que si $k$ est continue sur $\mathbb{R}$, alors il existe une constante réelle $C$ telle que $k(x) = Cx$ pour tout $x \in \mathbb{R}$.

---

## Correction Détaillée

### Partie A : Définition formelle de la continuité en un point.

Pour démontrer que $f(x) = x^2 + 5x - 3$ est continue en $x_0 = 2$ en utilisant la définition $(\epsilon, \delta)$, nous devons montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que si $|x - 2| < \delta$, alors $|f(x) - f(2)| < \epsilon$.

**Étape 1 : Calcul de $f(2)$.**
Nous calculons la valeur de la fonction au point $x_0 = 2$:
$f(2) = (2)^2 + 5(2) - 3 = 4 + 10 - 3 = 11$.

**Étape 2 : Analyse de l'expression $|f(x) - f(2)|$.**
Nous considérons l'expression $|f(x) - f(2)|$:
$$
|f(x) - f(2)| = |(x^2 + 5x - 3) - 11|
$$
$$
|f(x) - f(2)| = |x^2 + 5x - 14|
$$
Nous factorisons le polynôme $x^2 + 5x - 14$. Puisque $x=2$ est une racine (car $f(2)-f(2)=0$), $(x-2)$ doit être un facteur.
Par division polynomiale ou par inspection, nous trouvons :
$x^2 + 5x - 14 = (x-2)(x+7)$.
Donc,
$$
|f(x) - f(2)| = |(x-2)(x+7)| = |x-2||x+7|
$$

**Étape 3 : Majoration du terme $|x+7|$.**
Nous voulons majorer le terme $|x+7|$ en supposant que $x$ est "proche" de $2$.
Choisissons une première contrainte sur $\delta$, par exemple $\delta \le 1$.
Si $|x - 2| < \delta$ et $\delta \le 1$, alors $|x - 2| < 1$.
Ceci implique :
$-1 < x - 2 < 1$
En ajoutant $2$ à toutes les parties de l'inégalité :
$1 < x < 3$
Maintenant, nous voulons majorer $|x+7|$. En ajoutant $7$ à toutes les parties de l'inégalité $1 < x < 3$:
$1 + 7 < x + 7 < 3 + 7$
$8 < x + 7 < 10$
Puisque $x+7$ est compris entre $8$ et $10$, il est positif, et sa valeur absolue est $x+7$.
Ainsi, $|x+7| < 10$.

**Étape 4 : Détermination de $\delta$.**
En utilisant la majoration de l'étape 3, nous avons :
$|f(x) - f(2)| = |x-2||x+7| < |x-2| \cdot 10$.
Nous voulons que cette expression soit inférieure à $\epsilon$.
Nous posons donc $|x-2| \cdot 10 < \epsilon$.
Ceci implique $|x-2| < \frac{\epsilon}{10}$.
Nous avons deux conditions sur $\delta$: $\delta \le 1$ et $\delta \le \frac{\epsilon}{10}$.
Pour satisfaire les deux conditions simultanément, nous choisissons $\delta = \min\left(1, \frac{\epsilon}{10}\right)$.

**Étape 5 : Conclusion formelle.**
Soit $\epsilon > 0$.
Choisissons $\delta = \min\left(1, \frac{\epsilon}{10}\right)$.
Supposons que $|x - 2| < \delta$.
Puisque $\delta \le 1$, nous avons $|x - 2| < 1$.
Ceci implique $1 < x < 3$, et par conséquent $8 < x+7 < 10$.
Donc, $|x+7| < 10$.
Ensuite, nous utilisons la deuxième partie de la définition de $\delta$, $\delta \le \frac{\epsilon}{10}$.
Nous avons :
$$
|f(x) - f(2)| = |x-2||x+7|
$$
Puisque $|x-2| < \delta$ et $|x+7| < 10$ (sous la condition $\delta \le 1$), nous obtenons :
$$
|f(x) - f(2)| < \delta \cdot 10
$$
Puisque $\delta \le \frac{\epsilon}{10}$, nous avons :
$$
|f(x) - f(2)| < \left(\frac{\epsilon}{10}\right) \cdot 10
$$
$$
|f(x) - f(2)| < \epsilon
$$
Par conséquent, pour tout $\epsilon > 0$, il existe un $\delta = \min\left(1, \frac{\epsilon}{10}\right)$ tel que si $|x - 2| < \delta$, alors $|f(x) - f(2)| < \epsilon$.
La fonction $f(x) = x^2 + 5x - 3$ est donc continue en $x_0 = 2$.

### Partie B : Continuité des fonctions définies par morceaux.

Pour que la fonction $g$ soit continue en $x=0$, trois conditions doivent être satisfaites :
1.  La fonction $g$ doit être définie en $x=0$. C'est le cas, $g(0) = b$.
2.  La limite de $g(x)$ lorsque $x$ tend vers $0$ par la gauche doit exister.
3.  La limite de $g(x)$ lorsque $x$ tend vers $0$ par la droite doit exister.
4.  Ces trois valeurs doivent être égales : $\lim_{x \to 0^-} g(x) = \lim_{x \to 0^+} g(x) = g(0)$.

**Étape 1 : Calcul de $g(0)$.**
Par définition de la fonction $g$, nous avons $g(0) = b$.

**Étape 2 : Calcul de la limite à gauche $\lim_{x \to 0^-} g(x)$.**
Pour $x < 0$, $g(x) = \frac{\sin(ax)}{x}$.
Nous calculons la limite :
$$
\lim_{x \to 0^-} g(x) = \lim_{x \to 0^-} \frac{\sin(ax)}{x}
$$
Nous utilisons la limite remarquable $\lim_{u \to 0} \frac{\sin u}{u} = 1$.
Pour appliquer cette limite, nous multiplions et divisons par $a$ (en supposant $a \ne 0$ pour l'instant) :
$$
\lim_{x \to 0^-} \frac{\sin(ax)}{x} = \lim_{x \to 0^-} a \cdot \frac{\sin(ax)}{ax}
$$
En posant $u = ax$, lorsque $x \to 0^-$, $u \to 0^-$.
$$
\lim_{x \to 0^-} a \cdot \frac{\sin(ax)}{ax} = a \cdot \lim_{u \to 0^-} \frac{\sin u}{u}
$$
Puisque $\lim_{u \to 0^-} \frac{\sin u}{u} = 1$, nous obtenons :
$$
\lim_{x \to 0^-} g(x) = a \cdot 1 = a
$$
Si $a=0$, alors $\lim_{x \to 0^-} \frac{\sin(0x)}{x} = \lim_{x \to 0^-} \frac{0}{x} = 0$. La formule $a \cdot 1 = a$ reste valide.

**Étape 3 : Calcul de la limite à droite $\lim_{x \to 0^+} g(x)$.**
Pour $x > 0$, $g(x) = \frac{e^{2x}-1}{x}$.
Nous calculons la limite :
$$
\lim_{x \to 0^+} g(x) = \lim_{x \to 0^+} \frac{e^{2x}-1}{x}
$$
Nous utilisons la limite remarquable $\lim_{u \to 0} \frac{e^u-1}{u} = 1$.
Pour appliquer cette limite, nous multiplions et divisons par $2$ :
$$
\lim_{x \to 0^+} \frac{e^{2x}-1}{x} = \lim_{x \to 0^+} 2 \cdot \frac{e^{2x}-1}{2x}
$$
En posant $v = 2x$, lorsque $x \to 0^+$, $v \to 0^+$.
$$
\lim_{x \to 0^+} 2 \cdot \frac{e^{2x}-1}{2x} = 2 \cdot \lim_{v \to 0^+} \frac{e^v-1}{v}
$$
Puisque $\lim_{v \to 0^+} \frac{e^v-1}{v} = 1$, nous obtenons :
$$
\lim_{x \to 0^+} g(x) = 2 \cdot 1 = 2
$$

**Étape 4 : Égalisation des valeurs pour la continuité.**
Pour que $g$ soit continue en $x=0$, nous devons avoir :
$\lim_{x \to 0^-} g(x) = \lim_{x \to 0^+} g(x) = g(0)$.
En substituant les valeurs calculées :
$a = 2 = b$.
Par conséquent, pour que la fonction $g$ soit continue en $x=0$, les constantes $a$ et $b$ doivent prendre les valeurs $a=2$ et $b=2$.

### Partie C : Application du Théorème des Valeurs Intermédiaires.

Nous voulons démontrer qu'il existe au moins un point $c \in [0,1]$ tel que $h(c) = c$, où $h: [0,1] \to [0,1]$ est une fonction continue.
Ceci est équivalent à montrer que l'équation $h(x) - x = 0$ a au moins une solution dans l'intervalle $[0,1]$.

**Étape 1 : Définition d'une fonction auxiliaire.**
Considérons la fonction auxiliaire $k: [0,1] \to \mathbb{R}$ définie par $k(x) = h(x) - x$.

**Étape 2 : Vérification de la continuité de $k$.**
La fonction $h$ est donnée comme continue sur l'intervalle $[0,1]$.
La fonction $x \mapsto x$ est une fonction polynomiale, et donc elle est continue sur tout $\mathbb{R}$, et en particulier sur $[0,1]$.
Puisque $k(x)$ est la différence de deux fonctions continues sur $[0,1]$ ($h(x)$ et $x$), $k(x)$ est également continue sur $[0,1]$.

**Étape 3 : Évaluation de $k$ aux bornes de l'intervalle.**
Nous évaluons la fonction $k$ aux extrémités de l'intervalle $[0,1]$ :
Pour $x=0$:
$k(0) = h(0) - 0 = h(0)$.
Puisque la fonction $h$ a pour codomaine $[0,1]$, nous savons que $h(0) \in [0,1]$.
Donc, $h(0) \ge 0$. Par conséquent, $k(0) \ge 0$.

Pour $x=1$:
$k(1) = h(1) - 1$.
Puisque la fonction $h$ a pour codomaine $[0,1]$, nous savons que $h(1) \in [0,1]$.
Donc, $h(1) \le 1$. Par conséquent, $h(1) - 1 \le 0$.
Donc, $k(1) \le 0$.

**Étape 4 : Application du Théorème des Valeurs Intermédiaires (TVI).**
Nous avons établi que :
*   $k$ est continue sur l'intervalle fermé et borné $[0,1]$.
*   $k(0) \ge 0$.
*   $k(1) \le 0$.
Nous avons donc $k(0) \cdot k(1) \le 0$.
Le Théorème des Valeurs Intermédiaires stipule que si une fonction est continue sur un intervalle fermé $[a,b]$ et si $k(a)$ et $k(b)$ ont des signes opposés (ou l'un est nul), alors il existe au moins un $c \in [a,b]$ tel que $k(c) = 0$.
Dans notre cas, $a=0$ et $b=1$.
Puisque $k$ est continue sur $[0,1]$ et que $k(0) \ge 0$ et $k(1) \le 0$, le TVI garantit l'existence d'au moins un $c \in [0,1]$ tel que $k(c) = 0$.

**Étape 5 : Conclusion.**
Puisque $k(c) = 0$, par définition de $k(x)$, nous avons $h(c) - c = 0$.
Ceci implique $h(c) = c$.
Nous avons donc démontré qu'il existe au moins un point $c \in [0,1]$ tel que $h(c) = c$.

### Partie D : Équation fonctionnelle de Cauchy et continuité.

Soit $k: \mathbb{R} \to \mathbb{R}$ une fonction telle que $k(x+y) = k(x) + k(y)$ pour tout $x, y \in \mathbb{R}$.

**1. Démontrez que $k(0) = 0$.**
Nous utilisons la propriété de l'équation fonctionnelle en choisissant $x=0$ et $y=0$.
$k(0+0) = k(0) + k(0)$
$k(0) = 2k(0)$
En soustrayant $k(0)$ des deux côtés de l'équation :
$0 = k(0)$
Donc, $k(0) = 0$.

**2. Démontrez que $k(nx) = nk(x)$ pour tout $n \in \mathbb{Z}$ et tout $x \in \mathbb{R}$.**

*   **Cas $n \in \mathbb{N}^*$ (entiers positifs) :**
    Nous allons procéder par récurrence sur $n$.
    *   **Initialisation :** Pour $n=1$, $k(1x) = k(x)$ et $1k(x) = k(x)$. Donc $k(1x) = 1k(x)$ est vrai.
    *   **Hérédité :** Supposons que pour un certain entier $n \ge 1$, $k(nx) = nk(x)$ est vrai.
        Nous voulons montrer que $k((n+1)x) = (n+1)k(x)$.
        En utilisant l'équation fonctionnelle de Cauchy avec $y=nx$:
        $k((n+1)x) = k(x + nx) = k(x) + k(nx)$
        Par l'hypothèse de récurrence, $k(nx) = nk(x)$.
        Donc, $k((n+1)x) = k(x) + nk(x) = (1+n)k(x) = (n+1)k(x)$.
    *   **Conclusion :** Par le principe d'induction mathématique, $k(nx) = nk(x)$ pour tout $n \in \mathbb{N}^*$.

*   **Cas $n=0$ :**
    Nous avons $k(0x) = k(0)$. D'après la question précédente, $k(0)=0$.
    Et $0k(x) = 0$.
    Donc, $k(0x) = 0k(x)$ est vrai.

*   **Cas $n \in \mathbb{Z}^-$ (entiers négatifs) :**
    Soit $n$ un entier négatif. Alors $n = -m$ pour un certain entier positif $m \in \mathbb{N}^*$.
    Nous avons $k(x+(-x)) = k(x) + k(-x)$.
    Puisque $k(x+(-x)) = k(0)$, et nous savons que $k(0)=0$, nous avons :
    $0 = k(x) + k(-x)$
    Ceci implique $k(-x) = -k(x)$.
    Maintenant, considérons $k(nx) = k(-mx)$.
    $k(-mx) = -k(mx)$ (en utilisant $k(-z)=-k(z)$ avec $z=mx$).
    Puisque $m \in \mathbb{N}^*$, nous savons que $k(mx) = mk(x)$.
    Donc, $k(-mx) = -mk(x)$.
    Puisque $n = -m$, nous avons $-m = n$.
    Par conséquent, $k(nx) = nk(x)$ pour tout $n \in \mathbb{Z}^-$.

En combinant les trois cas, nous concluons que $k(nx) = nk(x)$ pour tout $n \in \mathbb{Z}$ et tout $x \in \mathbb{R}$.

**3. Démontrez que $k(qx) = qk(x)$ pour tout $q \in \mathbb{Q}$ et tout $x \in \mathbb{R}$.**
Soit $q \in \mathbb{Q}$. Par définition, $q$ peut s'écrire sous la forme $\frac{m}{n}$ où $m \in \mathbb{Z}$ et $n \in \mathbb{Z}^*$.
Nous voulons montrer que $k\left(\frac{m}{n}x\right) = \frac{m}{n}k(x)$.
Considérons $k(nx)$. D'après la question précédente, $k(nx) = nk(x)$.
Nous pouvons aussi écrire $nx = n \left(\frac{m}{n}x\right)$.
Donc, $k(nx) = k\left(n \cdot \left(\frac{m}{n}x\right)\right)$.
En utilisant la propriété $k(Ny) = Nk(y)$ pour $N \in \mathbb{Z}$ (ici $N=n$ et $y=\frac{m}{n}x$), nous avons :
$k\left(n \cdot \left(\frac{m}{n}x\right)\right) = n \cdot k\left(\frac{m}{n}x\right)$.
Ainsi, nous avons l'égalité :
$nk(x) = n \cdot k\left(\frac{m}{n}x\right)$.
Puisque $n \in \mathbb{Z}^*$, nous pouvons diviser par $n$ :
$k(x) = k\left(\frac{m}{n}x\right)$.
Attendez, il y a une erreur dans mon raisonnement. Reprenons.

Nous savons que $k(nx) = nk(x)$ pour $n \in \mathbb{Z}$.
Soit $q = \frac{m}{n}$ avec $m \in \mathbb{Z}$ et $n \in \mathbb{Z}^*$.
Nous voulons montrer $k(qx) = qk(x)$.
Considérons $k(x)$. Nous pouvons écrire $x = n \cdot \left(\frac{1}{n}x\right)$.
Donc $k(x) = k\left(n \cdot \left(\frac{1}{n}x\right)\right)$.
En utilisant la propriété $k(Ny) = Nk(y)$ pour $N=n$ et $y=\frac{1}{n}x$:
$k(x) = n \cdot k\left(\frac{1}{n}x\right)$.
En divisant par $n$ (puisque $n \ne 0$):
$\frac{1}{n}k(x) = k\left(\frac{1}{n}x\right)$.
Ceci montre que la propriété est vraie pour $q = \frac{1}{n}$.

Maintenant, nous voulons $k\left(\frac{m}{n}x\right)$.
Nous pouvons écrire $\frac{m}{n}x = m \cdot \left(\frac{1}{n}x\right)$.
En utilisant la propriété $k(Ny) = Nk(y)$ pour $N=m$ et $y=\frac{1}{n}x$:
$k\left(\frac{m}{n}x\right) = k\left(m \cdot \left(\frac{1}{n}x\right)\right) = m \cdot k\left(\frac{1}{n}x\right)$.
En substituant $k\left(\frac{1}{n}x\right) = \frac{1}{n}k(x)$ :
$k\left(\frac{m}{n}x\right) = m \cdot \left(\frac{1}{n}k(x)\right) = \frac{m}{n}k(x)$.
Donc, $k(qx) = qk(x)$ pour tout $q \in \mathbb{Q}$ et tout $x \in \mathbb{R}$.

**4. Démontrez que si $k$ est continue en un point $x_0 \in \mathbb{R}$, alors $k$ est continue sur tout $\mathbb{R}$.**
Supposons que $k$ est continue en $x_0$. Cela signifie que $\lim_{x \to x_0} k(x) = k(x_0)$.
Nous voulons montrer que $k$ est continue en un point arbitraire $a \in \mathbb{R}$.
C'est-à-dire, nous voulons montrer que $\lim_{x \to a} k(x) = k(a)$.

Considérons la limite $\lim_{h \to 0} k(h)$.
Puisque $k$ est continue en $x_0$, pour tout $\epsilon > 0$, il existe $\delta_0 > 0$ tel que si $|x - x_0| < \delta_0$, alors $|k(x) - k(x_0)| < \epsilon$.
Soit $h = x - x_0$. Alors $x = x_0 + h$. Lorsque $x \to x_0$, $h \to 0$.
L'inégalité $|x - x_0| < \delta_0$ devient $|h| < \delta_0$.
L'inégalité $|k(x) - k(x_0)| < \epsilon$ devient $|k(x_0+h) - k(x_0)| < \epsilon$.
En utilisant l'équation fonctionnelle de Cauchy, $k(x_0+h) = k(x_0) + k(h)$.
Donc, $|(k(x_0) + k(h)) - k(x_0)| < \epsilon$.
Ceci simplifie à $|k(h)| < \epsilon$.
Ainsi, pour tout $\epsilon > 0$, il existe $\delta_0 > 0$ tel que si $|h| < \delta_0$, alors $|k(h)| < \epsilon$.
Ceci est précisément la définition de $\lim_{h \to 0} k(h) = 0$.
Puisque $k(0)=0$ (démontré en D.1), cela signifie que $k$ est continue en $0$.

Maintenant, nous allons montrer que $k$ est continue en tout point $a \in \mathbb{R}$.
Nous devons montrer que $\lim_{x \to a} k(x) = k(a)$.
Considérons la limite $\lim_{h \to 0} k(a+h)$.
En utilisant l'équation fonctionnelle de Cauchy :
$k(a+h) = k(a) + k(h)$.
Donc,
$$
\lim_{x \to a} k(x) = \lim_{h \to 0} k(a+h)
$$
$$
\lim_{h \to 0} k(a+h) = \lim_{h \to 0} (k(a) + k(h))
$$
Par la propriété de la limite d'une somme (si les limites existent) :
$$
\lim_{h \to 0} (k(a) + k(h)) = \lim_{h \to 0} k(a) + \lim_{h \to 0} k(h)
$$
Puisque $k(a)$ est une constante par rapport à $h$, $\lim_{h \to 0} k(a) = k(a)$.
Nous avons démontré précédemment que $\lim_{h \to 0} k(h) = 0$.
Donc,
$$
\lim_{x \to a} k(x) = k(a) + 0 = k(a)
$$
Par conséquent, $k$ est continue en tout point $a \in \mathbb{R}$.

**5. Démontrez que si $k$ est continue sur $\mathbb{R}$, alors il existe une constante réelle $C$ telle que $k(x) = Cx$ pour tout $x \in \mathbb{R}$.**
Nous avons déjà démontré en D.3 que pour tout $q \in \mathbb{Q}$ et tout $x \in \mathbb{R}$, $k(qx) = qk(x)$.
Soit $x=1$. Alors $k(q \cdot 1) = qk(1)$ pour tout $q \in \mathbb{Q}$.
Posons $C = k(1)$. $C$ est une constante réelle.
Alors, pour tout nombre rationnel $q$, nous avons $k(q) = Cq$.

Maintenant, considérons un nombre réel arbitraire $x \in \mathbb{R}$.
Puisque les nombres rationnels sont denses dans $\mathbb{R}$, il existe une suite de nombres rationnels $(q_n)_{n \in \mathbb{N}}$ telle que $\lim_{n \to \infty} q_n = x$.
Puisque la fonction $k$ est continue sur $\mathbb{R}$ (par hypothèse de cette question), nous pouvons utiliser la propriété de continuité séquentielle :
$$
\lim_{n \to \infty} k(q_n) = k\left(\lim_{n \to \infty} q_n\right) = k(x)
$$
D'autre part, nous savons que pour chaque $q_n$ (qui est un nombre rationnel), $k(q_n) = Cq_n$.
Donc,
$$
\lim_{n \to \infty} k(q_n) = \lim_{n \to \infty} (Cq_n)
$$
Par la propriété de la limite d'un produit par une constante :
$$
\lim_{n \to \infty} (Cq_n) = C \cdot \lim_{n \to \infty} q_n
$$
Puisque $\lim_{n \to \infty} q_n = x$, nous avons :
$$
C \cdot \lim_{n \to \infty} q_n = Cx
$$
En combinant ces résultats, nous obtenons :
$$
k(x) = Cx
$$
Ceci est vrai pour tout $x \in \mathbb{R}$.
Par conséquent, si $k$ est continue sur $\mathbb{R}$, alors il existe une constante réelle $C$ (qui est $k(1)$) telle que $k(x) = Cx$ pour tout $x \in \mathbb{R}$.
