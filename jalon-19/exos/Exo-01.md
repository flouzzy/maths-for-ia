---
titre: "Exercice 1 : Dérivabilité"
difficulte: "★☆☆☆☆"
---

# Exercice 1 : Pratique et maîtrise conceptuelle

**Énoncé :**
Étudier la dérivabilité de la fonction $f(x) = x^2 \sin\left(\frac{1}{x}\right)$ pour $x \neq 0$ et $f(0)=0$. La dérivée est-elle continue en $0$ ?

**Résolution Zéro Ellipse :**
1. Sur $\mathbb{R}^*$, par les théorèmes d'opérations sur les fonctions dérivables (composition et produit de polynômes, rationnelles et trigonométriques), la fonction $f$ est infiniment dérivable.
2. Appliquons la règle du produit pour $x \neq 0$ :
   $$ f'(x) = 2x \sin\left(\frac{1}{x}\right) + x^2 \left( -\frac{1}{x^2} \right) \cos\left(\frac{1}{x}\right) = 2x \sin\left(\frac{1}{x}\right) - \cos\left(\frac{1}{x}\right) $$
3. Analysons le point critique $x=0$. Nous devons revenir à la définition originelle du taux d'accroissement :
   $$ \tau_0(x) = \frac{f(x) - f(0)}{x - 0} = \frac{x^2 \sin(1/x)}{x} = x \sin\left(\frac{1}{x}\right) $$
4. Puisque la fonction sinus est bornée par l'unité, nous établissons la majoration :
   $$ |\tau_0(x)| = |x| \cdot |\sin(1/x)| \leq |x| $$
5. Par le théorème d'encadrement (gendarmes), sachant que $\lim_{x \to 0} |x| = 0$, nous déduisons $\lim_{x \to 0} \tau_0(x) = 0$.
6. La limite existant et étant finie, $f$ est dérivable en $0$, et $f'(0) = 0$.
7. Étudions maintenant la continuité de la fonction dérivée $f'$ au point $0$.
8. Nous avons $f'(x) = 2x \sin(1/x) - \cos(1/x)$ pour $x \neq 0$.
9. Le premier terme $2x \sin(1/x)$ tend vers $0$ par le même argument d'encadrement que précédemment.
10. Cependant, le second terme $\cos(1/x)$ ne possède pas de limite en $0$ (il oscille indéfiniment entre $-1$ et $1$).
11. Par conséquent, $\lim_{x \to 0} f'(x)$ n'existe pas. La fonction dérivée $f'$ n'est donc pas continue en $0$. La fonction $f$ est dérivable, mais n'est pas de classe $\mathcal{C}^1$. $\blacksquare$
