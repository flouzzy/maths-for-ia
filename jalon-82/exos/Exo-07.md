# Exercice 7 : Résolution de l'équation des distributions $xT = 0$
Difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Nous avons vu que $x \delta_0 = 0$. Le but de cet exercice est de démontrer la réciproque : l'équation algébrique $x T = 0$ où $T \in \mathcal{D}'(\mathbb{R})$ admet pour solutions l'ensemble des distributions proportionnelles à la masse de Dirac.
Supposons que $T \in \mathcal{D}'(\mathbb{R})$ vérifie $x T = 0$.
1. Soit $\varphi \in \mathcal{D}(\mathbb{R})$ une fonction test vérifiant $\varphi(0) = 0$. En utilisant le lemme d'Hadamard (qui affirme qu'il existe une fonction $\psi \in \mathcal{D}(\mathbb{R})$ telle que $\varphi(x) = x\psi(x)$), montrez que $\langle T, \varphi \rangle = 0$.
2. Soit $\chi \in \mathcal{D}(\mathbb{R})$ une fonction test fixée telle que $\chi(0) = 1$. Pour une fonction test quelconque $f \in \mathcal{D}(\mathbb{R})$, on écrit la décomposition : $f(x) = f(0)\chi(x) + (f(x) - f(0)\chi(x))$.
   Déduisez-en la forme générale de la distribution $T$.

**Correction Détaillée :**
1. **Action sur les fonctions s'annulant en 0 :**
   Soit $\varphi \in \mathcal{D}(\mathbb{R})$ avec $\varphi(0) = 0$.
   D'après le lemme d'Hadamard, puisque $\varphi(0)=0$ et $\varphi \in C^\infty$, le rapport $\varphi(x)/x$ se prolonge en une fonction $C^\infty$ qui vaut $\varphi'(0)$ en 0. Comme $\varphi$ est à support compact, on peut s'arranger (par troncature douce si besoin) pour construire $\psi \in \mathcal{D}(\mathbb{R})$ telle que $\varphi(x) = x\psi(x)$.
   Calculons l'action de $T$ sur $\varphi$ :
   $$ \langle T, \varphi \rangle = \langle T, x\psi \rangle $$
   Par définition du produit d'une distribution par la fonction lisse $x \mapsto x$ :
   $$ \langle T, x\psi \rangle = \langle xT, \psi \rangle $$
   Or, par hypothèse, l'équation impose $xT = 0$. Donc l'action de $xT$ sur n'importe quelle fonction test est nulle.
   $$ \langle xT, \psi \rangle = \langle 0, \psi \rangle = 0 $$
   Conclusion intermédiaire : Si $\varphi(0) = 0$, alors $\langle T, \varphi \rangle = 0$.

2. **Généralisation à toute fonction test par décomposition :**
   Soit $f \in \mathcal{D}(\mathbb{R})$ une fonction test quelconque.
   Considérons la fonction $\chi$ définie dans l'énoncé, vérifiant $\chi(0)=1$.
   On définit la fonction $\varphi(x) = f(x) - f(0)\chi(x)$.
   Clairement, $\varphi$ est une combinaison linéaire de fonctions tests, donc $\varphi \in \mathcal{D}(\mathbb{R})$.
   Évaluons $\varphi$ en 0 :
   $$ \varphi(0) = f(0) - f(0)\chi(0) = f(0) - f(0)(1) = 0 $$
   D'après la question 1, puisque $\varphi(0) = 0$, nous devons avoir $\langle T, \varphi \rangle = 0$.
   Exploitons la linéarité de $T$ sur l'expression de $\varphi$ :
   $$ \langle T, f - f(0)\chi \rangle = 0 $$
   $$ \langle T, f \rangle - \langle T, f(0)\chi \rangle = 0 $$
   Comme $f(0)$ est un scalaire (un nombre complexe), on peut le sortir du crochet de dualité :
   $$ \langle T, f \rangle - f(0)\langle T, \chi \rangle = 0 $$
   $$ \langle T, f \rangle = f(0) \langle T, \chi \rangle $$
   Posons $C = \langle T, \chi \rangle$. C'est une constante scalaire qui ne dépend que de $T$ et du choix de $\chi$, mais qui est indépendante de $f$.
   On obtient alors :
   $$ \langle T, f \rangle = C \cdot f(0) = C \langle \delta_0, f \rangle $$
   Cette égalité est vraie pour toute fonction test $f$. Par conséquent, la distribution s'écrit formellement :
   $$ T = C \delta_0 $$
   Les seules solutions de l'équation $xT = 0$ sont les multiples de la masse de Dirac en l'origine.
