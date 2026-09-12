# Exercice 5 : Généralisation de Fatou par domination inférieure
$\bigstar\bigstar\bigstar\star\star$

## Énoncé
Soit $(f_n)$ une suite de fonctions mesurables (de signe quelconque) sur $(X, \mathcal{A}, \mu)$.
On suppose qu'il existe une fonction $g$ Lebesgue-intégrable telle que pour tout $n$, $f_n \geq g$ presque partout.
Démontrer rigoureusement que :
$$\int_X (\liminf_{n \to \infty} f_n) d\mu \leq \liminf_{n \to \infty} \int_X f_n d\mu$$

## Correction
La condition $f_n \geq g$ implique que les fonctions $f_n$ ne sont pas nécessairement positives, ce qui empêche d'appliquer directement le Lemme de Fatou classique.
Cependant, la fonction $g$ est intégrable, ce qui garantit que $\int_X g d\mu$ est finie.

**1. Retour au cas positif :**
Posons la suite de fonctions $h_n = f_n - g$.
Par hypothèse, $h_n \geq 0$ presque partout pour tout $n$.
Les $h_n$ sont mesurables et positives, on peut donc leur appliquer le Lemme de Fatou classique :
$$\int_X (\liminf_{n \to \infty} h_n) d\mu \leq \liminf_{n \to \infty} \int_X h_n d\mu$$

**2. Analyse du membre de gauche :**
$\liminf_{n \to \infty} h_n = \liminf_{n \to \infty} (f_n - g) = (\liminf_{n \to \infty} f_n) - g$ (car $g$ ne dépend pas de $n$).
Donc :
$$\int_X (\liminf_{n \to \infty} h_n) d\mu = \int_X ((\liminf_{n \to \infty} f_n) - g) d\mu$$
Puisque $g$ est intégrable, par linéarité de l'intégrale de Lebesgue :
$$\int_X (\liminf_{n \to \infty} h_n) d\mu = \int_X (\liminf_{n \to \infty} f_n) d\mu - \int_X g d\mu$$

**3. Analyse du membre de droite :**
De même, pour tout $n$, $\int_X h_n d\mu = \int_X (f_n - g) d\mu = \int_X f_n d\mu - \int_X g d\mu$.
Ainsi,
$$\liminf_{n \to \infty} \int_X h_n d\mu = \liminf_{n \to \infty} \left( \int_X f_n d\mu - \int_X g d\mu \right)$$
La soustraction par une constante finie commute avec la limite inférieure :
$$\liminf_{n \to \infty} \int_X h_n d\mu = \left( \liminf_{n \to \infty} \int_X f_n d\mu \right) - \int_X g d\mu$$

**4. Conclusion :**
En injectant ces deux résultats dans l'inégalité de Fatou pour $h_n$ :
$$\int_X (\liminf_{n \to \infty} f_n) d\mu - \int_X g d\mu \leq \left( \liminf_{n \to \infty} \int_X f_n d\mu \right) - \int_X g d\mu$$
Puisque $\int_X g d\mu$ est une valeur réelle finie, on peut l'ajouter de chaque côté de l'inégalité sans en changer le sens, ce qui donne le résultat escompté.
