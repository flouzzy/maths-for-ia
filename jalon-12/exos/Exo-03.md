# Exercice 03 (2 $\star$) : Géométrie de la similarité cosinus et formes linéaires associées

## Énoncé
Soit $E = \mathbb{R}^n$ un espace vectoriel euclidien de dimension $n \ge 1$, muni du produit scalaire canonique $\langle x, y \rangle = \sum_{i=1}^n x_i y_i$ pour $x=(x_1, \dots, x_n)$ et $y=(y_1, \dots, y_n)$ dans $E$. La norme associée est $\|x\| = \sqrt{\langle x, x \rangle}$.
Pour deux vecteurs $u, v \in E \setminus \{0\}$, la similarité cosinus entre $u$ et $v$ est définie par $\text{sim}(u, v) = \frac{\langle u, v \rangle}{\|u\| \|v\|}$.

1.  Montrer que pour tout $u, v \in E \setminus \{0\}$, on a $\text{sim}(u, v) \in [-1, 1]$.
2.  Soit $u \in E$ un vecteur non nul fixé. Décrire géométriquement l'ensemble $S_u = \{v \in E \setminus \{0\} \mid \text{sim}(u, v) = 1\}$.
3.  Soit $u \in E$ un vecteur non nul fixé. Décrire géométriquement l'ensemble $S'_u = \{v \in E \setminus \{0\} \mid \text{sim}(u, v) = -1\}$.
4.  Soit $u \in E$ un vecteur non nul fixé et $\alpha \in (-1, 1)$ un scalaire. Décrire géométriquement l'ensemble $H_{u, \alpha} = \{v \in E \setminus \{0\} \mid \text{sim}(u, v) = \alpha\}$.
5.  Pour un vecteur $u \in E$ non nul, on définit la forme linéaire $f_u: E \to \mathbb{R}$ par $f_u(v) = \langle u, v \rangle$. Montrer que l'ensemble $H_{u, \alpha}$ (défini à la question 4) peut être caractérisé en termes de $f_u$ et de la norme de $v$.

## Correction Détaillée
### Analyse et Stratégie
Cet exercice explore la notion de similarité cosinus, un concept central dans la conception de moteurs de recherche sémantiques et l'analyse de données, en l'abordant sous l'angle de la géométrie des espaces euclidiens et de l'algèbre linéaire. La difficulté de 2 étoiles indique que les questions requièrent une application rigoureuse des définitions et des propriétés fondamentales des espaces vectoriels munis d'un produit scalaire, sans nécessiter de théorèmes particulièrement avancés ou de calculs excessivement complexes.

La stratégie de résolution sera la suivante :
1.  **Question 1:** La borne de la similarité cosinus est une conséquence directe de l'inégalité de Cauchy-Schwarz, un pilier de la théorie des espaces euclidiens. Il s'agira de l'appliquer correctement.
2.  **Questions 2 et 3:** Les cas où la similarité cosinus atteint ses valeurs extrêmes (1 ou -1) correspondent à des situations géométriques spécifiques de colinéarité. L'analyse de l'égalité dans l'inégalité de Cauchy-Schwarz permettra de caractériser ces ensembles.
3.  **Question 4:** Pour une valeur intermédiaire $\alpha$, la similarité cosinus est directement liée au cosinus de l'angle entre les vecteurs. L'objectif sera de traduire cette condition en une description géométrique, en distinguant les cas de dimension $n$.
4.  **Question 5:** Cette dernière question vise à établir un lien formel entre la similarité cosinus et la notion de forme linéaire associée à un vecteur via le produit scalaire. Il s'agira de reformuler l'équation définissant l'ensemble $H_{u, \alpha}$ en utilisant la notation de la forme linéaire $f_u$.

Tout au long de la résolution, une attention particulière sera portée à la rigueur des démonstrations, à la justification de chaque étape algébrique ou logique, et à la vérification explicite des hypothèses (par exemple, vecteurs non nuls pour éviter les divisions par zéro).

### Résolution Pas-à-Pas

