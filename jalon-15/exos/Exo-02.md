---
title: "Exercice 2 - Jalon 15"
theme: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
difficulty: "1 étoile"
author: "Professeur Émérite"
date: "2023-10-27"
---

## Énoncé

Soit la suite de nombres réels $(u_n)_{n \in \mathbb{N}}$ définie pour tout $n \in \mathbb{N}$ par :
$$u_n = (-1)^n + \frac{1}{n+1}$$

1.  Démontrer que la suite $(u_n)$ est bornée.
2.  Identifier deux sous-suites convergentes distinctes de $(u_n)$ et déterminer leurs limites respectives.
3.  Déterminer l'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$.
4.  Expliquer en quoi cet exercice illustre le théorème de Bolzano-Weierstrass.

---

## Correction

### Question 1 : Démontrer que la suite $(u_n)$ est bornée.

Pour démontrer qu'une suite est bornée, il faut montrer qu'il existe un nombre réel $M > 0$ tel que pour tout $n \in \mathbb{N}$, $|u_n| \le M$.

Considérons l'expression de $u_n$: $u_n = (-1)^n + \frac{1}{n+1}$.

Nous pouvons analyser le comportement de $u_n$ en fonction de la parité de $n$.

*   **Cas 1 : $n$ est pair.**
    Si $n = 2k$ pour un certain $k \in \mathbb{N}$, alors $(-1)^n = (-1)^{2k} = 1$.
    Dans ce cas, $u_{2k} = 1 + \frac{1}{2k+1}$.
    Puisque $k \in \mathbb{N}$, $2k+1 \ge 1$. Donc $0 < \frac{1}{2k+1} \le 1$.
    Par conséquent, $1 < u_{2k} \le 1+1 = 2$.

*   **Cas 2 : $n$ est impair.**
    Si $n = 2k+1$ pour un certain $k \in \mathbb{N}$, alors $(-1)^n = (-1)^{2k+1} = -1$.
    Dans ce cas, $u_{2k+1} = -1 + \frac{1}{2k+1+1} = -1 + \frac{1}{2k+2}$.
    Puisque $k \in \mathbb{N}$, $2k+2 \ge 2$. Donc $0 < \frac{1}{2k+2} \le \frac{1}{2}$.
    Par conséquent, $-1 < u_{2k+1} \le -1 + \frac{1}{2} = -\frac{1}{2}$.

En combinant ces deux cas, nous observons que pour tout $n \in \mathbb{N}$ :
Si $n$ est pair, $1 < u_n \le 2$.
Si $n$ est impair, $-1 < u_n \le -\frac{1}{2}$.

