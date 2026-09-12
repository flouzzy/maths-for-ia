# Exercice 6 : Application à une limite supérieure
$\bigstar\bigstar\bigstar\star\star$

## Énoncé
En utilisant un raisonnement similaire au Lemme de Fatou, démontrer que si $(f_n)$ est une suite de fonctions mesurables, toutes majorées presque partout par une fonction intégrable $G$, alors :
$$\limsup_{n \to \infty} \int_X f_n d\mu \leq \int_X (\limsup_{n \to \infty} f_n) d\mu$$

## Correction
Il s'agit du "Fatou inversé". L'hypothèse clé est la majoration par une fonction intégrable $G$, c'est-à-dire $f_n \leq G$ pour tout $n$.

**1. Changement de signe :**
Posons $h_n = G - f_n$.
Puisque $f_n \leq G$, on a $h_n \geq 0$ presque partout.
Les $h_n$ sont mesurables et positives. On peut leur appliquer le Lemme de Fatou standard :
$$\int_X \liminf_{n \to \infty} h_n d\mu \leq \liminf_{n \to \infty} \int_X h_n d\mu$$

**2. Propriétés des limites inférieures/supérieures avec les signes :**
Rappelons que $\liminf (-a_n) = - \limsup (a_n)$.
Calculons $\liminf h_n$ :
$$\liminf_{n \to \infty} (G - f_n) = G + \liminf_{n \to \infty} (-f_n) = G - \limsup_{n \to \infty} f_n$$

**3. Application de l'intégrale sur le membre de gauche :**
$$\int_X \liminf_{n \to \infty} h_n d\mu = \int_X (G - \limsup f_n) d\mu = \int_X G d\mu - \int_X (\limsup f_n) d\mu$$
(L'utilisation de la linéarité est justifiée car $G$ est intégrable).

**4. Analyse du membre de droite :**
$$\liminf_{n \to \infty} \int_X h_n d\mu = \liminf_{n \to \infty} \int_X (G - f_n) d\mu = \liminf_{n \to \infty} \left( \int_X G d\mu - \int_X f_n d\mu \right)$$
$$\liminf_{n \to \infty} \int_X h_n d\mu = \int_X G d\mu + \liminf_{n \to \infty} \left( - \int_X f_n d\mu \right) = \int_X G d\mu - \limsup_{n \to \infty} \int_X f_n d\mu$$

**5. Conclusion :**
En remplaçant dans l'inégalité de départ :
$$\int_X G d\mu - \int_X (\limsup f_n) d\mu \leq \int_X G d\mu - \limsup \int_X f_n d\mu$$
Puisque $\int_X G d\mu$ est un réel fini, on peut la soustraire des deux côtés :
$$- \int_X (\limsup f_n) d\mu \leq - \limsup \int_X f_n d\mu$$
En multipliant par $-1$ (ce qui inverse le sens de l'inégalité) :
$$\int_X (\limsup f_n) d\mu \geq \limsup \int_X f_n d\mu$$
Ce qui est exactement l'inégalité demandée.
