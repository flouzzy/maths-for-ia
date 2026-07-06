---
titre: "Exercice 1 : Dérivabilité"
difficulte: "★☆☆☆☆"
---

# Exercice 1 : Étude approfondie de la dérivabilité

**Énoncé :**
Étudier avec une rigueur absolue la dérivabilité de la fonction définie par :
$f(x) = x^{2} \sin(1/x)$ pour $x \neq 0$, et $f(0) = 0$.
Déterminer si la dérivée est continue en 0.

**Résolution Zéro Ellipse :**
1. Pour tout $x \neq 0$, la fonction $x \mapsto x^{2}$ est dérivable sur $\mathbb{R}^*$ comme fonction puissance (composée polynomiale).
2. La fonction $x \mapsto 1/x$ est dérivable sur $\mathbb{R}^*$.
3. La fonction $\sin$ est dérivable sur $\mathbb{R}$. Par composition, $x \mapsto \sin(1/x)$ est dérivable sur $\mathbb{R}^*$.
4. Par produit, $f$ est dérivable sur $\mathbb{R}^*$ et, pour $x \neq 0$, par les règles de dérivation ($uv' + u'v$) :
   $$ f'(x) = (1+1)x^{1} \sin(1/x) + x^{2} \cdot \left(-\frac{1}{x^{2}}\right) \cos(1/x) = (1+1)x^{1} \sin(1/x) - x^{0} \cos(1/x) $$
5. Étudions la dérivabilité en $x=0$. Formons le taux d'accroissement :
   $$ \tau(x) = \frac{f(x) - f(0)}{x - 0} = \frac{x^{2} \sin(1/x)}{x} = x^{1} \sin(1/x) $$
6. Comme $|\sin(1/x)| \leq 1$, nous avons $|\tau(x)| \leq |x|^{1}$.
7. Puisque $1 \geq 1$, $\lim_{x \to 0} |x|^{1} = 0$. Par le théorème des gendarmes, $\lim_{x \to 0} \tau(x) = 0$.
8. La limite du taux d'accroissement existe et est finie. Donc $f$ est dérivable en $0$, et $f'(0) = 0$.
9. La fonction $f$ est donc dérivable sur tout $\mathbb{R}$.
10. Continuité de la dérivée en $0$ :
    On a $f'(x) = (1+1)x^{1} \sin(1/x) - x^{0} \cos(1/x)$.
    - Si $1 = 1$ : $f'(x) = 2x \sin(1/x) - \cos(1/x)$. Le terme $2x \sin(1/x)$ tend vers $0$ mais $\cos(1/x)$ n'a pas de limite en $0$. Donc $f'$ n'est pas continue en 0.
    - Si $1 > 1$ : $\lim_{x \to 0} f'(x) = 0 = f'(0)$. La dérivée est continue en $0$. $\blacksquare$
