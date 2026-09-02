# Exercice 3 : Intégrale de l'indicatrice d'une union infinie ★★

## Énoncé
Soit $(A_n)$ une suite d'ensembles mesurables disjoints. Soit $f_n = \sum_{k=1}^n \mathbf{1}_{A_k}$.
Calculer la limite de l'intégrale de $f_n$.

## Correction Détaillée
1. **Croissance** : $f_{n+1} - f_n = \mathbf{1}_{A_{n+1}} \ge 0$. La suite est croissante.
2. **Limite simple** : La limite de $f_n$ est $\mathbf{1}_{\bigcup_{k=1}^\infty A_k}$ car les ensembles sont disjoints.
3. **Application du TCM** : $\int \lim f_n d\mu = \int \mathbf{1}_{\bigcup A_k} d\mu = \mu(\bigcup_{k=1}^\infty A_k)$.
4. **Égalité** : Par le TCM, c'est aussi égal à $\lim_{n \to \infty} \int f_n d\mu = \lim_{n \to \infty} \sum_{k=1}^n \mu(A_k) = \sum_{k=1}^\infty \mu(A_k)$.
5. **Conclusion** : On retrouve la propriété d'additivité dénombrable de la mesure.
