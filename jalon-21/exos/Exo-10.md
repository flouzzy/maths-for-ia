---
uuid: "exo-21-10"
title: "Exercice 10 : Équation différentielle et limite uniforme"
difficulty: 5
---

# Exercice 10 : Équation différentielle et limite uniforme

**Niveau :** $★★★★★$

## Problème

Montrer que si $(f_n)$ est une suite de fonctions $C^1$ sur $[a,b]$ convergeant au moins en un point $x_0 \in [a,b]$, et si la suite des dérivées $(f_n')$ converge uniformément vers une fonction $g$, alors $(f_n)$ converge uniformément vers une fonction $f$ différentiable de dérivée $g$.

## Démonstration et Solution

**Théorème :** Soit $(f_n)$ une suite de fonctions de classe $C^1$ sur un segment $[a,b]$. Si la suite numérique $(f_n(x_0))$ converge pour au moins un point $x_0 \in [a,b]$, et si la suite des dérivées $(f_n')$ converge uniformément sur $[a,b]$ vers une fonction $g$, alors la suite $(f_n)$ converge uniformément sur $[a,b]$ vers une fonction $f$ qui est différentiable, et sa dérivée est exactement $f' = g$.

**Démonstration formelle :**
Puisque les fonctions $f_n$ sont de classe $C^1$, le Théorème Fondamental de l'Analyse nous permet d'écrire, pour tout point $x \in [a,b]$ et par rapport au point fixe $x_0$ :
$f_n(x) = f_n(x_0) + \int_{x_0}^x f_n'(t) dt$
La suite de fonctions $(f_n')$ converge uniformément vers la fonction limite $g$. Par le théorème de continuité des limites uniformes de suites de fonctions continues (les dérivées $f_n'$ sont continues car $f_n$ est $C^1$), la limite $g$ est elle-même une fonction continue sur $[a,b]$.
Par conséquent, $g$ est Riemann-intégrable sur $[a,b]$.
La convergence uniforme sur $[a,b]$ de $(f_n')$ vers $g$ nous autorise formellement à appliquer le théorème d'interversion de la limite et de l'intégrale sur le segment de bornes $x_0$ et $x$ (qui est inclus dans $[a,b]$).
C'est-à-dire que pour tout $x \in [a,b]$ :
$\lim_{n \to \infty} \int_{x_0}^x f_n'(t) dt = \int_{x_0}^x \lim_{n \to \infty} f_n'(t) dt = \int_{x_0}^x g(t) dt$
De plus, par hypothèse de l'énoncé, la suite de nombres réels $(f_n(x_0))$ converge. Appelons $C$ sa limite : $\lim_{n \to \infty} f_n(x_0) = C$.
En passant à la limite (simple, pour chaque $x$ fixé) dans l'équation intégrale initiale, nous obtenons :
$\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} f_n(x_0) + \lim_{n \to \infty} \int_{x_0}^x f_n'(t) dt = C + \int_{x_0}^x g(t) dt$
Posons alors la fonction limite $f$ définie sur $[a,b]$ par :
$f(x) = C + \int_{x_0}^x g(t) dt$
La fonction $f$ est ainsi la limite simple de la suite $(f_n)$.
La fonction $g$ étant continue, son intégrale de Riemann $\int_{x_0}^x g(t) dt$ est, par le Théorème Fondamental de l'Analyse, l'unique primitive de $g$ qui s'annule en $x_0$.
Cela implique immédiatement que $f$ est une fonction différentiable sur $[a,b]$ et que sa dérivée est $f'(x) = g(x)$.

Il reste à démontrer que la convergence de $(f_n)$ vers $f$ est non seulement simple, mais bien uniforme.
Calculons l'écart entre $f_n(x)$ et $f(x)$ en utilisant leurs formes intégrales respectives :
$f_n(x) - f(x) = (f_n(x_0) - C) + \int_{x_0}^x (f_n'(t) - g(t)) dt$
En appliquant l'inégalité triangulaire (la valeur absolue d'une somme est inférieure ou égale à la somme des valeurs absolues, et la valeur absolue d'une intégrale est inférieure ou égale à l'intégrale de la valeur absolue) :
$|f_n(x) - f(x)| \leq |f_n(x_0) - C| + \left| \int_{x_0}^x |f_n'(t) - g(t)| dt \right|$
Soit $\epsilon > 0$.
Par la convergence uniforme de $(f_n')$ vers $g$ sur $[a,b]$, il existe un rang $N_1$ tel que pour tout $n \geq N_1$ et tout $t \in [a,b]$, $|f_n'(t) - g(t)| \leq \frac{\epsilon}{2(b-a)}$.
Par la convergence numérique de $(f_n(x_0))$ vers $C$, il existe un rang $N_2$ tel que pour tout $n \geq N_2$, $|f_n(x_0) - C| \leq \frac{\epsilon}{2}$.
Posons $N = \max(N_1, N_2)$. Pour tout $n \geq N$ et pour tout $x \in [a,b]$, majorons l'intégrale :
$\left| \int_{x_0}^x |f_n'(t) - g(t)| dt \right| \leq \left| \int_{x_0}^x \frac{\epsilon}{2(b-a)} dt \right| = \frac{\epsilon}{2(b-a)} |x - x_0|$
Puisque $x$ et $x_0$ appartiennent au segment $[a,b]$, la distance maximale entre eux est $|x - x_0| \leq b - a$.
Donc, l'intégrale est majorée par $\frac{\epsilon}{2(b-a)} (b-a) = \frac{\epsilon}{2}$.
En combinant les deux majorations pour l'inégalité globale :
$|f_n(x) - f(x)| \leq \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$.
Cette inégalité finale ne dépend d'aucun $x$ particulier. En passant au supremum sur le compact $[a,b]$ :
$\sup_{x \in [a,b]} |f_n(x) - f(x)| \leq \epsilon$.
Ceci étant vrai pour tout $\epsilon > 0$ et pour un $n$ suffisamment grand, cela constitue la définition exacte de la limite : $\lim_{n \to \infty} \|f_n - f\|_{\infty} = 0$. La convergence de $(f_n)$ vers $f$ est donc rigoureusement uniforme sur $[a,b]$.
