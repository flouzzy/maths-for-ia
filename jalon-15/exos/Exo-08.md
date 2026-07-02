---
title: "Exercice 8 - Jalon 15"
subtitle: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
author: "Prof. A. Dubois"
date: "2023-10-27"
difficulty: "★★★★☆"
keywords:
  - sous-suite
  - valeur d'adhérence
  - Bolzano-Weierstrass
  - limite supérieure
  - limite inférieure
  - compacité
  - suite récurrente
---

## Énoncé de l'Exercice 8

Soit $(u_n)_{n \in \mathbb{N}}$ une suite bornée de nombres réels. On note $A(u)$ l'ensemble de ses valeurs d'adhérence.

1.  Démontrer que $A(u)$ est un ensemble non vide et compact de $\mathbb{R}$.

2.  On suppose de plus qu'il existe une fonction $f: \mathbb{R} \to \mathbb{R}$ continue telle que $u_{n+1} = f(u_n)$ pour tout $n \in \mathbb{N}$.
    a.  Montrer que si $x \in A(u)$, alors $f(x) \in A(u)$.
    b.  En déduire que si la suite $(u_n)$ converge, sa limite est un point fixe de $f$.
    c.  Montrer que si $A(u)$ est un singleton, alors la suite $(u_n)$ converge.

3.  On rappelle que la limite supérieure de $(u_n)$ est définie par $\limsup_{n \to \infty} u_n = \lim_{n \to \infty} \left( \sup_{k \ge n} u_k \right)$ et la limite inférieure par $\liminf_{n \to \infty} u_n = \lim_{n \to \infty} \left( \inf_{k \ge n} u_k \right)$.
    Démontrer que $\sup A(u) = \limsup_{n \to \infty} u_n$ et $\inf A(u) = \liminf_{n \to \infty} u_n$.

---

## Correction de l'Exercice 8

### Question 1 : Démontrer que $A(u)$ est un ensemble non vide et compact de $\mathbb{R}$.

Pour démontrer que $A(u)$ est compact, nous devons montrer qu'il est fermé et borné dans $\mathbb{R}$. De plus, nous devons montrer qu'il est non vide.

**1. $A(u)$ est non vide :**
La suite $(u_n)_{n \in \mathbb{N}}$ est bornée par hypothèse. D'après le théorème de Bolzano-Weierstrass, toute suite bornée de nombres réels admet au moins une sous-suite convergente. Soit $(u_{\phi(k)})_{k \in \mathbb{N}}$ une telle sous-suite convergente. Sa limite $L = \lim_{k \to \infty} u_{\phi(k)}$ est, par définition, une valeur d'adhérence de la suite $(u_n)$. Par conséquent, $L \in A(u)$, ce qui prouve que $A(u)$ est non vide.

**2. $A(u)$ est borné :**
Puisque la suite $(u_n)$ est bornée, il existe un intervalle fermé borné $[m, M]$ tel que $u_n \in [m, M]$ pour tout $n \in \mathbb{N}$.
Soit $x \in A(u)$. Par définition, il existe une sous-suite $(u_{\phi(k)})$ de $(u_n)$ qui converge vers $x$. Puisque $u_{\phi(k)} \in [m, M]$ pour tout $k$, et que l'intervalle $[m, M]$ est fermé, la limite $x$ doit également appartenir à $[m, M]$. En effet, si $x \notin [m, M]$, alors il existerait un $\epsilon > 0$ tel que l'intervalle $(x-\epsilon, x+\epsilon)$ ne contiendrait aucun point de $[m, M]$, ce qui contredirait la convergence de $(u_{\phi(k)})$ vers $x$.
Ainsi, tout élément de $A(u)$ appartient à $[m, M]$. Cela signifie que $A(u)$ est borné.

