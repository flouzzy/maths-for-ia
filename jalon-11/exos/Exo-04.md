# Exercice 4: Hyperplans et formes proportionnelles
## Énoncé
Soit $E = \mathbb{R}^3$ et sa base canonique $\mathcal{B} = (e_1, e_2, e_3)$. On considère les vecteurs :
$u_1 = (1, 1, 1)$, $u_2 = (1, 1, 0)$, $u_3 = (1, 0, 0)$
1. Montrer que $\mathcal{C} = (u_1, u_2, u_3)$ est une base de $E$.
2. Déterminer les formes linéaires constituant la base duale $\mathcal{C}^* = (u_1^*, u_2^*, u_3^*)$ exprimées dans la base duale $\mathcal{B}^* = (e_1^*, e_2^*, e_3^*)$.


## Correction détaillée
1. **Sens direct (proportionnalité implique même noyau) :**
   Supposons qu'il existe un scalaire $\lambda \neq 0$ tel que $\phi = \lambda \psi$.
   Soit $x \in \ker \phi$. Alors $\phi(x) = 0$, donc $\lambda \psi(x) = 0$. Comme $\lambda \neq 0$, on a $\psi(x) = 0$, donc $x \in \ker \psi$. Ainsi $\ker \phi \subset \ker \psi$.
   Symétriquement, $\psi = \frac{1}{\lambda} \phi$, ce qui donne $\ker \psi \subset \ker \phi$. Donc $\ker \phi = \ker \psi$.
2. **Sens réciproque (même noyau implique proportionnalité) :**
   Supposons que $\ker \phi = \ker \psi = H$. Comme $\phi \neq 0$, il existe un vecteur $e_0 \in E$ tel que $\phi(e_0) \neq 0$. Quitte à diviser par $\phi(e_0)$, on peut choisir $e_0$ tel que $\phi(e_0) = 1$.
3. **Décomposition d'un vecteur :** Soit $x \in E$ quelconque. Posons $x' = x - \phi(x)e_0$.
4. **Évaluation de $x'$ :** Évaluons $\phi$ en $x'$ :
   $$\phi(x') = \phi(x - \phi(x)e_0) = \phi(x) - \phi(x)\phi(e_0) = \phi(x) - \phi(x)(1) = 0$$
   Donc $x' \in \ker \phi$.
5. **Utilisation de l'égalité des noyaux :** Puisque $\ker \phi = \ker \psi$, on a nécessairement $x' \in \ker \psi$, ce qui implique $\psi(x') = 0$.
6. **Relation de proportionnalité :**
   $$\psi(x - \phi(x)e_0) = 0 \implies \psi(x) - \phi(x)\psi(e_0) = 0 \implies \psi(x) = \psi(e_0)\phi(x)$$
   Ceci étant vrai pour tout $x \in E$, en posant $\lambda = \psi(e_0)$, on obtient l'égalité des formes linéaires $\psi = \lambda \phi$.
7. **Conclusion :** Les deux formes linéaires sont proportionnelles.

$\blacksquare$
