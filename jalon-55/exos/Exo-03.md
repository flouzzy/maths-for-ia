---
uuid: "exo-55-03"
title: "Image continue d'un connexe"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 3 : Image continue d'un connexe

**Énoncé :**
Soit $f : X \to Y$ une application continue, où $X$ est connexe. Montrer que $f(X)$ est connexe.

**Solution :**
1. Considérons l'espace $f(X)$ muni de la topologie induite par $Y$.
2. Supposons par l'absurde que $f(X)$ n'est pas connexe. Il existe deux ouverts $U$ et $V$ de $Y$ tels que $(f(X) \cap U)$ et $(f(X) \cap V)$ forment une partition non triviale de $f(X)$.
3. Les ensembles $f^{-1}(U)$ et $f^{-1}(V)$ sont des ouverts de $X$ car $f$ est continue.
4. $f^{-1}(U) \cup f^{-1}(V) = f^{-1}(U \cup V) \supset f^{-1}(f(X)) = X$.
5. $f^{-1}(U) \cap f^{-1}(V) = f^{-1}(U \cap V)$. Or, sur l'image $f(X)$, $U$ et $V$ sont disjoints, ce qui signifie que l'intersection de leurs images réciproques dans $X$ est vide.
6. Comme $f(X) \cap U \neq \emptyset$ et $f(X) \cap V \neq \emptyset$, les images réciproques $f^{-1}(U)$ et $f^{-1}(V)$ sont non vides.
7. $X$ est donc partitionné par deux ouverts disjoints non vides, ce qui contredit la connexité de $X$. Ainsi, $f(X)$ est connexe.
