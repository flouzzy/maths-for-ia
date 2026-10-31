# Exercice 9 : Construction de la base de Haar $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
La fonction ondelette mère de Haar est définie sur $\mathbb{R}$ par :
$$ \psi(t) = \begin{cases} 1 & \text{si } 0 \leq t < 1/2 \\ -1 & \text{si } 1/2 \leq t < 1 \\ 0 & \text{sinon} \end{cases} $$
Pour tout entier $j \in \mathbb{Z}$ et $k \in \mathbb{Z}$, on définit $\psi_{j,k}(t) = 2^{j/2} \psi(2^j t - k)$.
Démontrer que la famille $(\psi_{j,k})_{j,k \in \mathbb{Z}}$ est une famille orthonormée de $L^2(\mathbb{R})$.

**Correction détaillée :**
1. **Norme unitaire :** Calculons $\|\psi_{j,k}\|^2$.
   $\|\psi_{j,k}\|^2 = \int_{-\infty}^{+\infty} |2^{j/2} \psi(2^j t - k)|^2 dt = 2^j \int_{-\infty}^{+\infty} |\psi(2^j t - k)|^2 dt$
   Effectuons le changement de variable $u = 2^j t - k \implies du = 2^j dt \implies dt = 2^{-j} du$.
   $\|\psi_{j,k}\|^2 = 2^j \int_{-\infty}^{+\infty} |\psi(u)|^2 2^{-j} du = \int_{-\infty}^{+\infty} |\psi(u)|^2 du$
   Or, $|\psi(u)| = 1$ sur $[0, 1]$ et $0$ ailleurs. Donc $\|\psi_{j,k}\|^2 = \int_0^1 1^2 du = 1$.

2. **Orthogonalité pour des translations de même échelle ($j = j'$ et $k \neq k'$) :**
   $\langle \psi_{j,k}, \psi_{j,k'} \rangle = \int_{-\infty}^{+\infty} 2^j \psi(2^j t - k) \psi(2^j t - k') dt$
   Avec le même changement de variable $u = 2^j t - k$ :
   $\langle \psi_{j,k}, \psi_{j,k'} \rangle = \int_{-\infty}^{+\infty} \psi(u) \psi(u + k - k') du$
   Le support de $\psi(u)$ est $[0, 1]$. Le support de $\psi(u + k - k')$ est $[-k+k', -k+k'+1]$.
   Puisque $k \neq k'$ sont des entiers, $|k - k'| \geq 1$. L'intersection des supports est de mesure nulle. Le produit des fonctions est presque partout nul.
   Donc $\langle \psi_{j,k}, \psi_{j,k'} \rangle = 0$.

3. **Orthogonalité pour des échelles différentes ($j \neq j'$) :**
   Supposons sans perte de généralité que $j > j'$. L'ondelette $\psi_{j,k}$ oscille beaucoup plus vite (échelle "fine") que $\psi_{j',k'}$ (échelle "grossière").
   Le support de $\psi_{j,k}$ est l'intervalle $I = [k 2^{-j}, (k+1) 2^{-j}]$, qui est de longueur $2^{-j}$.
   Le support de $\psi_{j',k'}$ est un intervalle de longueur $2^{-j'}$, qui est strictement plus grand car $j > j'$.
   Sur l'intervalle $I$, la fonction $\psi_{j',k'}$ est constante. En effet, elle ne change de valeur qu'à ses bornes ou en son milieu. Or, les bornes de $\psi_{j,k}$ sont contenues dans les intervalles où $\psi_{j',k'}$ est constante.
   Soit $c$ cette valeur constante sur $I$. Alors :
   $\langle \psi_{j,k}, \psi_{j',k'} \rangle = \int_I \psi_{j,k}(t) c dt = c 2^{j/2} \int_{k 2^{-j}}^{(k+1) 2^{-j}} \psi(2^j t - k) dt$
   Avec $u = 2^j t - k$, $du = 2^j dt$ :
   $\langle \psi_{j,k}, \psi_{j',k'} \rangle = c 2^{-j/2} \int_0^1 \psi(u) du$
   Or, par définition de $\psi$, son intégrale sur $[0, 1]$ est nulle :
   $\int_0^1 \psi(u) du = \int_0^{1/2} 1 du + \int_{1/2}^1 (-1) du = \frac{1}{2} - \frac{1}{2} = 0$.
   Donc $\langle \psi_{j,k}, \psi_{j',k'} \rangle = 0$.
   La famille est bien orthonormée.
