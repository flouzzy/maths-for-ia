# Exo 02 : Séries à termes positifs et intégration ($\bigstar\star\star\star\star$)

## Énoncé
On souhaite évaluer l'intégrale de la fonction $f(x) = \frac{x^2}{1 - x}$ sur l'intervalle $]0, 1[$.
1. Justifier le développement en série entière de $f(x)$ sur $]0, 1[$.
2. En déduire la valeur de $\int_0^1 \frac{x^2}{1 - x} \, dx$ sous forme de somme de série. Est-elle finie ?

## Correction Détaillée
**Étape 1 : Développement en série entière**
Pour tout $x \in ]0, 1[$, on a $|x| < 1$, ce qui permet d'utiliser le développement de la série géométrique :
$$ \frac{1}{1 - x} = \sum_{k=0}^{\infty} x^k $$
En multipliant par $x^2$, on obtient :
$$ f(x) = \frac{x^2}{1 - x} = x^2 \sum_{k=0}^{\infty} x^k = \sum_{k=0}^{\infty} x^{k+2} $$

**Étape 2 : Application du théorème de sommation**
Posons $u_k(x) = x^{k+2} \mathbf{1}_{]0, 1[}(x)$. Chaque fonction $u_k$ est mesurable et positive sur $]0, 1[$.
Par le théorème d'intégration terme à terme (Corollaire de Beppo Levi) :
$$ \int_0^1 f(x) \, dx = \int_0^1 \left(\sum_{k=0}^{\infty} u_k(x)\right) dx = \sum_{k=0}^{\infty} \int_0^1 x^{k+2} \, dx $$
On calcule chaque terme de la série :
$$ \int_0^1 x^{k+2} \, dx = \left[ \frac{x^{k+3}}{k+3} \right]_0^1 = \frac{1}{k+3} $$
La somme des intégrales est donc :
$$ \sum_{k=0}^{\infty} \frac{1}{k+3} = \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \dots $$
Cette somme correspond à la série harmonique (amputée de ses deux premiers termes). Or la série harmonique diverge vers $+\infty$.
Par conséquent, $\int_0^1 \frac{x^2}{1 - x} \, dx = +\infty$. La fonction $f$ n'est pas Lebesgue-intégrable.
