## Exercice 9 : Propriété de discrimination de la sigmoïde \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Montrer qu'une fonction continue $\sigma$ qui vérifie $\sigma(x) \to 1$ en $+\infty$ et $\sigma(x) \to 0$ en $-\infty$ est discriminatoire (esquisse de preuve).

**Correction :**
Soit $\mu$ une mesure telle que $\int \sigma(w^T x + b) d\mu(x) = 0$ pour tout $w, b$.
Pour $\lambda > 0$, posons $\sigma_\lambda(x) = \sigma(\lambda(w^T x + b))$.
Lorsque $\lambda \to +\infty$, par convergence dominée (puisque $\sigma$ est bornée et $\mu$ finie), $\sigma_\lambda(x)$ converge ponctuellement vers 1 si $w^T x + b > 0$, vers 0 si $w^T x + b < 0$, et vers $\sigma(0)$ si $w^T x + b = 0$.
La limite est donc (presque) la fonction indicatrice du demi-espace $H = \{x \mid w^T x + b > 0\}$.
En passant à la limite, on trouve que $\mu(H) = 0$ pour tout demi-espace ouvert.
Puisque l'ensemble des demi-espaces engendre la tribu borélienne, cela implique que la mesure $\mu$ s'annule sur tous les boréliens, donc $\mu = 0$. La fonction est donc discriminatoire.
