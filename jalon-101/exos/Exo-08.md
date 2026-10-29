# Exercice 08

**Théorème de l'application ouverte et l'isomorphisme de Banach: Étude d'un opérateur somme-différence entre espaces de suites.**

Difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

Dans cet exercice, nous allons explorer en profondeur les propriétés d'un opérateur linéaire continu défini entre l'espace des suites absolument sommables et l'espace des suites qui convergent vers zéro. L'objectif est de caractériser précisément son image, d'examiner si cette image est un espace de Banach, et d'en déduire si l'opérateur inverse est continu, en s'appuyant sur les théorèmes fondamentaux de l'analyse fonctionnelle.

Soient $X = \ell^1(\mathbb{N})$ l'espace des suites de nombres réels $x = (x_n)_{n \in \mathbb{N}}$ telles que $\sum_{n=0}^\infty |x_n| < \infty$, muni de la norme $\|x\|_1 = \sum_{n=0}^\infty |x_n|$.
Soit $Y = c_0(\mathbb{N})$ l'espace des suites de nombres réels $y = (y_n)_{n \in \mathbb{N}}$ telles que $\lim_{n \to \infty} y_n = 0$, muni de la norme $\|y\|_\infty = \sup_{n \in \mathbb{N}} |y_n|$.

On définit l'opérateur $T: X \to Y$ par la relation $(Tx)_n = \sum_{k=n}^\infty x_k$ pour tout $n \in \mathbb{N}$.

1.  **Propriétés fondamentales de l'opérateur $T$ :**
    a.  Montrer que $T$ est bien défini, c'est-à-dire que pour tout $x \in X$, $Tx \in Y$.
    b.  Montrer que $T$ est un opérateur linéaire.
    c.  Montrer que $T$ est continu et déterminer une borne supérieure pour sa norme d'opérateur $\|T\|$.
    d.  Montrer que $T$ est injectif.

2.  **Caractérisation de l'image $R(T)$ :**
    a.  Décrire précisément l'image $R(T)$ de l'opérateur $T$. Pour un $y \in Y$, quelle(s) condition(s) supplémentaire(s) doit-il satisfaire pour appartenir à $R(T)$ ?
    b.  Montrer que $T$ n'est pas surjectif sur $Y$. Donner un exemple explicite d'une suite $y \in Y$ qui n'appartient pas à $R(T)$.

