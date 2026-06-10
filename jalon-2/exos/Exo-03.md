# Exercice 3 - Difficulté: Niveau 2

## 1. Énoncé
Démontrer l'irrationalité de $\sqrt{3}$ par l'absurde.

## 2. Démonstration (Zéro Ellipse)
Par l'absurde, supposons que $\sqrt{3} \in \mathbb{Q}$. Alors il existe $p, q \in \mathbb{N}$ tels que $\sqrt{3} = \frac{p}{q}$ et $\text{pgcd}(p, q) = 1$. Élevons au carré : $3 = \frac{p^2}{q^2} \implies p^2 = 3q^2$. Donc $p^2$ est un multiple de 3. Puisque 3 est premier, $p$ est aussi un multiple de 3. Il existe $k \in \mathbb{N}$ tel que $p = 3k$. Alors $p^2 = (3k)^2 = 9k^2$. En substituant dans l'équation précédente : $9k^2 = 3q^2 \implies 3k^2 = q^2$. Donc $q^2$ est un multiple de 3. Puisque 3 est premier, $q$ est aussi un multiple de 3. Donc $p$ et $q$ sont tous deux multiples de 3. C'est une contradiction avec $\text{pgcd}(p, q) = 1$. Donc $\sqrt{3} \notin \mathbb{Q}$.
