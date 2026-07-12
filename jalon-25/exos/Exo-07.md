---
title: "Exercice 7 : L'inégalité de Cauchy-Schwarz pour les suites"
difficulty: 4
---

## Énoncé
L'espace $\ell^2(\mathbb{R})$ est l'ensemble des suites réelles $(u_n)_{n \in \mathbb{N}}$ telles que la série $\sum_{n=0}^\infty u_n^2$ converge.
1. Montrer que si $(u_n)$ et $(v_n)$ sont dans $\ell^2(\mathbb{R})$, alors pour tout $N \in \mathbb{N}$, on a $\sum_{n=0}^N |u_n v_n| \le \sqrt{\sum_{n=0}^N u_n^2} \sqrt{\sum_{n=0}^N v_n^2}$.
2. En déduire que la série $\sum u_n v_n$ converge absolument, et que $\ell^2(\mathbb{R})$ est bien un espace vectoriel.

## Correction Détaillée
**1. Inégalité sur sommes finies :**
Pour un entier $N$ fixé, considérons l'espace vectoriel $\mathbb{R}^{N+1}$ muni de son produit scalaire canonique $\langle x, y \rangle = \sum_{n=0}^N x_n y_n$.
Soient les vecteurs $U_N = (|u_0|, |u_1|, ..., |u_N|)$ et $V_N = (|v_0|, |v_1|, ..., |v_N|)$ dans cet espace.
Appliquons l'inégalité de Cauchy-Schwarz de dimension finie à $U_N$ et $V_N$ :
$\langle U_N, V_N \rangle \le \|U_N\| \cdot \|V_N\|$
(On peut omettre les valeurs absolues autour du produit scalaire car tous les termes de $U_N$ et $V_N$ sont positifs).
Explicitons chaque terme :
$\langle U_N, V_N \rangle = \sum_{n=0}^N |u_n| |v_n| = \sum_{n=0}^N |u_n v_n|$
$\|U_N\| = \sqrt{\sum_{n=0}^N |u_n|^2} = \sqrt{\sum_{n=0}^N u_n^2}$
$\|V_N\| = \sqrt{\sum_{n=0}^N |v_n|^2} = \sqrt{\sum_{n=0}^N v_n^2}$
On obtient donc directement l'inégalité demandée pour tout $N$ :
$$\sum_{n=0}^N |u_n v_n| \le \sqrt{\sum_{n=0}^N u_n^2} \sqrt{\sum_{n=0}^N v_n^2}$$

**2. Convergence absolue et structure d'espace vectoriel :**
Puisque $(u_n), (v_n) \in \ell^2(\mathbb{R})$, les séries $\sum u_n^2$ et $\sum v_n^2$ convergent.
Notons leurs sommes $S_u = \sum_{n=0}^\infty u_n^2$ et $S_v = \sum_{n=0}^\infty v_n^2$.
Puisque les termes d'une série à termes positifs forment une suite de sommes partielles croissante, on a pour tout $N$ :
$\sum_{n=0}^N u_n^2 \le S_u$ et $\sum_{n=0}^N v_n^2 \le S_v$.
Par suite, en injectant cela dans l'inégalité de la question 1 :
$\sum_{n=0}^N |u_n v_n| \le \sqrt{S_u} \sqrt{S_v}$ pour tout entier $N$.
La série $\sum |u_n v_n|$ est une série à termes positifs dont les sommes partielles sont majorées par la constante $\sqrt{S_u S_v}$.
D'après le théorème fondamental des séries à termes positifs, cela implique que la série converge.
Ainsi, la série $\sum u_n v_n$ converge absolument. L'application bilinéaire $(u, v) \mapsto \sum_{n=0}^\infty u_n v_n$ est donc bien définie (et c'est un produit scalaire).

Pour montrer que $\ell^2(\mathbb{R})$ est un sous-espace vectoriel de l'espace de toutes les suites réelles :
- La suite nulle est clairement dans $\ell^2$.
- Si $(u_n) \in \ell^2$ et $\lambda \in \mathbb{R}$, alors $\sum (\lambda u_n)^2 = \lambda^2 \sum u_n^2 < \infty$, donc $(\lambda u_n) \in \ell^2$. (Stabilité par multiplication externe).
- Si $(u_n), (v_n) \in \ell^2$, il faut montrer que $(u_n + v_n) \in \ell^2$.
  Calculons le terme général de la série de la somme :
  $(u_n + v_n)^2 = u_n^2 + 2u_nv_n + v_n^2$.
  - $\sum u_n^2$ converge (hypothèse).
  - $\sum v_n^2$ converge (hypothèse).
  - $\sum u_nv_n$ converge absolument d'après ce que nous venons de prouver, donc elle converge.
  Par linéarité de la somme des séries convergentes, la série $\sum (u_n + v_n)^2$ converge.
  Donc $(u_n + v_n) \in \ell^2$. (Stabilité par addition).
$\ell^2(\mathbb{R})$ est donc bien un espace vectoriel.
