## Mesurabilité par composition (continue $\circ$ mesurable) \quad $\bigstar\bigstar\star\star\star$

Soit $(X, \mathcal{F})$ un espace mesurable. Soit $f : X \to \mathbb{R}$ une fonction mesurable. Soit $g : \mathbb{R} \to \mathbb{R}$ une fonction continue.
Démontrez que la composition $h = g \circ f : X \to \mathbb{R}$ est mesurable.

### Correction Détaillée

Pour prouver que $h$ est mesurable, il suffit de montrer que pour tout ouvert $O \subset \mathbb{R}$, son image réciproque $h^{-1}(O) \in \mathcal{F}$. (En effet, la tribu borélienne $\mathcal{B}(\mathbb{R})$ est engendrée par les ouverts).

Soit $O$ un ouvert de $\mathbb{R}$.
Calculons l'image réciproque de $O$ par $h$ :
$$ h^{-1}(O) = (g \circ f)^{-1}(O) = f^{-1}(g^{-1}(O)) $$

Analysons cet ensemble pas à pas :
1. Puisque $g$ est continue et $O$ est un ouvert de $\mathbb{R}$, par définition topologique de la continuité, l'image réciproque $g^{-1}(O)$ est un ouvert de $\mathbb{R}$.
2. Tout ouvert de $\mathbb{R}$ est un borélien. Donc $g^{-1}(O) \in \mathcal{B}(\mathbb{R})$. Posons $B = g^{-1}(O)$.
3. Nous devons évaluer $f^{-1}(B)$ où $B \in \mathcal{B}(\mathbb{R})$.
4. Puisque $f$ est une fonction mesurable (par hypothèse), l'image réciproque de tout borélien appartient à $\mathcal{F}$. Ainsi, $f^{-1}(B) \in \mathcal{F}$.

Par conséquent, $h^{-1}(O) = f^{-1}(g^{-1}(O)) \in \mathcal{F}$.
Puisque cela est vrai pour tout ouvert $O$, la composition $h = g \circ f$ est mesurable.
