# Exercice 4 - Difficulté: Niveau 2.5

## 1. Énoncé
Démontrer qu'il y a une infinité de nombres premiers par l'absurde.

## 2. Démonstration (Zéro Ellipse)
Par l'absurde, supposons qu'il y a un nombre fini de nombres premiers. Notons-les $p_1, p_2, \dots, p_n$. Considérons le nombre $N = p_1 p_2 \dots p_n + 1$. $N$ n'est pas premier car $N > p_i$ pour tout $i$. Donc $N$ a un diviseur premier $q$. Ce nombre $q$ doit être l'un des $p_i$, disons $p_k$. Donc $p_k$ divise $N$. Mais $p_k$ divise aussi $p_1 \dots p_n$. Donc $p_k$ divise $N - p_1 \dots p_n = 1$. C'est absurde, un nombre premier ne divise pas 1. Donc il y a une infinité de nombres premiers.
