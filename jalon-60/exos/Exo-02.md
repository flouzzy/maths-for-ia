# Approximation du sinus

### Énoncé $\quad \bigstar\bigstar\star\star\star$

Démontrer que le réseau de neurones à une couche cachée peut approcher $f(x) = \sin(x)$ sur $[0, 2\pi]$. Quelle est l'influence de la largeur de la couche (nombre de neurones) sur l'erreur d'approximation uniforme ?

### Démonstration Détaillée

La fonction sinus est lipschitzienne sur le compact $[0, 2\pi]$ (constante de Lipschitz $L=1$). En découpant le domaine en intervalles de taille $\delta$, on obtient une erreur d'approximation en escalier de $O(\delta)$. Le lissage par des sigmoïdes introduit une erreur additionnelle, qui peut être rendue arbitrairement petite pour un paramètre d'échelle $k \to \infty$. L'erreur décroît généralement de l'ordre de $O(1/\sqrt{N})$ pour $N$ neurones, ce qui illustre le compromis entre complexité du réseau et précision.
