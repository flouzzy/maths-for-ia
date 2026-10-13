# Généralisation par les fonctions génératrices des moments

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

Démontrer le résultat de l'exercice précédent (somme de deux variables de Poisson indépendantes) en utilisant le formalisme analytique des fonctions génératrices des moments (ou fonctions caractéristiques), prouvant l'élégance de ce formalisme sur le calcul convolutif direct.

### Correction

Soient $X \sim \mathcal{P}(\lambda)$ et $Y \sim \mathcal{P}(\mu)$ deux variables aléatoires indépendantes, et $S = X + Y$.

**1. Rappel théorique fondamental :**
La fonction caractéristique (ou fonction génératrice des moments) de la somme de deux variables aléatoires **indépendantes** est le produit mathématique de leurs fonctions caractéristiques individuelles.
$\phi_S(t) = \mathbb{E}[e^{itS}] = \mathbb{E}[e^{it(X+Y)}] = \mathbb{E}[e^{itX} e^{itY}]$.
Par indépendance des variables $e^{itX}$ et $e^{itY}$ (théorème des coalitions), l'espérance du produit est le produit des espérances :
$\phi_S(t) = \mathbb{E}[e^{itX}] \cdot \mathbb{E}[e^{itY}] = \phi_X(t) \cdot \phi_Y(t)$.

**2. Calcul de la fonction caractéristique d'une loi de Poisson :**
Soit $V \sim \mathcal{P}(\theta)$. Calculons sa fonction caractéristique $\phi_V(t) = \mathbb{E}[e^{itV}]$.
Par le théorème de transfert :
$\phi_V(t) = \sum_{k=0}^\infty e^{itk} \mathbb{P}(V=k) = \sum_{k=0}^\infty (e^{it})^k e^{-\theta} \frac{\theta^k}{k!}$
On factorise la constante exponentielle et on regroupe les termes à la puissance $k$ :
$\phi_V(t) = e^{-\theta} \sum_{k=0}^\infty \frac{(\theta e^{it})^k}{k!}$
On identifie la série de Taylor de la fonction exponentielle mathématique $\sum_{k=0}^\infty \frac{z^k}{k!} = e^z$ pour $z = \theta e^{it}$ :
$\phi_V(t) = e^{-\theta} e^{\theta e^{it}} = e^{\theta(e^{it} - 1)}$.

**3. Application à la somme $S = X + Y$ :**
Les fonctions caractéristiques marginales sont donc $\phi_X(t) = e^{\lambda(e^{it} - 1)}$ et $\phi_Y(t) = e^{\mu(e^{it} - 1)}$.
En appliquant le théorème de produit pour variables indépendantes :
$\phi_S(t) = \phi_X(t) \cdot \phi_Y(t) = e^{\lambda(e^{it} - 1)} \cdot e^{\mu(e^{it} - 1)}$
Par les propriétés algébriques de la fonction exponentielle :
$\phi_S(t) = e^{\lambda(e^{it} - 1) + \mu(e^{it} - 1)} = e^{(\lambda + \mu)(e^{it} - 1)}$

**4. Conclusion et identification :**
L'expression obtenue, $e^{(\lambda + \mu)(e^{it} - 1)}$, correspond parfaitement à la signature analytique de la fonction caractéristique d'une loi de Poisson de paramètre $(\lambda + \mu)$.
D'après le théorème de caractérisation univoque de Lévy (l'application qui à une loi associe sa fonction caractéristique est bijective), on conclut que la distribution probabiliste de $S$ est exactement la loi $\mathcal{P}(\lambda + \mu)$.
Cette démonstration analytique est considérablement plus courte et évite toute sommation combinatoire.
