# Exercice 10 : Équivalence de Topologies sur un Espace de Sobolev Ponderé

Cet exercice approfondit la compréhension des théorèmes fondamentaux de l'analyse fonctionnelle (Théorème de l'application ouverte, Théorème du graphe fermé, Théorème d'isomorphisme de Banach) en les appliquant à la démonstration de l'équivalence de deux normes sur un espace de fonctions subtil. La rigueur dans la vérification des propriétés des espaces de Banach et des opérateurs est primordiale.

Difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $X$ l'espace vectoriel des fonctions $f: \mathbb{R} \to \mathbb{C}$ qui satisfont les conditions suivantes :
1.  $f \in L^1(\mathbb{R})$ (c'est-à-dire $\int_{\mathbb{R}} |f(x)| dx < \infty$).
2.  $f$ est absolument continue sur tout intervalle compact de $\mathbb{R}$.
3.  La dérivée (presque partout) de $f$, notée $f'$, est dans $L^1(\mathbb{R})$.

Nous munissons $X$ de deux normes différentes :
*   $\|f\|_1 = \|f\|_{L^1} + \|f'\|_{L^1}$, où $\|g\|_{L^1} = \int_{\mathbb{R}} |g(x)| dx$.
*   $\|f\|_2 = \|f\|_{L^\infty} + \|f'\|_{L^1}$, où $\|g\|_{L^\infty} = \mathrm{ess\,sup}_{x \in \mathbb{R}} |g(x)|$.

**Question 1.** Démontrer que $X$ est bien un espace vectoriel.
*(Note : Il est un résultat classique que si $f \in L^1(\mathbb{R})$ et $f' \in L^1(\mathbb{R})$, alors $f$ est continue et $f(x) \to 0$ lorsque $|x| \to \infty$. De plus, $f$ est donnée par $f(x) = \int_{-\infty}^x f'(t) dt$ et $\int_{\mathbb{R}} f'(t) dt = 0$. Vous pouvez utiliser ce résultat sans démonstration, en le citant explicitement.)*

**Question 2.** Démontrer que $(X, \|\cdot\|_1)$ est un espace de Banach.

**Question 3.** Démontrer que $(X, \|\cdot\|_2)$ est un espace de Banach.

**Question 4.** Démontrer que les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes sur $X$. C'est-à-dire, il existe des constantes $C_1, C_2 > 0$ telles que pour tout $f \in X$, on a $C_1 \|f\|_1 \le \|f\|_2 \le C_2 \|f\|_1$.
*(Vous devrez ici utiliser le Théorème de l'isomorphisme de Banach ou l'un de ses corollaires, ainsi que les propriétés des fonctions dans $X$.)*

---
## Correction de l'Exercice 10

### Question 1. Démontrer que $X$ est bien un espace vectoriel.

Soient $f, g \in X$ et $\alpha \in \mathbb{C}$.
1.  **Stabilité par addition :**
    *   $f, g \in L^1(\mathbb{R}) \implies f+g \in L^1(\mathbb{R})$ (par l'inégalité triangulaire $\|f+g\|_{L^1} \le \|f\|_{L^1} + \|g\|_{L^1}$).
    *   $f, g$ sont absolument continues sur tout compact $\implies f+g$ est absolument continue sur tout compact.
    *   $f', g' \in L^1(\mathbb{R}) \implies (f+g)' = f'+g' \in L^1(\mathbb{R})$ (par linéarité de la dérivation et $\|f'+g'\|_{L^1} \le \|f'\|_{L^1} + \|g'\|_{L^1}$).
    Donc $f+g \in X$.
2.  **Stabilité par multiplication scalaire :**
    *   $f \in L^1(\mathbb{R}) \implies \alpha f \in L^1(\mathbb{R})$ (car $\|\alpha f\|_{L^1} = |\alpha| \|f\|_{L^1}$).
    *   $f$ est absolument continue sur tout compact $\implies \alpha f$ est absolument continue sur tout compact.
    *   $f' \in L^1(\mathbb{R}) \implies (\alpha f)' = \alpha f' \in L^1(\mathbb{R})$ (car $\|\alpha f'\|_{L^1} = |\alpha| \|f'\|_{L^1}$).
    Donc $\alpha f \in X$.
3.  **Existence de l'élément nul :** La fonction nulle $0(x)=0$ pour tout $x \in \mathbb{R}$ satisfait toutes les conditions : elle est dans $L^1$, absolument continue et sa dérivée (qui est aussi 0) est dans $L^1$. Donc $0 \in X$.

Ainsi, $X$ est un espace vectoriel.
*Rappel du résultat classique cité dans l'énoncé:* Pour $f \in X$, nous savons que $f$ est continue et $f(x) \to 0$ lorsque $|x| \to \infty$. De plus, $f(x) = \int_{-\infty}^x f'(t) dt$ pour tout $x \in \mathbb{R}$, et $\int_{\mathbb{R}} f'(t) dt = 0$. En particulier, $f \in C_0(\mathbb{R})$ et $f \in L^\infty(\mathbb{R})$.

### Question 2. Démontrer que $(X, \|\cdot\|_1)$ est un espace de Banach.

Pour montrer que $(X, \|\cdot\|_1)$ est un espace de Banach, nous devons montrer qu'il est complet. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $(X, \|\cdot\|_1)$.
Puisque $\|f_n - f_m\|_1 = \|f_n - f_m\|_{L^1} + \|f_n' - f_m'\|_{L^1}$, la suite de Cauchy $(f_n)$ dans $X$ implique :
1.  $(f_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $L^1(\mathbb{R})$.
2.  $(f_n')_{n \in \mathbb{N}}$ est une suite de Cauchy dans $L^1(\mathbb{R})$.

Puisque $L^1(\mathbb{R})$ est un espace de Banach, il existe $f \in L^1(\mathbb{R})$ tel que $f_n \to f$ dans $L^1(\mathbb{R})$.
De même, il existe $g \in L^1(\mathbb{R})$ tel que $f_n' \to g$ dans $L^1(\mathbb{R})$.

Nous devons maintenant montrer que $f \in X$ et que $f_n \to f$ dans $(X, \|\cdot\|_1)$.
Pour cela, il faut montrer que $f' = g$ (au sens des distributions), et que $f$ est absolument continue.

Pour toute fonction test $\phi \in C_c^\infty(\mathbb{R})$, nous avons :
$\int_{\mathbb{R}} f_n'(x) \phi(x) dx = -\int_{\mathbb{R}} f_n(x) \phi'(x) dx$.
En passant à la limite quand $n \to \infty$ :
$\lim_{n \to \infty} \int_{\mathbb{R}} f_n'(x) \phi(x) dx = \int_{\mathbb{R}} g(x) \phi(x) dx$ (car $f_n' \to g$ dans $L^1$).
$\lim_{n \to \infty} \int_{\mathbb{R}} f_n(x) \phi'(x) dx = \int_{\mathbb{R}} f(x) \phi'(x) dx$ (car $f_n \to f$ dans $L^1$, et $\phi'$ est bornée).
Donc, $\int_{\mathbb{R}} g(x) \phi(x) dx = -\int_{\mathbb{R}} f(x) \phi'(x) dx$.
Ceci signifie que $g$ est la dérivée distributionnelle de $f$, c'est-à-dire $f'=g$ au sens des distributions.

Maintenant, nous utilisons le résultat fondamental de la théorie de la distribution : si une fonction $f \in L^1(\mathbb{R})$ a une dérivée distributionnelle $f'$ qui est aussi dans $L^1(\mathbb{R})$, alors $f$ est absolument continue et sa dérivée presque partout est $f'$.
Puisque $f \in L^1(\mathbb{R})$ et $f'=g \in L^1(\mathbb{R})$, les conditions de la définition de $X$ sont satisfaites pour $f$. Donc $f \in X$.

Enfin, nous devons montrer que $f_n \to f$ dans $(X, \|\cdot\|_1)$.
Nous avons déjà $f_n \to f$ dans $L^1(\mathbb{R})$ et $f_n' \to g$ dans $L^1(\mathbb{R})$.
Puisque $g=f'$, cela signifie que $f_n' \to f'$ dans $L^1(\mathbb{R})$.
Donc, $\|f_n - f\|_1 = \|f_n - f\|_{L^1} + \|f_n' - f'\|_{L^1} \to 0$ lorsque $n \to \infty$.
Par conséquent, $(X, \|\cdot\|_1)$ est un espace de Banach.

### Question 3. Démontrer que $(X, \|\cdot\|_2)$ est un espace de Banach.

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $(X, \|\cdot\|_2)$.
Puisque $\|f_n - f_m\|_2 = \|f_n - f_m\|_{L^\infty} + \|f_n' - f_m'\|_{L^1}$, la suite de Cauchy $(f_n)$ dans $X$ implique :
1.  $(f_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $L^\infty(\mathbb{R})$.
2.  $(f_n')_{n \in \mathbb{N}}$ est une suite de Cauchy dans $L^1(\mathbb{R})$.

Puisque $L^\infty(\mathbb{R})$ est un espace de Banach, il existe $f \in L^\infty(\mathbb{R})$ tel que $f_n \to f$ dans $L^\infty(\mathbb{R})$. Cela implique également que $f_n \to f$ uniformément (à un ensemble de mesure nulle près), et donc $f_n \to f$ ponctuellement.
Puisque $L^1(\mathbb{R})$ est un espace de Banach, il existe $g \in L^1(\mathbb{R})$ tel que $f_n' \to g$ dans $L^1(\mathbb{R})$.

En utilisant le résultat cité dans la Question 1, pour chaque $f_n \in X$, nous avons $f_n(x) = \int_{-\infty}^x f_n'(t) dt$.
En passant à la limite ponctuelle pour $f_n(x)$ et à la limite en $L^1$ pour $f_n'(t)$ :
Pour chaque $x \in \mathbb{R}$, $f(x) = \lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \int_{-\infty}^x f_n'(t) dt$.
Comme $f_n' \to g$ dans $L^1(\mathbb{R})$, pour tout $x$, $\int_{-\infty}^x f_n'(t) dt \to \int_{-\infty}^x g(t) dt$.
Donc, $f(x) = \int_{-\infty}^x g(t) dt$.
Cette égalité implique plusieurs choses pour $f$:
*   $f$ est absolument continue (car l'intégrale d'une fonction $L^1$ est absolument continue).
*   La dérivée presque partout de $f$ est $f'(x) = g(x)$. Puisque $g \in L^1(\mathbb{R})$, on a $f' \in L^1(\mathbb{R})$.
*   Comme $f_n \in X$, $f_n(x) \to 0$ pour $|x| \to \infty$. Puisque $f_n \to f$ uniformément, $f(x) \to 0$ pour $|x| \to \infty$. Donc $f \in C_0(\mathbb{R})$.
*   Puisque $f \in C_0(\mathbb{R})$ et $f' \in L^1(\mathbb{R})$, il s'ensuit que $f \in L^1(\mathbb{R})$. (En effet, $|f(x)| \le \|f'\|_{L^1}$ pour tout $x$, donc $f$ est bornée. Et $f$ s'annule à l'infini. Il est un fait que si $f \in C_0(\mathbb{R})$ et $f' \in L^1(\mathbb{R})$, alors $f \in L^1(\mathbb{R})$).
    En particulier, pour $f \in C_0(\mathbb{R})$ avec $f' \in L^1(\mathbb{R})$, on a $\int f'(t) dt = 0$. Puisque $f(x) = \int_{-\infty}^x f'(t) dt$, cela garantit que $f(x) \to 0$ à l'infini des deux côtés.

Ainsi, $f$ satisfait toutes les conditions pour appartenir à $X$: $f \in L^1(\mathbb{R})$, $f$ est absolument continue sur tout compact, et $f' \in L^1(\mathbb{R})$.

Enfin, nous montrons que $f_n \to f$ dans $(X, \|\cdot\|_2)$:
$\|f_n - f\|_2 = \|f_n - f\|_{L^\infty} + \|f_n' - f'\|_{L^1}$.
Nous savons que $\|f_n - f\|_{L^\infty} \to 0$ et $\|f_n' - f'\|_{L^1} \to 0$ (car $f_n' \to g=f'$).
Par conséquent, $\|f_n - f\|_2 \to 0$.
Donc, $(X, \|\cdot\|_2)$ est un espace de Banach.

### Question 4. Démontrer que les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes sur $X$.

Nous avons deux espaces de Banach, $(X, \|\cdot\|_1)$ et $(X, \|\cdot\|_2)$, qui sont vectoriellement identiques. Nous voulons montrer que les normes sont équivalentes. Pour cela, il suffit de montrer que l'opérateur identité $Id: (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ est continu et que son inverse $Id^{-1}: (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ est également continu. Le Théorème d'isomorphisme de Banach affirme qu'un opérateur linéaire continu et bijectif entre deux espaces de Banach a un inverse continu.

1.  **Vérifier la continuité de $Id: (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ :**
    Nous devons trouver une constante $C_2 > 0$ telle que pour tout $f \in X$, $\|f\|_2 \le C_2 \|f\|_1$.
    Par définition, $\|f\|_2 = \|f\|_{L^\infty} + \|f'\|_{L^1}$.
    Par définition, $\|f\|_1 = \|f\|_{L^1} + \|f'\|_{L^1}$.
    Puisque $f \in X$, nous savons (d'après la Question 1) que $f(x) = \int_{-\infty}^x f'(t) dt$ et que $f \in C_0(\mathbb{R})$.
    De cette expression, nous pouvons majorer la norme $L^\infty$ de $f$:
    $|f(x)| = \left| \int_{-\infty}^x f'(t) dt \right| \le \int_{-\infty}^x |f'(t)| dt \le \int_{\mathbb{R}} |f'(t)| dt = \|f'\|_{L^1}$.
    Par conséquent, $\|f\|_{L^\infty} \le \|f'\|_{L^1}$.
    Maintenant, nous pouvons majorer $\|f\|_2$:
    $\|f\|_2 = \|f\|_{L^\infty} + \|f'\|_{L^1} \le \|f'\|_{L^1} + \|f'\|_{L^1} = 2 \|f'\|_{L^1}$.
    Ensuite, nous relions $\|f'\|_{L^1}$ à $\|f\|_1$:
    $\|f'\|_{L^1} \le \|f\|_{L^1} + \|f'\|_{L^1} = \|f\|_1$.
    En combinant ces inégalités, nous obtenons :
    $\|f\|_2 \le 2 \|f'\|_{L^1} \le 2 \|f\|_1$.
    Ainsi, $Id: (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ est continu avec $C_2=2$.

2.  **Appliquer le Théorème d'isomorphisme de Banach pour la continuité de l'inverse :**
    Nous avons montré que $(X, \|\cdot\|_1)$ et $(X, \|\cdot\|_2)$ sont des espaces de Banach.
    L'opérateur identité $Id: X \to X$ est linéaire et bijectif (car c'est l'identité).
    Nous avons montré que $Id: (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ est continu.
    Le Théorème d'isomorphisme de Banach (aussi connu sous le nom de Théorème de l'application ouverte, appliqué à un isomorphisme) stipule que si un opérateur linéaire $T$ est bijectif et continu entre deux espaces de Banach, alors son inverse $T^{-1}$ est aussi continu.
    Appliquons ceci à $T=Id$: l'opérateur $Id^{-1}: (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ est continu.
    Cela signifie qu'il existe une constante $C_1' > 0$ telle que pour tout $f \in X$, $\|f\|_1 \le C_1' \|f\|_2$.

    Cette inégalité signifie :
    $\|f\|_{L^1} + \|f'\|_{L^1} \le C_1' (\|f\|_{L^\infty} + \|f'\|_{L^1})$.
    C'est la deuxième partie de l'équivalence des normes. Elle est non-triviale sans l'utilisation de ce théorème. En effet, elle implique en particulier qu'il existe une constante $M$ telle que $\|f\|_{L^1} \le M (\|f\|_{L^\infty} + \|f'\|_{L^1})$, c'est-à-dire que la norme $L^1$ d'une fonction dans $X$ est majorée par sa norme $L^\infty$ et la norme $L^1$ de sa dérivée.

En combinant les deux étapes, nous avons trouvé $C_2=2$ et l'existence d'un $C_1'>0$. On peut écrire l'équivalence des normes comme $C_1 \|f\|_1 \le \|f\|_2 \le C_2 \|f\|_1$ avec $C_1 = 1/C_1'$ et $C_2=2$.
Par conséquent, les normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes sur $X$.