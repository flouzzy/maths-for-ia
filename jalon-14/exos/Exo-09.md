---
uuid: "jalon-14-exo-09"
title: "Exercice 9 : Convergence d'une suite produit par le critère de Cauchy"
tags: ["math/analyse", "suites", "exercice"]
---
# Exercice 9 : Convergence d'une suite produit par le critère de Cauchy
## Énoncé
Soit $(u_n)_{n \in \mathbb{N}^*}$ la suite de nombres réels définie pour tout $n \in \mathbb{N}^*$ par le produit :
$$u_n = \prod_{k=1}^n \left(1 + \frac{1}{k^2}\right)$$

1.  Montrer rigoureusement que pour tout $n \in \mathbb{N}^*$, $u_n > 0$.
2.  On considère la suite $(v_n)_{n \in \mathbb{N}^*}$ définie par $v_n = \ln(u_n)$. Démontrer, en utilisant la définition rigoureuse ($\epsilon, N$), que la suite $(v_n)$ est une suite de Cauchy.
3.  En déduire, en justifiant chaque étape et en invoquant les propriétés fondamentales de l'analyse réelle, que la suite $(u_n)$ converge vers une limite finie.

## Correction Détaillée
Nous allons aborder cet exercice en suivant scrupuleusement les définitions et théorèmes de l'analyse, sans aucune ellipse.

### Question 1 : Montrer que pour tout $n \in \mathbb{N}^*$, $u_n > 0$.

**Raisonnement :**
La suite $(u_n)$ est définie comme un produit de termes. Pour montrer que $u_n$ est strictement positif, il suffit de montrer que chaque terme du produit est strictement positif.

**Démonstration :**
1.  Soit $k \in \mathbb{N}^*$. Le terme général du produit est $\left(1 + \frac{1}{k^2}\right)$.
2.  Pour tout $k \in \mathbb{N}^*$, $k \ge 1$. Par conséquent, $k^2 \ge 1$.
3.  Il s'ensuit que $\frac{1}{k^2} > 0$.
4.  En ajoutant 1 à cette inégalité, nous obtenons $1 + \frac{1}{k^2} > 1 + 0$, c'est-à-dire $1 + \frac{1}{k^2} > 1$.
5.  Puisque $1 + \frac{1}{k^2} > 1$, chaque terme du produit est strictement positif.
6.  La suite $u_n$ est le produit de $n$ termes strictement positifs : $u_n = \left(1 + \frac{1}{1^2}\right) \times \left(1 + \frac{1}{2^2}\right) \times \dots \times \left(1 + \frac{1}{n^2}\right)$.
7.  Un produit de nombres strictement positifs est lui-même strictement positif.
8.  Par conséquent, pour tout $n \in \mathbb{N}^*$, $u_n > 0$.

### Question 2 : Démontrer, en utilisant la définition rigoureuse ($\epsilon, N$), que la suite $(v_n)$ est une suite de Cauchy.

**Raisonnement :**
La suite $(v_n)$ est définie par $v_n = \ln(u_n)$. En utilisant les propriétés du logarithme, nous pouvons transformer le produit en une somme, ce qui est souvent plus facile à manipuler pour le critère de Cauchy. Ensuite, nous appliquerons la définition de Cauchy pour les suites, en utilisant une inégalité appropriée pour majorer la différence $|v_m - v_n|$.

