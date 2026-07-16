---
titre: "Exercice 7 : Dérivabilité"
difficulte: "★★★★☆"
---

# Exercice 7 : Pratique et maîtrise conceptuelle

**Énoncé :**
Soit $f$ de classe $\mathcal{C}^1$ sur $[a,b]$. Démontrer le lemme de Riemann-Lebesgue pour une phase linéaire : $\lim_{\lambda \to \infty} \int_a^b f(t) \sin(\lambda t) dt = 0$.

**Résolution Zéro Ellipse :**
1. La régularité $\mathcal{C}^1$ de $f$ incite naturellement à utiliser une intégration par parties.
2. Posons $u(t) = f(t) \implies u'(t) = f'(t)$ et $v'(t) = \sin(\lambda t) \implies v(t) = -\frac{\cos(\lambda t)}{\lambda}$.
3. Appliquons la formule d'intégration par parties :
   $\int_a^b f(t) \sin(\lambda t) dt = \left[ -f(t) \frac{\cos(\lambda t)}{\lambda} \right]_a^b + \int_a^b f'(t) \frac{\cos(\lambda t)}{\lambda} dt$.
4. Évaluons le terme tout intégré :
   $\left[ -f(t) \frac{\cos(\lambda t)}{\lambda} \right]_a^b = \frac{f(a)\cos(\lambda a) - f(b)\cos(\lambda b)}{\lambda}$.
5. Puisque $f$ est continue sur un compact, elle est bornée. Le numérateur est borné indépendamment de $\lambda$. Ainsi, ce terme tend vers $0$ lorsque $\lambda \to \infty$.
6. Majorons le terme intégral restant en utilisant la valeur absolue :
   $| \int_a^b f'(t) \frac{\cos(\lambda t)}{\lambda} dt | \leq \int_a^b \frac{|f'(t)| \cdot |\cos(\lambda t)|}{\lambda} dt \leq \frac{1}{\lambda} \int_a^b |f'(t)| dt$.
7. Puisque $f \in \mathcal{C}^1$, sa dérivée $f'$ est continue, donc l'intégrale $\int_a^b |f'(t)| dt$ est une constante finie fixée $K$.
8. La majoration devient $K / \lambda$, qui tend inexorablement vers $0$ lorsque $\lambda \to \infty$.
9. La somme des limites nulles certifie le résultat. $\blacksquare$
