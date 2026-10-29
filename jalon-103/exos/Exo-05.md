# Exercice 5 : Espace de Hardy

## Énoncé

Soit $H^2(\mathbb{D})$ l'espace de Hardy des fonctions analytiques sur le disque unité dont la série de Taylor $\sum a_n z^n$ vérifie $\sum |a_n|^2 < \infty$. Le produit scalaire est $\langle f, g \rangle = \sum a_n \overline{b_n}$. Évaluer $L_w(f) = f(w)$ pour $|w| < 1$.

*Niveau de difficulté :* $\bigstar\bigstar\bigstar\star\star$

## Correction

1. **Expression de l'évaluation :** $f(w) = \sum_{n=0}^\infty a_n w^n$.
2. **Continuité :** Par Cauchy-Schwarz, $|f(w)| \le (\sum |a_n|^2)^{1/2} (\sum |w|^{2n})^{1/2} = \|f\| \frac{1}{\sqrt{1-|w|^2}}$. Donc $L_w$ est continue.
3. **Théorème de Riesz :** Il existe $k_w \in H^2$ tel que $f(w) = \langle f, k_w \rangle$.
4. **Identification du noyau :** On a $\langle f, k_w \rangle = \sum a_n \overline{(k_w)_n}$. Or $f(w) = \sum a_n w^n$.
5. **Conclusion :** En identifiant terme à terme, on obtient $\overline{(k_w)_n} = w^n$, soit $(k_w)_n = \overline{w}^n$. La fonction représentant est $k_w(z) = \sum_{n=0}^\infty \overline{w}^n z^n = \frac{1}{1 - \overline{w}z}$, le fameux noyau de Szegő.
