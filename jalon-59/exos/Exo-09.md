### Exercice 9 : Contre-exemple sur la droite réelle entière \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f_n(x) = \sin(x + n\pi)$. Montrer que la famille $(f_n)$ est uniformément bornée et uniformément équicontinue sur $\mathbb{R}$, mais qu'elle n'admet aucune sous-suite convergeant uniformément sur $\mathbb{R}$. Le théorème d'Arzelà-Ascoli est-il contredit ?

**Correction :**
1. $|f_n(x)| \le 1$, donc la famille est uniformément bornée.
2. La dérivée $f_n'(x) = \cos(x + n\pi)$ est bornée par 1. Par les accroissements finis, toutes les fonctions sont 1-lipschitziennes, donc la famille est équicontinue.
3. $f_n(x) = \sin(x) \cos(n\pi) + \cos(x) \sin(n\pi) = (-1)^n \sin(x)$.
La suite vaut alternativement $\sin(x)$ et $-\sin(x)$. Les seules sous-suites possibles qui convergent le font si on restreint $n$ à être toujours pair ou toujours impair, disons la suite constante $\sin(x)$.
Wait, si on extrait les pairs, la sous-suite est constante égale à $\sin(x)$, qui converge uniformément vers elle-même.
Changeons la suite pour le contre-exemple classique : $f_n(x) = f(x - n)$ où $f$ est une "bosse" (ex: $f(x) = \max(0, 1-|x|)$).
Alors $\sup_{x \in \mathbb{R}} |f_n - f_m| = 1$ pour $n \neq m$. Aucune sous-suite ne peut être de Cauchy pour la norme uniforme, donc aucune ne converge uniformément.
4. L'hypothèse manquante d'Arzelà-Ascoli est que le domaine **doit être compact**. Ici, $\mathbb{R}$ ne l'est pas.
