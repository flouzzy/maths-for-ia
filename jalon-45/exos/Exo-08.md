---
title: "Exercice 8 : Différentiabilité et Gradient"
difficulty: "★★★★☆"
---

# Exercice 8 : Une fonction dérivable selon tout vecteur mais non différentiable

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

Soit $f : \mathbb{R}^2 \to \mathbb{R}$ définie par $f(x, y) = \left( \frac{x^2 y}{x^4 + y^2} \right)^2$ si $(x, y) \neq (0, 0)$ et $f(0, 0) = 0$. Montrer que pour tout vecteur $v \in \mathbb{R}^2$, la dérivée directionnelle $D_v f(0, 0)$ existe et vaut $0$. Montrer cependant que $f$ n'est pas continue en $(0, 0)$ et par conséquent non différentiable.

---
## Correction Détaillée

**1. Dérivées directionnelles en l'origine :**
Soit $v = (\alpha, \beta) \in \mathbb{R}^2$. Calculons la dérivée directionnelle par définition :
$$ D_v f(0, 0) = \lim_{t \to 0} \frac{f(t\alpha, t\beta) - f(0, 0)}{t} $$
Si $\beta = 0$, $f(t\alpha, 0) = 0$ pour tout $t \neq 0$, donc la limite est $0$.
Si $\beta \neq 0$, pour $t \neq 0$ :
$$ f(t\alpha, t\beta) = \left( \frac{t^2\alpha^2 \cdot t\beta}{t^4\alpha^4 + t^2\beta^2} \right)^2 = \left( \frac{t^3 \alpha^2 \beta}{t^2(t^2\alpha^4 + \beta^2)} \right)^2 = \left( \frac{t \alpha^2 \beta}{t^2\alpha^4 + \beta^2} \right)^2 = \frac{t^2 \alpha^4 \beta^2}{(t^2\alpha^4 + \beta^2)^2} $$
Le quotient est donc :
$$ \frac{f(t\alpha, t\beta) - 0}{t} = \frac{t \alpha^4 \beta^2}{(t^2\alpha^4 + \beta^2)^2} $$
Lorsque $t \to 0$, le dénominateur tend vers $\beta^4 \neq 0$, et le numérateur tend vers $0$. Ainsi, la limite est bien $0$.
Toutes les dérivées directionnelles existent en l'origine et valent $0$.

**2. Étude de la continuité le long d'une parabole :**
L'expression de la fonction nous invite à tester la trajectoire d'approche $y = x^2$.
Soit la suite de points $P_n = (x_n, x_n^2)$ avec $x_n = \frac{1}{n}$. Evidemment $P_n \to (0,0)$ quand $n \to \infty$.
Évaluons $f$ le long de ce chemin :
$$ f(x, x^2) = \left( \frac{x^2 \cdot x^2}{x^4 + (x^2)^2} \right)^2 = \left( \frac{x^4}{2x^4} \right)^2 = \left( \frac{1}{2} \right)^2 = \frac{1}{4} $$
La limite de $f(x,y)$ quand on approche l'origine sur la parabole $y=x^2$ vaut $\frac{1}{4}$, ce qui est différent de $f(0,0) = 0$.
La fonction n'admet donc pas de limite en $(0,0)$, elle y est discontinue.

**Conclusion :**
Puisque la différentiabilité en un point implique la continuité en ce point (Théorème fondamental), la fonction $f$ ne peut pas être différentiable en $(0,0)$, et ce, malgré l'existence de toutes ses dérivées directionnelles. C'est l'illustration de l'impasse géométrique des simples dérivées unidimensionnelles.
