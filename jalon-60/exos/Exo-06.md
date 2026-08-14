# La propriété discriminatoire

### Énoncé $\quad \bigstar\bigstar\bigstar\bigstar\star$

Définir ce que signifie pour une fonction d'activation d'être discriminatoire et démontrer que la limite des fonctions discriminatoires contient les fonctions trigonométriques complexes.

### Démonstration Détaillée

Une fonction $\sigma$ est discriminatoire si $\int_{I_n} \sigma(w^T x + b) d\mu(x) = 0$ pour tous $w,b$ implique $\mu=0$. Cybenko démontre cela en montrant que l'espace vectoriel engendré par les fonctions $\sigma(w^T x + b)$ contient par passage à la limite les exponentielles complexes $x \mapsto e^{i w^T x}$. Par injectivité de la transformée de Fourier des mesures, la nullité de l'intégrale contre ces exponentielles impose $\mu = 0$.
