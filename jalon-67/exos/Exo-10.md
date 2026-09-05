# Exercice 10 : Mesure de comptage et Espérance en loi de Poisson \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $X$ une variable aléatoire suivant une loi de Poisson de paramètre $\lambda > 0$.
Retrouver $\mathbb{E}[X]$ en utilisant l'approche de la théorie de la mesure et le TCM.

**Solution Détaillée :**
1. L'espérance est définie formellement par l'intégrale de Lebesgue par rapport à la mesure de probabilité discrète : $\mathbb{E}[X] = \int_{\mathbb{N}} x dP(x)$.
2. Soit l'espace $(\mathbb{N}, \mathcal{P}(\mathbb{N}), \mu)$ où $\mu(\{k\}) = P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}$.
3. L'identité $\mathbb{E}[X]$ est l'intégrale de la fonction $f(k) = k$ par rapport à $\mu$.
4. On peut écrire $f(k) = \sum_{n=1}^\infty \mathbf{1}_{\{k \ge n\}}$.
5. Comme $\mathbf{1}_{\{k \ge n\}} \ge 0$, le corollaire du TCM permet d'échanger la somme et l'intégrale :
   $$ \mathbb{E}[X] = \int_{\mathbb{N}} \left( \sum_{n=1}^\infty \mathbf{1}_{\{k \ge n\}} \right) d\mu(k) = \sum_{n=1}^\infty \int_{\mathbb{N}} \mathbf{1}_{\{k \ge n\}} d\mu(k) $$
6. Or, $\int_{\mathbb{N}} \mathbf{1}_{\{k \ge n\}} d\mu(k) = \mu(\{k \ge n\}) = P(X \ge n)$.
7. Cette égalité célèbre s'appelle la formule de l'espérance par la queue de distribution.
8. On retrouve bien l'espérance classique. C'est une application puissante du fait que toute intégrale d'une fonction positive sur un espace mesuré est la somme des aires horizontales (intégrale de Lebesgue).
