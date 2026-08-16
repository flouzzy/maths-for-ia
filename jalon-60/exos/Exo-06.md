## Exercice 6 : Fonctions d'activation polynomiales \quad $\bigstar\bigstar\bigstar\star\star$

Le théorème d'approximation universelle est-il valable si la fonction d'activation est un polynôme de degré $d$ fini, $\sigma(x) = P(x)$ ?

**Correction :**
Non. L'espace vectoriel engendré par les fonctions de la forme $P(w^T x + b)$ pour divers $w, b$ est un espace de polynômes à $n$ variables de degré maximal $d$.
Puisque le degré est borné, cet espace est de dimension finie (précisément $\binom{n+d}{n}$).
Un sous-espace de dimension finie dans $\mathcal{C}(I_n)$ (qui est de dimension infinie) est toujours fermé et d'intérieur vide, il ne peut donc pas être dense dans $\mathcal{C}(I_n)$.
On ne peut approximer à n'importe quelle précision des fonctions comme $\exp(x)$ ou $\sin(x)$ avec des polynômes d'un degré globalement borné par $d$. C'est pourquoi la fonction d'activation doit être non polynomiale pour garantir l'universalité.
