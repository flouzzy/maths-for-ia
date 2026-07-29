# Intégration par parties pour les intégrales impropres

**Difficulté :** $\star\star\star\star$

**Énoncé :**
Montrer la convergence et calculer la valeur de l'intégrale (fonction Gamma en 2) :
$$ N = \int_0^{+\infty} t e^{-t} dt $$

**Correction Zéro Ellipse :**
1. **Typage :** La fonction $f(t) = t e^{-t}$ est continue et positive sur $[0, +\infty[$. L'intégrale est impropre en $+\infty$.
2. **Calcul sur un segment fini :** Soit $X > 0$. On pose $N(X) = \int_0^X t e^{-t} dt$.
3. **Intégration par parties :** Posons :
   - $u(t) = t \implies u'(t) = 1$
   - $v'(t) = e^{-t} \implies v(t) = -e^{-t}$
   Les fonctions $u$ et $v$ sont de classe $C^1$ sur $[0, X]$, le théorème d'intégration par parties s'applique rigoureusement :
   $$ \int_0^X u(t) v'(t) dt = \left[ u(t) v(t) \right]_0^X - \int_0^X u'(t) v(t) dt $$
   $$ N(X) = \left[ -t e^{-t} \right]_0^X - \int_0^X 1 \cdot (-e^{-t}) dt $$
   $$ N(X) = (-X e^{-X} - 0) + \int_0^X e^{-t} dt $$
4. **Calcul de la deuxième intégrale :**
   $$ \int_0^X e^{-t} dt = \left[ -e^{-t} \right]_0^X = -e^{-X} - (-e^0) = 1 - e^{-X} $$
   D'où $N(X) = -X e^{-X} + 1 - e^{-X}$.
5. **Passage à la limite :**
   - Par le théorème de croissances comparées, l'exponentielle l'emporte sur les polynômes : $\lim_{X \to +\infty} X e^{-X} = \lim_{X \to +\infty} \frac{X}{e^X} = 0$.
   - Trivialement, $\lim_{X \to +\infty} e^{-X} = 0$.
6. **Conclusion :**
   $$ \lim_{X \to +\infty} N(X) = -0 + 1 - 0 = 1 $$
   La limite est finie. L'intégrale converge et $\int_0^{+\infty} t e^{-t} dt = 1$.
