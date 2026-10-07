# Exercice 1

## Exercice 1 : Mesurabilité d'une fonction constante $\bigstar\star\star\star\star$

Soit $(\Omega, \mathcal{F})$ un espace mesurable. Montrer qu'une application constante $X : \Omega \to \mathbb{R}$, définie par $\forall \omega \in \Omega, X(\omega) = c$ (où $c \in \mathbb{R}$), est une variable aléatoire.

### Correction pas à pas

1. **Définition de la mesurabilité**
   Une application $X : \Omega \to \mathbb{R}$ est une variable aléatoire si pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque $X^{-1}(B)$ appartient à la tribu $\mathcal{F}$.

2. **Analyse de l'image réciproque pour une constante**
   Soit $B \in \mathcal{B}(\mathbb{R})$. L'image réciproque est définie par :
   $$ X^{-1}(B) = \{ \omega \in \Omega \mid X(\omega) \in B \} $$
   Puisque $X(\omega) = c$ pour tout $\omega \in \Omega$, il n'y a que deux cas possibles :
   - Soit $c \in B$. Dans ce cas, pour tout $\omega \in \Omega$, la condition $X(\omega) \in B$ est vérifiée. Donc, $X^{-1}(B) = \Omega$.
   - Soit $c \notin B$. Dans ce cas, pour aucun $\omega \in \Omega$, la condition $X(\omega) \in B$ n'est vérifiée. Donc, $X^{-1}(B) = \emptyset$.

3. **Conclusion**
   Dans tous les cas possibles, $X^{-1}(B)$ est soit $\Omega$, soit $\emptyset$.
   Or, par définition d'une tribu, $\mathcal{F}$ contient toujours l'ensemble vide $\emptyset$ et l'espace entier $\Omega$.
   Donc $X^{-1}(B) \in \mathcal{F}$ pour tout borélien $B$.
   L'application constante est bien mesurable, c'est une variable aléatoire.
