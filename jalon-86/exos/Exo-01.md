## Vérification de la mesurabilité d'une fonction simple \quad $\bigstar\star\star\star\star$

**Énoncé :**
Soit un espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$ où $\Omega = \{a, b, c, d\}$ et la tribu est $\mathcal{F} = \{\emptyset, \{a, b\}, \{c, d\}, \Omega\}$.
On définit la fonction $X : \Omega \to \mathbb{R}$ par $X(a) = 1, X(b) = 1, X(c) = 2, X(d) = 2$.
Démontrer rigoureusement que $X$ est une variable aléatoire réelle.

**Correction Explicative :**
1. Pour prouver que $X$ est une variable aléatoire, il faut montrer que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, l'image réciproque $X^{-1}(B)$ appartient à la tribu $\mathcal{F}$.
2. Analysons les valeurs prises par $X$. La fonction $X$ ne prend que deux valeurs : $1$ et $2$.
3. Considérons un borélien quelconque $B \subset \mathbb{R}$. Selon que $B$ contienne ou non les valeurs $1$ et $2$, nous avons quatre cas mutuellement exclusifs pour l'image réciproque $X^{-1}(B) = \{ \omega \in \Omega \mid X(\omega) \in B \}$ :
   - Cas 1 : $1 \notin B$ et $2 \notin B$.
     Alors aucune issue $\omega$ ne satisfait $X(\omega) \in B$. L'image réciproque est $X^{-1}(B) = \emptyset$.
     Puisque $\mathcal{F}$ est une tribu, elle contient l'ensemble vide : $\emptyset \in \mathcal{F}$.
   - Cas 2 : $1 \in B$ et $2 \notin B$.
     Les seules issues vérifiant $X(\omega) \in B$ sont celles pour lesquelles $X(\omega) = 1$.
     Ainsi, $X^{-1}(B) = \{a, b\}$. Par définition de la tribu donnée, on a bien $\{a, b\} \in \mathcal{F}$.
   - Cas 3 : $1 \notin B$ et $2 \in B$.
     Les seules issues vérifiant $X(\omega) \in B$ sont celles pour lesquelles $X(\omega) = 2$.
     Ainsi, $X^{-1}(B) = \{c, d\}$. Par définition de la tribu donnée, on a bien $\{c, d\} \in \mathcal{F}$.
   - Cas 4 : $1 \in B$ et $2 \in B$.
     Toutes les issues vérifient $X(\omega) \in B$. L'image réciproque est $X^{-1}(B) = \{a, b, c, d\} = \Omega$.
     Puisque $\mathcal{F}$ est une tribu, $\Omega \in \mathcal{F}$.
4. Conclusion : Dans tous les cas possibles, pour n'importe quel borélien $B$, $X^{-1}(B) \in \mathcal{F}$. Par conséquent, la fonction $X$ est bien une application mesurable, et donc une variable aléatoire réelle sur l'espace $(\Omega, \mathcal{F})$.
