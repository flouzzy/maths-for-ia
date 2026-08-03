---
title: "Exercice 9 : Continuité via le développement de Taylor (Bonus 1D)"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 9 : Continuité via le développement de Taylor

## Énoncé

Montrer que la fonction suivante admet une limite finie en $(0,0)$ et la calculer :
$$ f(x, y) = \frac{\sin(x^2 + y^2)}{x^2 + y^2} $$

## Solution détaillée

1. **Identification de la structure globale** :
   L'expression dépend uniquement de la quantité $x^2 + y^2$, qui correspond au carré de la distance à l'origine.
   Cette symétrie radiale invite immédiatement au changement de variable ou au passage en coordonnées polaires.

2. **Changement de variable scalaire** :
   Plutôt que d'utiliser explicitement $r$ et $\theta$, posons une nouvelle variable réelle positive :
   $$ u = x^2 + y^2 $$

   La question de la limite de $f(x,y)$ quand $(x,y) \to (0,0)$ dans $\mathbb{R}^2$ se réduit exactement à l'étude de la limite d'une fonction d'une seule variable $u$ lorsque $u \to 0^+$.
   En effet, si $\|(x,y)\| = \sqrt{x^2+y^2} \to 0$, alors la quantité $u = x^2+y^2$ tend vers $0$ par valeurs positives.

3. **Transformation de la fonction** :
   Avec le changement de variable, la fonction s'écrit :
   $$ g(u) = \frac{\sin(u)}{u} $$
   Nous cherchons donc à évaluer $\lim_{u \to 0^+} g(u)$.

4. **Résolution de la limite 1D** :
   La limite $\lim_{u \to 0} \frac{\sin(u)}{u}$ est une limite de référence fondamentale en analyse réelle (démontrable via un développement de Taylor-Young : $\sin(u) = u - u^3/6 + o(u^3)$, ou via le taux d'accroissement de la fonction sinus en 0).
   On sait que :
   $$ \lim_{u \to 0} \frac{\sin(u)}{u} = 1 $$

5. **Conclusion formelle** :
   Puisque $u = x^2 + y^2$ tend vers $0$ lorsque $(x,y) \to (0,0)$ et que la composition des limites est valide (les fonctions étant continues au voisinage pointé de $0$) :
   $$ \lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2} = \lim_{u \to 0^+} \frac{\sin(u)}{u} = 1 $$

   La limite existe bien et vaut $1$. La fonction est prolongeable par continuité à l'origine en posant $f(0,0) = 1$.
