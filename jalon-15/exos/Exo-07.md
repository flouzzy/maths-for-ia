---
title: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
theme: "Analyse réelle : Suites et séries"
difficulty: 4
jalon: 15
exercice_number: 7
author: "Professeur Émérite de Mathématiques"
date: "2023-10-27"
keywords:
  - suite bornée
  - valeurs d'adhérence
  - sous-suite convergente
  - théorème de Bolzano-Weierstrass
  - convergence de suite
  - moyenne de Cesaro
  - suite périodique
```

# Exercice 7 : Analyse d'une suite complexe et de sa moyenne de Cesaro

Soit $(x_n)_{n \in \mathbb{N}}$ une suite de nombres réels définie pour tout $n \in \mathbb{N}$ par :
$$x_n = \cos\left(\frac{n\pi}{3}\right) + \frac{(-1)^n}{n+1}$$

1.  Montrer que la suite $(x_n)$ est bornée.
2.  Déterminer l'ensemble $A$ de toutes les valeurs d'adhérence de $(x_n)$. Justifier rigoureusement votre réponse.
3.  La suite $(x_n)$ converge-t-elle ?
4.  Soit $(y_N)_{N \in \mathbb{N}^*}$ la suite définie par $y_N = \frac{1}{N} \sum_{k=0}^{N-1} x_k$. La suite $(y_N)$ converge-t-elle ? Si oui, quelle est sa limite ?

---

# Correction de l'Exercice 7

## Question 1 : Montrer que la suite $(x_n)$ est bornée.

Pour montrer que la suite $(x_n)$ est bornée, nous devons trouver une constante $M > 0$ telle que $|x_n| \le M$ pour tout $n \in \mathbb{N}$.
La suite $(x_n)$ est définie par $x_n = \cos\left(\frac{n\pi}{3}\right) + \frac{(-1)^n}{n+1}$.

Nous allons majorer séparément les valeurs absolues de chaque terme.

Pour le premier terme, $\cos\left(\frac{n\pi}{3}\right)$ :
La fonction cosinus est bornée, et pour tout $t \in \mathbb{R}$, on a $|\cos(t)| \le 1$.
Ainsi, pour tout $n \in \mathbb{N}$, nous avons :
$$\left|\cos\left(\frac{n\pi}{3}\right)\right| \le 1$$

Pour le second terme, $\frac{(-1)^n}{n+1}$ :
Pour tout $n \in \mathbb{N}$, nous avons :
$$\left|\frac{(-1)^n}{n+1}\right| = \frac{|(-1)^n|}{|n+1|} = \frac{1}{n+1}$$
Puisque $n \in \mathbb{N}$, $n \ge 0$, donc $n+1 \ge 1$.
Par conséquent, $\frac{1}{n+1} \le 1$ pour tout $n \in \mathbb{N}$.
Ainsi, pour tout $n \in \mathbb{N}$, nous avons :
$$\left|\frac{(-1)^n}{n+1}\right| \le 1$$

Maintenant, nous utilisons l'inégalité triangulaire pour $x_n$:
$$|x_n| = \left|\cos\left(\frac{n\pi}{3}\right) + \frac{(-1)^n}{n+1}\right| \le \left|\cos\left(\frac{n\pi}{3}\right)\right| + \left|\frac{(-1)^n}{n+1}\right|$$
En utilisant les majorations établies précédemment :
$$|x_n| \le 1 + 1 = 2$$
Donc, pour tout $n \in \mathbb{N}$, $|x_n| \le 2$.
La suite $(x_n)$ est donc bornée par $M=2$.

## Question 2 : Déterminer l'ensemble $A$ de toutes les valeurs d'adhérence de $(x_n)$. Justifier rigoureusement votre réponse.

Soit $x_n = u_n + v_n$, où $u_n = \cos\left(\frac{n\pi}{3}\right)$ et $v_n = \frac{(-1)^n}{n+1}$.

Commençons par analyser la suite $(v_n)$ :
$$v_n = \frac{(-1)^n}{n+1}$$
Nous avons $\lim_{n \to \infty} |v_n| = \lim_{n \to \infty} \frac{1}{n+1} = 0$.
Par conséquent, $\lim_{n \to \infty} v_n = 0$.

Maintenant, analysons la suite $(u_n)$ :
$$u_n = \cos\left(\frac{n\pi}{3}\right)$$
La suite $(u_n)$ est une suite périodique. La période de $\cos(k\theta)$ est $2\pi/\theta$. Ici $\theta = \pi/3$, donc la période est $2\pi/(\pi/3) = 6$.
Les valeurs prises par $u_n$ sont :
- $u_0 = \cos(0) = 1$
- $u_1 = \cos(\pi/3) = 1/2$
- $u_2 = \cos(2\pi/3) = -1/2$
- $u_3 = \cos(\pi) = -1$
- $u_4 = \cos(4\pi/3) = -1/2$
- $u_5 = \cos(5\pi/3) = 1/2$
- $u_6 = \cos(2\pi) = 1 = u_0$
L'ensemble des valeurs prises par la suite $(u_n)$ est $S_u = \{1, 1/2, -1/2, -1\}$.
Puisque $(u_n)$ est une suite périodique, l'ensemble de ses valeurs d'adhérence est précisément l'ensemble des valeurs qu'elle prend, c'est-à-dire $S_u$.

Soit $L$ une valeur d'adhérence de $(x_n)$. Par définition, il existe une sous-suite $(x_{\phi(k)})_{k \in \mathbb{N}}$ qui converge vers $L$.
$$x_{\phi(k)} = u_{\phi(k)} + v_{\phi(k)}$$
Puisque $\lim_{n \to \infty} v_n = 0$, il s'ensuit que $\lim_{k \to \infty} v_{\phi(k)} = 0$.
Donc, si $x_{\phi(k)} \to L$, alors $u_{\phi(k)} = x_{\phi(k)} - v_{\phi(k)} \to L - 0 = L$.
Ceci signifie que toute valeur d'adhérence de $(x_n)$ doit être une valeur d'adhérence de $(u_n)$.
Par conséquent, $A \subseteq S_u$.

Réciproquement, montrons que chaque élément de $S_u$ est une valeur d'adhérence de $(x_n)$.
Soit $L \in S_u$. Par définition de $S_u$, il existe un indice $j \in \{0, 1, 2, 3, 4, 5\}$ tel que $u_j = L$.
Considérons la sous-suite $(x_{6k+j})_{k \in \mathbb{N}}$.
Pour cette sous-suite, le terme $u_{6k+j}$ est :
$$u_{6k+j} = \cos\left(\frac{(6k+j)\pi}{3}\right) = \cos\left(2k\pi + \frac{j\pi}{3}\right) = \cos\left(\frac{j\pi}{3}\right) = u_j = L$$
Le terme $v_{6k+j}$ est :
$$v_{6k+j} = \frac{(-1)^{6k+j}}{6k+j+1} = \frac{(-1)^j}{6k+j+1}$$
Puisque $\lim_{k \to \infty} (6k+j+1) = \infty$, nous avons $\lim_{k \to \infty} v_{6k+j} = 0$.
Par conséquent, la sous-suite $(x_{6k+j})$ converge vers $L$:
$$\lim_{k \to \infty} x_{6k+j} = \lim_{k \to \infty} (u_{6k+j} + v_{6k+j}) = L + 0 = L$$
Ceci montre que chaque élément de $S_u$ est une valeur d'adhérence de $(x_n)$.
Par conséquent, $S_u \subseteq A$.

En combinant les deux inclusions ($A \subseteq S_u$ et $S_u \subseteq A$), nous concluons que l'ensemble des valeurs d'adhérence de $(x_n)$ est $A = S_u$.
$$A = \left\lbrace1, \frac{1}{2}, -\frac{1}{2}, -1\right\rbrace$$

## Question 3 : La suite $(x_n)$ converge-t-elle ?

Une suite de nombres réels converge si et seulement si elle est bornée et possède une unique valeur d'adhérence.
D'après la question 1, la suite $(x_n)$ est bornée.
D'après la question 2, l'ensemble des valeurs d'adhérence de $(x_n)$ est $A = \{1, 1/2, -1/2, -1\}$.
Cet ensemble contient quatre éléments distincts.
Puisque la suite $(x_n)$ possède plus d'une valeur d'adhérence, elle ne converge pas.

## Question 4 : Soit $(y_N)_{N \in \mathbb{N}^*}$ la suite définie par $y_N = \frac{1}{N} \sum_{k=0}^{N-1} x_k$. La suite $(y_N)$ converge-t-elle ? Si oui, quelle est sa limite ?

La suite $(y_N)$ est la moyenne de Cesaro de la suite $(x_n)$.
Nous avons $x_k = \cos\left(\frac{k\pi}{3}\right) + \frac{(-1)^k}{k+1}$.
Donc, $y_N = \frac{1}{N} \sum_{k=0}^{N-1} \left(\cos\left(\frac{k\pi}{3}\right) + \frac{(-1)^k}{k+1}\right)$.
Nous pouvons séparer la somme en deux parties :
$$y_N = \frac{1}{N} \sum_{k=0}^{N-1} \cos\left(\frac{k\pi}{3}\right) + \frac{1}{N} \sum_{k=0}^{N-1} \frac{(-1)^k}{k+1}$$

Considérons le second terme : $T_N^{(2)} = \frac{1}{N} \sum_{k=0}^{N-1} \frac{(-1)^k}{k+1}$.
La série $\sum_{k=0}^{\infty} \frac{(-1)^k}{k+1}$ est une série alternée.
Soit $a_k = \frac{1}{k+1}$. La suite $(a_k)$ est positive, décroissante et tend vers 0.
D'après le critère de Leibniz, la série $\sum_{k=0}^{\infty} (-1)^k a_k$ converge. Sa somme est $\ln(2)$.
Soit $S = \sum_{k=0}^{\infty} \frac{(-1)^k}{k+1}$.
Alors $\sum_{k=0}^{N-1} \frac{(-1)^k}{k+1}$ est la $N$-ième somme partielle de cette série convergente.
Notons $P_N = \sum_{k=0}^{N-1} \frac{(-1)^k}{k+1}$. Nous savons que $\lim_{N \to \infty} P_N = S = \ln(2)$.
Le terme $T_N^{(2)}$ est alors $\frac{P_N}{N}$.
Puisque $P_N$ converge vers une limite finie $S$, et $N \to \infty$, nous avons :
$$\lim_{N \to \infty} T_N^{(2)} = \lim_{N \to \infty} \frac{P_N}{N} = 0$$

Considérons le premier terme : $T_N^{(1)} = \frac{1}{N} \sum_{k=0}^{N-1} \cos\left(\frac{k\pi}{3}\right)$.
La suite $u_k = \cos\left(\frac{k\pi}{3}\right)$ est périodique de période 6.
Calculons la somme des termes sur une période complète :
$$P = \sum_{k=0}^{5} \cos\left(\frac{k\pi}{3}\right) = \cos(0) + \cos(\pi/3) + \cos(2\pi/3) + \cos(\pi) + \cos(4\pi/3) + \cos(5\pi/3)$$
$$P = 1 + \frac{1}{2} - \frac{1}{2} - 1 - \frac{1}{2} + \frac{1}{2} = 0$$
Soit $N \in \mathbb{N}^*$. Nous pouvons écrire $N = 6q + r$, où $q = \lfloor N/6 \rfloor$ est le quotient et $r = N \pmod 6$ est le reste, avec $0 \le r < 6$.
La somme $\sum_{k=0}^{N-1} \cos\left(\frac{k\pi}{3}\right)$ peut s'écrire comme :
$$\sum_{k=0}^{N-1} u_k = \sum_{k=0}^{6q-1} u_k + \sum_{k=6q}^{N-1} u_k$$
La première partie est la somme de $q$ périodes complètes :
$$\sum_{k=0}^{6q-1} u_k = q \cdot P = q \cdot 0 = 0$$
La seconde partie est la somme des $r$ premiers termes de la période suivante (ou les $r$ derniers termes de la somme si $N-1$ est le dernier indice) :
$$\sum_{k=6q}^{N-1} u_k = \sum_{j=0}^{r-1} u_{6q+j} = \sum_{j=0}^{r-1} \cos\left(\frac{(6q+j)\pi}{3}\right) = \sum_{j=0}^{r-1} \cos\left(2q\pi + \frac{j\pi}{3}\right) = \sum_{j=0}^{r-1} \cos\left(\frac{j\pi}{3}\right)$$
Cette somme est une somme finie de $r$ termes, où $r \in \{0, 1, 2, 3, 4, 5\}$.
La valeur maximale de cette somme est $1 + 1/2 = 3/2$ (pour $r=2$). La valeur minimale est $-1/2$ (pour $r=5$).
En général, cette somme est bornée. Soit $M_S = \max_{0 \le r < 6} \left|\sum_{j=0}^{r-1} \cos\left(\frac{j\pi}{3}\right)\right|$. On a $M_S = 3/2$.
Donc, $\left|\sum_{k=0}^{N-1} \cos\left(\frac{k\pi}{3}\right)\right| = \left|\sum_{j=0}^{r-1} \cos\left(\frac{j\pi}{3}\right)\right| \le M_S$.
Par conséquent, $T_N^{(1)} = \frac{1}{N} \sum_{k=0}^{N-1} \cos\left(\frac{k\pi}{3}\right)$ satisfait :
$$\left|T_N^{(1)}\right| \le \frac{M_S}{N}$$
Puisque $M_S$ est une constante finie et $N \to \infty$, nous avons :
$$\lim_{N \to \infty} T_N^{(1)} = 0$$

En combinant les limites des deux termes :
$$\lim_{N \to \infty} y_N = \lim_{N \to \infty} T_N^{(1)} + \lim_{N \to \infty} T_N^{(2)} = 0 + 0 = 0$$
La suite $(y_N)$ converge, et sa limite est $0$.

**Conclusion :** La suite $(y_N)$ converge vers $0$.
