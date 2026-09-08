---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon-66]]"
next: "[[Jalon-68]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo Levi)

## 1. Introduction au concept

L'intégration de Lebesgue vise à pallier les défauts de l'intégrale de Riemann, notamment vis-à-vis des passages à la limite. Le Théorème de Convergence Monotone, ou théorème de Beppo Levi (1906), établit que pour une suite croissante de fonctions mesurables positives, la limite de l'intégrale est l'intégrale de la limite.

Imaginez une structure tridimensionnelle dont le volume augmente progressivement sans jamais se rétracter. Si nous mesurons le volume à chaque étape de croissance, la limite de ces volumes successifs sera exactement égale au volume de la structure finale. Ce principe fondamental autorise l'interversion entre le symbole de la limite (ou de la somme infinie) et le symbole de l'intégrale, ce qui est crucial en analyse fonctionnelle et en probabilités.

## 2. Définitions, Théorèmes et Exemples

### A. Cadre formel

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré, où :
- $X$ est un ensemble,
- $\mathcal{F}$ est une tribu sur $X$,
- $\mu$ est une mesure positive sur $(X, \mathcal{F})$.

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $\mathbb{R}^+ \cup \{+\infty\}$.

### B. Théorème de Convergence Monotone (Beppo Levi)

**Théorème :**
Si pour presque tout $x \in X$, la suite $(f_n(x))_{n \in \mathbb{N}}$ est croissante (c'est-à-dire $f_n \le f_{n+1}$ $\mu$-presque partout), alors la fonction limite $f = \lim_{n \to \infty} f_n$ est mesurable, et on a l'égalité :
$$ \int_X f(x) \, d\mu(x) = \lim_{n \to \infty} \int_X f_n(x) \, d\mu(x) $$

**Corollaire (Théorème d'intégration terme à terme) :**
Pour toute suite $(u_n)_{n \in \mathbb{N}}$ de fonctions mesurables positives :
$$ \int_X \left( \sum_{n=0}^{+\infty} u_n(x) \right) d\mu(x) = \sum_{n=0}^{+\infty} \int_X u_n(x) \, d\mu(x) $$

### C. Exemples concrets

1. **Fonctions indicatrices emboîtées :**
   Sur $X = \mathbb{R}$ avec la mesure de Lebesgue $\lambda$, posons $f_n(x) = \mathbf{1}_{[-n, n]}(x)$.
   Les ensembles $A_n = [-n, n]$ forment une suite croissante ($A_n \subset A_{n+1}$), et leur union est $\mathbb{R}$.
   La suite $(f_n)$ est croissante et converge vers $f(x) = \mathbf{1}_{\mathbb{R}}(x) = 1$.
   L'intégrale de $f_n$ est $\lambda([-n, n]) = 2n$.
   On a bien $\lim_{n \to \infty} \int f_n d\lambda = \lim_{n \to \infty} 2n = +\infty$, ce qui correspond à $\int 1 d\lambda = +\infty$.

2. **Suite géométrique :**
   Considérons $X = [0, 1)$ avec la mesure de Lebesgue. Soit $u_n(x) = x^n$.
   Les fonctions $u_n$ sont mesurables et positives. Par le corollaire, l'intégrale de la somme est la somme des intégrales :
   $$ \int_0^1 \left( \sum_{n=0}^\infty x^n \right) dx = \sum_{n=0}^\infty \int_0^1 x^n dx $$
   La somme intérieure est $\frac{1}{1-x}$. L'intégrale de $\frac{1}{1-x}$ sur $[0, 1)$ diverge.
   La somme des intégrales est $\sum_{n=0}^\infty \frac{1}{n+1}$, qui est la série harmonique, et diverge également. L'égalité $+\infty = +\infty$ est vérifiée.

3. **Approximation par des fonctions étagées :**
   Toute fonction mesurable positive $f$ peut être écrite comme limite croissante d'une suite de fonctions étagées $(s_n)$.
   Par exemple, pour $f(x) = x^2$ sur $[0, 1]$, on peut poser $s_n(x) = \frac{\lfloor 2^n x^2 \rfloor}{2^n}$.
   La suite $(s_n)$ croît vers $f$. Le théorème garantit que $\lim \int s_n d\lambda = \int x^2 d\lambda = \frac{1}{3}$.

4. **Mesure de comptage :**
   Sur $X = \mathbb{N}$ muni de la tribu discrète $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu$. L'intégrale par rapport à $\mu$ est une série.
   Soit une suite double positive $a_{n,k} \ge 0$. Posons $u_k(n) = a_{n,k}$.
   Le corollaire donne l'interversion des sommes pour les séries à termes positifs :
   $$ \sum_{n=0}^\infty \sum_{k=0}^\infty a_{n,k} = \sum_{k=0}^\infty \sum_{n=0}^\infty a_{n,k} $$

5. **Masse de Dirac :**
   Sur $\mathbb{R}$, considérons la mesure de Dirac $\delta_0$.
   Soit $f_n(x) = e^{-x^2/n}$. Pour tout $x$, $f_n(x)$ croît vers $f(x) = 1$.
   L'intégrale de $f_n$ par rapport à $\delta_0$ est $f_n(0) = 1$.
   La limite des intégrales est $1$, et l'intégrale de la limite $f(x)=1$ par rapport à $\delta_0$ est $1$.

### D. Cas limites et conditions restrictives

Le théorème est faux en général si les fonctions changent de signe, ou si la suite n'est pas croissante. Par exemple, posons $f_n(x) = n \mathbf{1}_{(0, 1/n)}(x)$ sur $[0, 1]$.
- La suite n'est pas monotone.
- $\int_0^1 f_n(x) dx = 1$ pour tout $n$.
- Mais $f_n(x) \to 0$ pour tout $x \in [0, 1]$. L'intégrale de la limite est $0$, ce qui est différent de la limite des intégrales ($1$). Le théorème de convergence monotone ne s'applique pas car la suite n'est pas croissante.

## 3. Démonstrations

### Démonstration du Théorème de Beppo Levi

**Étape 1 : Mesurabilité de la limite et première inégalité**

Puisque la suite $(f_n)$ est mesurable, le sup (qui correspond ici à la limite simple due à la croissance de la suite) est une fonction mesurable à valeurs dans $[0, +\infty]$. Notons $f = \lim f_n$.

Comme $f_n \le f_{n+1}$ et $f = \sup f_n$, on a $f_n \le f$ pour tout $n$.
Par la croissance de l'intégrale (établie au Jalon 66), on obtient :
$$ \int_X f_n d\mu \le \int_X f d\mu $$
Puisque la suite numérique $\left( \int_X f_n d\mu \right)$ est croissante dans $[0, +\infty]$, elle admet une limite. En passant à la limite, on obtient la première inégalité :
$$ \lim_{n \to \infty} \int_X f_n d\mu \le \int_X f d\mu $$

**Étape 2 : Inégalité inverse via les fonctions étagées**

Considérons une fonction étagée simple $s$ telle que $0 \le s \le f$.
Fixons un réel $c \in (0, 1)$.
Pour chaque $n \in \mathbb{N}$, on définit l'ensemble :
$$ A_n = \{ x \in X \mid f_n(x) \ge c s(x) \} $$

Puisque $f_n$ et $s$ sont mesurables, $A_n$ est un ensemble mesurable ($A_n \in \mathcal{F}$).
Comme la suite $(f_n)$ est croissante, la suite d'ensembles $(A_n)$ est une suite croissante d'ensembles : $A_n \subset A_{n+1}$.
Montrons que l'union des $A_n$ recouvre presque tout $X$. Soit $x \in X$ tel que $s(x) > 0$ (sur l'ensemble où $s(x)=0$, $x$ appartient à tous les $A_n$).
Comme $c < 1$ et $0 < s(x) \le f(x) = \lim f_n(x)$, il existe un rang $N$ à partir duquel $f_n(x) \ge c s(x)$. Donc $x \in \bigcup_{n} A_n$. L'union $\bigcup A_n = X$.

**Étape 3 : Intégration sur les ensembles $A_n$**

Sur l'ensemble $A_n$, nous avons par définition $f_n \ge c s$.
Par conséquent, puisque toutes les fonctions sont positives :
$$ \int_X f_n d\mu \ge \int_{A_n} f_n d\mu \ge \int_{A_n} c s d\mu = c \int_{A_n} s d\mu $$

La fonction étagée $s$ s'écrit sous la forme canonique $s = \sum_{i=1}^k \alpha_i \mathbf{1}_{E_i}$, avec $\alpha_i \ge 0$ et $E_i \in \mathcal{F}$ disjoints.
Ainsi,
$$ \int_{A_n} s d\mu = \sum_{i=1}^k \alpha_i \mu(A_n \cap E_i) $$

**Étape 4 : Continuité monotone de la mesure**

Pour chaque $i$, la suite d'ensembles $(A_n \cap E_i)_{n}$ est une suite croissante d'ensembles mesurables, de limite $\bigcup_n (A_n \cap E_i) = X \cap E_i = E_i$.
Par la propriété de continuité croissante de la mesure $\mu$ (Jalon 63), on a :
$$ \lim_{n \to \infty} \mu(A_n \cap E_i) = \mu(E_i) $$

En passant à la limite dans l'expression de l'intégrale de $s$ sur $A_n$ :
$$ \lim_{n \to \infty} \int_{A_n} s d\mu = \sum_{i=1}^k \alpha_i \lim_{n \to \infty} \mu(A_n \cap E_i) = \sum_{i=1}^k \alpha_i \mu(E_i) = \int_X s d\mu $$

**Étape 5 : Conclusion**

Revenons à l'inégalité de l'Étape 3 : $\int_X f_n d\mu \ge c \int_{A_n} s d\mu$.
En passant à la limite quand $n \to \infty$ :
$$ \lim_{n \to \infty} \int_X f_n d\mu \ge c \int_X s d\mu $$
Cette inégalité est valable pour tout $c \in (0, 1)$. En faisant tendre $c$ vers $1$, on obtient :
$$ \lim_{n \to \infty} \int_X f_n d\mu \ge \int_X s d\mu $$
Cette dernière inégalité est vraie pour toute fonction étagée $s \le f$.
Par définition de l'intégrale de $f$ (qui est le supremum des intégrales des fonctions étagées qui la minorent) :
$$ \lim_{n \to \infty} \int_X f_n d\mu \ge \sup_{s \le f} \int_X s d\mu = \int_X f d\mu $$
En combinant ceci avec l'inégalité de l'Étape 1, on conclut :
$$ \lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu $$
Ceci achève la démonstration.

## 4. Applications en Physique, Logique et Intelligence Artificielle

### Intelligence Artificielle et Processus Stochastiques

En apprentissage automatique, particulièrement en apprentissage par renforcement (Reinforcement Learning) et dans l'étude théorique des algorithmes stochastiques, nous avons souvent affaire à des valeurs espérées de coûts cumulés sur un horizon infini.

Considérons une suite de récompenses positives $(R_t)_{t \in \mathbb{N}}$ acquises au cours du temps. L'espérance du gain total cumulé se formule comme $\mathbb{E} \left[ \sum_{t=0}^\infty \gamma^t R_t \right]$, où $\gamma \in (0,1)$ est un facteur d'actualisation.
En définissant $S_N = \sum_{t=0}^N \gamma^t R_t$, la suite $(S_N)$ est une suite croissante de variables aléatoires (fonctions mesurables positives sur l'espace probabilisé $\Omega$).
Le théorème de convergence monotone autorise l'interversion de l'espérance (qui est une intégrale de Lebesgue) et de la limite :
$$ \mathbb{E} \left[ \sum_{t=0}^\infty \gamma^t R_t \right] = \lim_{N \to \infty} \mathbb{E} [S_N] = \sum_{t=0}^\infty \gamma^t \mathbb{E} [R_t] $$
Cette garantie théorique est fondamentale pour l'équation de Bellman et la convergence des algorithmes de type Q-Learning, assurant que l'accumulation infinie de l'espérance des gains locaux converge rigoureusement vers la valeur de la politique globale.
