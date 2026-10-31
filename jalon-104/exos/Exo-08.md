# Exercice 8 : Produit tensoriel et base de L^2(R^2) $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(e_n(x))_{n \in \mathbb{N}}$ une base hilbertienne de $L^2(\mathbb{R})$.
Pour tout $(n, m) \in \mathbb{N}^2$, on définit la fonction de deux variables $\phi_{n,m}(x,y) = e_n(x) e_m(y)$.
Démontrer que la famille $(\phi_{n,m})_{(n,m) \in \mathbb{N}^2}$ forme une famille orthonormée dans $H = L^2(\mathbb{R}^2)$. (On admettra qu'elle forme une base hilbertienne).

**Correction détaillée :**
Pour montrer que la famille est orthonormée, il faut calculer le produit scalaire dans $L^2(\mathbb{R}^2)$ pour deux paires d'indices $(n, m)$ et $(k, l)$ :
$$ \langle \phi_{n,m}, \phi_{k,l} \rangle_{L^2(\mathbb{R}^2)} = \iint_{\mathbb{R}^2} \phi_{n,m}(x,y) \overline{\phi_{k,l}(x,y)} dx dy $$
En remplaçant par les définitions :
$$ \langle \phi_{n,m}, \phi_{k,l} \rangle = \iint_{\mathbb{R}^2} e_n(x) e_m(y) \overline{e_k(x) e_l(y)} dx dy $$
Par le théorème de Fubini, puisque les fonctions sont séparables et les intégrales sont dans $L^2$, on peut séparer l'intégrale double en le produit de deux intégrales simples :
$$ \langle \phi_{n,m}, \phi_{k,l} \rangle = \left( \int_{\mathbb{R}} e_n(x) \overline{e_k(x)} dx \right) \times \left( \int_{\mathbb{R}} e_m(y) \overline{e_l(y)} dy \right) $$
On reconnaît les produits scalaires dans $L^2(\mathbb{R})$ :
$$ \langle \phi_{n,m}, \phi_{k,l} \rangle = \langle e_n, e_k \rangle_{L^2(\mathbb{R})} \times \langle e_m, e_l \rangle_{L^2(\mathbb{R})} $$
Or, la famille $(e_n)$ est une base hilbertienne de $L^2(\mathbb{R})$, elle est donc en particulier orthonormée.
Ainsi, $\langle e_n, e_k \rangle = \delta_{nk}$ et $\langle e_m, e_l \rangle = \delta_{ml}$.
Par conséquent :
$$ \langle \phi_{n,m}, \phi_{k,l} \rangle = \delta_{nk} \delta_{ml} $$
Cette quantité vaut 1 si et seulement si $n = k$ et $m = l$ simultanément. Dans tous les autres cas, elle vaut 0.
La famille $(\phi_{n,m})$ est donc bien une famille orthonormée de l'espace de Hilbert $L^2(\mathbb{R}^2)$.
