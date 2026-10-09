# Exercice 9

## Exercice 9 : Propriété de la fonction de répartition $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $X$ une variable aléatoire réelle et $F(x) = \mathbb{P}(X \leq x)$ sa fonction de répartition.
Démontrer rigoureusement que $F$ est continue à droite en tout point $x_0 \in \mathbb{R}$, c'est-à-dire : $\lim_{x \to x_0^+} F(x) = F(x_0)$.
*Indication : Utiliser la continuité décroissante d'une mesure de probabilité.*

### Correction pas à pas

1. **Définition de la limite par valeurs supérieures**
   Pour montrer la limite à droite, on considère une suite $(x_n)_{n \in \mathbb{N}}$ de réels strictement décroissante qui converge vers $x_0$.
   Par exemple, la suite $x_n = x_0 + \frac{1}{n}$ pour $n \geq 1$.
   Il faut prouver que $\lim_{n \to \infty} F(x_n) = F(x_0)$.

2. **Traduction en termes d'événements**
   Considérons la suite d'événements : $A_n = \{ \omega \in \Omega \mid X(\omega) \leq x_n \}$.
   Par définition, $\mathbb{P}(A_n) = F(x_n)$.
   Puisque la suite $(x_n)$ est décroissante ($x_{n+1} \leq x_n$), si $X(\omega) \leq x_{n+1}$, alors automatiquement $X(\omega) \leq x_n$.
   Donc les événements sont emboîtés de manière décroissante : $A_1 \supset A_2 \supset A_3 \supset \dots$

3. **L'intersection des événements**
   Quelle est l'intersection de cette suite décroissante d'événements ?
   $$ A = \bigcap_{n=1}^{\infty} A_n = \bigcap_{n=1}^{\infty} \{ X \leq x_n \} $$
   Si un réel $X(\omega)$ est inférieur ou égal à $x_n$ pour tout $n$, et sachant que $x_n \to x_0$ en décroissant, cela implique rigoureusement que $X(\omega) \leq x_0$.
   Réciproquement, si $X(\omega) \leq x_0$, puisque $x_0 < x_n$ pour tout $n$, on a bien $X(\omega) \leq x_n$ pour tout $n$.
   Donc l'intersection est exactement :
   $$ A = \{ X \leq x_0 \} $$

4. **Axiome de continuité décroissante de la probabilité**
   D'après les axiomes de Kolmogorov (Jalon 85), toute mesure de probabilité $\mathbb{P}$ est continue par rapport aux suites décroissantes d'événements. Cela signifie que :
   $$ \mathbb{P}\left( \bigcap_{n=1}^{\infty} A_n \right) = \lim_{n \to \infty} \mathbb{P}(A_n) $$
   En remplaçant par nos expressions :
   $$ \mathbb{P}(X \leq x_0) = \lim_{n \to \infty} \mathbb{P}(X \leq x_n) $$
   Soit :
   $$ F(x_0) = \lim_{n \to \infty} F(x_n) $$
   Puisque ce résultat est vrai pour toute suite $(x_n)$ décroissant vers $x_0$, la fonction de répartition $F$ est bien continue à droite.
