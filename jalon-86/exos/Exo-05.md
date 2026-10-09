# Exercice 5

## Exercice 5 : Composition avec une fonction continue $\bigstar\bigstar\bigstar\star\star$

Soit $X$ une variable aléatoire sur $(\Omega, \mathcal{F})$ et $f : \mathbb{R} \to \mathbb{R}$ une fonction continue.
Démontrer que la fonction composée $Z = f \circ X$ est une variable aléatoire.

### Correction pas à pas

1. **Définition de la variable aléatoire composée**
   La fonction $Z : \Omega \to \mathbb{R}$ est définie par $Z(\omega) = f(X(\omega))$.
   Pour montrer que $Z$ est une variable aléatoire, nous devons prouver que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, $Z^{-1}(B) \in \mathcal{F}$.

2. **Décomposition de l'image réciproque**
   L'image réciproque s'écrit :
   $Z^{-1}(B) = (f \circ X)^{-1}(B) = X^{-1}(f^{-1}(B))$.

3. **Mesurabilité de la fonction continue**
   La tribu borélienne $\mathcal{B}(\mathbb{R})$ est engendrée par les ouverts de $\mathbb{R}$.
   Puisque $f$ est une fonction continue, par définition topologique de la continuité, l'image réciproque de tout ouvert $O$ de l'espace d'arrivée est un ouvert de l'espace de départ.
   Donc si $O$ est ouvert, $f^{-1}(O)$ est ouvert, et donc $f^{-1}(O) \in \mathcal{B}(\mathbb{R})$.
   Cela prouve que $f$ est une fonction borélienne-mesurable (ou $\mathcal{B}(\mathbb{R})/\mathcal{B}(\mathbb{R})$-mesurable).
   Ainsi, pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, son image réciproque $A = f^{-1}(B)$ est également un borélien de $\mathbb{R}$, donc $A \in \mathcal{B}(\mathbb{R})$.

4. **Conclusion avec la variable aléatoire initiale**
   Nous devons évaluer $X^{-1}(A)$.
   Puisque $X$ est une variable aléatoire ($\mathcal{F}/\mathcal{B}(\mathbb{R})$-mesurable) et que $A \in \mathcal{B}(\mathbb{R})$, l'image réciproque $X^{-1}(A)$ appartient à $\mathcal{F}$.
   Donc $(f \circ X)^{-1}(B) \in \mathcal{F}$ pour tout borélien $B$.
   La composée d'une fonction continue et d'une variable aléatoire est une variable aléatoire.
