# Exercice 10 : Lemme de Fatou comme conséquence de Beppo Levi ($\bigstar$$\bigstar$$\bigstar$$\bigstar$$\bigstar$)

## Énoncé

En utilisant uniquement le théorème de convergence monotone, démontrer le Lemme de Fatou : $\int_X \liminf f_n \le \liminf \int_X f_n$.

## Correction Détaillée

1. **Définition de la limite inférieure :** Pour une suite de fonctions positives $(f_n)$, on définit la limite inférieure ponctuelle :
   $$ g(x) = \liminf_{n \to \infty} f_n(x) = \lim_{n \to \infty} \left( \inf_{k \ge n} f_k(x) \right) $$
2. **Construction d'une suite croissante :** Posons $g_n(x) = \inf_{k \ge n} f_k(x)$.
   Pour chaque $x$, l'ensemble des indices $\{k \ge n+1\}$ est inclus dans l'ensemble $\{k \ge n\}$. Le borne inférieure sur le premier ensemble est donc supérieure ou égale à la borne inférieure sur le second :
   $$ g_n(x) \le g_{n+1}(x) $$
   La suite $(g_n)$ est donc une suite croissante de fonctions mesurables positives.
3. **Application de Beppo Levi :** La limite de la suite $(g_n)$ est précisément la fonction $g$. Le théorème de convergence monotone s'applique rigoureusement :
   $$ \int_X \lim_{n \to \infty} g_n \,d\mu = \lim_{n \to \infty} \int_X g_n \,d\mu $$
   C'est-à-dire : $\int_X (\liminf f_n) \,d\mu = \lim_{n \to \infty} \int_X g_n \,d\mu$.
4. **Majoration par les termes originaux :** Par définition de l'infimum, pour tout $k \ge n$, on a $g_n(x) \le f_k(x)$. Donc $g_n(x) \le f_n(x)$.
   Par croissance de l'intégrale, $\int_X g_n \,d\mu \le \int_X f_n \,d\mu$.
5. **Passage à la limite inférieure :** Prenons la limite inférieure (qui est une vraie limite pour le membre de gauche) des deux côtés :
   $$ \lim_{n \to \infty} \int_X g_n \,d\mu \le \liminf_{n \to \infty} \int_X f_n \,d\mu $$
6. **Conclusion :** En combinant l'étape 3 et 5, on obtient le célèbre lemme :
   $$ \int_X \liminf_{n \to \infty} f_n \,d\mu \le \liminf_{n \to \infty} \int_X f_n \,d\mu $$
