# Exercice 7 : Dépendance continue du point fixe aux paramètres
**Niveau :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(X, d)$ un espace métrique complet et $(\Lambda, d_\Lambda)$ un espace des paramètres (métrique).
On considère une famille d'applications $(f_\lambda)_{\lambda \in \Lambda}$ de $X$ dans $X$, telle que :
- (Uniforme contraction) Il existe $k \in [0, 1[$ tel que pour tout $\lambda \in \Lambda$, et pour tous $x, y \in X$, $d(f_\lambda(x), f_\lambda(y)) \leq k \, d(x, y)$.
- (Régularité) Pour tout $x \in X$, l'application $\lambda \mapsto f_\lambda(x)$ est continue sur $\Lambda$.
Démontrer que l'application $\lambda \mapsto x^*_\lambda$, où $x^*_\lambda$ est l'unique point fixe de $f_\lambda$, est continue.

**Démonstration pas à pas :**
1. Soit $\lambda_0 \in \Lambda$ un paramètre fixé, et $x^*_{\lambda_0}$ son point fixe correspondant. Soit $\lambda \in \Lambda$ un paramètre perturbé, et $x^*_\lambda$ son point fixe associé.
2. Nous voulons majorer la distance $d(x^*_\lambda, x^*_{\lambda_0})$.
   Utilisons l'inégalité triangulaire en insérant le point $f_\lambda(x^*_{\lambda_0})$ :
   $d(x^*_\lambda, x^*_{\lambda_0}) = d(f_\lambda(x^*_\lambda), f_{\lambda_0}(x^*_{\lambda_0}))$
   $d(x^*_\lambda, x^*_{\lambda_0}) \leq d(f_\lambda(x^*_\lambda), f_\lambda(x^*_{\lambda_0})) + d(f_\lambda(x^*_{\lambda_0}), f_{\lambda_0}(x^*_{\lambda_0}))$.
3. Par la propriété d'uniforme contraction de la famille (qui est fondamentale ici), le premier terme se majore par $k \, d(x^*_\lambda, x^*_{\lambda_0})$ :
   $d(x^*_\lambda, x^*_{\lambda_0}) \leq k \, d(x^*_\lambda, x^*_{\lambda_0}) + d(f_\lambda(x^*_{\lambda_0}), f_{\lambda_0}(x^*_{\lambda_0}))$.
4. En soustrayant le premier terme des deux côtés, il vient :
   $(1 - k) d(x^*_\lambda, x^*_{\lambda_0}) \leq d(f_\lambda(x^*_{\lambda_0}), f_{\lambda_0}(x^*_{\lambda_0}))$.
5. Puisque $k < 1$, nous pouvons diviser par $1 - k > 0$ :
   $d(x^*_\lambda, x^*_{\lambda_0}) \leq \frac{1}{1 - k} d(f_\lambda(x^*_{\lambda_0}), f_{\lambda_0}(x^*_{\lambda_0}))$.
6. Utilisons l'hypothèse de continuité par rapport au paramètre. L'élément $x = x^*_{\lambda_0}$ étant fixé, la fonction $\lambda \mapsto f_\lambda(x^*_{\lambda_0})$ est continue en $\lambda_0$.
   Cela signifie que $\lim_{\lambda \to \lambda_0} d(f_\lambda(x^*_{\lambda_0}), f_{\lambda_0}(x^*_{\lambda_0})) = 0$.
7. Par le théorème d'encadrement des limites (les distances étant positives), l'inégalité obtenue à l'étape 5 entraîne inévitablement que :
   $\lim_{\lambda \to \lambda_0} d(x^*_\lambda, x^*_{\lambda_0}) = 0$.
   La fonction qui associe à un paramètre le point fixe du système dynamique contractant est donc globalement continue. C'est la base théorique garantissant qu'un entraînement perturbé de modèles de Deep Equilibrium converge vers une région proche de l'idéal théorique.
