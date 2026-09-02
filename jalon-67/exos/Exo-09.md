# Exo 09 : Continuité croissante de la mesure par Beppo Levi ($\bigstar$\bigstar$\bigstar$\bigstar$\bigstar$)

## Énoncé
Soit $(A_n)_{n \in \mathbb{N}}$ une suite croissante d'ensembles mesurables, c'est-à-dire $A_n \subset A_{n+1}$.
On pose $A = \bigcup_{n \in \mathbb{N}} A_n$.
Démontrer que $\lim_{n \to \infty} \mu(A_n) = \mu(A)$ en n'utilisant *que* le théorème de Beppo Levi.

## Correction Détaillée
**Étape 1 : Formulation avec les indicatrices**
Considérons les fonctions indicatrices $f_n(x) = \mathbf{1}_{A_n}(x)$.
Par définition, l'intégrale de Lebesgue d'une fonction indicatrice donne la mesure de l'ensemble :
$$ \int_X f_n \, d\mu = \mu(A_n) $$

**Étape 2 : Vérification des hypothèses du TCM**
- **Positivité :** Pour tout $x$, $f_n(x) \in \{0, 1\}$, donc $f_n(x) \ge 0$.
- **Croissance :** Puisque $A_n \subset A_{n+1}$, si $x \in A_n$ alors $x \in A_{n+1}$. Cela implique que $\mathbf{1}_{A_n}(x) \le \mathbf{1}_{A_{n+1}}(x)$. La suite $(f_n)$ est donc une suite de fonctions croissantes.

**Étape 3 : Limite simple des fonctions indicatrices**
Quelle est la limite de $f_n(x)$ lorsque $n \to \infty$ ?
Soit $x \in X$.
- S'il existe un rang $N$ tel que $x \in A_N$, alors pour tout $n \ge N$, $x \in A_n$ (par croissance). Ainsi $f_n(x) = 1$ pour tout $n \ge N$, et la limite est $1$.
- S'il n'existe aucun rang $n$ tel que $x \in A_n$, alors pour tout $n$, $f_n(x) = 0$, et la limite est $0$.
Remarquons que "exister un $N$ tel que $x \in A_N$" équivaut exactement à dire que $x \in \bigcup_n A_n = A$.
Par conséquent, la limite simple de la suite $(f_n)$ est la fonction $f(x) = \mathbf{1}_A(x)$.

**Étape 4 : Application du TCM**
Par le théorème de convergence monotone, l'intégrale de la limite est la limite des intégrales :
$$ \int_X \lim_{n \to \infty} f_n \, d\mu = \lim_{n \to \infty} \int_X f_n \, d\mu $$
Ce qui se traduit par :
$$ \int_X \mathbf{1}_A \, d\mu = \lim_{n \to \infty} \mu(A_n) $$
Donc :
$$ \mu(A) = \lim_{n \to \infty} \mu(A_n) $$
Le théorème de continuité de la mesure n'est en fait qu'un cas très particulier du théorème de convergence monotone !