3.  **Continuité de l'opérateur inverse et les théorèmes de Banach :**
    a.  Montrer que $R(T)$ n'est pas un sous-espace fermé de $Y$. En déduire que $R(T)$ n'est pas un espace de Banach (muni de la norme $\|\cdot\|_\infty$).
    b.  En utilisant le Théorème de l'Isomorphisme de Banach (ou le Théorème de l'Application Ouverte), expliquer pourquoi l'opérateur inverse $T^{-1}: R(T) \to X$ (qui est bien défini par la question 1.d) ne peut pas être continu.
    c.  Construire explicitement une suite $(y^{(j)})_{j \in \mathbb{N}}$ d'éléments de $R(T)$ telle que $\|y^{(j)}\|_\infty \to 0$ lorsque $j \to \infty$, mais dont la suite des images $(T^{-1}(y^{(j)}))_{j \in \mathbb{N}}$ n'est pas bornée dans $X$ (c'est-à-dire $\|T^{-1}(y^{(j)})\|_1 \to \infty$). Cela confirme directement la non-continuité de $T^{-1}$.

---

# Correction de l'Exercice 08

### 1. Propriétés fondamentales de l'opérateur $T$ :

a. **$T$ est bien défini :**
Soit $x = (x_n)_{n \in \mathbb{N}} \in \ell^1(\mathbb{N})$. Par définition, $\sum_{k=0}^\infty |x_k| < \infty$.
Pour chaque $n \in \mathbb{N}$, la somme partielle $\sum_{k=n}^\infty x_k$ est une série absolument convergente, car $\sum_{k=n}^\infty |x_k| \le \sum_{k=0}^\infty |x_k| < \infty$. Ainsi, $(Tx)_n$ est bien défini pour chaque $n$.
Il nous reste à montrer que la suite $Tx = ((Tx)_n)_{n \in \mathbb{N}}$ appartient à $Y = c_0(\mathbb{N})$. Par définition d'une série convergente, $\lim_{n \to \infty} \sum_{k=n}^\infty x_k = 0$. Par conséquent, $(Tx)_n \to 0$ lorsque $n \to \infty$.
Donc, $Tx \in c_0(\mathbb{N})$. L'opérateur $T$ est bien défini.

b. **$T$ est linéaire :**
Soient $x, z \in \ell^1(\mathbb{N})$ et $\alpha \in \mathbb{R}$.
Pour tout $n \in \mathbb{N}$:
$(T(x+z))_n = \sum_{k=n}^\infty (x_k+z_k) = \sum_{k=n}^\infty x_k + \sum_{k=n}^\infty z_k = (Tx)_n + (Tz)_n$.
Donc $T(x+z) = Tx + Tz$.
$(T(\alpha x))_n = \sum_{k=n}^\infty (\alpha x_k) = \alpha \sum_{k=n}^\infty x_k = \alpha (Tx)_n$.
Donc $T(\alpha x) = \alpha Tx$.
$T$ est un opérateur linéaire.

c. **$T$ est continu et sa norme :**
Pour tout $x \in \ell^1(\mathbb{N})$:
$\|Tx\|_\infty = \sup_{n \in \mathbb{N}} |(Tx)_n| = \sup_{n \in \mathbb{N}} \left| \sum_{k=n}^\infty x_k \right|$.
Par l'inégalité triangulaire pour les séries absolument convergentes :
$\left| \sum_{k=n}^\infty x_k \right| \le \sum_{k=n}^\infty |x_k| \le \sum_{k=0}^\infty |x_k| = \|x\|_1$.
Cette inégalité est valable pour tout $n \in \mathbb{N}$. Donc, en prenant le supremum:
$\|Tx\|_\infty \le \|x\|_1$.
Cette inégalité montre que $T$ est continu et que sa norme d'opérateur $\|T\|$ satisfait $\|T\| \le 1$.
Pour déterminer la norme exacte, considérons la suite $x^{(0)} = (1, 0, 0, \dots) \in \ell^1(\mathbb{N})$.
$\|x^{(0)}\|_1 = 1$.
$(Tx^{(0)})_0 = 1$, $(Tx^{(0)})_n = 0$ pour $n \ge 1$.
Donc $Tx^{(0)} = (1, 0, 0, \dots) \in c_0(\mathbb{N})$.
$\|Tx^{(0)}\|_\infty = 1$.
Puisque $\|Tx^{(0)}\|_\infty = 1 \cdot \|x^{(0)}\|_1$, nous avons $\|T\| \ge 1$.
Combinant ceci avec $\|T\| \le 1$, nous concluons que $\|T\| = 1$.

d. **$T$ est injectif :**
Supposons que $Tx = 0$ pour un certain $x \in \ell^1(\mathbb{N})$.
Alors, pour tout $n \in \mathbb{N}$, $(Tx)_n = \sum_{k=n}^\infty x_k = 0$.
En particulier:
$(Tx)_0 = x_0 + x_1 + x_2 + \dots = 0$.
$(Tx)_1 = x_1 + x_2 + \dots = 0$.
De ces deux équations, on déduit $x_0 = (Tx)_0 - (Tx)_1 = 0 - 0 = 0$.
Plus généralement, pour tout $n \in \mathbb{N}$:
$(Tx)_n = \sum_{k=n}^\infty x_k = 0$.
$(Tx)_{n+1} = \sum_{k=n+1}^\infty x_k = 0$.
Donc $x_n = (Tx)_n - (Tx)_{n+1} = 0 - 0 = 0$.
Puisque $x_n = 0$ pour tout $n \in \mathbb{N}$, cela signifie que $x$ est la suite nulle.
Par conséquent, $T$ est injectif.

### 2. Caractérisation de l'image $R(T)$ :

a. **Description de $R(T)$ :**
Soit $y = (y_n)_{n \in \mathbb{N}} \in R(T)$. Par définition, il existe $x = (x_n)_{n \in \mathbb{N}} \in \ell^1(\mathbb{N})$ tel que $y = Tx$.
Cela signifie que $y_n = \sum_{k=n}^\infty x_k$ pour tout $n \in \mathbb{N}$.
Nous avons déjà établi que si $y \in R(T)$, alors $y \in c_0(\mathbb{N})$.
De plus, pour tout $n \in \mathbb{N}$:
$y_n = x_n + \sum_{k=n+1}^\infty x_k = x_n + y_{n+1}$.
Donc, $x_n = y_n - y_{n+1}$.
Puisque $x \in \ell^1(\mathbb{N})$, la condition nécessaire et suffisante pour que $y \in R(T)$ est que la suite $(y_n - y_{n+1})_{n \in \mathbb{N}}$ appartienne à $\ell^1(\mathbb{N})$.
Ainsi, $R(T) = \left\{ y \in c_0(\mathbb{N}) \mid \sum_{n=0}^\infty |y_n - y_{n+1}| < \infty \right\}$.

b. **$T$ n'est pas surjectif sur $Y$ :**
Pour montrer que $T$ n'est pas surjectif, il suffit de trouver une suite $y \in c_0(\mathbb{N})$ telle que $\sum_{n=0}^\infty |y_n - y_{n+1}|$ diverge.
Considérons la suite $y = (y_n)_{n \in \mathbb{N}}$ définie par $y_n = \frac{(-1)^n}{\ln(n+2)}$.
Cette suite appartient à $c_0(\mathbb{N})$ car $\lim_{n \to \infty} \frac{(-1)^n}{\ln(n+2)} = 0$.
Calculons les différences $y_n - y_{n+1}$:
$y_n - y_{n+1} = \frac{(-1)^n}{\ln(n+2)} - \frac{(-1)^{n+1}}{\ln(n+3)} = (-1)^n \left( \frac{1}{\ln(n+2)} + \frac{1}{\ln(n+3)} \right)$.
Calculons la somme des valeurs absolues de ces différences :
$\sum_{n=0}^\infty |y_n - y_{n+1}| = \sum_{n=0}^\infty \left| (-1)^n \left( \frac{1}{\ln(n+2)} + \frac{1}{\ln(n+3)} \right) \right|$
$= \sum_{n=0}^\infty \left( \frac{1}{\ln(n+2)} + \frac{1}{\ln(n+3)} \right)$.
Pour $n$ suffisamment grand, $\ln(n+2) \approx \ln n$. Donc les termes de la somme sont asymptotiquement équivalents à $\frac{2}{\ln n}$.
La série $\sum_{n=0}^\infty \frac{1}{\ln(n+2)}$ diverge (par comparaison avec la série harmonique $\sum \frac{1}{n}$, puisque $\ln(n+2) < n+2$, donc $\frac{1}{\ln(n+2)} > \frac{1}{n+2}$ pour $n$ assez grand).
Ainsi, $\sum_{n=0}^\infty |y_n - y_{n+1}|$ diverge.
Par conséquent, $y \notin R(T)$.
Ceci prouve que $T$ n'est pas surjectif.

### 3. Continuité de l'opérateur inverse et les théorèmes de Banach :

a. **$R(T)$ n'est pas un sous-espace fermé de $Y$ :**
Un espace normé est un espace de Banach si et seulement si il est complet. Un sous-espace d'un espace de Banach est un espace de Banach si et seulement si il est fermé. L'espace $Y = c_0(\mathbb{N})$ est un espace de Banach. Si $R(T)$ n'est pas fermé dans $Y$, alors $R(T)$ n'est pas un espace de Banach.
Pour montrer que $R(T)$ n'est pas fermé, nous devons construire une suite $(y^{(j)})_{j \in \mathbb{N}}$ d'éléments de $R(T)$ qui converge dans $Y$ vers un élément $y \in Y$ tel que $y \notin R(T)$.
Reprenons la suite $y = (y_n)_{n \in \mathbb{N}}$ définie par $y_n = \frac{(-1)^n}{\ln(n+2)}$ que nous avons montrée être dans $Y \setminus R(T)$.
Pour chaque entier $J \ge 0$, définissons la suite tronquée $y^{(J)} = (y_n^{(J)})_{n \in \mathbb{N}}$ par :
$y_n^{(J)} = y_n$ si $n < J$
$y_n^{(J)} = 0$ si $n \ge J$.
Chaque $y^{(J)}$ est une suite nulle à partir d'un certain rang. Cela signifie que la suite $(y_n^{(J)} - y_{n+1}^{(J)})_{n \in \mathbb{N}}$ ne contient qu'un nombre fini de termes non nuls, à savoir $y_n - y_{n+1}$ pour $n < J-1$ et $y_{J-1} - 0 = y_{J-1}$ pour $n=J-1$.
Donc $\sum_{n=0}^\infty |y_n^{(J)} - y_{n+1}^{(J)}| < \infty$.
Ainsi, chaque $y^{(J)} \in R(T)$.
Maintenant, nous allons montrer que $(y^{(J)})_{J \in \mathbb{N}}$ converge vers $y$ dans $Y$:
$\|y^{(J)} - y\|_\infty = \sup_{n \in \mathbb{N}} |y_n^{(J)} - y_n|$.
Par construction, $y_n^{(J)} - y_n = 0$ pour $n < J$, et $y_n^{(J)} - y_n = -y_n$ pour $n \ge J$.
Donc $\|y^{(J)} - y\|_\infty = \sup_{n \ge J} |y_n| = \sup_{n \ge J} \left| \frac{(-1)^n}{\ln(n+2)} \right| = \sup_{n \ge J} \frac{1}{\ln(n+2)}$.
Puisque $\lim_{n \to \infty} \frac{1}{\ln(n+2)} = 0$, il s'ensuit que $\lim_{J \to \infty} \sup_{n \ge J} \frac{1}{\ln(n+2)} = 0$.
Ainsi, $y^{(J)} \to y$ dans $Y$.
Puisque $y^{(J)} \in R(T)$ pour tout $J$, et $y \notin R(T)$, cela signifie que $R(T)$ n'est pas un sous-espace fermé de $Y$.
Comme $Y$ est un espace de Banach, et $R(T)$ est un sous-espace non fermé de $Y$, $R(T)$ n'est pas un espace de Banach (muni de la norme $\|\cdot\|_\infty$).

b. **Non-continuité de l'opérateur inverse $T^{-1}$ :**
Nous avons $T: X \to R(T)$ est un opérateur linéaire, continu et bijectif (car injectif par 1.d et surjectif sur son image $R(T)$ par définition).
L'espace $X = \ell^1(\mathbb{N})$ est un espace de Banach.
L'espace $R(T)$ est un espace normé (muni de la norme $\|\cdot\|_\infty$ héritée de $Y$).
Le Théorème de l'Isomorphisme de Banach (qui est une conséquence du Théorème de l'Application Ouverte) stipule que si $T: X \to Z$ est un opérateur linéaire bijectif entre deux espaces de Banach $X$ et $Z$, alors son inverse $T^{-1}: Z \to X$ est également continu.
Dans notre cas, $X$ est un espace de Banach, mais $R(T)$ (muni de la norme $\|\cdot\|_\infty$) n'est pas un espace de Banach, comme montré en 3.a.
Par conséquent, les conditions d'application du Théorème de l'Isomorphisme de Banach ne sont pas remplies pour $T: X \to R(T)$. Cela nous permet de conclure que $T^{-1}: R(T) \to X$ ne peut pas être continu. Si $T^{-1}$ était continu, alors $T$ serait un isomorphisme topologique, ce qui impliquerait que $R(T)$ serait un espace de Banach, en contradiction avec notre conclusion de 3.a.

