# Exercice 9

## Exercice 9 : Fermeture faible d'une boule et non réflexivité \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Dans un espace de Banach réflexif $E$, toute boule fermée est faiblement compacte. Montrer que l'espace des fonctions continues $C([0, 1])$ muni de la norme $\| \cdot \|_\infty$ n'est pas réflexif en exhibant une suite de la boule unité qui n'admet aucune sous-suite faiblement convergente.

**Correction :**
*Analyse de l'énoncé :* On utilise le théorème d'Eberlein-Šmulian : si la boule est faiblement compacte, toute suite admet une sous-suite faiblement convergente. On construit un contre-exemple explicite dans $C([0, 1])$.
*Résolution pas-à-pas :*
1. **Étape 1 : Construction de la suite.**
   Construisons une suite de fonctions $f_n \in C([0, 1])$ telles que $\|f_n\|_\infty \le 1$.
   On définit $f_n(t)$ comme une fonction "triangle" (ou "dent de scie") avec des pics très abrupts.
   Par exemple, pour chaque $k = 0, 1, \dots, 2^n-1$, $f_n(k/2^n) = 0$ et $f_n((k+1/2)/2^n) = 1$, interpolée linéairement.
   Ces fonctions oscillent de plus en plus vite.
2. **Étape 2 : Action des masses de Dirac (formes linéaires continues).**
   Sur $C([0, 1])$, pour tout $t \in [0, 1]$, l'application d'évaluation $\delta_t(f) = f(t)$ est une forme linéaire continue.
   Supposons qu'il existe une sous-suite faiblement convergente $f_{\phi(n)} \rightharpoonup f$.
   Cela impliquerait que pour toute forme continue, $L(f_{\phi(n)}) \to L(f)$.
   En particulier, pour tout $t$, on aurait $f_{\phi(n)}(t) \to f(t)$.
3. **Étape 3 : Preuve de la contradiction.**
   Par le théorème de convergence dominée (ou le théorème de Baire sur la limite simple de fonctions continues), si une telle $f$ existait, ce serait une fonction de première classe de Baire.
   Cependant, la suite de "dents de scie" prend les valeurs $0$ et $1$ sur des ensembles de plus en plus denses. Pour tout point $t$, l'évaluation $f_{\phi(n)}(t)$ ne converge pas, sauf si l'on extrait une sous-suite spécifiquement pour $t$.
   Un point $t_0$ choisi adéquatement montrera que pour n'importe quelle sous-suite, $f_{\phi(n)}(t_0)$ ne converge pas (par un argument diagonal de Baire).
   Donc il n'y a pas de limite faible. L'espace n'étant pas faiblement séquentiellement compact, il n'est pas réflexif par Eberlein-Šmulian.
