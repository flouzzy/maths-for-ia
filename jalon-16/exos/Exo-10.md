# Exercice 10 : Séries entrelacées et astuces de manipulation

## Énoncé
Soit $(u_n)$ la suite définie par :
$u_{2k} = \frac{1}{2^{2k}}$ et $u_{2k+1} = \frac{1}{3^{2k+1}}$.
Étudier la convergence de la série $\sum u_n$. Pourquoi la règle de d'Alembert est-elle inopérante ici ?

## Correction Détaillée
1. **Positivité :**
   La suite est clairement à termes strictement positifs.

2. **Tentative par la règle de d'Alembert :**
   Étudions le quotient $q_n = \frac{u_{n+1}}{u_n}$.
   Cas $n = 2k$ (pair) :
   $$q_{2k} = \frac{u_{2k+1}}{u_{2k}} = \frac{\frac{1}{3^{2k+1}}}{\frac{1}{2^{2k}}} = \frac{2^{2k}}{3^{2k+1}} = \frac{1}{3} \left(\frac{2}{3}\right)^{2k}$$
   Comme $2/3 < 1$, $\lim_{k \to \infty} q_{2k} = 0$.

   Cas $n = 2k+1$ (impair) :
   $$q_{2k+1} = \frac{u_{2k+2}}{u_{2k+1}} = \frac{\frac{1}{2^{2k+2}}}{\frac{1}{3^{2k+1}}} = \frac{3^{2k+1}}{2^{2k+2}} = \frac{3}{4} \left(\frac{3}{2}\right)^{2k}$$
   Comme $3/2 > 1$, $\lim_{k \to \infty} q_{2k+1} = +\infty$.

   La suite des quotients n'admet pas de limite unique (elle possède une sous-suite tendant vers 0 et une sous-suite divergente). Le critère de d'Alembert échoue.

3. **Tentative par le critère de Cauchy :**
   Calculons $\sqrt[n]{u_n}$.
   Cas $n = 2k$ : $\sqrt[2k]{u_{2k}} = \left(2^{-2k}\right)^{\frac{1}{2k}} = \frac{1}{2}$.
   Cas $n = 2k+1$ : $\sqrt[2k+1]{u_{2k+1}} = \left(3^{-(2k+1)}\right)^{\frac{1}{2k+1}} = \frac{1}{3}$.
   La suite de Cauchy n'a pas non plus de limite (elle oscille entre $1/2$ et $1/3$).
   Mais la limite supérieure (limsup) de Cauchy existe :
   $\limsup \sqrt[n]{u_n} = \max(1/2, 1/3) = 1/2$.
   D'après le critère de Cauchy généralisé, comme $\limsup < 1$, la série converge.

4. **Preuve directe par séparation des termes :**
   Puisque les termes sont positifs, on peut sommer les termes pairs et impairs séparément :
   $\sum u_n = \sum_{k=0}^\infty u_{2k} + \sum_{k=0}^\infty u_{2k+1}$
   $\sum_{k=0}^\infty \frac{1}{2^{2k}} = \sum_{k=0}^\infty \left(\frac{1}{4}\right)^k = \frac{1}{1 - 1/4} = \frac{4}{3}$ (Série géométrique convergente).
   $\sum_{k=0}^\infty \frac{1}{3^{2k+1}} = \frac{1}{3} \sum_{k=0}^\infty \left(\frac{1}{9}\right)^k = \frac{1}{3} \cdot \frac{1}{1 - 1/9} = \frac{1}{3} \cdot \frac{9}{8} = \frac{3}{8}$ (Série géométrique convergente).
   La somme de deux séries convergentes est convergente.
   $\sum u_n = \frac{4}{3} + \frac{3}{8} = \frac{32 + 9}{24} = \frac{41}{24}$.
