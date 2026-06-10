# Exercice 6 - Difficulté: Niveau 3.5

## 1. Énoncé
Démontrer par l'absurde que $\log_2(3)$ est irrationnel.

## 2. Démonstration (Zéro Ellipse)
Par l'absurde, supposons que $\log_2(3) \in \mathbb{Q}$. Alors il existe $p, q \in \mathbb{N}^*$ (car le log est positif) tels que $\log_2(3) = \frac{p}{q}$. Donc $2^{\frac{p}{q}} = 3$. En élevant à la puissance $q$, on obtient $2^p = 3^q$. C'est une égalité entre entiers. $2^p$ est un nombre pair. $3^q$ est un nombre impair. Un nombre pair ne peut pas être égal à un nombre impair, d'où contradiction. $\log_2(3)$ est donc irrationnel.
