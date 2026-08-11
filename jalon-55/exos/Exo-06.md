---
uuid: "exo-55-06"
title: "Connexité de R^n privé d'un point"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 6 : Connexité de R^n privé d'un point

**Énoncé :**
Montrer que pour tout $n \geq 2$, l'espace $\mathbb{R}^n \setminus \{0\}$ est connexe par arcs (et donc connexe). Pourquoi cela échoue-t-il pour $n = 1$ ?

**Solution :**
1. Soit $x, y \in \mathbb{R}^n \setminus \{0\}$ avec $n \geq 2$.
2. Si le segment de droite $[x, y]$ ne passe pas par l'origine, alors il constitue un chemin continu de $x$ à $y$ : $\gamma(t) = (1-t)x + ty \neq 0$ pour $t \in [0, 1]$.
3. Si le segment $[x, y]$ passe par l'origine (c'est-à-dire que $y = -\lambda x$ pour un $\lambda > 0$), on ne peut pas emprunter ce segment directement.
4. Cependant, comme $n \geq 2$, il existe un point $z \in \mathbb{R}^n$ tel que $z$ n'est pas colinéaire à $x$ (et donc ni à $y$).
5. Alors, les segments de droite $[x, z]$ et $[z, y]$ ne passent pas par l'origine.
6. Le chemin défini en parcourant d'abord le segment de $x$ à $z$, puis de $z$ à $y$ est un chemin continu dans $\mathbb{R}^n \setminus \{0\}$.
7. L'espace $\mathbb{R}^n \setminus \{0\}$ est donc connexe par arcs.
8. Pour $n=1$, l'espace est $\mathbb{R} \setminus \{0\} = ]-\infty, 0[ \cup ]0, +\infty[$. C'est l'union disjointe de deux ouverts non vides, donc ce n'est pas connexe (et donc pas connexe par arcs). L'astuce du point intermédiaire non colinéaire est impossible en dimension 1.
