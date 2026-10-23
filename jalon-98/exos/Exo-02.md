# Exercice 2 : Sous-linéarité et norme
$\bigstar\bigstar\star\star\star$

## Énoncé
Soit $E$ un espace vectoriel normé. On définit $p : E \to \mathbb{R}$ par $p(x) = \limsup_{n \to \infty} \|x/n\|^{1/n}$.
Est-ce que $p$ est une fonctionnelle sous-linéaire ? (On supposera que la limite supérieure existe toujours et vaut 1, ceci est un exemple formel pour manipuler les axiomes).
Soit plus simplement $q(x) = \sqrt{\|x\|}$. La fonctionnelle $q$ est-elle sous-linéaire ?

## Correction Détaillée
Étudions $q(x) = \sqrt{\|x\|}$.
Pour que $q$ soit sous-linéaire, elle doit vérifier l'homogénéité positive :
Pour $\lambda > 0$, $q(\lambda x) = \sqrt{\|\lambda x\|} = \sqrt{\lambda \|x\|} = \sqrt{\lambda} \sqrt{\|x\|} = \sqrt{\lambda} q(x)$.
Si $q$ était sous-linéaire, on aurait $q(\lambda x) = \lambda q(x)$.
Ceci imposerait $\sqrt{\lambda} = \lambda$ pour tout $\lambda > 0$, ce qui est faux (par exemple pour $\lambda = 4$).
Donc $q$ **n'est pas** une fonctionnelle sous-linéaire. $\blacksquare$
