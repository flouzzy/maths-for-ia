# Exercice 8 : Dérivées des suites de fonctions

## Énoncé
Soit $f_n(x) = \frac{\sin(nx)}{\sqrt{n}}$.
1. Montrer que $f_n$ converge uniformément vers 0 sur $\mathbb{R}$.
2. Étudier la convergence de la suite des dérivées $(f_n')$.
3. Que conclut-on sur le théorème de dérivation sous le signe limite ?

## Correction Détaillée

1. **Convergence uniforme de $f_n$ :**
Pour tout $x \in \mathbb{R}$, $|f_n(x)| = \frac{|\sin(nx)|}{\sqrt{n}} \le \frac{1}{\sqrt{n}}$.
Le supremum $\sup_{x \in \mathbb{R}} |f_n(x)| \le \frac{1}{\sqrt{n}}$, qui tend vers 0 lorsque $n \to \infty$.
Donc $(f_n)$ converge uniformément vers la fonction nulle $f=0$ sur $\mathbb{R}$.

2. **Suite des dérivées :**
$f_n'(x) = \frac{n \cos(nx)}{\sqrt{n}} = \sqrt{n} \cos(nx)$.
En $x = 0$, $f_n'(0) = \sqrt{n}$, qui diverge vers $+\infty$.
La suite $(f_n')$ ne converge même pas simplement sur $\mathbb{R}$.

3. **Conclusion :**
La convergence uniforme d'une suite de fonctions dérivables $(f_n)$ vers $f$ **n'implique pas** la convergence de la suite des dérivées vers la dérivée de la limite.
Pour que $\lim f_n' = f'$, il faut supposer la convergence uniforme de la suite **des dérivées** $(f_n')$, ce qui n'est pas le cas ici.