1.  **Montrer que pour tout $u, v \in E \setminus \{0\}$, on a $\text{sim}(u, v) \in [-1, 1]$.**
    Soient $u, v \in E \setminus \{0\}$ deux vecteurs non nuls de l'espace euclidien $E = \mathbb{R}^n$.
    La similarité cosinus est définie par $\text{sim}(u, v) = \frac{\langle u, v \rangle}{\|u\| \|v\|}$.
    L'espace $E$ étant un espace euclidien, il est muni d'un produit scalaire $\langle \cdot, \cdot \rangle$ et d'une norme associée $\| \cdot \|$. L'inégalité de Cauchy-Schwarz s'applique pour tout couple de vecteurs dans $E$.
    L'inégalité de Cauchy-Schwarz stipule que pour tout $x, y \in E$, on a $|\langle x, y \rangle| \le \|x\| \|y\|$.
    Appliquons cette inégalité aux vecteurs $u$ et $v$:
    $$|\langle u, v \rangle| \le \|u\| \|v\|$$
    Par hypothèse, $u$ et $v$ sont des vecteurs non nuls. Par conséquent, leurs normes $\|u\|$ et $\|v\|$ sont strictement positives. Le produit $\|u\| \|v\|$ est donc également strictement positif.
    Nous pouvons diviser l'inégalité par $\|u\| \|v\|$ sans en changer le sens :
    $$\frac{|\langle u, v \rangle|}{\|u\| \|v\|} \le \frac{\|u\| \|v\|}{\|u\| \|v\|}$$
    $$\frac{|\langle u, v \rangle|}{\|u\| \|v\|} \le 1$$
    Par définition de la valeur absolue, $\frac{|\langle u, v \rangle|}{\|u\| \|v\|}$ est égal à $\left| \frac{\langle u, v \rangle}{\|u\| \|v\|} \right|$.
    Donc, nous obtenons :
    $$\left| \text{sim}(u, v) \right| \le 1$$
    Cette inégalité est équivalente à la double inégalité suivante :
    $$-1 \le \text{sim}(u, v) \le 1$$
    Ainsi, pour tout $u, v \in E \setminus \{0\}$, la similarité cosinus $\text{sim}(u, v)$ appartient bien à l'intervalle fermé $[-1, 1]$.

2.  **Soit $u \in E$ un vecteur non nul fixé. Décrire géométriquement l'ensemble $S_u = \{v \in E \setminus \{0\} \mid \text{sim}(u, v) = 1\}$.**
    L'ensemble $S_u$ est défini par la condition $\text{sim}(u, v) = 1$.
    En utilisant la définition de la similarité cosinus, cette condition s'écrit :
    $$\frac{\langle u, v \rangle}{\|u\| \|v\|} = 1$$
    Puisque $\|u\| \|v\|$ est strictement positif (car $u \ne 0$ et $v \ne 0$), nous pouvons multiplier les deux côtés de l'équation par $\|u\| \|v\|$ :
    $$\langle u, v \rangle = \|u\| \|v\|$$
    Nous savons que l'égalité dans l'inégalité de Cauchy-Schwarz, c'est-à-dire $|\langle u, v \rangle| = \|u\| \|v\|$, est atteinte si et seulement si les vecteurs $u$ et $v$ sont linéairement dépendants. Cela signifie qu'il existe un scalaire $\lambda \in \mathbb{R}$ tel que $v = \lambda u$.
    Substituons $v = \lambda u$ dans l'équation $\langle u, v \rangle = \|u\| \|v\|$ :
    $$\langle u, \lambda u \rangle = \|u\| \|\lambda u\|$$
    En utilisant les propriétés de linéarité du produit scalaire et de la norme :
    $$\lambda \langle u, u \rangle = |\lambda| \|u\| \|u\|$$
    $$\lambda \|u\|^2 = |\lambda| \|u\|^2$$
    Puisque $u \ne 0$, $\|u\|^2$ est strictement positif. Nous pouvons diviser les deux côtés de l'équation par $\|u\|^2$ :
    $$\lambda = |\lambda|$$
    L'égalité $\lambda = |\lambda|$ est vraie si et seulement si $\lambda \ge 0$.
    De plus, la définition de $S_u$ exige que $v \ne 0$. Si $\lambda = 0$, alors $v = 0 \cdot u = 0$, ce qui contredit la condition $v \in E \setminus \{0\}$. Par conséquent, $\lambda$ doit être strictement positif.
    Ainsi, l'ensemble $S_u$ est l'ensemble des vecteurs $v$ qui sont des multiples scalaires strictement positifs de $u$.
    Géométriquement, $S_u$ représente la demi-droite ouverte issue de l'origine et passant par le vecteur $u$. Tous les vecteurs de $S_u$ sont colinéaires à $u$ et ont la même direction que $u$.

