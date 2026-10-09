# Exercice 6

## Exercice 6 : Mesurabilité de la limite simple $\bigstar\bigstar\bigstar\star\star$

Soit $(X_n)_{n \in \mathbb{N}}$ une suite de variables aléatoires sur $(\Omega, \mathcal{F})$.
Supposons que pour tout $\omega \in \Omega$, la limite $X(\omega) = \lim_{n \to +\infty} X_n(\omega)$ existe.
Démontrer que la fonction limite $X$ est une variable aléatoire.

### Correction pas à pas

1. **Caractérisation de la limite par les sup et inf**
   Pour une suite convergente de nombres réels, la limite est égale à la limite supérieure et à la limite inférieure :
   $$ \lim_{n \to \infty} x_n = \limsup_{n \to \infty} x_n = \inf_{k \geq 0} \sup_{n \geq k} x_n $$
   Nous allons d'abord montrer que le supremum dénombrable de variables aléatoires est une variable aléatoire.

2. **Mesurabilité du supremum dénombrable**
   Soit $Y = \sup_{n \geq 0} X_n$.
   Pour prouver que $Y$ est mesurable, il suffit de regarder les événements $\{Y \leq a\}$ pour tout réel $a$.
   Le supremum d'une suite est inférieur ou égal à $a$ si et seulement si tous les éléments de la suite sont inférieurs ou égaux à $a$.
   $$ \{ \omega \mid \sup_{n \geq 0} X_n(\omega) \leq a \} = \bigcap_{n=0}^{\infty} \{ \omega \mid X_n(\omega) \leq a \} $$
   Comme chaque $X_n$ est une variable aléatoire, les événements $\{X_n \leq a\} \in \mathcal{F}$.
   La tribu $\mathcal{F}$ est stable par intersection dénombrable, donc $\{Y \leq a\} \in \mathcal{F}$.
   Ainsi, $Y = \sup_n X_n$ est mesurable.

3. **Mesurabilité de l'infimum dénombrable**
   Par un raisonnement symétrique (ou en remarquant que $\inf_n X_n = -\sup_n (-X_n)$), l'infimum dénombrable de variables aléatoires est aussi une variable aléatoire.

4. **Conclusion pour la limite**
   La fonction limite s'écrit :
   $$ X = \inf_{k \geq 0} \left( \sup_{n \geq k} X_n \right) $$
   Pour chaque $k$, $Z_k = \sup_{n \geq k} X_n$ est mesurable d'après le point 2.
   Ensuite, $X = \inf_{k \geq 0} Z_k$ est mesurable d'après le point 3.
   La limite simple d'une suite de variables aléatoires est donc une variable aléatoire.