**Démonstration :**
1.  **Expression de $v_n$ en tant que somme :**
    Nous avons $v_n = \ln(u_n) = \ln\left(\prod_{k=1}^n \left(1 + \frac{1}{k^2}\right)\right)$.
    En utilisant la propriété du logarithme $\ln(a \cdot b) = \ln(a) + \ln(b)$ (qui s'étend à un produit fini), nous obtenons :
    $v_n = \sum_{k=1}^n \ln\left(1 + \frac{1}{k^2}\right)$.

2.  **Définition d'une suite de Cauchy :**
    Une suite $(v_n)_{n \in \mathbb{N}^*}$ est dite de Cauchy si pour tout $\epsilon > 0$, il existe un entier $N \in \mathbb{N}^*$ tel que pour tous entiers $m, n$ vérifiant $m > n \ge N$, on a $|v_m - v_n| < \epsilon$.

3.  **Calcul de $|v_m - v_n|$ pour $m > n$ :**
    Soient $m, n \in \mathbb{N}^*$ tels que $m > n$.
    $v_m - v_n = \sum_{k=1}^m \ln\left(1 + \frac{1}{k^2}\right) - \sum_{k=1}^n \ln\left(1 + \frac{1}{k^2}\right)$.
    Les termes de $k=1$ à $n$ s'annulent, il reste donc :
    $v_m - v_n = \sum_{k=n+1}^m \ln\left(1 + \frac{1}{k^2}\right)$.

4.  **Utilisation de la positivité des termes et d'une inégalité :**
    Pour tout $k \in \mathbb{N}^*$, nous avons $1 + \frac{1}{k^2} > 1$ (d'après la question 1).
    Puisque la fonction logarithme népérien est strictement croissante et $\ln(1)=0$, il s'ensuit que $\ln\left(1 + \frac{1}{k^2}\right) > 0$.
    Par conséquent, la somme $\sum_{k=n+1}^m \ln\left(1 + \frac{1}{k^2}\right)$ est une somme de termes positifs, donc elle est positive.
    Ainsi, $|v_m - v_n| = \sum_{k=n+1}^m \ln\left(1 + \frac{1}{k^2}\right)$.

    Nous utilisons maintenant l'inégalité fondamentale $\ln(1+x) \le x$ pour tout $x \ge 0$.
    Ici, $x = \frac{1}{k^2}$. Puisque $k \in \mathbb{N}^*$, $k^2 > 0$, donc $\frac{1}{k^2} > 0$.
    Appliquons l'inégalité : $\ln\left(1 + \frac{1}{k^2}\right) \le \frac{1}{k^2}$.

    En sommant cette inégalité pour $k$ allant de $n+1$ à $m$ :
    $|v_m - v_n| \le \sum_{k=n+1}^m \frac{1}{k^2}$.

5.  **Lien avec la convergence d'une série de Riemann :**
    La série $\sum_{k=1}^\infty \frac{1}{k^2}$ est une série de Riemann de la forme $\sum_{k=1}^\infty \frac{1}{k^p}$ avec $p=2$.
    Puisque $p=2 > 1$, cette série est convergente.
    Une propriété fondamentale des séries convergentes est que la suite de ses sommes partielles est une suite de Cauchy. Plus précisément, pour une série $\sum a_k$ convergente, pour tout $\epsilon > 0$, il existe un entier $N \in \mathbb{N}^*$ tel que pour tous $m > n \ge N$, $|\sum_{k=n+1}^m a_k| < \epsilon$.
    Appliquons ceci à la série $\sum_{k=1}^\infty \frac{1}{k^2}$. Pour tout $\epsilon > 0$, il existe un entier $N \in \mathbb{N}^*$ tel que pour tous $m > n \ge N$, on a $\sum_{k=n+1}^m \frac{1}{k^2} < \epsilon$.

6.  **Conclusion pour $(v_n)$ :**
    En combinant les résultats des étapes précédentes :
    Pour tout $\epsilon > 0$, nous avons trouvé un entier $N \in \mathbb{N}^*$ tel que pour tous $m > n \ge N$,
    $|v_m - v_n| \le \sum_{k=n+1}^m \frac{1}{k^2} < \epsilon$.
    Ceci correspond exactement à la définition d'une suite de Cauchy.
    Par conséquent, la suite $(v_n)$ est une suite de Cauchy.

### Question 3 : En déduire, en justifiant rigoureusement, que la suite $(u_n)$ converge vers une limite finie.

**Raisonnement :**
Nous avons montré que $(v_n)$ est une suite de Cauchy de nombres réels. L'espace $\mathbb{R}$ est complet, ce qui signifie que toute suite de Cauchy de nombres réels converge vers une limite réelle. Ensuite, nous utiliserons la relation $u_n = e^{v_n}$ et la continuité de la fonction exponentielle pour déduire la convergence de $(u_n)$.

**Démonstration :**
1.  **Convergence de $(v_n)$ :**
    D'après la question 2, la suite $(v_n)$ est une suite de Cauchy.
    Les termes de la suite $(v_n)$ sont des nombres réels.
    Le théorème fondamental de l'analyse réelle stipule que l'espace des nombres réels $\mathbb{R}$ est complet. Cela signifie que toute suite de Cauchy de nombres réels converge vers une limite finie dans $\mathbb{R}$.
    Par conséquent, la suite $(v_n)$ converge vers une limite $L \in \mathbb{R}$.
    Nous pouvons écrire $\lim_{n \to \infty} v_n = L$.

2.  **Relation entre $(u_n)$ et $(v_n)$ :**
    Par définition, $v_n = \ln(u_n)$.
    En appliquant la fonction exponentielle aux deux membres de cette égalité, nous obtenons $e^{v_n} = e^{\ln(u_n)}$.
    Puisque $u_n > 0$ (d'après la question 1), la fonction exponentielle et la fonction logarithme népérien sont des fonctions réciproques l'une de l'autre, donc $e^{\ln(u_n)} = u_n$.
    Ainsi, nous avons $u_n = e^{v_n}$.

3.  **Convergence de $(u_n)$ par continuité :**
    Nous savons que la suite $(v_n)$ converge vers $L$.
    La fonction exponentielle, $f(x) = e^x$, est une fonction continue sur tout $\mathbb{R}$.
    Une propriété essentielle des fonctions continues est que si une suite $(x_n)$ converge vers une limite $x$, alors la suite $(f(x_n))$ converge vers $f(x)$.
    Appliquons cette propriété avec $x_n = v_n$ et $f(x) = e^x$.
    Puisque $\lim_{n \to \infty} v_n = L$ et que $f(x) = e^x$ est continue en $L$, nous pouvons affirmer que :
    $\lim_{n \to \infty} u_n = \lim_{n \to \infty} e^{v_n} = e^{\lim_{n \to \infty} v_n} = e^L$.

4.  **Conclusion :**
    La suite $(u_n)$ converge vers la limite finie $e^L$.
    La convergence est ainsi rigoureusement établie.
