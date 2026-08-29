---
uuid: "jalon-66-exo-07"
title: "Exercice 7 - Jalon 66"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Construction de fonction simple approchante

**Énoncé :**
Soit $f : \mathbb{R} \to [0, +\infty[$ une fonction mesurable.
Démontrer de manière constructive qu'il existe une suite croissante $(s_n)$ de fonctions simples positives, telle que pour tout $x \in \mathbb{R}$, $\lim_{n \to +\infty} s_n(x) = f(x)$.

**Corrigé :**
C'est un théorème fondamental d'approximation. La démonstration repose sur un découpage dyadique de l'axe des ordonnées.

Pour chaque entier $n \ge 1$, nous découpons l'intervalle des valeurs $[0, n]$ en $n 2^n$ sous-intervalles de longueur $1/2^n$.
Définissons les ensembles mesurables (images réciproques) :
Pour $k \in \{0, 1, \dots, n2^n - 1\}$ :
$$A_{n,k} = \left\{ x \in \mathbb{R} \mid \frac{k}{2^n} \le f(x) < \frac{k+1}{2^n} \right\}$$
Et pour la "queue" des grandes valeurs :
$$B_n = \{ x \in \mathbb{R} \mid f(x) \ge n \}$$

Définissons alors la fonction simple $s_n$ par :
$$s_n(x) = \sum_{k=0}^{n2^n - 1} \frac{k}{2^n} \mathbf{1}_{A_{n,k}}(x) + n \mathbf{1}_{B_n}(x)$$

**1. $s_n$ est une fonction simple positive :**
$s_n$ prend un nombre fini de valeurs (les fractions $k/2^n$ et $n$). Les ensembles $A_{n,k}$ et $B_n$ sont mesurables car $f$ l'est. Donc $s_n \in \mathcal{E}^+$.

**2. Croissance de la suite ($s_n \le s_{n+1}$) :**
Prenons un point $x \in \mathbb{R}$.
- Si $f(x) < n$, $x$ appartient à un unique $A_{n,k}$. Ainsi $s_n(x) = k/2^n$.
  Au rang $n+1$, l'intervalle $[k/2^n, (k+1)/2^n[$ est coupé en deux moitiés :
  $[2k/2^{n+1}, (2k+1)/2^{n+1}[$ et $[(2k+1)/2^{n+1}, (2k+2)/2^{n+1}[$.
  Si $f(x)$ tombe dans la 1ère moitié, $s_{n+1}(x) = 2k/2^{n+1} = k/2^n = s_n(x)$.
  Si $f(x)$ tombe dans la 2ème moitié, $s_{n+1}(x) = (2k+1)/2^{n+1} > k/2^n = s_n(x)$.
  Dans les deux cas, $s_{n+1}(x) \ge s_n(x)$.
- Si $f(x) \ge n$, $s_n(x) = n$.
  Au rang $n+1$, soit $f(x) \ge n+1$ (et alors $s_{n+1}(x) = n+1 > n = s_n(x)$), soit $n \le f(x) < n+1$, auquel cas $x \in A_{n+1, k}$ pour un $k \ge n 2^{n+1}$.
  Donc $s_{n+1}(x) = k/2^{n+1} \ge n 2^{n+1} / 2^{n+1} = n = s_n(x)$.
La suite $(s_n)$ est donc bien croissante ponctuellement.

**3. Convergence vers $f$ :**
Fixons $x \in \mathbb{R}$. Puisque $f(x) \in [0, +\infty[$, il existe un entier $N$ tel que $n > f(x)$ pour tout $n \ge N$.
Pour tout $n \ge N$, $x$ tombe dans l'un des ensembles $A_{n,k}$.
Par définition de $A_{n,k}$, on a $\frac{k}{2^n} \le f(x) < \frac{k+1}{2^n}$.
Or $s_n(x) = \frac{k}{2^n}$.
Ainsi :
$$0 \le f(x) - s_n(x) < \frac{1}{2^n}$$
En faisant tendre $n \to +\infty$, $1/2^n \to 0$, donc $\lim_{n \to +\infty} s_n(x) = f(x)$.
La démonstration est complète.
