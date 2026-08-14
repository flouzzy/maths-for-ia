# Évaluation de la densité

### Énoncé $\quad \bigstar\bigstar\bigstar\bigstar\star$

Soit $S$ le sous-espace engendré par l'architecture. Montrer que si la fermeture de $S$ pour la norme uniforme est strictement incluse dans $\mathcal{C}(I_n)$, alors il existe une mesure non triviale orthogonale à $S$.

### Démonstration Détaillée

Ceci est une application directe du théorème de Hahn-Banach (forme analytique) et du théorème de représentation de Riesz-Markov-Kakutani. Si $\bar{S} \neq \mathcal{C}(I_n)$, l'espace $\bar{S}$ est un sous-espace fermé propre. Par le corollaire de Hahn-Banach, il existe une forme linéaire continue $L \neq 0$ s'annulant sur $S$. Par le théorème de Riesz, $L(f) = \int_{I_n} f d\mu$ pour une mesure de Borel signée finie $\mu$. Ainsi, $\int \sigma(w^T x + b) d\mu(x) = 0$ pour tous $w, b$, ce qui contredit la propriété discriminatoire de la sigmoïde.
