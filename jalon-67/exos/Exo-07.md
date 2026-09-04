# Exercice 07 : Contre-exemple avec la mesure de comptage ($\bigstar$$\bigstar$$\bigstar$$\bigstar$$\star$)

## Énoncé

Dans $(\mathbb{N}, \mathcal{P}(\mathbb{N}), \mu)$ où $\mu$ est la mesure de comptage, trouver une suite $(f_n)$ de fonctions positives qui converge vers 0, mais telle que $\lim \int f_n \neq 0$. Pourquoi Beppo Levi ne s'applique-t-il pas ?

## Correction Détaillée

1. **L'espace mesuré :** L'intégrale par rapport à la mesure de comptage sur $\mathbb{N}$ n'est autre que la somme de la série : $\int_{\mathbb{N}} f \,d\mu = \sum_{k \in \mathbb{N}} f(k)$.
2. **Construction de $(f_n)$ :** Soit $f_n(k) = \mathbf{1}_{\{n\}}(k)$. La fonction $f_n$ vaut 1 au point $n$ et 0 partout ailleurs.
3. **Limite simple :** Pour tout $k$ fixé, il existe un rang $N > k$ (en l'occurrence $N = k+1$). Pour tout $n \ge N$, $f_n(k) = 0$. Donc la limite simple de la suite est la fonction nulle : $f(k) = \lim_{n \to \infty} f_n(k) = 0$.
4. **Intégrale de la limite :** $\int_{\mathbb{N}} f \,d\mu = \sum_{k \in \mathbb{N}} 0 = 0$.
5. **Limite des intégrales :** Pour tout $n$, $\int_{\mathbb{N}} f_n \,d\mu = \sum_{k \in \mathbb{N}} \mathbf{1}_{\{n\}}(k) = 1$. Donc $\lim_{n \to \infty} \int_{\mathbb{N}} f_n \,d\mu = 1$.
6. **Inégalité :** On a bien $\int \lim f_n = 0 \neq 1 = \lim \int f_n$.
7. **Analyse de Beppo Levi :** Le théorème ne s'applique pas car la suite $(f_n)$ n'est pas croissante. Par exemple, pour $k=1$, la suite $f_n(1)$ prend les valeurs $0, 1, 0, 0, \dots$ ce qui n'est pas croissant.
