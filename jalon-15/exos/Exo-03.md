---
title: "Exercice 3 : Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
jalon: 15
difficulty: 2
theme: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
---

# Exercice 3

Soit la suite réelle $(u_n)_{n \in \mathbb{N}}$ définie pour tout $n \in \mathbb{N}$ par :
$$u_n = \frac{n}{n+1} \cos\left(\frac{n\pi}{3}\right)$$

1.  Montrer que la suite $(u_n)$ est bornée.
2.  En déduire, en utilisant le théorème de Bolzano-Weierstrass, l'existence d'au moins une sous-suite convergente.
3.  Déterminer l'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$. Pour chaque valeur d'adhérence $L$, on précisera une sous-suite de $(u_n)$ qui converge vers $L$.

---

# Correction de l'Exercice 3

## Question 1 : Montrer que la suite $(u_n)$ est bornée.

Pour tout $n \in \mathbb{N}$, nous avons $n \ge 0$.
Par conséquent, $n+1 > 0$.
Le terme $\frac{n}{n+1}$ est toujours positif ou nul.
De plus, $n < n+1$, donc $\frac{n}{n+1} < 1$.
Ainsi, pour tout $n \in \mathbb{N}$, $0 \le \frac{n}{n+1} < 1$.

Concernant le terme $\cos\left(\frac{n\pi}{3}\right)$, nous savons que la fonction cosinus est bornée. Pour tout $x \in \mathbb{R}$, $-1 \le \cos(x) \le 1$.
Donc, pour tout $n \in \mathbb{N}$, $-1 \le \cos\left(\frac{n\pi}{3}\right) \le 1$.

En combinant ces deux inégalités, nous pouvons majorer la valeur absolue de $u_n$:
$$|u_n| = \left|\frac{n}{n+1} \cos\left(\frac{n\pi}{3}\right)\right| = \left|\frac{n}{n+1}\right| \cdot \left|\cos\left(\frac{n\pi}{3}\right)\right|$$
Puisque $0 \le \frac{n}{n+1} < 1$ et $0 \le \left|\cos\left(\frac{n\pi}{3}\right)\right| \le 1$, nous obtenons :
$$|u_n| \le 1 \cdot 1 = 1$$
Ainsi, pour tout $n \in \mathbb{N}$, $-1 \le u_n \le 1$.
La suite $(u_n)$ est donc bornée.

## Question 2 : En déduire, en utilisant le théorème de Bolzano-Weierstrass, l'existence d'au moins une sous-suite convergente.

Le théorème de Bolzano-Weierstrass stipule que toute suite réelle bornée admet au moins une sous-suite convergente.
D'après la question 1, nous avons montré que la suite $(u_n)$ est bornée.
Par application directe du théorème de Bolzano-Weierstrass, nous pouvons affirmer qu'il existe au moins une sous-suite de $(u_n)$ qui converge.

## Question 3 : Déterminer l'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$. Pour chaque valeur d'adhérence $L$, on précisera une sous-suite de $(u_n)$ qui converge vers $L$.

Pour déterminer les valeurs d'adhérence de $(u_n)$, nous allons analyser le comportement du terme $\cos\left(\frac{n\pi}{3}\right)$. La fonction cosinus est $2\pi$-périodique. Le terme $\frac{n\pi}{3}$ est $2\pi$-périodique en $n$ si $\frac{(n+P)\pi}{3} = \frac{n\pi}{3} + 2k\pi$ pour un entier $k$. Cela signifie $\frac{P\pi}{3} = 2k\pi$, soit $P=6k$. La période minimale pour $n$ est donc $P=6$.
Les valeurs prises par $\cos\left(\frac{n\pi}{3}\right)$ dépendent de $n \pmod 6$:
*   Si $n = 6k$ (pour $k \in \mathbb{N}$), alors $\cos\left(\frac{6k\pi}{3}\right) = \cos(2k\pi) = 1$.
*   Si $n = 6k+1$, alors $\cos\left(\frac{(6k+1)\pi}{3}\right) = \cos\left(2k\pi + \frac{\pi}{3}\right) = \cos\left(\frac{\pi}{3}\right) = \frac{1}{2}$.
*   Si $n = 6k+2$, alors $\cos\left(\frac{(6k+2)\pi}{3}\right) = \cos\left(2k\pi + \frac{2\pi}{3}\right) = \cos\left(\frac{2\pi}{3}\right) = -\frac{1}{2}$.
*   Si $n = 6k+3$, alors $\cos\left(\frac{(6k+3)\pi}{3}\right) = \cos\left(2k\pi + \pi\right) = \cos(\pi) = -1$.
*   Si $n = 6k+4$, alors $\cos\left(\frac{(6k+4)\pi}{3}\right) = \cos\left(2k\pi + \frac{4\pi}{3}\right) = \cos\left(\frac{4\pi}{3}\right) = -\frac{1}{2}$.
*   Si $n = 6k+5$, alors $\cos\left(\frac{(6k+5)\pi}{3}\right) = \cos\left(2k\pi + \frac{5\pi}{3}\right) = \cos\left(\frac{5\pi}{3}\right) = \frac{1}{2}$.

