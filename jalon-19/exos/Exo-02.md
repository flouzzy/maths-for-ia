---
titre: "Exercice 2 : Dérivabilité"
difficulte: "★☆☆☆☆"
---

# Exercice 2 : Pratique et maîtrise conceptuelle

**Énoncé :**
Démontrer l'inégalité de Taylor-Lagrange à l'ordre 1 : si $f \in \mathcal{C}^2([a,b])$, alors $|f(b) - f(a) - f'(a)(b-a)| \leq \frac{(b-a)^2}{2} \sup_{t \in [a,b]} |f''(t)|$.

**Résolution Zéro Ellipse :**
1. Définissons la constante $M = \sup_{t \in [a,b]} |f''(t)|$. Ce supremum est atteint car $f''$ est continue (puisque $f \in \mathcal{C}^2$) sur le compact $[a,b]$.
2. Considérons la fonction auxiliaire $\varphi : [a,b] \to \mathbb{R}$ définie par l'écart au développement de Taylor :
   $$ \varphi(x) = f(x) - f(a) - f'(a)(x-a) - K(x-a)^2 $$
   où la constante $K$ est choisie spécifiquement de sorte que $\varphi(b) = 0$.
3. Cette contrainte $\varphi(b) = 0$ impose algébriquement la valeur de $K$ :
   $$ K = \frac{f(b) - f(a) - f'(a)(b-a)}{(b-a)^2} $$
4. La fonction $\varphi$ vérifie par construction $\varphi(a) = 0$ (calcul direct) et $\varphi(b) = 0$.
5. Par ailleurs, $\varphi$ est continue sur $[a,b]$ et dérivable sur $]a,b[$. Nous pouvons lui appliquer le théorème de Rolle.
6. Il existe donc un réel $c \in ]a,b[$ tel que $\varphi'(c) = 0$.
7. Explicitons la dérivée de $\varphi$ :
   $$ \forall x \in [a,b], \quad \varphi'(x) = f'(x) - f'(a) - 2K(x-a) $$
8. Appliquée en $x=c$, la relation donne :
   $$ \varphi'(c) = f'(c) - f'(a) - 2K(c-a) = 0 \implies 2K(c-a) = f'(c) - f'(a) $$
9. La fonction dérivée $f'$ est elle-même continue sur $[a,c]$ et dérivable sur $]a,c[$. Appliquons le Théorème des Accroissements Finis à $f'$ sur l'intervalle $[a,c]$.
10. Il existe un réel $d \in ]a,c[$ tel que $f'(c) - f'(a) = f''(d)(c-a)$.
11. En combinant les équations des étapes 8 et 10, nous obtenons :
    $$ 2K(c-a) = f''(d)(c-a) $$
12. Puisque $c \in ]a,b[$, nous avons $c - a > 0$. Nous pouvons simplifier par $(c-a)$ pour obtenir $K = \frac{f''(d)}{2}$.
13. Remplaçons $K$ par son expression définie à l'étape 3 :
    $$ \frac{f(b) - f(a) - f'(a)(b-a)}{(b-a)^2} = \frac{f''(d)}{2} $$
14. En passant à la valeur absolue et en multipliant par $(b-a)^2$, il vient :
    $$ |f(b) - f(a) - f'(a)(b-a)| = \frac{(b-a)^2}{2} |f''(d)| $$
15. Puisque $d \in ]a,c[ \subset [a,b]$, $|f''(d)| \leq M$. L'inégalité est strictement établie. $\blacksquare$
