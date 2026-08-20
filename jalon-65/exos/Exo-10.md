## L'invariance par translation est préservée \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction mesurable pour la tribu de Borel. Soit $h \in \mathbb{R}$ un réel.
Démontrez formellement que la fonction translatée $f_h(x) = f(x - h)$ est également mesurable.

### Correction Détaillée

Soit $f_h : x \mapsto f(x - h)$. On peut la voir comme la composée $f_h = f \circ \tau_h$ où $\tau_h(x) = x - h$ est la fonction de translation.

Pour démontrer que $f_h$ est mesurable, il suffit de démontrer que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, $f_h^{-1}(B) \in \mathcal{B}(\mathbb{R})$.
Soit $B \in \mathcal{B}(\mathbb{R})$.
Calculons l'image réciproque :
$$ f_h^{-1}(B) = (f \circ \tau_h)^{-1}(B) = \tau_h^{-1}(f^{-1}(B)) $$

1. Puisque $f$ est mesurable, l'ensemble $A = f^{-1}(B)$ est un borélien ($A \in \mathcal{B}(\mathbb{R})$).
2. Nous devons évaluer $\tau_h^{-1}(A)$.
   Par définition géométrique : $\tau_h(x) \in A \iff x - h \in A \iff x \in \{y + h \mid y \in A\}$.
   Donc $\tau_h^{-1}(A) = A + h$ (l'ensemble $A$ translaté de $h$).
3. Il nous reste à prouver que la translation d'un borélien est un borélien.
   La tribu borélienne $\mathcal{B}(\mathbb{R})$ est la plus petite tribu contenant tous les ouverts $\mathcal{O}$.
   La translation $x \mapsto x + h$ est un homéomorphisme (bijection continue d'inverse continu). Par conséquent, l'image d'un ouvert par une translation est un ouvert : si $O \in \mathcal{O}$, alors $O+h \in \mathcal{O}$.
   Considérons la collection $\mathcal{M} = \{E \subset \mathbb{R} \mid E-h \in \mathcal{B}(\mathbb{R})\}$.
   On vérifie aisément que $\mathcal{M}$ est une tribu :
   - $\emptyset - h = \emptyset \in \mathcal{B}(\mathbb{R})$, donc $\emptyset \in \mathcal{M}$.
   - Stabilité par complémentaire : $(\mathbb{R} \setminus E) - h = \mathbb{R} \setminus (E-h) \in \mathcal{B}(\mathbb{R})$.
   - Stabilité par union dénombrable : $(\bigcup E_n) - h = \bigcup (E_n - h) \in \mathcal{B}(\mathbb{R})$.
   Puisque $O-h \in \mathcal{O} \subset \mathcal{B}(\mathbb{R})$ pour tout ouvert $O$, la tribu $\mathcal{M}$ contient tous les ouverts.
   Or $\mathcal{B}(\mathbb{R})$ est la PLUS PETITE tribu contenant les ouverts, donc $\mathcal{B}(\mathbb{R}) \subset \mathcal{M}$.
   Cela signifie que pour tout borélien $E \in \mathcal{B}(\mathbb{R})$, son translaté $E+h \in \mathcal{B}(\mathbb{R})$.

Appliqué à $A = f^{-1}(B)$, on conclut que l'ensemble $f_h^{-1}(B) = A + h$ est un borélien.
Ainsi, $f_h$ est mesurable.
