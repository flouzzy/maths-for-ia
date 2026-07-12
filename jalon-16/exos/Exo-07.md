# Exercice 07 : Séries de Bertrand

## Énoncé
Étudier, selon les valeurs du réel $\beta$, la convergence de la série $\sum_{n \ge 2} \frac{1}{n (\ln n)^\beta}$.

## Correction Détaillée
1. **Typage et fonctions :**
   La fonction $f(t) = \frac{1}{t (\ln t)^\beta}$ est définie, continue, positive et décroissante sur $[2, +\infty[$.
   Ceci est justifié car son dénominateur est le produit de deux fonctions croissantes et positives. On peut utiliser le théorème de comparaison série-intégrale.

2. **Comparaison avec l'intégrale :**
   La série $\sum f(n)$ et l'intégrale $\int_2^{+\infty} f(t)dt$ sont de même nature.
   Calculons l'intégrale impropre sur un segment $[2, X]$ :
   $$I(X) = \int_2^X \frac{1}{t (\ln t)^\beta} dt$$

3. **Changement de variable ou primitive directe :**
   Posons $u = \ln t$. On a $du = \frac{1}{t} dt$.
   Les bornes deviennent $\ln 2$ et $\ln X$.
   $$I(X) = \int_{\ln 2}^{\ln X} \frac{1}{u^\beta} du = \int_{\ln 2}^{\ln X} u^{-\beta} du$$

4. **Évaluation selon les cas :**
   - **Cas $\beta \neq 1$ :**
     Une primitive est $\left[\frac{u^{-\beta+1}}{-\beta+1}\right]$.
     $$I(X) = \frac{1}{1-\beta} \left( (\ln X)^{1-\beta} - (\ln 2)^{1-\beta} \right)$$
     Si $\beta > 1$, $1-\beta < 0$, donc $(\ln X)^{1-\beta} \to 0$ en $+\infty$. L'intégrale converge.
     Si $\beta < 1$, $1-\beta > 0$, donc $(\ln X)^{1-\beta} \to +\infty$. L'intégrale diverge.
   - **Cas $\beta = 1$ :**
     L'intégrale est $\int \frac{1}{u} du = [\ln |u|]$.
     $$I(X) = \ln(\ln X) - \ln(\ln 2)$$
     Lorsque $X \to +\infty$, $\ln(\ln X) \to +\infty$. L'intégrale diverge.

5. **Conclusion Mathématique :**
   La série de Bertrand $\sum \frac{1}{n (\ln n)^\beta}$ converge si et seulement si $\beta > 1$.