3.  **Soit $u \in E$ un vecteur non nul fixé. Décrire géométriquement l'ensemble $S'_u = \{v \in E \setminus \{0\} \mid \text{sim}(u, v) = -1\}$.**
    L'ensemble $S'_u$ est défini par la condition $\text{sim}(u, v) = -1$.
    En utilisant la définition de la similarité cosinus :
    $$\frac{\langle u, v \rangle}{\|u\| \|v\|} = -1$$
    Puisque $\|u\| \|v\|$ est strictement positif, nous multiplions les deux côtés de l'équation par $\|u\| \|v\|$ :
    $$\langle u, v \rangle = -\|u\| \|v\|$$
    Cette équation implique que $|\langle u, v \rangle| = \|u\| \|v\|$ (car $-x = |x|$ si $x \le 0$) et que $\langle u, v \rangle$ est négatif.
    Comme à la question précédente, l'égalité dans l'inégalité de Cauchy-Schwarz implique que $u$ et $v$ sont linéairement dépendants, c'est-à-dire $v = \lambda u$ pour un certain scalaire $\lambda \in \mathbb{R}$.
    Substituons $v = \lambda u$ dans l'équation $\langle u, v \rangle = -\|u\| \|v\|$ :
    $$\langle u, \lambda u \rangle = -\|u\| \|\lambda u\|$$
    $$\lambda \langle u, u \rangle = -|\lambda| \|u\| \|u\|$$
    $$\lambda \|u\|^2 = -|\lambda| \|u\|^2$$
    Puisque $u \ne 0$, $\|u\|^2$ est strictement positif. Nous pouvons diviser les deux côtés de l'équation par $\|u\|^2$ :
    $$\lambda = -|\lambda|$$
    L'égalité $\lambda = -|\lambda|$ est vraie si et seulement si $\lambda \le 0$.
    De plus, la définition de $S'_u$ exige que $v \ne 0$. Si $\lambda = 0$, alors $v = 0 \cdot u = 0$, ce qui contredit la condition $v \in E \setminus \{0\}$. Par conséquent, $\lambda$ doit être strictement négatif.
    Ainsi, l'ensemble $S'_u$ est l'ensemble des vecteurs $v$ qui sont des multiples scalaires strictement négatifs de $u$.
    Géométriquement, $S'_u$ représente la demi-droite ouverte issue de l'origine et passant par le vecteur $-u$. Tous les vecteurs de $S'_u$ sont colinéaires à $u$ et ont la direction opposée à $u$.

4.  **Soit $u \in E$ un vecteur non nul fixé et $\alpha \in (-1, 1)$ un scalaire. Décrire géométriquement l'ensemble $H_{u, \alpha} = \{v \in E \setminus \{0\} \mid \text{sim}(u, v) = \alpha\}$.**
    L'ensemble $H_{u, \alpha}$ est défini par la condition $\text{sim}(u, v) = \alpha$.
    En utilisant la définition de la similarité cosinus :
    $$\frac{\langle u, v \rangle}{\|u\| \|v\|} = \alpha$$
    Puisque $\|u\| \|v\|$ est strictement positif, nous multiplions les deux côtés de l'équation par $\|u\| \|v\|$ :
    $$\langle u, v \rangle = \alpha \|u\| \|v\|$$
    Dans un espace euclidien, l'angle non orienté $\theta$ entre deux vecteurs non nuls $u$ et $v$ est défini par la relation $\cos \theta = \frac{\langle u, v \rangle}{\|u\| \|v\|}$. L'angle $\theta$ est traditionnellement pris dans l'intervalle $[0, \pi]$.
    La condition $\text{sim}(u, v) = \alpha$ est donc équivalente à $\cos \theta = \alpha$.
    Puisque $\alpha \in (-1, 1)$, il existe un unique angle $\theta_0 \in (0, \pi)$ tel que $\cos \theta_0 = \alpha$.
    L'ensemble $H_{u, \alpha}$ est donc l'ensemble des vecteurs $v \in E \setminus \{0\}$ tels que l'angle entre $u$ et $v$ est égal à $\theta_0$.

    Nous devons considérer la description géométrique en fonction de la dimension $n$ de l'espace $E$:
    *   **Cas $n=1$**: L'espace $E = \mathbb{R}$. Les vecteurs $u$ et $v$ sont des scalaires non nuls.
        $\text{sim}(u, v) = \frac{uv}{|u||v|}$.
        Si $u$ et $v$ ont le même signe, $uv > 0$ et $|u||v| = uv$, donc $\text{sim}(u, v) = 1$.
        Si $u$ et $v$ ont des signes opposés, $uv < 0$ et $|u||v| = -uv$, donc $\text{sim}(u, v) = -1$.
        Dans le cas $n=1$, la similarité cosinus ne peut prendre que les valeurs $1$ ou $-1$. Puisque $\alpha \in (-1, 1)$, aucune valeur de $v$ ne peut satisfaire la condition $\text{sim}(u, v) = \alpha$.
        Par conséquent, pour $n=1$, l'ensemble $H_{u, \alpha}$ est vide.

    *   **Cas $n=2$**: L'espace $E = \mathbb{R}^2$. L'ensemble des vecteurs $v$ formant un angle $\theta_0 \in (0, \pi)$ avec $u$ est constitué de deux demi-droites distinctes issues de l'origine. Ces deux demi-droites sont symétriques par rapport à la droite orthogonale à $u$ passant par l'origine. Elles ne contiennent pas l'origine car $v \ne 0$.

    *   **Cas $n \ge 3$**: L'espace $E = \mathbb{R}^n$. L'ensemble des vecteurs $v$ formant un angle $\theta_0 \in (0, \pi)$ avec $u$ est un cône de révolution (sans le sommet, car $v \ne 0$). L'axe de ce cône est la droite vectorielle engendrée par $u$, c'est-à-dire $\text{Vect}(u)$. Le demi-angle au sommet de ce cône est $\theta_0 = \arccos(\alpha)$.

    En résumé, pour $\alpha \in (-1, 1)$ :
    *   Si $n=1$, $H_{u, \alpha} = \emptyset$.
    *   Si $n=2$, $H_{u, \alpha}$ est l'union de deux demi-droites distinctes issues de l'origine.
    *   Si $n \ge 3$, $H_{u, \alpha}$ est un cône de révolution d'axe $\text{Vect}(u)$ et de demi-angle au sommet $\arccos(\alpha)$, privé de son sommet (l'origine).

