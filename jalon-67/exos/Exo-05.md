# Exercice 5 : Limite de fonctions non intégrables ★★★

## Énoncé
Soit $f_n(x) = \frac{n}{1+n^2 x^2} \mathbf{1}_{]0, 1[}(x)$.
Calculer la limite de l'intégrale et l'intégrale de la limite. Le TCM est-il applicable ?

## Correction Détaillée
1. **Intégrale de chaque fonction** : $\int_0^1 \frac{n}{1+(nx)^2} dx = [\arctan(nx)]_0^1 = \arctan(n)$.
2. **Limite des intégrales** : $\lim_{n \to \infty} \arctan(n) = \frac{\pi}{2}$.
3. **Limite simple** : Pour tout $x \in ]0, 1[$, $f_n(x) = \frac{n}{1+n^2 x^2} \sim \frac{1}{n x^2} \to 0$. Donc $f = 0$ presque partout.
4. **Intégrale de la limite** : $\int 0 = 0$.
5. **Conclusion** : $0 \neq \pi/2$. Le TCM ne s'applique pas car la suite $(f_n)$ n'est pas croissante en tout point de l'intervalle.
