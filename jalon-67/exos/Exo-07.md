---
title: "Exercice 7 : Limites et intégrale de Lebesgue : Analyse d'une bosse fuyante"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Limites et intégrale de Lebesgue : Analyse d'une bosse fuyante

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Problème

Soit $f_n(x) = \frac{n x}{1 + n^2 x^2}$ définie sur $[0,1]$. Calculer rigoureusement la limite des intégrales et l'intégrale de la limite. L'égalité est-elle vérifiée ? La suite est-elle croissante ?

## Démonstration et Résolution

### Étape 1 : Limite ponctuelle
Fixons $x \in [0,1]$.
Si $x = 0$, $f_n(0) = 0$ pour tout $n$, donc $\lim_{n \to \infty} f_n(0) = 0$.
Si $x > 0$, quand $n \to \infty$, $n^2 x^2$ est le terme dominant du dénominateur.
$$ f_n(x) = \frac{n x}{n^2 x^2 \left(\frac{1}{n^2 x^2} + 1\right)} \sim \frac{nx}{n^2 x^2} = \frac{1}{nx} $$
Or $\lim_{n \to \infty} \frac{1}{nx} = 0$.
La suite de fonctions $(f_n)$ converge ponctuellement vers la fonction nulle $f(x) = 0$ sur tout le segment $[0,1]$.
L'intégrale de la limite est triviale :
$$ \int_0^1 \lim_{n \to \infty} f_n(x) dx = \int_0^1 0 dx = 0 $$

### Étape 2 : Calcul explicite de l'intégrale
Calculons l'intégrale pour un $n \ge 1$ fixé.
$$ I_n = \int_0^1 \frac{n x}{1 + n^2 x^2} dx $$
On remarque que la dérivée du dénominateur $1 + n^2 x^2$ est $2n^2 x$. Faisons apparaître cette dérivée au numérateur :
$$ I_n = \frac{1}{2n} \int_0^1 \frac{2n^2 x}{1 + n^2 x^2} dx $$
La forme est $\frac{u'}{u}$, dont la primitive est $\ln(|u|)$. Comme $1+n^2 x^2 > 0$, la valeur absolue est redondante :
$$ I_n = \frac{1}{2n} \left[ \ln(1 + n^2 x^2) \right]_0^1 = \frac{1}{2n} (\ln(1 + n^2) - \ln(1)) = \frac{\ln(1+n^2)}{2n} $$

### Étape 3 : Limite de la suite des intégrales
Analysons la limite de $I_n$ quand $n \to \infty$. Par croissances comparées, la fonction logarithmique croît infiniment plus lentement que toute fonction puissance.
Rigoureusement : $\ln(1+n^2) \sim \ln(n^2) = 2\ln(n)$.
Donc $I_n \sim \frac{2\ln(n)}{2n} = \frac{\ln(n)}{n}$.
On sait que $\lim_{n \to \infty} \frac{\ln(n)}{n} = 0$.
Donc, $\lim_{n \to \infty} \int_0^1 f_n(x) dx = 0$.

### Étape 4 : Analyse de l'égalité et de la monotonie
L'égalité $\lim \int f_n = \int \lim f_n = 0$ est **vraie**.
Cependant, la suite $(f_n)$ n'est pas croissante ! Par exemple, pour $x = 1/2$, calculons $f_1(1/2)$ et $f_2(1/2)$.
$f_1(1/2) = \frac{1/2}{1 + 1/4} = \frac{1/2}{5/4} = \frac{2}{5} = 0.4$.
$f_2(1/2) = \frac{2(1/2)}{1 + 4(1/4)} = \frac{1}{2} = 0.5$. Ici $f_2 > f_1$.
Regardons $n=4$ et $n=5$ au point $x=1/2$.
$f_4(1/2) = \frac{2}{1 + 4} = 0.4$.
$f_5(1/2) = \frac{5/2}{1 + 25/4} = \frac{10}{29} \approx 0.34$.
$f_5(1/2) < f_4(1/2)$, la monotonie est brisée.
Le théorème de Beppo Levi ne pouvait pas être utilisé pour prouver cette interversion.