5.  **Pour un vecteur $u \in E$ non nul, on définit la forme linéaire $f_u: E \to \mathbb{R}$ par $f_u(v) = \langle u, v \rangle$. Montrer que l'ensemble $H_{u, \alpha}$ (défini à la question 4) peut être caractérisé en termes de $f_u$ et de la norme de $v$.**
    L'ensemble $H_{u, \alpha}$ est défini comme :
    $$H_{u, \alpha} = \{v \in E \setminus \{0\} \mid \text{sim}(u, v) = \alpha\}$$
    D'après la résolution de la question 4, la condition $\text{sim}(u, v) = \alpha$ est équivalente à l'équation :
    $$\frac{\langle u, v \rangle}{\|u\| \|v\|} = \alpha$$
    Puisque $\|u\| \|v\|$ est strictement positif (car $u \ne 0$ et $v \ne 0$), nous pouvons multiplier les deux côtés de l'équation par $\|u\| \|v\|$ :
    $$\langle u, v \rangle = \alpha \|u\| \|v\|$$
    Par définition, la forme linéaire $f_u: E \to \mathbb{R}$ est donnée par $f_u(v) = \langle u, v \rangle$.
    Substituons cette définition dans l'équation précédente :
    $$f_u(v) = \alpha \|u\| \|v\|$$
    Ainsi, l'ensemble $H_{u, \alpha}$ peut être caractérisé comme l'ensemble des vecteurs $v \in E \setminus \{0\}$ qui satisfont la relation :
    $$f_u(v) = \alpha \|u\| \|v\|$$
    Cette caractérisation exprime la condition de similarité cosinus en reliant la valeur de la forme linéaire $f_u(v)$ à la norme du vecteur $v$, pondérée par le scalaire $\alpha$ et la norme du vecteur de référence $u$. Elle met en évidence que, pour un vecteur $v$ donné, la similarité cosinus est directement proportionnelle à la valeur de la forme linéaire $f_u(v)$ divisée par la norme de $v$.

### Conclusion

Cet exercice a permis d'approfondir la compréhension de la similarité cosinus, un concept fondamental en intelligence artificielle pour les moteurs de recherche sémantiques et l'analyse de données. Nous avons démontré sa borne naturelle entre -1 et 1, découlant de l'inégalité de Cauchy-Schwarz, et avons exploré sa riche interprétation géométrique.

Les cas extrêmes de similarité (1 et -1) correspondent à des vecteurs colinéaires de même ou de direction opposée, respectivement, formant des demi-droites. Pour une similarité cosinus $\alpha \in (-1, 1)$, l'ensemble des vecteurs satisfaisant cette condition se manifeste géométriquement comme un cône de révolution (privé de son sommet) dont l'axe est le vecteur de référence $u$ et le demi-angle au sommet est $\arccos(\alpha)$, avec des cas dégénérés pour les dimensions inférieures. Enfin, nous avons établi un lien direct entre la similarité cosinus et la forme linéaire $f_u(v) = \langle u, v \rangle$, montrant que la condition de similarité peut être exprimée par $f_u(v) = \alpha \|u\| \|v\|$. Cette dernière caractérisation souligne la dualité inhérente aux espaces euclidiens, où chaque vecteur $u$ peut être naturellement associé à une forme linéaire $f_u$ par le produit scalaire, offrant une perspective algébrique sur une propriété géométrique.
