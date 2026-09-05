# Exercice 5 : Mesure de comptage et inversion de doubles sommes
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

### Énoncé

Soit $(a_{i,j})_{(i,j) \in \mathbb{N}^2}$ une suite double de nombres réels positifs. En utilisant le Théorème de Convergence Monotone avec la mesure de comptage, démontrer que $\sum_{i=0}^{+\infty} \sum_{j=0}^{+\infty} a_{i,j} = \sum_{j=0}^{+\infty} \sum_{i=0}^{+\infty} a_{i,j}$.

---
### Correction détaillée

1. Considérons l'espace mesurable $(\mathbb{N}, \mathcal{P}(\mathbb{N}), \mu)$ où $\mu$ est la mesure de comptage (pour tout $A \subset \mathbb{N}$, $\mu(A) = \text{card}(A)$).
2. Toute fonction $f: \mathbb{N} \to \mathbb{R}$ correspond à une suite $(f(i))_{i \in \mathbb{N}}$. L'intégrale par rapport à $\mu$ est la somme de la série : $\int_{\mathbb{N}} f \, d\mu = \sum_{i=0}^{+\infty} f(i)$.
3. Posons $u_j(i) = a_{i,j}$ pour $(i,j) \in \mathbb{N}^2$. Les $u_j$ sont des fonctions mesurables positives sur $\mathbb{N}$.
4. Le corollaire du Théorème de Convergence Monotone stipule que pour une suite de fonctions mesurables positives :
   $$\int_{\mathbb{N}} \left( \sum_{j=0}^{+\infty} u_j \right) d\mu = \sum_{j=0}^{+\infty} \int_{\mathbb{N}} u_j \, d\mu$$
5. Évaluons le terme de gauche. Soit $S(i) = \sum_{j=0}^{+\infty} u_j(i) = \sum_{j=0}^{+\infty} a_{i,j}$. L'intégrale de $S$ par rapport à $\mu$ est la somme sur $i$ de la fonction $S$ :
   $$\int_{\mathbb{N}} S \, d\mu = \sum_{i=0}^{+\infty} S(i) = \sum_{i=0}^{+\infty} \left( \sum_{j=0}^{+\infty} a_{i,j} \right)$$
6. Évaluons le terme de droite. L'intégrale de chaque $u_j$ par rapport à $\mu$ est $\sum_{i=0}^{+\infty} u_j(i) = \sum_{i=0}^{+\infty} a_{i,j}$. La somme sur $j$ de ces intégrales donne :
   $$\sum_{j=0}^{+\infty} \int_{\mathbb{N}} u_j \, d\mu = \sum_{j=0}^{+\infty} \left( \sum_{i=0}^{+\infty} a_{i,j} \right)$$
7. Par l'égalité établie au point 4, nous avons l'inversion inconditionnelle des doubles sommes :
   $$\sum_{i=0}^{+\infty} \sum_{j=0}^{+\infty} a_{i,j} = \sum_{j=0}^{+\infty} \sum_{i=0}^{+\infty} a_{i,j}$$
Cette démonstration extrêmement élégante révèle la puissance unificatrice de la théorie de la mesure, qui traite les séries discrètes et les intégrales continues dans un cadre abstrait unique.
