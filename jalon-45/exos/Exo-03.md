---
title: "Exercice 3 : Différentiabilité et Gradient"
difficulty: "★★★☆☆"
---

# Exercice 3 : Étude d'un prolongement par continuité

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $f : \mathbb{R}^2 \to \mathbb{R}$ définie par $f(x, y) = \frac{x^3 - y^3}{x^2 + y^2}$ si $(x, y) \neq (0, 0)$, et $f(0, 0) = 0$. Montrer que $f$ est continue en $(0, 0)$, qu'elle y admet des dérivées partielles, mais qu'elle n'y est pas différentiable.

---
## Correction Détaillée

**1. Continuité en $(0, 0)$ :**
Passons en coordonnées polaires : $x = r\cos(\theta)$ et $y = r\sin(\theta)$, avec $r > 0$.
$$ f(r\cos(\theta), r\sin(\theta)) = \frac{r^3\cos^3(\theta) - r^3\sin^3(\theta)}{r^2} = r(\cos^3(\theta) - \sin^3(\theta)) $$
On peut majorer la valeur absolue :
$$ |f(r\cos(\theta), r\sin(\theta))| \le r (|\cos^3(\theta)| + |\sin^3(\theta)|) \le 2r $$
Puisque $\lim_{r \to 0} 2r = 0$, indépendamment de $\theta$, on a $\lim_{(x,y) \to (0,0)} f(x,y) = 0 = f(0,0)$. Donc $f$ est continue en $(0,0)$.

**2. Existence des dérivées partielles en $(0, 0)$ :**
Par définition du taux d'accroissement en $(0,0)$ :
$$ \frac{\partial f}{\partial x}(0, 0) = \lim_{t \to 0} \frac{f(t, 0) - f(0, 0)}{t} = \lim_{t \to 0} \frac{\frac{t^3}{t^2} - 0}{t} = \lim_{t \to 0} \frac{t}{t} = 1 $$
$$ \frac{\partial f}{\partial y}(0, 0) = \lim_{t \to 0} \frac{f(0, t) - f(0, 0)}{t} = \lim_{t \to 0} \frac{\frac{-t^3}{t^2} - 0}{t} = \lim_{t \to 0} \frac{-t}{t} = -1 $$
Les dérivées partielles existent et valent $\nabla f(0, 0) = (1, -1)^T$.

**3. Non-différentiabilité en $(0, 0)$ :**
Si $f$ était différentiable en $(0,0)$, la différentielle serait donnée par $df_{(0,0)}(h_1, h_2) = 1 \cdot h_1 - 1 \cdot h_2 = h_1 - h_2$.
Le développement limité à l'ordre 1 devrait s'écrire : $f(h_1, h_2) = f(0,0) + h_1 - h_2 + \|h\|\epsilon(h)$ avec $\epsilon(h) \to 0$.
Formons le quotient :
$$ \epsilon(h_1, h_2) = \frac{f(h_1, h_2) - (h_1 - h_2)}{\sqrt{h_1^2 + h_2^2}} = \frac{\frac{h_1^3 - h_2^3}{h_1^2 + h_2^2} - \frac{h_1(h_1^2 + h_2^2) - h_2(h_1^2 + h_2^2)}{h_1^2 + h_2^2}}{\sqrt{h_1^2 + h_2^2}} $$
$$ = \frac{h_1^3 - h_2^3 - h_1^3 - h_1h_2^2 + h_2h_1^2 + h_2^3}{(h_1^2 + h_2^2)^{3/2}} = \frac{h_1^2h_2 - h_1h_2^2}{(h_1^2 + h_2^2)^{3/2}} $$
Étudions la limite de ce quotient lorsque $(h_1, h_2)$ s'approche de $(0,0)$ le long de la droite $h_2 = h_1 > 0$ :
$$ \epsilon(h_1, h_1) = \frac{h_1^3 - h_1^3}{(2h_1^2)^{3/2}} = 0 $$
Mais le long de la droite $h_2 = -h_1 > 0$ :
$$ \epsilon(h_1, -h_1) = \frac{h_1^2(-h_1) - h_1(-h_1)^2}{(2h_1^2)^{3/2}} = \frac{-2h_1^3}{2^{3/2} h_1^3} = -\frac{2}{2\sqrt{2}} = -\frac{1}{\sqrt{2}} \neq 0 $$
La limite de $\epsilon(h)$ n'est pas nulle, la fonction n'est donc pas différentiable en $(0,0)$.