Les valeurs prises par $\cos\left(\frac{n\pi}{3}\right)$ sont donc cycliquement $1, \frac{1}{2}, -\frac{1}{2}, -1, -\frac{1}{2}, \frac{1}{2}, \dots$.
L'ensemble des valeurs prises par $\cos\left(\frac{n\pi}{3}\right)$ est fini : $\left\lbrace1, \frac{1}{2}, -\frac{1}{2}, -1\right\rbrace$.

Considérons maintenant le comportement du terme $\frac{n}{n+1}$ lorsque $n \to \infty$.
Nous avons $\lim_{n \to \infty} \frac{n}{n+1} = \lim_{n \to \infty} \frac{1}{1 + \frac{1}{n}} = 1$.

Nous allons construire des sous-suites de $(u_n)$ en sélectionnant les indices $n$ selon leur reste modulo 6.

1.  **Sous-suite pour $n=6k$ :**
    Soit la sous-suite $(u_{6k})_{k \in \mathbb{N}}$.
    $$u_{6k} = \frac{6k}{6k+1} \cos\left(\frac{6k\pi}{3}\right) = \frac{6k}{6k+1} \cdot 1$$
    Lorsque $k \to \infty$, $\frac{6k}{6k+1} \to 1$.
    Donc, $\lim_{k \to \infty} u_{6k} = 1 \cdot 1 = 1$.
    Ainsi, $L_1 = 1$ est une valeur d'adhérence de $(u_n)$.

2.  **Sous-suite pour $n=6k+1$ :**
    Soit la sous-suite $(u_{6k+1})_{k \in \mathbb{N}}$.
    $$u_{6k+1} = \frac{6k+1}{6k+1+1} \cos\left(\frac{(6k+1)\pi}{3}\right) = \frac{6k+1}{6k+2} \cdot \frac{1}{2}$$
    Lorsque $k \to \infty$, $\frac{6k+1}{6k+2} = \frac{6 + 1/k}{6 + 2/k} \to \frac{6}{6} = 1$.
    Donc, $\lim_{k \to \infty} u_{6k+1} = 1 \cdot \frac{1}{2} = \frac{1}{2}$.
    Ainsi, $L_2 = \frac{1}{2}$ est une valeur d'adhérence de $(u_n)$.

3.  **Sous-suite pour $n=6k+2$ :**
    Soit la sous-suite $(u_{6k+2})_{k \in \mathbb{N}}$.
    $$u_{6k+2} = \frac{6k+2}{6k+2+1} \cos\left(\frac{(6k+2)\pi}{3}\right) = \frac{6k+2}{6k+3} \cdot \left(-\frac{1}{2}\right)$$
    Lorsque $k \to \infty$, $\frac{6k+2}{6k+3} = \frac{6 + 2/k}{6 + 3/k} \to \frac{6}{6} = 1$.
    Donc, $\lim_{k \to \infty} u_{6k+2} = 1 \cdot \left(-\frac{1}{2}\right) = -\frac{1}{2}$.
    Ainsi, $L_3 = -\frac{1}{2}$ est une valeur d'adhérence de $(u_n)$.