Ainsi, pour tout $n \in \mathbb{N}$, nous avons $-1 < u_n \le 2$.
Cela signifie que la suite $(u_n)$ est bornée inférieurement par $-1$ et bornée supérieurement par $2$.
Nous pouvons donc choisir $M=2$ (ou n'importe quel nombre réel supérieur ou égal à 2).
En effet, pour tout $n \in \mathbb{N}$, $|u_n| \le \max(|-1|, |2|) = 2$.
La suite $(u_n)$ est donc bornée.

### Question 2 : Identifier deux sous-suites convergentes distinctes de $(u_n)$ et déterminer leurs limites respectives.

Nous allons construire deux sous-suites en sélectionnant les termes de $(u_n)$ en fonction de la parité de leur indice.

*   **Première sous-suite : $(u_{2k})_{k \in \mathbb{N}}$ (sous-suite des termes d'indices pairs).**
    Pour tout $k \in \mathbb{N}$, $u_{2k} = (-1)^{2k} + \frac{1}{2k+1} = 1 + \frac{1}{2k+1}$.
    Lorsque $k \to \infty$, le terme $\frac{1}{2k+1}$ tend vers $0$.
    Donc, $\lim_{k \to \infty} u_{2k} = \lim_{k \to \infty} \left(1 + \frac{1}{2k+1}\right) = 1 + 0 = 1$.
    La sous-suite $(u_{2k})$ converge vers $1$.

*   **Deuxième sous-suite : $(u_{2k+1})_{k \in \mathbb{N}}$ (sous-suite des termes d'indices impairs).**
    Pour tout $k \in \mathbb{N}$, $u_{2k+1} = (-1)^{2k+1} + \frac{1}{2k+1+1} = -1 + \frac{1}{2k+2}$.
    Lorsque $k \to \infty$, le terme $\frac{1}{2k+2}$ tend vers $0$.
    Donc, $\lim_{k \to \infty} u_{2k+1} = \lim_{k \to \infty} \left(-1 + \frac{1}{2k+2}\right) = -1 + 0 = -1$.
    La sous-suite $(u_{2k+1})$ converge vers $-1$.

Nous avons identifié deux sous-suites convergentes distinctes : $(u_{2k})$ qui converge vers $1$, et $(u_{2k+1})$ qui converge vers $-1$. Leurs limites sont distinctes ($1 \ne -1$).

### Question 3 : Déterminer l'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$.

Une valeur d'adhérence d'une suite $(u_n)$ est la limite d'une sous-suite convergente de $(u_n)$. D'après la question précédente, nous savons déjà que $1$ et $-1$ sont des valeurs d'adhérence. Il nous reste à montrer qu'il n'y en a pas d'autres.

Soit $L$ une valeur d'adhérence de $(u_n)$. Par définition, il existe une sous-suite $(u_{\varphi(k)})_{k \in \mathbb{N}}$ qui converge vers $L$.
La suite des indices $(\varphi(k))_{k \in \mathbb{N}}$ est une suite strictement croissante d'entiers naturels.

Pour chaque $k$, l'indice $\varphi(k)$ est soit pair, soit impair.
Il y a deux possibilités pour la suite des indices $(\varphi(k))$ :
1.  La suite $(\varphi(k))$ contient une infinité d'indices pairs.
2.  La suite $(\varphi(k))$ contient une infinité d'indices impairs.

*   **Cas A : La suite $(\varphi(k))$ contient une infinité d'indices pairs.**
    Dans ce cas, nous pouvons extraire de $(u_{\varphi(k)})$ une sous-sous-suite $(u_{\varphi(k_j)})_{j \in \mathbb{N}}$ où tous les indices $\varphi(k_j)$ sont pairs.
    Pour cette sous-sous-suite, $\varphi(k_j) = 2m_j$ pour certains entiers $m_j$.
    Alors $u_{\varphi(k_j)} = u_{2m_j} = 1 + \frac{1}{2m_j+1}$.
    Puisque $(u_{\varphi(k)})$ converge vers $L$, toute sous-sous-suite doit également converger vers $L$.
    Donc, $\lim_{j \to \infty} u_{\varphi(k_j)} = L$.
    Or, $\lim_{j \to \infty} \left(1 + \frac{1}{2m_j+1}\right) = 1$.
    Par unicité de la limite, $L=1$.

*   **Cas B : La suite $(\varphi(k))$ contient une infinité d'indices impairs.**
    Dans ce cas, nous pouvons extraire de $(u_{\varphi(k)})$ une sous-sous-suite $(u_{\varphi(k_j)})_{j \in \mathbb{N}}$ où tous les indices $\varphi(k_j)$ sont impairs.
    Pour cette sous-sous-suite, $\varphi(k_j) = 2m_j+1$ pour certains entiers $m_j$.
    Alors $u_{\varphi(k_j)} = u_{2m_j+1} = -1 + \frac{1}{2m_j+2}$.
    Puisque $(u_{\varphi(k)})$ converge vers $L$, toute sous-sous-suite doit également converger vers $L$.
    Donc, $\lim_{j \to \infty} u_{\varphi(k_j)} = L$.
    Or, $\lim_{j \to \infty} \left(-1 + \frac{1}{2m_j+2}\right) = -1$.
    Par unicité de la limite, $L=-1$.

Puisque la suite des indices $(\varphi(k))$ est infinie, elle doit nécessairement contenir une infinité d'indices pairs ou une infinité d'indices impairs (ou les deux).
Si elle contient une infinité d'indices pairs, alors $L=1$.
Si elle contient une infinité d'indices impairs, alors $L=-1$.
Il n'y a pas d'autre possibilité pour $L$.

Par conséquent, l'ensemble de toutes les valeurs d'adhérence de la suite $(u_n)$ est $\{-1, 1\}$.

### Question 4 : Expliquer en quoi cet exercice illustre le théorème de Bolzano-Weierstrass.

Le théorème de Bolzano-Weierstrass stipule que :
**Toute suite bornée de nombres réels admet au moins une sous-suite convergente.**

Dans cet exercice, nous avons démontré les points suivants :
1.  **La suite $(u_n)$ est bornée.** (Réponse à la question 1)
    Nous avons montré que pour tout $n \in \mathbb{N}$, $-1 < u_n \le 2$. La suite est donc bornée.

2.  **La suite $(u_n)$ admet au moins une sous-suite convergente.** (Réponse à la question 2)
    Nous avons explicitement construit deux sous-suites convergentes :
    *   $(u_{2k})$ qui converge vers $1$.
    *   $(u_{2k+1})$ qui converge vers $-1$.
    Le théorème de Bolzano-Weierstrass garantit l'existence d'au moins une telle sous-suite. Ici, nous en avons trouvé deux distinctes, ce qui est en accord avec le théorème.

Cet exercice illustre donc directement le théorème de Bolzano-Weierstrass en fournissant un exemple concret d'une suite bornée et en montrant, par construction, l'existence de sous-suites convergentes, comme le prédit le théorème. Il montre même qu'une suite bornée peut avoir plusieurs valeurs d'adhérence distinctes.
