## Exercice 5 : Compacité de la sphère unité \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :** Démontrer que la sphère unité $S^{n-1} = \{x \in \mathbb{R}^n \mid \|x\|_2 = 1\}$ est un compact de $\mathbb{R}^n$.

**Correction Détaillée :**
Nous utilisons le théorème de Heine-Borel pour les espaces de dimension finie, qui stipule qu'une partie de $\mathbb{R}^n$ est compacte si et seulement si elle est fermée et bornée.
1. **Bornée :** Pour tout point $x \in S^{n-1}$, sa norme euclidienne est exactement $1$. La sphère est donc intégralement contenue dans la boule fermée centrée à l'origine et de rayon 1, $\bar{B}(0, 1)$. Elle est donc bornée.
2. **Fermée :** L'application norme $f : \mathbb{R}^n \to \mathbb{R}$ définie par $f(x) = \|x\|_2$ est une fonction continue (car 1-lipschitzienne par l'inégalité triangulaire inversée).
Le singleton $\{1\}$ est un fermé de $\mathbb{R}$.
Or, par définition, $S^{n-1} = f^{-1}(\{1\})$. L'image réciproque d'un fermé par une application continue étant fermée, $S^{n-1}$ est une partie fermée de $\mathbb{R}^n$.
Puisque $S^{n-1}$ est à la fois fermée et bornée dans l'espace euclidien de dimension finie $\mathbb{R}^n$, elle est compacte.