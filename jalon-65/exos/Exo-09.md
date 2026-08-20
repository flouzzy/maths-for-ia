## Mesurabilité d'une fonction continue par morceaux \quad $\bigstar\bigstar\bigstar\bigstar\star$

Démontrez, en utilisant les axiomes de la théorie de la mesure, qu'une fonction définie sur un intervalle $[a,b]$ et continue par morceaux est nécessairement borélienne.

### Correction Détaillée

Soit $f : [a,b] \to \mathbb{R}$ une fonction continue par morceaux.
Par définition de la continuité par morceaux, il existe une subdivision finie de l'intervalle $[a,b]$ en $n$ points $x_0 = a < x_1 < \dots < x_n = b$ telle que sur chaque intervalle ouvert $I_k = ]x_{k-1}, x_k[$, la restriction $f_{|I_k}$ coïncide avec une fonction continue $g_k : [x_{k-1}, x_k] \to \mathbb{R}$, et $f$ admet des limites à gauche et à droite aux points $x_k$.

Posons $F_k = \{x_0, x_1, \dots, x_n\}$ l'ensemble fini des points de discontinuité potentielle.
$F_k$ est une union finie de singletons, donc un borélien.
Les intervalles $I_k$ sont ouverts, donc des boréliens. L'espace complet $[a,b]$ est partitionné par la réunion disjointe $F_k \cup \bigcup_{k=1}^n I_k$.

Soit $B \in \mathcal{B}(\mathbb{R})$ un borélien. Analysons $f^{-1}(B)$ :
$$ f^{-1}(B) = \{x \in [a,b] \mid f(x) \in B\} $$
On peut décomposer cet ensemble suivant la partition de notre domaine :
$$ f^{-1}(B) = \left( \bigcup_{k=1}^n \{x \in I_k \mid f(x) \in B\} \right) \cup \{x \in F_k \mid f(x) \in B\} $$
$$ f^{-1}(B) = \left( \bigcup_{k=1}^n (f_{|I_k}^{-1}(B)) \right) \cup (F_k \cap f^{-1}(B)) $$

1. L'ensemble $\{x \in F_k \mid f(x) \in B\}$ est un sous-ensemble d'un ensemble fini $F_k$. Tout sous-ensemble fini d'un borélien est un borélien.
2. Pour chaque intervalle ouvert $I_k$, la restriction $f_{|I_k}$ est continue. Or, toute fonction continue est borélienne. L'image réciproque $f_{|I_k}^{-1}(B)$ est donc l'intersection d'un borélien de la droite avec l'ouvert $I_k$, ce qui est formellement un borélien de $\mathbb{R}$.

Ainsi, $f^{-1}(B)$ est l'union finie de boréliens. C'est donc un borélien.
Puisque l'image réciproque de tout borélien est un borélien, la fonction $f$ est borélienne.
