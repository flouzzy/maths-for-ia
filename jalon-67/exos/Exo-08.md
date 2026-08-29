---
title: "Exercice 8 : Réciproque partielle : l'égalité n'implique pas la croissance"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 8 : Réciproque partielle : l'égalité n'implique pas la croissance

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Problème

Démontrer en fournissant un contre-exemple explicite qu'il existe une suite de fonctions mesurables positives $(f_n)$ non croissante telle que $\lim_{n \to \infty} \int f_n = \int \lim_{n \to \infty} f_n$.

## Démonstration et Résolution

### Étape 1 : Construction d'un contre-exemple géométrique simple
Considérons l'espace mesuré $([0,1], \mathcal{B}([0,1]), \lambda)$.
Définissons la suite de fonctions $f_n : [0,1] \to \mathbb{R}$ par :
$$ f_n(x) = x^n $$
Cette suite est trivialement composée de fonctions mesurables et strictement positives sur $(0,1]$.

### Étape 2 : Vérification de la non-croissance
Pour tout $x \in (0,1)$, $x < 1$. Multiplier par un nombre inférieur à 1 décroît la valeur absolue.
Donc $x^{n+1} < x^n$, c'est-à-dire $f_{n+1}(x) < f_n(x)$.
La suite est **strictement décroissante** sur $(0,1)$. L'hypothèse fondamentale du théorème de Beppo Levi (la croissance) est radicalement violée.

### Étape 3 : Limite ponctuelle et son intégrale
Pour $x \in [0,1)$, on a $\lim_{n \to \infty} x^n = 0$.
Pour $x = 1$, $\lim_{n \to \infty} 1^n = 1$.
La fonction limite $f$ est la fonction indicatrice du singleton $\{1\}$.
La mesure de Lebesgue d'un singleton est nulle : $\lambda(\{1\}) = 0$.
Par conséquent, l'intégrale de la fonction limite est nulle :
$$ \int_0^1 f(x) dx = \int_0^1 \mathbf{1}_{\{1\}}(x) dx = 0 $$

### Étape 4 : Limite de l'intégrale
Calculons l'intégrale de $f_n$ :
$$ \int_0^1 x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1} $$
En passant à la limite quand $n \to \infty$ :
$$ \lim_{n \to \infty} \int_0^1 f_n(x) dx = \lim_{n \to \infty} \frac{1}{n+1} = 0 $$

### Étape 5 : Conclusion
Les deux valeurs coïncident : $0 = 0$. L'égalité de l'interversion limite/intégrale tient parfaitement, pourtant la suite est décroissante. Cela prouve que la monotonie croissante est une condition suffisante (théorème direct) mais nullement une condition nécessaire (réciproque fausse).
