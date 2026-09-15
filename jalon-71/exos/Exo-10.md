## Exercice 10 : Mesure de Probabilité Marginale \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit un vecteur aléatoire $(X, Y)$ de densité de probabilité conjointe $f(x, y) = \frac{1}{\pi} e^{-x^2-y^2}$.
Prouver que la fonction $f_X(x) = \int_{\mathbb{R}} f(x, y) dy$ est une densité de probabilité légitime (intégrale valant 1) en utilisant le théorème de Fubini-Tonelli.

**Correction :**
1. Une fonction $g$ est une densité de probabilité si elle est positive presque partout et que son intégrale vaut 1.
2. Clairement, $f(x, y) \ge 0$ pour tout $(x,y)$, car l'exponentielle est toujours positive.
3. Puisque l'intégrale d'une fonction positive est positive, $f_X(x) = \int_\mathbb{R} f(x, y) dy \ge 0$.
4. Il reste à vérifier que $\int_\mathbb{R} f_X(x) dx = 1$.
   $$ \int_{\mathbb{R}} f_X(x) dx = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} f(x, y) dy \right) dx $$
5. Comme $f$ est positive, le théorème de Tonelli nous garantit que nous pouvons intervertir ou regrouper les intégrales. De plus, on nous donne que $f(x,y)$ est une densité conjointe, donc par définition $\iint_{\mathbb{R}^2} f(x,y) dx dy = 1$.
6. L'intégrale itérée est donc égale à l'intégrale double, qui vaut $1$.
7. Si l'on souhaite calculer explicitement $f_X(x)$ :
   $$ f_X(x) = \int_{\mathbb{R}} \frac{1}{\pi} e^{-x^2} e^{-y^2} dy = \frac{1}{\pi} e^{-x^2} \int_{\mathbb{R}} e^{-y^2} dy $$
8. On sait que l'intégrale de Gauss $\int_\mathbb{R} e^{-y^2} dy = \sqrt{\pi}$.
   Donc $f_X(x) = \frac{1}{\pi} e^{-x^2} \sqrt{\pi} = \frac{1}{\sqrt{\pi}} e^{-x^2}$.
9. On vérifie aisément que $\int_\mathbb{R} \frac{1}{\sqrt{\pi}} e^{-x^2} dx = \frac{1}{\sqrt{\pi}} \times \sqrt{\pi} = 1$. L'exercice confirme analytiquement la cohérence de la marginalisation.
