---
uuid: "exo-55-07"
title: "Composantes connexes des matrices inversibles"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Composantes connexes des matrices inversibles

**Énoncé :**
Soit $GL_n(\mathbb{R})$ l'ensemble des matrices $n \times n$ inversibles à coefficients réels. Montrer que $GL_n(\mathbb{R})$ n'est pas connexe.

**Solution :**
1. Considérons l'application déterminant, $\det : M_n(\mathbb{R}) \to \mathbb{R}$. C'est une application polynomiale en les coefficients de la matrice, donc elle est continue.
2. Par définition, $GL_n(\mathbb{R}) = \{ A \in M_n(\mathbb{R}) \mid \det(A) \neq 0 \}$.
3. L'image de $GL_n(\mathbb{R})$ par le déterminant est l'ensemble $\mathbb{R}^* = \mathbb{R} \setminus \{0\}$.
4. Si $GL_n(\mathbb{R})$ était connexe, alors par le théorème de l'image continue d'un connexe, l'ensemble $\det(GL_n(\mathbb{R})) = \mathbb{R}^*$ devrait être connexe.
5. Or, nous savons que $\mathbb{R}^*$ n'est pas connexe (il est séparé par 0 en deux ouverts $]-\infty, 0[$ et $]0, +\infty[$).
6. Cette contradiction prouve que l'hypothèse de départ est fausse. Par conséquent, $GL_n(\mathbb{R})$ n'est pas connexe.
7. (Note additionnelle : On montre classiquement qu'il possède exactement deux composantes connexes : $GL_n^+(\mathbb{R})$ et $GL_n^-(\mathbb{R})$ définis par le signe du déterminant, qui elles, sont connexes par arcs).
