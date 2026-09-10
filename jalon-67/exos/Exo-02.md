## Exercice 2 : Suite avec pic mouvant \quad $\bigstar\bigstar\star\star\star$

On pose $f_n(x) = n e^{-nx}$ sur $]0, +\infty[$.
**Question :** La suite $(f_n)$ satisfait-elle aux hypothèses du théorème de Beppo Levi ? Calculer la limite des intégrales et l'intégrale de la limite. Conclure.

**Solution :**
1. Pour $x > 0$ fixé, étudions le signe de $f_{n+1}(x) - f_n(x)$. Ce n'est pas toujours positif. En particulier, $f_n(x) \to 0$ pour tout $x > 0$.
2. La limite simple est $f \equiv 0$. Son intégrale est donc $0$.
3. Calculons $\int_0^\infty f_n(x) dx = \int_0^\infty n e^{-nx} dx = [-e^{-nx}]_0^\infty = 1$.
4. La limite des intégrales (1) est différente de l'intégrale de la limite (0).
5. Conclusion : La suite $(f_n)$ n'est pas croissante presque partout. Le théorème de Beppo Levi ne s'applique pas, illustrant l'importance cruciale de l'hypothèse de monotonie. $\blacksquare$
