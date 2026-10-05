# Exercice 9 : Support d'une distribution
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
On dit qu'une distribution $T$ est nulle sur un ouvert $\Omega$ si pour toute $\varphi \in \mathcal{D}(\mathbb{R})$ dont le support est inclus dans $\Omega$, on a $\langle T, \varphi \rangle = 0$. Le support de $T$ est le complémentaire de la réunion de tous les ouverts où $T$ est nulle. Déterminer rigoureusement le support du Dirac $\delta_0$.

## Correction Détaillée
1. Soit un ouvert $\Omega \subset \mathbb{R}$ tel que $0 \notin \Omega$. Montrons que $\delta_0$ est nulle sur $\Omega$.
2. Soit $\varphi \in \mathcal{D}(\mathbb{R})$ telle que $\text{supp}(\varphi) \subset \Omega$.
3. Comme $0 \notin \Omega$, on a $0 \notin \text{supp}(\varphi)$. Or, par définition du support, en dehors de $\text{supp}(\varphi)$, la fonction $\varphi$ vaut rigoureusement $0$.
4. Ainsi, $\varphi(0) = 0$.
5. L'évaluation donne : $\langle \delta_0, \varphi \rangle = \varphi(0) = 0$. Donc $\delta_0$ est nulle sur $\Omega = \mathbb{R} \setminus \{0\}$.
6. Le complémentaire de cet ouvert est le singleton $\{0\}$. Le support de $\delta_0$ est donc inclus dans $\{0\}$.
7. Pour montrer que le support n'est pas l'ensemble vide, il faut prouver que $\delta_0$ n'est pas nulle sur tout ouvert contenant $0$.
8. Considérons un ouvert quelconque $U$ contenant $0$.
9. Construisons une fonction test "bosse" $\varphi_0 \in \mathcal{D}(\mathbb{R})$ telle que $\varphi_0(0) = 1$ et $\text{supp}(\varphi_0) \subset U$ (possible en adaptant la fonction $\rho$ de l'Exemple 1 du cours).
10. Pour cette fonction, $\langle \delta_0, \varphi_0 \rangle = \varphi_0(0) = 1 \neq 0$.
11. Donc $\delta_0$ n'est pas nulle sur $U$. Le point $0$ ne peut pas être retiré du support.
12. En conclusion, le support de la distribution $\delta_0$ est exactement le singleton $\{0\}$. C'est une distribution à support ponctuel.