**3. $A(u)$ est fermé :**
Pour montrer que $A(u)$ est fermé, nous allons montrer que toute suite convergente d'éléments de $A(u)$ a sa limite dans $A(u)$.
Soit $(x_j)_{j \in \mathbb{N}}$ une suite d'éléments de $A(u)$ qui converge vers un réel $x$. Nous devons montrer que $x \in A(u)$.
Puisque $x_j \in A(u)$ pour chaque $j$, il existe une sous-suite $(u_{\phi_j(k)})_{k \in \mathbb{N}}$ de $(u_n)$ qui converge vers $x_j$.
Nous allons construire une sous-suite de $(u_n)$ qui converge vers $x$.
Pour chaque $j \in \mathbb{N}$, puisque $u_{\phi_j(k)} \to x_j$ lorsque $k \to \infty$, il existe un indice $k_j$ tel que pour tout $k \ge k_j$, $|u_{\phi_j(k)} - x_j| < \frac{1}{j+1}$.
De plus, puisque $x_j \to x$ lorsque $j \to \infty$, il existe un indice $J$ tel que pour tout $j \ge J$, $|x_j - x| < \frac{1}{j+1}$.
Nous pouvons construire une sous-suite $(u_{\psi(j)})$ de $(u_n)$ qui converge vers $x$ de la manière suivante :
Pour chaque $j \in \mathbb{N}$, choisissons un indice $n_j = \phi_j(k_j)$ tel que $n_j > n_{j-1}$ (pour assurer que la suite d'indices est strictement croissante) et tel que $|u_{n_j} - x_j| < \frac{1}{j+1}$.
Alors, pour ce $n_j$, nous avons :
$|u_{n_j} - x| = |u_{n_j} - x_j + x_j - x| \le |u_{n_j} - x_j| + |x_j - x|$.
Puisque $x_j \to x$, pour tout $\epsilon > 0$, il existe $J_1$ tel que pour $j \ge J_1$, $|x_j - x| < \epsilon/2$.
Puisque $u_{\phi_j(k)} \to x_j$, pour tout $j$, il existe $K_j$ tel que pour $k \ge K_j$, $|u_{\phi_j(k)} - x_j| < \epsilon/2$.
Nous pouvons choisir une sous-suite $(u_{\psi(j)})$ de $(u_n)$ telle que pour chaque $j$, $u_{\psi(j)}$ est un terme de la sous-suite $(u_{\phi_j(k)})$ et $\psi(j) > \psi(j-1)$ (pour assurer que c'est bien une sous-suite) et $|u_{\psi(j)} - x_j| < \frac{1}{j+1}$.
Alors, pour $j$ suffisamment grand (plus grand que $J_1$ et tel que $\frac{1}{j+1} < \epsilon/2$), nous avons :
$|u_{\psi(j)} - x| \le |u_{\psi(j)} - x_j| + |x_j - x| < \frac{1}{j+1} + |x_j - x| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$.
Ainsi, la sous-suite $(u_{\psi(j)})$ converge vers $x$. Par conséquent, $x \in A(u)$.
Donc $A(u)$ est fermé.

**Conclusion :**
Puisque $A(u)$ est non vide, borné et fermé dans $\mathbb{R}$, il est compact d'après le théorème de Heine-Borel.

### Question 2 : Propriétés des suites récurrentes.

**2.a. Montrer que si $x \in A(u)$, alors $f(x) \in A(u)$.**
Soit $x \in A(u)$. Par définition, il existe une sous-suite $(u_{\phi(k)})_{k \in \mathbb{N}}$ de $(u_n)$ qui converge vers $x$.
Puisque $f$ est une fonction continue, et que $u_{\phi(k)} \to x$ lorsque $k \to \infty$, la suite $(f(u_{\phi(k)}))_{k \in \mathbb{N}}$ converge vers $f(x)$.
Or, par la relation de récurrence $u_{n+1} = f(u_n)$, nous avons $f(u_{\phi(k)}) = u_{\phi(k)+1}$.
Donc, la suite $(u_{\phi(k)+1})_{k \in \mathbb{N}}$ est une sous-suite de $(u_n)$ (car $\phi(k)+1$ est une suite d'indices strictement croissante si $\phi(k)$ l'est) qui converge vers $f(x)$.
Par conséquent, $f(x)$ est une valeur d'adhérence de la suite $(u_n)$, ce qui signifie $f(x) \in A(u)$.

**2.b. En déduire que si la suite $(u_n)$ converge, sa limite est un point fixe de $f$.**
Supposons que la suite $(u_n)$ converge vers une limite $L$.
Si $(u_n)$ converge vers $L$, alors l'ensemble de ses valeurs d'adhérence est le singleton $A(u) = \{L\}$. En effet, toute sous-suite de $(u_n)$ converge vers $L$.
D'après la question 2.a, si $x \in A(u)$, alors $f(x) \in A(u)$.
Puisque $L \in A(u)$, il s'ensuit que $f(L) \in A(u)$.
Comme $A(u) = \{L\}$, la seule possibilité est que $f(L) = L$.
Par conséquent, $L$ est un point fixe de $f$.

**2.c. Montrer que si $A(u)$ est un singleton, alors la suite $(u_n)$ converge.**
Supposons que $A(u) = \{L\}$ pour un certain réel $L$.
Nous voulons montrer que $\lim_{n \to \infty} u_n = L$.
Puisque la suite $(u_n)$ est bornée, elle est contenue dans un intervalle fermé borné $[m, M]$.
Supposons par l'absurde que $(u_n)$ ne converge pas vers $L$.
Cela signifie qu'il existe un $\epsilon_0 > 0$ tel que pour tout $N \in \mathbb{N}$, il existe un $n \ge N$ tel que $|u_n - L| \ge \epsilon_0$.
Autrement dit, il existe une infinité de termes de la suite $(u_n)$ qui se trouvent en dehors de l'intervalle ouvert $(L-\epsilon_0, L+\epsilon_0)$.
Ces termes forment une sous-suite $(u_{\psi(k)})$ telle que $u_{\psi(k)} \notin (L-\epsilon_0, L+\epsilon_0)$ pour tout $k$.
Cette sous-suite $(u_{\psi(k)})$ est elle-même bornée (car $(u_n)$ est bornée).
D'après le théorème de Bolzano-Weierstrass, cette sous-suite $(u_{\psi(k)})$ admet une sous-suite convergente $(u_{\psi(\chi(j))})$.
Soit $L' = \lim_{j \to \infty} u_{\psi(\chi(j))}$. Par définition, $L'$ est une valeur d'adhérence de $(u_n)$, donc $L' \in A(u)$.
Cependant, puisque $u_{\psi(\chi(j))} \notin (L-\epsilon_0, L+\epsilon_0)$ pour tout $j$, la limite $L'$ doit également satisfaire $|L' - L| \ge \epsilon_0$.
En effet, si $|L' - L| < \epsilon_0$, alors pour $j$ suffisamment grand, $u_{\psi(\chi(j))}$ serait dans $(L-\epsilon_0, L+\epsilon_0)$, ce qui est une contradiction.
Donc $L' \ne L$.
Ceci contredit l'hypothèse que $A(u) = \{L\}$ est un singleton.
Par conséquent, l'hypothèse que $(u_n)$ ne converge pas vers $L$ est fausse.
La suite $(u_n)$ converge donc vers $L$.

### Question 3 : Relation entre $A(u)$ et les limites supérieure et inférieure.

Soit $L^* = \limsup_{n \to \infty} u_n$ et $L_* = \liminf_{n \to \infty} u_n$.

**1. Démontrons que $L^* \in A(u)$ et $L_* \in A(u)$.**
Par définition, $L^* = \lim_{n \to \infty} v_n$, où $v_n = \sup_{k \ge n} u_k$. La suite $(v_n)$ est décroissante et minorée (par n'importe quel minorant de $(u_n)$), donc elle converge.
Pour montrer que $L^* \in A(u)$, nous devons construire une sous-suite de $(u_n)$ qui converge vers $L^*$.
Pour tout $\epsilon > 0$ et pour tout $N \in \mathbb{N}$, il existe $k \ge N$ tel que $u_k > L^* - \epsilon$. (Si ce n'était pas le cas, alors pour un certain $\epsilon_0 > 0$ et $N_0$, pour tout $k \ge N_0$, $u_k \le L^* - \epsilon_0$, ce qui impliquerait $v_{N_0} \le L^* - \epsilon_0$, contredisant $v_n \to L^*$).
De plus, pour tout $\epsilon > 0$, il existe $N_0 \in \mathbb{N}$ tel que pour tout $n \ge N_0$, $v_n < L^* + \epsilon$. Cela implique que pour tout $n \ge N_0$ et tout $k \ge n$, $u_k \le v_n < L^* + \epsilon$.
Combinons ces deux propriétés pour construire la sous-suite :
Pour $\epsilon = 1$, il existe $n_1 \ge 0$ tel que $L^* - 1 < u_{n_1} < L^* + 1$.
Pour $\epsilon = 1/2$, il existe $n_2 > n_1$ tel que $L^* - 1/2 < u_{n_2} < L^* + 1/2$.
En général, pour $\epsilon = 1/j$, il existe $n_j > n_{j-1}$ tel que $L^* - 1/j < u_{n_j} < L^* + 1/j$.
La suite $(u_{n_j})_{j \in \mathbb{N}}$ est une sous-suite de $(u_n)$ et, par le théorème des gendarmes, elle converge vers $L^*$.
Donc $L^* \in A(u)$.

De manière similaire, pour $L_* = \liminf_{n \to \infty} u_n = \lim_{n \to \infty} w_n$, où $w_n = \inf_{k \ge n} u_k$. La suite $(w_n)$ est croissante et majorée, donc elle converge.
Pour tout $\epsilon > 0$ et pour tout $N \in \mathbb{N}$, il existe $k \ge N$ tel que $u_k < L_* + \epsilon$.
De plus, pour tout $\epsilon > 0$, il existe $N_0 \in \mathbb{N}$ tel que pour tout $n \ge N_0$, $w_n > L_* - \epsilon$. Cela implique que pour tout $n \ge N_0$ et tout $k \ge n$, $u_k \ge w_n > L_* - \epsilon$.
En utilisant une construction similaire à celle pour $L^*$, nous pouvons construire une sous-suite de $(u_n)$ qui converge vers $L_*$.
Donc $L_* \in A(u)$.

**2. Démontrons que pour tout $x \in A(u)$, $L_* \le x \le L^*$.**
Soit $x \in A(u)$. Il existe une sous-suite $(u_{\phi(k)})$ qui converge vers $x$.
Par définition de $v_n = \sup_{j \ge n} u_j$, nous avons $u_j \le v_n$ pour tout $j \ge n$.
En particulier, pour tout $k$ tel que $\phi(k) \ge n$, nous avons $u_{\phi(k)} \le v_n$.
En passant à la limite lorsque $k \to \infty$ (et donc $\phi(k) \to \infty$), nous obtenons $x \le v_n$ pour tout $n$.
Ensuite, en passant à la limite lorsque $n \to \infty$, nous obtenons $x \le \lim_{n \to \infty} v_n = L^*$.

De même, par définition de $w_n = \inf_{j \ge n} u_j$, nous avons $u_j \ge w_n$ pour tout $j \ge n$.
En particulier, pour tout $k$ tel que $\phi(k) \ge n$, nous avons $u_{\phi(k)} \ge w_n$.
En passant à la limite lorsque $k \to \infty$, nous obtenons $x \ge w_n$ pour tout $n$.
Ensuite, en passant à la limite lorsque $n \to \infty$, nous obtenons $x \ge \lim_{n \to \infty} w_n = L_*$.
Ainsi, pour tout $x \in A(u)$, nous avons $L_* \le x \le L^*$.

**3. Conclusion :**
Nous avons montré que $L^* \in A(u)$ et que $L^*$ est un majorant de $A(u)$. Par définition du supremum, $L^*$ est le plus petit des majorants de $A(u)$. Par conséquent, $\sup A(u) = L^* = \limsup_{n \to \infty} u_n$.
De même, nous avons montré que $L_* \in A(u)$ et que $L_*$ est un minorant de $A(u)$. Par définition de l'infimum, $L_*$ est le plus grand des minorants de $A(u)$. Par conséquent, $\inf A(u) = L_* = \liminf_{n \to \infty} u_n$.

Ceci conclut la démonstration.

```
```
```
