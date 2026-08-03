---
title: "Exercice 8 : Limite d'une fonction rationnelle complexe"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 8 : Limite d'une fonction rationnelle complexe

## Énoncé

Étudier l'existence de la limite en $(0,0)$ de la fonction :
$$ f(x, y) = \frac{x y^3}{x^2 + y^6} $$

## Solution détaillée

1. **Première approche : l'axe des abscisses et des ordonnées** :
   - Axe des abscisses ($y=0, x \neq 0$) : $f(x, 0) = \frac{0}{x^2} = 0 \implies$ limite est $0$.
   - Axe des ordonnées ($x=0, y \neq 0$) : $f(0, y) = \frac{0}{y^6} = 0 \implies$ limite est $0$.

2. **Deuxième approche : les droites ($y = mx$)** :
   Approchons selon une droite de pente $m$.
   $$ f(x, mx) = \frac{x(mx)^3}{x^2 + (mx)^6} = \frac{m^3 x^4}{x^2 + m^6 x^6} $$
   Pour $x \neq 0$, divisons par $x^2$ :
   $$ f(x, mx) = \frac{m^3 x^2}{1 + m^6 x^4} $$
   Lorsque $x \to 0$, l'expression tend vers $\frac{0}{1} = 0$.
   Les limites selon toutes les directions linéaires sont nulles, ce qui pourrait suggérer que la limite est $0$.
   Cependant, il faut tester des courbes non linéaires.

3. **Troisième approche : égaliser les puissances au dénominateur** :
   Le dénominateur est $x^2 + y^6$. Pour donner le même poids aux deux termes, trouvons un chemin de la forme $x = c y^k$ tel que $(c y^k)^2 \approx y^6$.
   On a $y^{2k} = y^6$, ce qui implique $2k = 6$, donc $k=3$.
   Considérons la courbe cubique $x = y^3$.

4. **Limite le long du chemin $x = y^3$** :
   Évaluons $f$ le long de cette trajectoire. Pour $y \neq 0$ :
   $$ f(y^3, y) = \frac{y^3 \cdot y^3}{(y^3)^2 + y^6} = \frac{y^6}{y^6 + y^6} = \frac{y^6}{2y^6} = \frac{1}{2} $$

   La limite le long de ce chemin cubique est $\frac{1}{2}$.

5. **Conclusion** :
   La limite suivant la trajectoire rectiligne $y=0$ (et d'autres droites) vaut $0$.
   La limite suivant la trajectoire courbe $x=y^3$ vaut $\frac{1}{2}$.
   Les limites différant selon le chemin d'approche, la limite globale de la fonction $f$ en $(0,0)$ **n'existe pas**.