4.  **Sous-suite pour $n=6k+3$ :**
    Soit la sous-suite $(u_{6k+3})_{k \in \mathbb{N}}$.
    $$u_{6k+3} = \frac{6k+3}{6k+3+1} \cos\left(\frac{(6k+3)\pi}{3}\right) = \frac{6k+3}{6k+4} \cdot (-1)$$
    Lorsque $k \to \infty$, $\frac{6k+3}{6k+4} = \frac{6 + 3/k}{6 + 4/k} \to \frac{6}{6} = 1$.
    Donc, $\lim_{k \to \infty} u_{6k+3} = 1 \cdot (-1) = -1$.
    Ainsi, $L_4 = -1$ est une valeur d'adhérence de $(u_n)$.

5.  **Sous-suite pour $n=6k+4$ :**
    Soit la sous-suite $(u_{6k+4})_{k \in \mathbb{N}}$.
    $$u_{6k+4} = \frac{6k+4}{6k+4+1} \cos\left(\frac{(6k+4)\pi}{3}\right) = \frac{6k+4}{6k+5} \cdot \left(-\frac{1}{2}\right)$$
    Lorsque $k \to \infty$, $\frac{6k+4}{6k+5} = \frac{6 + 4/k}{6 + 5/k} \to \frac{6}{6} = 1$.
    Donc, $\lim_{k \to \infty} u_{6k+4} = 1 \cdot \left(-\frac{1}{2}\right) = -\frac{1}{2}$.
    Cette valeur d'adhérence est déjà trouvée ($L_3$).

6.  **Sous-suite pour $n=6k+5$ :**
    Soit la sous-suite $(u_{6k+5})_{k \in \mathbb{N}}$.
    $$u_{6k+5} = \frac{6k+5}{6k+5+1} \cos\left(\frac{(6k+5)\pi}{3}\right) = \frac{6k+5}{6k+6} \cdot \frac{1}{2}$$
    Lorsque $k \to \infty$, $\frac{6k+5}{6k+6} = \frac{6 + 5/k}{6 + 6/k} \to \frac{6}{6} = 1$.
    Donc, $\lim_{k \to \infty} u_{6k+5} = 1 \cdot \frac{1}{2} = \frac{1}{2}$.
    Cette valeur d'adhérence est déjà trouvée ($L_2$).

L'ensemble des valeurs d'adhérence que nous avons identifiées est $\left\lbrace1, \frac{1}{2}, -\frac{1}{2}, -1\right\rbrace$.

Pour montrer que ce sont *toutes* les valeurs d'adhérence, considérons une sous-suite quelconque $(u_{\phi(k)})$ de $(u_n)$ qui converge vers une limite $L$.
Nous avons $u_{\phi(k)} = \frac{\phi(k)}{\phi(k)+1} \cos\left(\frac{\phi(k)\pi}{3}\right)$.
Puisque $\lim_{k \to \infty} \frac{\phi(k)}{\phi(k)+1} = 1$ (car $\phi(k) \to \infty$ lorsque $k \to \infty$), et que $\lim_{k \to \infty} u_{\phi(k)} = L$, il s'ensuit que la sous-suite $\left(\cos\left(\frac{\phi(k)\pi}{3}\right)\right)_{k \in \mathbb{N}}$ doit également converger vers $L$.
Or, la suite $\left(\cos\left(\frac{n\pi}{3}\right)\right)_{n \in \mathbb{N}}$ ne prend qu'un nombre fini de valeurs : $\left\lbrace1, \frac{1}{2}, -\frac{1}{2}, -1\right\rbrace$.
Si une sous-suite d'une suite ne prenant qu'un nombre fini de valeurs converge, alors sa limite doit nécessairement être l'une de ces valeurs.
Par conséquent, $L$ doit appartenir à l'ensemble $\left\lbrace1, \frac{1}{2}, -\frac{1}{2}, -1\right\rbrace$.

L'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$ est donc exactement $\left\lbrace1, \frac{1}{2}, -\frac{1}{2}, -1\right\rbrace$.
