---
title: "Exercice 6 - Jalon 15"
subtitle: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
author: "Professeur Émérite de Mathématiques"
date: "2023-10-27"
difficulty: "★★★"
keywords:
  - sous-suite
  - valeur d'adhérence
  - Bolzano-Weierstrass
  - suite bornée
  - suite convergente
  - limite supérieure
  - limite inférieure
---

# Exercice 6

Soit la suite réelle $(x_n)_{n \in \mathbb{N}}$ définie pour tout $n \in \mathbb{N}$ par :
$$x_n = \frac{n \pmod 3}{n+1} + \cos\left(\frac{n\pi}{2}\right)$$
où $n \pmod 3$ désigne le reste de la division euclidienne de $n$ par $3$.

1.  Démontrer que la suite $(x_n)$ est bornée.
2.  En déduire, en utilisant le théorème de Bolzano-Weierstrass, que la suite $(x_n)$ admet au moins une sous-suite convergente.
3.  Déterminer l'ensemble de toutes les valeurs d'adhérence de la suite $(x_n)$.
4.  En déduire la limite supérieure et la limite inférieure de la suite $(x_n)$.

---

# Correction de l'Exercice 6

## Question 1 : Démontrer que la suite $(x_n)$ est bornée.

Pour tout $n \in \mathbb{N}$, la suite $(x_n)$ est définie par $x_n = \frac{n \pmod 3}{n+1} + \cos\left(\frac{n\pi}{2}\right)$.

Nous allons analyser les bornes de chacun des deux termes composant $x_n$.

*   **Analyse du terme $\frac{n \pmod 3}{n+1}$ :**
    Le reste de la division euclidienne de $n$ par $3$, noté $n \pmod 3$, est un entier qui appartient à l'ensemble $\{0, 1, 2\}$.
    Ainsi, pour tout $n \in \mathbb{N}$, nous avons l'encadrement suivant :
    $$0 \le n \pmod 3 \le 2$$
    Le dénominateur $n+1$ est toujours strictement positif pour $n \in \mathbb{N}$ (il vaut au minimum $1$ pour $n=0$). Nous pouvons donc diviser l'inégalité par $n+1$ sans en changer le sens :
    $$\frac{0}{n+1} \le \frac{n \pmod 3}{n+1} \le \frac{2}{n+1}$$
    $$0 \le \frac{n \pmod 3}{n+1} \le \frac{2}{n+1}$$
    Pour $n=0$, le terme vaut $\frac{0}{1} = 0$.
    Pour $n \ge 0$, $n+1 \ge 1$, ce qui implique $\frac{1}{n+1} \le 1$. Par conséquent, $\frac{2}{n+1} \le 2$.
    Donc, pour tout $n \in \mathbb{N}$, nous avons :
    $$0 \le \frac{n \pmod 3}{n+1} \le 2$$

*   **Analyse du terme $\cos\left(\frac{n\pi}{2}\right)$ :**
    La fonction cosinus est une fonction bornée. Pour tout argument réel $X$, nous savons que $-1 \le \cos(X) \le 1$.
    En particulier, pour $X = \frac{n\pi}{2}$, nous avons :
    $$-1 \le \cos\left(\frac{n\pi}{2}\right) \le 1$$

*   **Combinaison des bornes :**
    En additionnant les inégalités obtenues pour les deux termes, nous obtenons un encadrement pour $x_n$ :
    $$0 + (-1) \le \frac{n \pmod 3}{n+1} + \cos\left(\frac{n\pi}{2}\right) \le 2 + 1$$
    $$-1 \le x_n \le 3$$
    Puisque tous les termes de la suite $(x_n)$ sont compris entre $-1$ et $3$, la suite $(x_n)$ est bornée. Par exemple, on peut affirmer que $|x_n| \le 3$ pour tout $n \in \mathbb{N}$.

## Question 2 : En déduire, en utilisant le théorème de Bolzano-Weierstrass, que la suite $(x_n)$ admet au moins une sous-suite convergente.

Le théorème de Bolzano-Weierstrass est un résultat fondamental de l'analyse réelle. Il stipule que toute suite réelle bornée admet au moins une sous-suite convergente.

D'après la question 1, nous avons démontré que la suite $(x_n)$ est une suite de nombres réels et qu'elle est bornée.
Par conséquent, en appliquant directement le théorème de Bolzano-Weierstrass, nous pouvons conclure que la suite $(x_n)$ admet au moins une sous-suite convergente.

## Question 3 : Déterminer l'ensemble de toutes les valeurs d'adhérence de la suite $(x_n)$.

Soit $y_n = \frac{n \pmod 3}{n+1}$ et $z_n = \cos\left(\frac{n\pi}{2}\right)$. Ainsi, $x_n = y_n + z_n$.

