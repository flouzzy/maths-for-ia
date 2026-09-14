# Exercice 10 : Produit infini de mesures de probabilité (Esquisse) (★★★★★)

**Énoncé :**
Un espace mesuré fondamental pour modéliser une suite infinie de lancers de pièces est le produit cartésien dénombrable $\Omega = \{0, 1\}^{\mathbb{N}^*}$.
On munit chaque facteur $\{0,1\}$ de la tribu des parties, et de la mesure de probabilité $p(\{1\}) = p, p(\{0\}) = 1-p$ (avec $p \in ]0,1[$).
La tribu sur $\Omega$ est engendrée par les "cylindres" (les événements dépendant d'un nombre fini de lancers).
On admet qu'il existe une unique mesure produit sur $\Omega$, notée $\mathbb{P}$.
Soit $E_n = \{\omega \in \Omega \mid \omega_n = 1\}$ l'événement "le n-ième lancer est un 1".
Montrer que pour tout $N \in \mathbb{N}^*$ et toute séquence de lancers $(x_1, \dots, x_N) \in \{0, 1\}^N$, on retrouve la loi binomiale par le calcul de l'intersection des événements $E_k$.

**Correction :**
1. L'ensemble fondamental décrivant un résultat exact sur les $N$ premiers lancers est $C = \bigcap_{i=1}^N A_i$ où $A_i = E_i$ si $x_i = 1$ et $A_i = E_i^c$ si $x_i = 0$.
2. Géométriquement, l'ensemble $C$ est un "rectangle mesurable" (un cylindre) de l'espace produit car il s'écrit comme :
   $C = \{x_1\} \times \{x_2\} \times \dots \times \{x_N\} \times \Omega_{N+1} \times \dots$ où $\Omega_k = \{0, 1\}$ pour $k > N$.
3. Par définition de la mesure produit (étendue au cas infini, souvent appelée mesure de Kolmogorov sur les cylindres), la mesure du produit est le produit des mesures marginales :
   $\mathbb{P}(C) = p(x_1) p(x_2) \dots p(x_N) \times 1 \times 1 \dots$
   Si on a $k$ succès ($x_i=1$) et $N-k$ échecs ($x_i=0$) parmi ces $N$ valeurs fixées, le produit vaut $p^k (1-p)^{N-k}$.
4. Pour retrouver la loi Binomiale, il s'agit de s'intéresser à l'événement $B_k =$ "obtenir exactement $k$ succès lors des $N$ premiers lancers". $B_k$ est l'union disjointe de tous les cylindres $C$ ayant $k$ composantes valant $1$.
   Il y a $\binom{N}{k}$ cylindres de ce type. Comme ils sont disjoints, la $\sigma$-additivité donne :
   $\mathbb{P}(B_k) = \sum \mathbb{P}(C) = \binom{N}{k} p^k (1-p)^{N-k}$.
   La mesure produit permet de construire rigoureusement l'espace des possibles et les probabilités pour une infinité d'expériences aléatoires indépendantes.
