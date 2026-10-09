# Exercice 9 : Intégration par rapport à une mesure non finie

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $\Omega = \mathbb{N}^*$, muni de la tribu des parties $\mathcal{P}(\mathbb{N}^*)$.
On définit une mesure $m$ sur $\Omega$ (ce n'est pas une mesure de probabilité) par $m(\{k\}) = \frac{1}{k^2}$.
Soit la fonction $X : \Omega \to \mathbb{R}$ définie par $X(k) = k$.
1. La mesure de l'espace total $m(\Omega)$ est-elle finie ?
2. Calculer l'intégrale (espérance généralisée) de $X$ par rapport à $m$. La fonction $X$ est-elle intégrable ?

### Correction détaillée

1. Calculons la mesure totale de l'espace $\Omega$ :
   $$ m(\Omega) = \sum_{k=1}^{\infty} m(\{k\}) = \sum_{k=1}^{\infty} \frac{1}{k^2} $$
   Cette série est une série de Riemann convergente (exposant $\alpha = 2 > 1$).
   Sa somme est un résultat classique connu sous le nom de problème de Bâle (résolu par Euler) :
   $$ m(\Omega) = \frac{\pi^2}{6} $$
   La mesure totale est finie. On pourrait la normaliser pour en faire une probabilité en divisant chaque poids par $\pi^2/6$.

2. Étudions l'intégrabilité de la fonction $X(k) = k$. L'intégrale de Lebesgue par rapport à cette mesure discrète est la série :
   $$ \int_{\Omega} X \, \mathrm{d}m = \sum_{k=1}^{\infty} X(k) m(\{k\}) $$
   $$ \int_{\Omega} X \, \mathrm{d}m = \sum_{k=1}^{\infty} k \frac{1}{k^2} = \sum_{k=1}^{\infty} \frac{1}{k} $$
   On reconnaît la série harmonique. Or, la série harmonique diverge vers l'infini : $\sum_{k=1}^{\infty} \frac{1}{k} = +\infty$.

   La fonction $X$ a donc une intégrale infinie. Elle n'appartient pas à $\mathcal{L}^1(\Omega, m)$, elle n'est pas intégrable, malgré le fait que la mesure de l'espace total soit finie.
   Cela illustre le cas d'une variable qui prend des valeurs qui grandissent "trop vite" ($k$) par rapport à la vitesse à laquelle les probabilités décroissent ($1/k^2$).