Nous allons d'abord déterminer la limite de $y_n$ lorsque $n \to \infty$.
D'après la question 1, nous avons l'encadrement $0 \le y_n \le \frac{2}{n+1}$.
Puisque $\lim_{n \to \infty} 0 = 0$ et $\lim_{n \to \infty} \frac{2}{n+1} = 0$, le théorème des gendarmes (ou théorème d'encadrement) nous permet de conclure que :
$$\lim_{n \to \infty} y_n = 0$$

Ensuite, nous allons analyser le comportement de $z_n = \cos\left(\frac{n\pi}{2}\right)$. Les valeurs de $z_n$ dépendent du reste de la division de $n$ par $4$. Nous allons examiner les quatre cas possibles pour $n \pmod 4$:

*   Si $n = 4k$ pour un entier $k \ge 0$:
    $z_{4k} = \cos\left(\frac{4k\pi}{2}\right) = \cos(2k\pi) = 1$.
*   Si $n = 4k+1$ pour un entier $k \ge 0$:
    $z_{4k+1} = \cos\left(\frac{(4k+1)\pi}{2}\right) = \cos\left(2k\pi + \frac{\pi}{2}\right) = \cos\left(\frac{\pi}{2}\right) = 0$.
*   Si $n = 4k+2$ pour un entier $k \ge 0$:
    $z_{4k+2} = \cos\left(\frac{(4k+2)\pi}{2}\right) = \cos(2k\pi + \pi) = \cos(\pi) = -1$.
*   Si $n = 4k+3$ pour un entier $k \ge 0$:
    $z_{4k+3} = \cos\left(\frac{(4k+3)\pi}{2}\right) = \cos\left(2k\pi + \frac{3\pi}{2}\right) = \cos\left(\frac{3\pi}{2}\right) = 0$.

La suite $(z_n)$ prend donc les valeurs $1, 0, -1, 0, 1, 0, -1, 0, \dots$ de manière cyclique. L'ensemble des valeurs d'adhérence de la suite $(z_n)$ est $\{-1, 0, 1\}$.

Maintenant, nous allons déterminer les valeurs d'adhérence de $(x_n)$ en considérant des sous-suites basées sur $n \pmod 4$. Pour chaque cas, nous utiliserons le fait que $\lim_{n \to \infty} y_n = 0$, ce qui implique que $\lim_{k \to \infty} y_{\phi(k)} = 0$ pour toute sous-suite $(y_{\phi(k)})$.

1.  **Considérons la sous-suite $(x_{4k})$ pour $k \in \mathbb{N}$ :**
    $x_{4k} = \frac{4k \pmod 3}{4k+1} + \cos\left(\frac{4k\pi}{2}\right)$.
    Puisque $4k = 3k + k$, on a $4k \pmod 3 = k \pmod 3$.
    Donc, $x_{4k} = \frac{k \pmod 3}{4k+1} + 1$.
    Nous savons que $0 \le k \pmod 3 \le 2$. Par conséquent, $0 \le \frac{k \pmod 3}{4k+1} \le \frac{2}{4k+1}$.
    Comme $\lim_{k \to \infty} \frac{2}{4k+1} = 0$, par le théorème des gendarmes, $\lim_{k \to \infty} \frac{k \pmod 3}{4k+1} = 0$.
    Ainsi, $\lim_{k \to \infty} x_{4k} = 0 + 1 = 1$.
    La valeur $1$ est donc une valeur d'adhérence de la suite $(x_n)$.

2.  **Considérons la sous-suite $(x_{4k+1})$ pour $k \in \mathbb{N}$ :**
    $x_{4k+1} = \frac{(4k+1) \pmod 3}{(4k+1)+1} + \cos\left(\frac{(4k+1)\pi}{2}\right)$.
    Puisque $4k+1 = 3k + k + 1$, on a $(4k+1) \pmod 3 = (k+1) \pmod 3$.
    Donc, $x_{4k+1} = \frac{(k+1) \pmod 3}{4k+2} + 0$.
    Nous savons que $0 \le (k+1) \pmod 3 \le 2$. Par conséquent, $0 \le \frac{(k+1) \pmod 3}{4k+2} \le \frac{2}{4k+2}$.
    Comme $\lim_{k \to \infty} \frac{2}{4k+2} = 0$, par le théorème des gendarmes, $\lim_{k \to \infty} \frac{(k+1) \pmod 3}{4k+2} = 0$.
    Ainsi, $\lim_{k \to \infty} x_{4k+1} = 0 + 0 = 0$.
    La valeur $0$ est donc une valeur d'adhérence de la suite $(x_n)$.

3.  **Considérons la sous-suite $(x_{4k+2})$ pour $k \in \mathbb{N}$ :**
    $x_{4k+2} = \frac{(4k+2) \pmod 3}{(4k+2)+1} + \cos\left(\frac{(4k+2)\pi}{2}\right)$.
    Puisque $4k+2 = 3k + k + 2$, on a $(4k+2) \pmod 3 = (k+2) \pmod 3$.
    Donc, $x_{4k+2} = \frac{(k+2) \pmod 3}{4k+3} + (-1)$.
    Nous savons que $0 \le (k+2) \pmod 3 \le 2$. Par conséquent, $0 \le \frac{(k+2) \pmod 3}{4k+3} \le \frac{2}{4k+3}$.
    Comme $\lim_{k \to \infty} \frac{2}{4k+3} = 0$, par le théorème des gendarmes, $\lim_{k \to \infty} \frac{(k+2) \pmod 3}{4k+3} = 0$.
    Ainsi, $\lim_{k \to \infty} x_{4k+2} = 0 + (-1) = -1$.
    La valeur $-1$ est donc une valeur d'adhérence de la suite $(x_n)$.

4.  **Considérons la sous-suite $(x_{4k+3})$ pour $k \in \mathbb{N}$ :**
    $x_{4k+3} = \frac{(4k+3) \pmod 3}{(4k+3)+1} + \cos\left(\frac{(4k+3)\pi}{2}\right)$.
    Puisque $4k+3 = 3k + k + 3$, on a $(4k+3) \pmod 3 = k \pmod 3$.
    Donc, $x_{4k+3} = \frac{k \pmod 3}{4k+4} + 0$.
    Nous savons que $0 \le k \pmod 3 \le 2$. Par conséquent, $0 \le \frac{k \pmod 3}{4k+4} \le \frac{2}{4k+4}$.
    Comme $\lim_{k \to \infty} \frac{2}{4k+4} = 0$, par le théorème des gendarmes, $\lim_{k \to \infty} \frac{k \pmod 3}{4k+4} = 0$.
    Ainsi, $\lim_{k \to \infty} x_{4k+3} = 0 + 0 = 0$.
    Cette sous-suite converge vers $0$, ce qui confirme que $0$ est une valeur d'adhérence.

Nous avons identifié trois valeurs d'adhérence pour la suite $(x_n)$: $\{-1, 0, 1\}$.
Pour montrer que ce sont les *seules* valeurs d'adhérence, considérons une sous-suite quelconque $(x_{\phi(k)})$ qui converge vers une limite $L$.
Nous avons $x_{\phi(k)} = y_{\phi(k)} + z_{\phi(k)}$.
Puisque $\lim_{n \to \infty} y_n = 0$, toute sous-suite $(y_{\phi(k)})$ converge également vers $0$.
Par conséquent, la limite $L$ de $(x_{\phi(k)})$ est donnée par :
$$L = \lim_{k \to \infty} x_{\phi(k)} = \lim_{k \to \infty} (y_{\phi(k)} + z_{\phi(k)}) = \lim_{k \to \infty} y_{\phi(k)} + \lim_{k \to \infty} z_{\phi(k)} = 0 + \lim_{k \to \infty} z_{\phi(k)}$$
Donc, $L = \lim_{k \to \infty} z_{\phi(k)}$.
La suite $(z_n)$ ne prend que les valeurs $1, 0, -1, 0, \dots$. Toute sous-suite convergente de $(z_n)$ doit nécessairement converger vers l'une de ces valeurs qui apparaissent une infinité de fois. C'est-à-dire, la limite d'une sous-suite convergente de $(z_n)$ doit être une valeur d'adhérence de $(z_n)$. L'ensemble des valeurs d'adhérence de $(z_n)$ est précisément $\{-1, 0, 1\}$.
Par conséquent, la limite $L$ de toute sous-suite convergente de $(x_n)$ doit appartenir à l'ensemble $\{-1, 0, 1\}$.

L'ensemble de toutes les valeurs d'adhérence de la suite $(x_n)$ est donc $\{-1, 0, 1\}$.

## Question 4 : En déduire la limite supérieure et la limite inférieure de la suite $(x_n)$.

Pour une suite réelle bornée, la limite supérieure est la plus grande de ses valeurs d'adhérence, et la limite inférieure est la plus petite de ses valeurs d'adhérence.

D'après la question 3, l'ensemble des valeurs d'adhérence de la suite $(x_n)$ est $\{-1, 0, 1\}$.

*   La limite supérieure de $(x_n)$, notée $\limsup_{n \to \infty} x_n$, est la plus grande valeur dans l'ensemble des valeurs d'adhérence :
    $$\limsup_{n \to \infty} x_n = \max(\{-1, 0, 1\}) = 1$$

*   La limite inférieure de $(x_n)$, notée $\liminf_{n \to \infty} x_n$, est la plus petite valeur dans l'ensemble des valeurs d'adhérence :
    $$\liminf_{n \to \infty} x_n = \min(\{-1, 0, 1\}) = -1$$
