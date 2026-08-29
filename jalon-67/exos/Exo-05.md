---
title: "Exercice 5 : Inversion limite et intégrale non bornée"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 5 : Inversion limite et intégrale non bornée

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Problème

Soit $f_n(x) = \frac{\sqrt{n} \sin(x/n)}{x(1+x^2)}$ sur $(0, \infty)$. La suite de fonctions est-elle croissante ? Justifier rigoureusement le calcul de la limite de son intégrale.

## Démonstration et Résolution

### Étape 1 : Étude de la fonction
Considérons $f_n(x) = \frac{\sqrt{n} \sin(x/n)}{x(1+x^2)}$ pour $x > 0$.
Pour $x > 0$ et $n \ge 1$, nous savons que $0 < \sin(x/n) \le x/n$.
Ainsi, $f_n(x)$ n'est *pas* nécessairement une suite positive pour tout $x$ (car le sinus devient négatif), et même sur les intervalles où elle est positive, sa croissance en $n$ n'est pas garantie. Le Théorème de Convergence Monotone n'est **pas** directement applicable à $(f_n)$.

### Étape 2 : Convergence ponctuelle
Pour un $x > 0$ fixé, étudions la limite quand $n \to \infty$.
$$ \sqrt{n} \sin\left(\frac{x}{n}\right) = \sqrt{n} \left( \frac{x}{n} - \frac{x^3}{6n^3} + o\left(\frac{1}{n^3}\right) \right) = \frac{x}{\sqrt{n}} + o\left(\frac{1}{\sqrt{n}}\right) $$
Donc, pour tout $x > 0$, la limite ponctuelle est :
$$ \lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \frac{1}{x(1+x^2)} \cdot \frac{x}{\sqrt{n}} = 0 $$

### Étape 3 : Trouver une domination (Alternative à Beppo Levi)
Puisque $(f_n)$ n'est pas croissante, nous devons utiliser le Théorème de Convergence Dominée.
Majorons formellement la valeur absolue de $f_n(x)$.
On utilise l'inégalité fondamentale $|\sin(u)| \le |u|$ vraie pour tout $u \in \mathbb{R}$.
$$ |f_n(x)| = \frac{\sqrt{n} |\sin(x/n)|}{x(1+x^2)} \le \frac{\sqrt{n} (x/n)}{x(1+x^2)} = \frac{1}{\sqrt{n}(1+x^2)} $$
Pour tout $n \ge 1$, $\frac{1}{\sqrt{n}} \le 1$. Donc :
$$ |f_n(x)| \le \frac{1}{1+x^2} $$
Posons $g(x) = \frac{1}{1+x^2}$. Cette fonction est strictement positive et mesurable sur $(0, \infty)$.

### Étape 4 : Intégrabilité du majorant
Vérifions que $g$ est intégrable sur $(0, \infty)$ :
$$ \int_0^\infty \frac{1}{1+x^2} dx = \left[ \arctan(x) \right]_0^\infty = \frac{\pi}{2} - 0 = \frac{\pi}{2} < +\infty $$
La fonction dominante $g$ est bien Lebesgue-intégrable.

### Étape 5 : Conclusion par Convergence Dominée
Puisque $(f_n)$ converge ponctuellement vers la fonction nulle $f(x)=0$, et qu'elle est bornée par une fonction $g \in L^1(0,\infty)$, le théorème de convergence dominée s'applique.
$$ \lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty \lim_{n \to \infty} f_n(x) dx = \int_0^\infty 0 dx = 0 $$
Le calcul est rigoureusement validé, démontrant que l'absence de monotonie interdit Beppo-Levi mais appelle à la convergence dominée.