c. **Construction d'une suite démontrant la non-continuité de $T^{-1}$ :**
Pour montrer directement que $T^{-1}$ n'est pas continu, nous devons trouver une suite $(y^{(j)})_{j \in \mathbb{N}}$ dans $R(T)$ telle que $\|y^{(j)}\|_\infty \to 0$ lorsque $j \to \infty$, mais $\|T^{-1}(y^{(j)})\|_1$ n'est pas bornée (c'est-à-dire $\|T^{-1}(y^{(j)})\|_1 \to \infty$).
Soit $j \in \mathbb{N}$ un entier strictement positif.
Définissons la suite $x^{(j)} = (x_n^{(j)})_{n \in \mathbb{N}}$ par:
$x_n^{(j)} = \frac{(-1)^n}{j}$ pour $0 \le n < 2^j$.
$x_n^{(j)} = 0$ pour $n \ge 2^j$.
Cette suite $x^{(j)}$ est un élément de $\ell^1(\mathbb{N})$ (car elle est nulle à partir d'un certain rang).
Calculons sa norme dans $\ell^1$:
$\|x^{(j)}\|_1 = \sum_{n=0}^\infty |x_n^{(j)}| = \sum_{n=0}^{2^j-1} \left| \frac{(-1)^n}{j} \right| = \sum_{n=0}^{2^j-1} \frac{1}{j} = 2^j \cdot \frac{1}{j} = \frac{2^j}{j}$.
Lorsque $j \to \infty$, $\frac{2^j}{j} \to \infty$. Ainsi, $\|x^{(j)}\|_1$ est non bornée.

Maintenant, construisons $y^{(j)} = T(x^{(j)})$. Par définition, $y^{(j)} \in R(T)$.
Pour $n \in \mathbb{N}$, $(y^{(j)})_n = \sum_{k=n}^\infty x_k^{(j)}$.
Si $n \ge 2^j$, alors $x_k^{(j)} = 0$ pour tout $k \ge n$, donc $(y^{(j)})_n = 0$.
Si $0 \le n < 2^j$, alors $(y^{(j)})_n = \sum_{k=n}^{2^j-1} \frac{(-1)^k}{j} = \frac{1}{j} \sum_{k=n}^{2^j-1} (-1)^k$.
Analysons la somme $\sum_{k=n}^{2^j-1} (-1)^k$:
Le nombre de termes dans cette somme est $(2^j-1) - n + 1 = 2^j - n$.
Puisque $j \ge 1$, $2^j$ est un nombre pair.
Si $n$ est pair, alors $2^j - n$ est pair. La somme de $2^j - n$ termes alternés commençant par $(-1)^n = 1$ est 0.
Si $n$ est impair, alors $2^j - n$ est impair. La somme de $2^j - n$ termes alternés commençant par $(-1)^n = -1$ est $-1$.
Donc, pour $0 \le n < 2^j$:
$(y^{(j)})_n = \begin{cases} 0 & \text{si } n \text{ est pair} \\ -1/j & \text{si } n \text{ est impair} \end{cases}$.
La suite $y^{(j)}$ est donc de la forme $(0, -1/j, 0, -1/j, \dots, \text{derniers termes avant } 2^j \text{ puis } 0, 0, \dots)$.
Calculons la norme de $y^{(j)}$ dans $Y$:
$\|y^{(j)}\|_\infty = \sup_{n \in \mathbb{N}} |(y^{(j)})_n| = \max(0, |-1/j|) = 1/j$.
Lorsque $j \to \infty$, $\|y^{(j)}\|_\infty = 1/j \to 0$.

En résumé, nous avons construit une suite $(y^{(j)})_{j \in \mathbb{N}}$ dans $R(T)$ telle que :
- $\|y^{(j)}\|_\infty \to 0$ lorsque $j \to \infty$.
- $T^{-1}(y^{(j)}) = x^{(j)}$, et $\|T^{-1}(y^{(j)})\|_1 = \|x^{(j)}\|_1 = \frac{2^j}{j} \to \infty$ lorsque $j \to \infty$.

Cette construction explicite montre qu'il n'existe aucune constante $C$ telle que $\|T^{-1}(y)\|_1 \le C \|y\|_\infty$ pour tout $y \in R(T)$.
Par conséquent, l'opérateur inverse $T^{-1}: R(T) \to X$ n'est pas continu.