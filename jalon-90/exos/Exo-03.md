# Exercice 3 : L'exemple de la masse glissante

Niveau : $\bigstar\bigstar\star\star\star$

Sur l'espace mesuré $(\Omega, \mathcal{F}, \mathbb{P}) = (]0, 1], \mathcal{B}(]0, 1]), \lambda)$, on pose $X_n(\omega) = n \mathbb{1}_{\left]0, \frac{1}{n}\right]}(\omega)$.
1. Montrer que $X_n \xrightarrow{\text{p.s.}} 0$.
2. Étudier la convergence dans $L^1$ de la suite $(X_n)$. Que remarque-t-on ?

## Correction

**1. Convergence presque sûre vers 0 :**
Soit $\omega \in ]0, 1]$. Il existe un rang $N_\omega \in \mathbb{N}^*$ tel que pour tout $n \ge N_\omega$, on a $\frac{1}{n} < \omega$.
Pour tout $n \ge N_\omega$, on a donc $\omega \notin \left]0, \frac{1}{n}\right]$.
Par définition de la fonction indicatrice, cela signifie que pour tout $n \ge N_\omega$, $\mathbb{1}_{\left]0, \frac{1}{n}\right]}(\omega) = 0$.
D'où, pour tout $n \ge N_\omega$, $X_n(\omega) = n \times 0 = 0$.
La suite numérique $(X_n(\omega))$ est donc stationnaire à 0 à partir d'un certain rang, elle converge donc vers $0$.
Ceci étant vrai pour tout $\omega \in ]0, 1]$, on a $X_n \xrightarrow{\text{p.s.}} 0$ (ici, l'ensemble de convergence est tout l'univers, de mesure 1).

**2. Étude de la convergence dans $L^1$ :**
Évaluons $\mathbb{E}[|X_n - 0|] = \mathbb{E}[X_n]$ puisque $X_n \ge 0$.
$$\mathbb{E}[X_n] = \int_0^1 n \mathbb{1}_{\left]0, \frac{1}{n}\right]}(\omega) d\lambda(\omega) = n \lambda\left(\left]0, \frac{1}{n}\right]\right) = n \times \frac{1}{n} = 1$$
La suite $\mathbb{E}[|X_n - 0|]$ est constante et égale à 1. Elle ne tend donc pas vers 0.
Ainsi, $(X_n)$ ne converge pas vers $0$ dans $L^1$.
**Remarque :** Cet exercice illustre le fait que la convergence presque sûre n'implique pas la convergence dans $L^p$. La masse se concentre vers 0 en devenant infinie, ce qui empêche l'espérance de l'erreur de tendre vers 0. On ne peut pas appliquer le théorème de convergence dominée de Lebesgue car il n'existe pas de variable aléatoire intégrable $Y$ telle que $|X_n| \le Y$ pour tout $n$.
