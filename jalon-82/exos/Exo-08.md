# Exercice 8 : Produit d'une distribution par une fonction C-infinie

\subsection*{Exercice 8 : Produit d'une distribution par une fonction C-infinie \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Soit $T \in \mathcal{D}'(\mathbb{R})$ et $\alpha \in C^\infty(\mathbb{R})$. Montrer que le produit $\alpha T$ défini par $\langle \alpha T, \phi \rangle = \langle T, \alpha \phi \rangle$ est une distribution.

**Démonstration pas à pas :**
1. **Action bien définie :** Pour $\phi \in \mathcal{D}(\mathbb{R})$, la fonction produit $\alpha \phi$ est le produit de deux fonctions $C^\infty$, donc elle est $C^\infty$.
   De plus, $\text{supp}(\alpha \phi) \subset \text{supp}(\phi)$, donc $\alpha \phi$ est à support compact. Ainsi $\alpha \phi \in \mathcal{D}(\mathbb{R})$, et l'action est bien définie.
2. **Linéarité :** Immédiate par la bilinéarité du produit et de la forme $T$.
3. **Continuité :** Supposons $\phi_n \xrightarrow{\mathcal{D}} 0$. Les supports des $\phi_n$ sont dans un compact commun $K$.
   Les supports des $\alpha \phi_n$ sont donc aussi dans $K$.
   Toute dérivée de $\alpha \phi_n$ fait intervenir la formule de Leibniz : $(\alpha \phi_n)^{(k)} = \sum_{j=0}^k \binom{k}{j} \alpha^{(j)} \phi_n^{(k-j)}$.
   Sur le compact $K$, les fonctions $\alpha^{(j)}$ sont bornées. Puisque toutes les dérivées de $\phi_n$ tendent uniformément vers 0 sur $K$, il en est de même pour $(\alpha \phi_n)^{(k)}$.
   Donc $\alpha \phi_n \xrightarrow{\mathcal{D}} 0$. Par la continuité de $T$, $\langle T, \alpha \phi_n \rangle \to 0$.
   La forme $\alpha T$ est bien continue. $\blacksquare$
