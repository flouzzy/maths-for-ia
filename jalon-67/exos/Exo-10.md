# Exercice 10 : Démonstration du théorème de Beppo Levi ★☆☆☆☆

**Énoncé :**
Restituer les grandes lignes de la preuve du théorème de Beppo Levi.

**Correction :**
1. L'inégalité $\lim \int f_n \le \int f$ est évidente car $f_n \le f$, donc par monotonie de l'intégrale $\int f_n \le \int f$, d'où le passage à la limite.
2. Pour l'autre inégalité, on prend une fonction étagée $0 \le s \le f$ et un réel $0 < \alpha < 1$.
3. On définit les ensembles mesurables $A_n = \{x \mid f_n(x) \ge \alpha s(x)\}$.
4. Comme $f_n$ croît vers $f$ et $\alpha < 1$, l'union croissante des $A_n$ couvre tout l'espace $X$.
5. $\int f_n \ge \int_{A_n} f_n \ge \alpha \int_{A_n} s$.
6. La continuité séquentielle croissante de la mesure implique que $\lim \int_{A_n} s = \int_X s$.
7. En faisant $\alpha \to 1$ puis le supremum sur toutes les $s \le f$, on obtient $\lim \int f_n \ge \int f$.
